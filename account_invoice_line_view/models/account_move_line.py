from odoo import fields, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    # Related/computed helper fields here
    commercial_partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        related="move_id.commercial_partner_id",
        store=True,
    )

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        related="move_id.partner_id",
        store=True,
    )

    product_categ_id = fields.Many2one(
        comodel_name="product.category",
        related="product_id.categ_id",
    )

    product_tmpl_id = fields.Many2one(
        string="Product Template",
        comodel_name="product.template",
        related="product_id.product_tmpl_id",
        readonly=False,
        store=True,
        help="Technical: used in views",
    )

    date_invoice = fields.Date(
        string="Invoice date",
        related="move_id.invoice_date",
        store=True,
    )

    user_id = fields.Many2one(
        string="Responsible",
        related="move_id.user_id",
        store=True,
    )

    # The states are hard coded, but they could be fetched from account invoice
    # model if that is necessary
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("proforma", "Pro-forma"),
            ("proforma2", "Pro-forma"),
            ("open", "Open"),
            ("paid", "Paid"),
            ("cancel", "Cancelled"),
        ],
        string="State",
        related="move_id.state",
        store=True,
    )

    # Hard coded types were removed 12.10.2022
    invoice_type = fields.Selection(
        string="Type",
        related="move_id.move_type",
    )
