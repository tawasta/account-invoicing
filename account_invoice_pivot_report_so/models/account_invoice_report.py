from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    sale_id = fields.Many2one(
        "sale.order", readonly=True
    )

    def _from(self):                                                                                                        
       return (                                                                                                            
           super(AccountInvoiceReport, self)._from()                                                                       
           + """LEFT JOIN sale_order order ON                                                                              
           order.id = line.move_id.sale_id"""                                                                                      
       )  

    def _select(self):
        return (
            super(AccountInvoiceReport, self)._select()
            + ", line.move_id.sale_id as sale_id"
        )

