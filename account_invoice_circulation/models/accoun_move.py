from odoo import _, api, fields, models
from odoo.exceptions import UserError


class AccountMove(models.Model):

    _inherit = "account.move"

    invoice_approved = fields.Boolean(
        string="Approved", default=False, readonly=True, copy=False
    )

    account_invoice_circulation_id = fields.Many2one(
        comodel_name="account.invoice.circulation",
        string="Circulation",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=False,
    )

    allow_approve = fields.Boolean(
        compute="_compute_allow_approve",
        string="Can invoice be approved",
        help="Current user can approve the invoice",
    )

    # Helper field to show a readonly-approver in form view
    current_approver_id = fields.Many2one(
        string="Current approver",
        comodel_name="res.users",
        compute="_compute_current_approver_id",
        readonly=True,
    )

    def action_post(self):
        # Don't allow posting if circulation is not done
        for record in self:
            if record.account_invoice_circulation_id and not record.invoice_approved:
                msg = _("{} has to approve the invoice before confirming.").format(
                    record.current_approver_id.name
                )
                raise UserError(msg)

        return super().action_post()

    def action_invoice_approve(self):
        current_user = self.env.user

        for record in self:
            if current_user != record.invoice_user_id and not current_user.has_group(
                "account.group_account_manager"
            ):

                msg = _(
                    "%s or a manager should approve the invoice first"
                    % record.invoice_user_id.name
                )

                raise UserError(msg)

            msg = _("%s has approved this invoice" % current_user.name)
            record.sudo().message_post(body=msg)

            circulation = record.account_invoice_circulation_id
            lines = circulation.circulation_line_ids

            current_line = lines.filtered(lambda r: record.user_id == r.user_id)
            next_lines = lines.filtered(lambda r: current_line.sequence < r.sequence)

            if not next_lines:
                msg = _("All approvers have approved this invoice")
                record.sudo().message_post(body=msg)

                # Set as approved
                record.invoice_approved = True

                # Assign to validator
                record.invoice_user_id = circulation.user_id.id

            else:
                record.invoice_user_id = next_lines[0].user_id.id

    def _compute_allow_approve(self):
        for record in self:
            user_match = record.invoice_user_id == self.env.user
            record.allow_approve = user_match and not record.invoice_approved

    @api.onchange("invoice_user_id")
    def _compute_current_approver_id(self):
        for record in self:
            record.current_approver_id = record.invoice_user_id

    @api.onchange("account_invoice_circulation_id")
    def _compute_approver_and_circulation_status(self):
        for record in self:
            circulation_id = record.account_invoice_circulation_id
            # No circulation, mark as approved
            if not circulation_id:
                record.invoice_approved = True

            if circulation_id.circulation_line_ids:
                # Set the first approver as user, invoice as not approved
                approver = circulation_id.circulation_line_ids[0].user_id.id
                record.invoice_user_id = approver
                record.current_approver_id = approver
                record.invoice_approved = False
