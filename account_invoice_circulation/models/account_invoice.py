from odoo import _, api, fields, models
from odoo.exceptions import UserError


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    invoice_approved = fields.Boolean(string="Approved", default=False, readonly=True)

    account_invoice_circulation_id = fields.Many2one(
        comodel_name="account.invoice.circulation", string="Circulation",
        readonly=True, states={'draft': [('readonly', False)]}
    )

    allow_approve = fields.Boolean(
        comodel_name='res.users', compute='_compute_allow_approve',
        string='Can invoice be approved', help='Current user can approve the invoice',
    )

    def action_invoice_approve(self):

        current_user = self.env.user

        for record in self:
            if current_user != record.user_id and not current_user.has_group(
                "account.group_account_manager"
            ):

                msg = _(
                    "%s or a manager should approve the invoice first"
                    % record.user_id.name
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
                record.user_id = circulation.user_id.id

            else:
                record.user_id = next_lines[0].user_id.id

    def _compute_allow_approve(self):
        for record in self:
            user_match = record.user_id == self.env.user

            record.allow_approve = user_match and not record.invoice_approved

    @api.multi
    def write(self, vals):
        if "account_invoice_circulation_id" in vals:
            # No circulation, mark as approved
            if not vals["account_invoice_circulation_id"]:
                vals["invoice_approved"] = True

            circulation_id = self.env["account.invoice.circulation"].browse(
                [vals["account_invoice_circulation_id"]]
            )

            if circulation_id.circulation_line_ids:
                # Set as not approved
                vals["invoice_approved"] = False

                # Set the first approver as user
                vals["user_id"] = circulation_id.circulation_line_ids[0].user_id.id

        return super(AccountInvoice, self).write(vals)
