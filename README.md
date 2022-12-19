[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Pipeline Status](https://gitlab.com/tawasta/odoo/account-invoicing/badges/14.0-dev/pipeline.svg)](https://gitlab.com/tawasta/odoo/account-invoicing/-/pipelines/)

Invoicing
=========

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_account_region_type](account_account_region_type/) | 14.0.1.0.0 |  | Set region type for an account
[account_financial_report_partner_ref](account_financial_report_partner_ref/) | 14.0.1.0.1 |  | A ref number of a partner is added to General Ledger report
[account_financial_report_totals](account_financial_report_totals/) | 14.0.1.0.0 |  | Adds totals of each column to trial balance
[account_fiscal_position_company_not_required](account_fiscal_position_company_not_required/) | 14.0.1.0.0 |  | Company will not be required on fiscal positions
[account_fiscal_position_type](account_fiscal_position_type/) | 14.0.1.0.0 |  | Fiscal Position type
[account_invoice_accounting_date](account_invoice_accounting_date/) | 14.0.1.0.0 |  | Allows setting a distinct invoice date and accounting date
[account_invoice_auditlog_rules](account_invoice_auditlog_rules/) | 14.0.1.0.0 |  | Adds audit log rules for account.move and account.move.line
[account_invoice_commission](account_invoice_commission/) | 14.0.1.0.3 |  | account_invoice_commission
[account_invoice_commission_payment](account_invoice_commission_payment/) | 14.0.1.6.6 |  | Allows Making commission payments from invoices
[account_invoice_commission_payment_queue](account_invoice_commission_payment_queue/) | 14.0.1.0.1 |  | Create commission payments as queued jobs
[account_invoice_commission_payment_variant_company](account_invoice_commission_payment_variant_company/) | 14.0.1.0.0 |  | Use product variant company as recipient in invoice commission payments
[account_invoice_country_group_text](account_invoice_country_group_text/) | 14.0.1.0.0 |  | Get account invoice report text from country groups setting
[account_invoice_disable_sending](account_invoice_disable_sending/) | 14.0.1.0.0 |  | Don't show 'Send & Print' in invoices
[account_invoice_disable_unique_sequence](account_invoice_disable_unique_sequence/) | 14.0.1.0.1 |  | Allows multiple invoices to exist with the same sequence number
[account_invoice_email](account_invoice_email/) | 14.0.1.1.0 |  | Send invoice email to invoice email address instead of default email address
[account_invoice_invoice_transmit_method_required](account_invoice_invoice_transmit_method_required/) | 14.0.1.0.0 |  | Set invoice transmit method as required
[account_invoice_line_related_sale_order](account_invoice_line_related_sale_order/) | 14.0.1.0.0 |  | Related sale of an invoice line
[account_invoice_line_view](account_invoice_line_view/) | 14.0.1.0.6 |  | Add a readonly invoice line view
[account_invoice_merge_attachment](account_invoice_merge_attachment/) | 14.0.1.1.0 |  | Consider attachment during invoice merge process
[account_invoice_merge_different_users](account_invoice_merge_different_users/) | 14.0.1.0.0 |  | Allow merging invoices with different users
[account_invoice_merge_never_merge_lines](account_invoice_merge_never_merge_lines/) | 14.0.1.1.0 |  | Never merge lines while merging invoices.
[account_invoice_merge_ordered](account_invoice_merge_ordered/) | 14.0.1.0.1 |  | Account Invoice Merge - keep line order
[account_invoice_notice_period](account_invoice_notice_period/) | 14.0.1.0.0 |  | Notice period field for invoices and partners
[account_invoice_overdue_interest](account_invoice_overdue_interest/) | 14.0.1.0.0 |  | Overdue interest % field for invoices and partners
[account_invoice_partner_clause_to_narration](account_invoice_partner_clause_to_narration/) | 14.0.1.0.0 |  | Adds a clause from partner to invoice narration field
[account_invoice_partner_income_expense_account](account_invoice_partner_income_expense_account/) | 14.0.1.0.1 |  | Partner-specific income and expense accounts for invoice lines
[account_invoice_partner_warning_text](account_invoice_partner_warning_text/) | 14.0.1.0.0 |  | Adds Partner warning text to invoice
[account_invoice_payment_date](account_invoice_payment_date/) | 14.0.1.1.1 |  | Save the date when invoice was fully paid
[account_invoice_pivot_report_delivery_address_country](account_invoice_pivot_report_delivery_address_country/) | 14.0.1.0.2 |  | Group pivot report by delivery address country
[account_invoice_pivot_report_product_template](account_invoice_pivot_report_product_template/) | 14.0.1.0.0 |  | Group pivot report by Product Template
[account_invoice_quick_post](account_invoice_quick_post/) | 14.0.1.0.0 |  | Post (confirm) invoices from line view
[account_invoice_related_sale_order](account_invoice_related_sale_order/) | 14.0.1.0.1 |  | Related Sale Orders of Invoice
[account_invoice_related_sale_order_customer](account_invoice_related_sale_order_customer/) | 14.0.1.0.0 |  | Related Customer of Invoice sale order
[account_invoice_report_reference_is_description](account_invoice_report_reference_is_description/) | 14.0.1.0.0 |  | Invoice print - replace Reference header with Description
[account_invoice_report_title](account_invoice_report_title/) | 14.0.1.1.0 |  | Report Titles for account invoices
[account_invoice_salesperson_email](account_invoice_salesperson_email/) | 14.0.1.0.1 |  | Account Invoice - Salesperson e-mail to note field
[account_invoice_stock_picking](account_invoice_stock_picking/) | 14.0.1.1.0 |  | Add related stock pickings to invoice
[account_invoice_stock_picking_downpayment](account_invoice_stock_picking_downpayment/) | 14.0.1.2.5 |  | Prevent validating pickings with open down payments
[account_invoice_vendor_invoice_created](account_invoice_vendor_invoice_created/) | 14.0.1.0.0 |  | Show related vendor invoice on customer invoices
[account_invoice_vendor_invoice_to_sale](account_invoice_vendor_invoice_to_sale/) | 14.0.1.0.1 |  | Adds a wizards for creating a SO from vendor invoice
[account_invoice_vendor_shipping_address](account_invoice_vendor_shipping_address/) | 14.0.1.0.0 |  | Allows defining a supplier address for vendor invoices
[account_invoice_warranty_case](account_invoice_warranty_case/) | 14.0.1.0.0 |  | Creating an invoice from Sale order sets its warranty case as True
[account_payment_commission_send_email](account_payment_commission_send_email/) | 14.0.1.0.1 |  | Account payment commission send email
[account_report_invoice_bank_transfer](account_report_invoice_bank_transfer/) | 14.0.1.0.1 |  | Add a bank transfer section for invoices
[account_report_invoice_business_code](account_report_invoice_business_code/) | 14.0.1.0.1 |  | Show business code in invoice PDF
[account_report_invoice_customer_contact](account_report_invoice_customer_contact/) | 14.0.1.0.1 |  | Show customer contact in invoice PDF
[account_report_invoice_delivery_date](account_report_invoice_delivery_date/) | 14.0.1.0.1 |  | Delivery date to invoice report template
[account_report_invoice_eori](account_report_invoice_eori/) | 14.0.1.0.0 |  | Adds customers EORI number to Invoice Report
[account_report_invoice_hide_customer_code](account_report_invoice_hide_customer_code/) | 14.0.1.0.0 |  | Invoice Report - Hide customer code
[account_report_invoice_hide_incoterm_under_note](account_report_invoice_hide_incoterm_under_note/) | 14.0.1.0.0 |  | Invoice print - hide Incoterm under note
[account_report_invoice_hide_invoice_name](account_report_invoice_hide_invoice_name/) | 14.0.1.0.0 |  | Account invoice report - Hide invoice name
[account_report_invoice_hide_origin](account_report_invoice_hide_origin/) | 14.0.1.0.0 |  | Account invoice report - Hide origin
[account_report_invoice_payment](account_report_invoice_payment/) | 14.0.1.0.0 |  | Account Report Invoice payment
[account_report_invoice_payment_term_text](account_report_invoice_payment_term_text/) | 14.0.1.0.0 |  | Show 'Payment terms:' text on Invoice pdf print
[account_report_invoice_quantity_decimals](account_report_invoice_quantity_decimals/) | 14.0.1.0.0 |  | Modifications to invoice print decimal precision
[account_report_invoice_reformat](account_report_invoice_reformat/) | 14.0.1.0.0 |  | Reformat invoice print elements for cleaner look
[account_report_invoice_show_invoice_address](account_report_invoice_show_invoice_address/) | 14.0.1.0.0 |  | Account Invoice PDF report - Show Invoice address
[account_report_show_duplicate_addresses](account_report_show_duplicate_addresses/) | 14.0.1.0.1 |  | Show delivery address even if it is same as invoicing address
[account_report_title](account_report_title/) | 14.0.1.0.1 |  | Report titles for account invoices
[account_tax_report](account_tax_report/) | 14.0.1.0.2 |  | Finnish VAT-summary report.


Unported addons
---------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_invoicing_stock](account_invoicing_stock/) | 14.0.1.0.0 (unported) |  | Account invoicing stock

[//]: # (end addons)
