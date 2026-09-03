from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def _get_import_file_type(self, file_data):
        """Identify Finvoice files for the Odoo 19 import framework.

        account_edi_finvoice detects Finvoice inside its own
        _get_edi_decoder, using the file_data["type"] key that Odoo 19
        replaced with file_data["import_file_type"]. Detection belongs in
        this hook instead, the same way core does it for Factur-X,
        FatturaPA and Factura-e.
        """
        tree = file_data["xml_tree"]
        if tree is not None and self._is_finvoice(tree):
            return "finvoice"
        return super()._get_import_file_type(file_data)

    def _get_edi_decoder(self, file_data, new=False):
        """Return a decoder for Finvoice instead of importing inline.

        In Odoo 19 this hook must *return* {"priority", "decoder"} and do
        no work itself: the framework calls the decoder later, inside a
        rollbackable transaction, as decoder(record, file_data, new).
        """

        if file_data["import_file_type"] == "finvoice":
            return {
                "priority": 20,
                "decoder": self._import_finvoice_document,
            }

        # account_edi_finvoice's own override reads file_data["type"],
        # which no longer exists in Odoo 19, so calling super() would
        # raise KeyError for every attachment (PDFs included). Feed it a
        # value that is never "xml" - no _get_import_file_type in core or
        # in this database returns that string - so its Finvoice branch is
        # skipped and it simply forwards to the core implementation.
        # This key can be dropped once account_edi_finvoice is migrated.
        file_data["type"] = file_data["import_file_type"]
        return super()._get_edi_decoder(file_data, new=new)

    def _import_finvoice_document(self, invoice, file_data, new=False):
        """Decoder entry point for the account import framework.

        Returns nothing on success: the framework treats a truthy return
        value as the reason the file could not be decoded.
        """
        self._import_finvoice(file_data["xml_tree"], invoice)
