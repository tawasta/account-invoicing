from odoo import models, api
from odoo.osv import expression
from odoo.tools import formatLang


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def name_get(self):
        """
        Override name get to show PO line order, name, qty, uom and price
        """
        result = []
        for doc in self:
            price = formatLang(
                self.env,
                doc.price_unit,
                monetary=True,
                currency_obj=doc.currency_id
            )

            name = '[{0}] {1}: {2} {3}, {4}'.format(
                doc.order_id.name,
                doc.name,
                doc.product_qty,
                doc.product_uom.name,
                price,
            )

            result.append((doc.id, name))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100,
                     name_get_uid=None):
        """
        Override name search to allow searching by qty or price
        """
        args = args or []
        domain = []
        if name:
            domain = [
                '|',
                '|',
                ('name', operator, name),
                ('product_qty', operator, name),
                ('price_unit', operator, name),
            ]

        order_line_ids = self._search(
            expression.AND([domain, args]),
            limit=limit,
            access_rights_uid=name_get_uid
        )
        return self.browse(order_line_ids).name_get()
