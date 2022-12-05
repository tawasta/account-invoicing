from odoo import _, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _prepare_invoice(self):
        """Assign phone and email values to Invoice's narration-field"""
        vals = super(SaleOrder, self)._prepare_invoice()
        email = self.user_id.partner_id.email
        # Conditions to add newlines
        email_line = "\n" if vals.get("narration") else ""

        if email:
            vals["narration"] += "{}{}{}".format(email_line, _("Handler: "), email)

        vals["salesperson_email"] = self.user_id.partner_id.email
        return vals
