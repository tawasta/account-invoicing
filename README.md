[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Pipeline Status](https://gitlab.com/tawasta/odoo/event/badges/12.0-dev/pipeline.svg)](https://gitlab.com/tawasta/odoo/account-invoicing/-/pipelines/)

Event
=====
Odoo Account Invoicing Addons.

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_bank_statement_reconcile_reference](account_bank_statement_reconcile_reference/) | 12.0.1.4.0 |  | Use invoice reference for reconciliation proposition
[account_invoice_auditlog_rules](account_invoice_auditlog_rules/) | 12.0.1.0.0 |  | Adds audit log rules for account.invoice and account.invoice.line
[account_invoice_circulation](account_invoice_circulation/) | 12.0.1.6.4 |  | Adds invoice circulation for vendor invoices
[account_invoice_circulation_mandatory_analytic](account_invoice_circulation_mandatory_analytic/) | 12.0.1.0.0 |  | Analytic account info is required on invoice lines
[account_invoice_commission](account_invoice_commission/) | 12.0.1.0.1 |  | account_invoice_commission
[account_invoice_commission_payment](account_invoice_commission_payment/) | 12.0.1.3.0 |  | Allows Making commission payments from invoices
[account_invoice_company_mismatch](account_invoice_company_mismatch/) | 12.0.1.0.0 |  | Invoice Company Mismatch Warning
[account_invoice_confirm_queue](account_invoice_confirm_queue/) | 12.0.1.0.0 |  | Use queue when confirming multiple invoices
[account_invoice_country_group_text](account_invoice_country_group_text/) | 12.0.1.0.0 |  | Get account invoice report text from country groups setting
[account_invoice_customer](account_invoice_customer/) | 12.0.1.0.0 |  | Invoice Customer
[account_invoice_description](account_invoice_description/) | 12.0.1.0.0 |  | Invoice internal note, that is not shown to partners
[account_invoice_disable_due_date_auto_update](account_invoice_disable_due_date_auto_update/) | 12.0.1.2.0 |  | Disable due date auto update on vendor invoices
[account_invoice_disable_online_preview](account_invoice_disable_online_preview/) | 12.0.1.0.0 |  | Don't send preview link with invoices
[account_invoice_disable_partner_bank_validation](account_invoice_disable_partner_bank_validation/) | 12.0.1.0.0 |  | Allows selecting any bank account for invoices, disregarding the account owner
[account_invoice_display_name_number_only](account_invoice_display_name_number_only/) | 12.0.1.0.2 |  | Use invoice number as record name in emails
[account_invoice_hide_outstanding_debits](account_invoice_hide_outstanding_debits/) | 12.0.1.0.0 |  | Don't show outstanding debit -info in vendor invoices
[account_invoice_invoice_transmit_method_required](account_invoice_invoice_transmit_method_required/) | 12.0.1.0.0 |  | Set invoice transmit method as required
[account_invoice_line_price_total](account_invoice_line_price_total/) | 12.0.1.0.0 |  | Adds untaxed amount to invoice line
[account_invoice_line_sale_order_number](account_invoice_line_sale_order_number/) | 12.0.1.0.0 |  | Adds sale order number to invoice line
[account_invoice_line_sales_agent](account_invoice_line_sales_agent/) | 12.0.1.0.0 |  | Adds sales agent to invoice line
[account_invoice_line_view](account_invoice_line_view/) | 12.0.1.1.0 |  | Add a readonly invoice line view
[account_invoice_link_purchase_order_from_vendor](account_invoice_link_purchase_order_from_vendor/) | 12.0.1.0.0 |  | Link Purchase order to Vendor bill
[account_invoice_mail_light_template](account_invoice_mail_light_template/) | 12.0.1.0.1 |  | Invoice emails use light mail template
[account_invoice_mail_optional_follower_notification](account_invoice_mail_optional_follower_notification/) | 12.0.1.0.0 |  | Don't send invoice emails to followers by default
[account_invoice_mandatory_payment_term](account_invoice_mandatory_payment_term/) | 12.0.1.2.0 |  | Set invoice payment term as mandatory
[account_invoice_margin_from_sale](account_invoice_margin_from_sale/) | 12.0.1.0.0 |  | Pass margin data from sale to invoice
[account_invoice_margin_ignore](account_invoice_margin_ignore/) | 12.0.1.2.0 |  | Ignore products when calculating invoice margins
[account_invoice_mass_create](account_invoice_mass_create/) | 12.0.1.1.1 |  | Mass create invoices for partners
[account_invoice_mass_refund](account_invoice_mass_refund/) | 12.0.1.1.0 |  | Allows refunding and unreconciling multiple invoices
[account_invoice_merge_attachment](account_invoice_merge_attachment/) | 12.0.1.1.0 |  | Consider attachment during invoice merge process
[account_invoice_merge_line_info](account_invoice_merge_line_info/) | 12.0.1.0.0 |  | Show order number and date on new invoice's lines
[account_invoice_merge_never_merge_lines](account_invoice_merge_never_merge_lines/) | 12.0.1.0.0 |  | Account Invoice Merge - never merge lines
[account_invoice_merge_ordered](account_invoice_merge_ordered/) | 12.0.1.0.1 |  | Account Invoice Merge - keep line order
[account_invoice_merge_reset_cost](account_invoice_merge_reset_cost/) | 12.0.1.0.0 |  | Reset the line cost price when merging invoices
[account_invoice_notice_period](account_invoice_notice_period/) | 12.0.1.2.0 |  | Notice period field for invoices and partners
[account_invoice_origin_to_comment](account_invoice_origin_to_comment/) | 12.0.1.0.2 |  | When confirming invoice, copy origin to the comment
[account_invoice_origin_to_description](account_invoice_origin_to_description/) | 12.0.1.1.1 |  | When confirming invoice, copy origin to the description
[account_invoice_overdue_interest](account_invoice_overdue_interest/) | 12.0.1.1.2 |  | Overdue interest % field for invoices and partners
[account_invoice_partner_income_expense_account](account_invoice_partner_income_expense_account/) | 12.0.1.0.1 |  | Partner-specific income and expense accounts for invoice lines
[account_invoice_partner_warning_text](account_invoice_partner_warning_text/) | 12.0.1.0.0 |  | Adds Partner warning text to Invoice
[account_invoice_payment_ref](account_invoice_payment_ref/) | 12.0.1.0.0 |  | Backported payment reference from 13.0
[account_invoice_pivot_report_delivery_address_country](account_invoice_pivot_report_delivery_address_country/) | 12.0.1.0.1 |  | Group pivot report by Delivery Address Country
[account_invoice_pivot_report_product_template](account_invoice_pivot_report_product_template/) | 12.0.1.0.0 |  | Group pivot report by Product Template
[account_invoice_product_count](account_invoice_product_count/) | 12.0.1.0.0 |  | Show product total count on invoice
[account_invoice_promised_delivery_range](account_invoice_promised_delivery_range/) | 12.0.1.0.0 |  | Adds new fields for storing date range of promised delivery
[account_invoice_purchase_review](account_invoice_purchase_review/) | 12.0.1.0.0 |  | Link vendor invoices to purchases and review the invoices
[account_invoice_refund_preserve_analytic_tags](account_invoice_refund_preserve_analytic_tags/) | 12.0.1.0.0 |  | Preserve analytic tags for refunds
[account_invoice_related_sale_order](account_invoice_related_sale_order/) | 12.0.1.0.0 |  | Related Sale Orders of Invoice
[account_invoice_report_bank_information](account_invoice_report_bank_information/) | 12.0.1.0.1 |  | Banking information to invoice template
[account_invoice_report_customer](account_invoice_report_customer/) | 12.0.1.0.0 |  | Invoice Report - Customer
[account_invoice_report_delivery_date](account_invoice_report_delivery_date/) | 12.0.1.0.0 |  | Delivery date to invoice template
[account_invoice_report_header](account_invoice_report_header/) | 12.0.1.0.0 |  | Account invoice report - Header
[account_invoice_report_hide_customer_code](account_invoice_report_hide_customer_code/) | 12.0.1.0.0 |  | Invoice Report - Hide customer code
[account_invoice_report_hide_reference](account_invoice_report_hide_reference/) | 12.0.1.0.1 |  | Invoice Report - Hide reference
[account_invoice_report_line_price_tax](account_invoice_report_line_price_tax/) | 12.0.1.0.0 |  | Account Invoice Report - Price tax on lines
[account_invoice_report_reference_number](account_invoice_report_reference_number/) | 12.0.1.0.0 |  | Invoice Report - Reference number
[account_invoice_report_show_duplicate_addresses](account_invoice_report_show_duplicate_addresses/) | 12.0.1.0.0 |  | Show delivery address even if it is same as invoicing address
[account_invoice_report_signed_values](account_invoice_report_signed_values/) | 12.0.1.0.1 |  | Changes some values to signed versions on refund reports
[account_invoice_report_title](account_invoice_report_title/) | 12.0.1.1.0 |  | Report Titles for account invoices
[account_invoice_salesperson_email](account_invoice_salesperson_email/) | 12.0.1.0.0 |  | Account Invoice - Salesperson e-mail to note field
[account_invoice_salesperson_phone_and_email](account_invoice_salesperson_phone_and_email/) | 12.0.1.0.0 |  | Account Invoice - Salesperson Phonenumber and e-mail to note field
[account_invoice_show_refunds_in_tree](account_invoice_show_refunds_in_tree/) | 12.0.1.0.0 |  | Show also refund invoices in tree view
[account_invoice_stock_pickings](account_invoice_stock_pickings/) | 12.0.1.0.1 |  | Stock pickings in invoice
[account_invoice_vendor_invoice_created](account_invoice_vendor_invoice_created/) | 12.0.1.0.0 |  | Show related vendor invoice on customer invoices
[account_invoice_vendor_invoice_to_sale](account_invoice_vendor_invoice_to_sale/) | 12.0.1.2.2 |  | Adds a wizards for creating a SO from vendor invoice
[account_invoice_vendor_invoice_tree_untaxed](account_invoice_vendor_invoice_tree_untaxed/) | 12.0.1.0.0 |  | Show untaxed amount in the list of vendor invoices
[account_invoice_vendor_invoice_work_date](account_invoice_vendor_invoice_work_date/) | 12.0.1.0.0 |  | Add new field work_date to Account Invoice
[account_invoice_vendor_invoice_work_description](account_invoice_vendor_invoice_work_description/) | 12.0.1.0.0 |  | Add new field work_description to Account Invoice
[account_invoice_vendor_invoice_work_title](account_invoice_vendor_invoice_work_title/) | 12.0.1.0.0 |  | Add new field work_title to Account Invoice
[account_invoicing_stock](account_invoicing_stock/) | 12.0.1.0.0 |  | Account invoicing stock
[account_tax_report](account_tax_report/) | 12.0.1.0.3 |  | Finnish VAT-summary report.


Unported addons
---------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_dashboard_refund_buttons](account_dashboard_refund_buttons/) | 12.0.1.0.0 (unported) |  | Shortcut buttons for refund creation
[account_invoice_client_order_ref](account_invoice_client_order_ref/) | 12.0.1.0.0 (unported) |  | Pass SO core reference field's contents to invoice
[account_invoice_default_my](account_invoice_default_my/) | 12.0.1.0.0 (unported) |  | Show invoices by default
[account_invoice_default_parent](account_invoice_default_parent/) | 12.0.1.0.0 (unported) |  | Default parent for new shipping addresses
[account_invoice_line_total](account_invoice_line_total/) | 12.0.1.1.1 (unported) |  | Adds invoice line total (with taxes) to invoice lines
[account_invoice_margin_in_tree](account_invoice_margin_in_tree/) | 12.0.1.0.0 (unported) |  | Show the margin field in invoice list
[account_invoice_margin_percent](account_invoice_margin_percent/) | 12.0.1.0.0 (unported) |  | Shows the margin profit percentage in invoices
[account_invoice_order_number_in_comments](account_invoice_order_number_in_comments/) | 12.0.1.0.0 (unported) |  | Invoicing a SO stores the order # in invoice's comment field
[account_invoice_partner_quick_insert](account_invoice_partner_quick_insert/) | 12.0.1.0.0 (unported) |  | Partner address fields as editable on invoice
[account_invoice_partner_strict](account_invoice_partner_strict/) | 12.0.1.1.0 (unported) |  | Only allow correct type and parent for invoice addresses
[account_invoice_review](account_invoice_review/) | 12.0.0.1.0 (unported) |  | Allows marking invoices as reviewed
[account_invoice_transmit_method_einvoice](account_invoice_transmit_method_einvoice/) | 12.0.1.0.0 (unported) |  | Add einvoice transmit method
[account_invoice_transmit_type_translatable](account_invoice_transmit_type_translatable/) | 12.0.1.0.0 (unported) |  | Add translations to transmit methods
[account_refund_form_total_string](account_refund_form_total_string/) | 12.0.1.0.0 (unported) |  | The string better indicates a refund
[account_refund_line_negative_warning](account_refund_line_negative_warning/) | 12.0.1.0.0 (unported) |  | Show a warning when trying to add negative lines to a refund

[//]: # (end addons)
