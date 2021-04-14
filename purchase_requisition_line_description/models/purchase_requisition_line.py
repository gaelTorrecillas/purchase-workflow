# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.fields import first


class PurchaseRequisitionLine(models.Model):
    _inherit = "purchase.requisition.line"

    name = fields.Text(string="Description")

    @api.onchange('product_id')
    def _onchange_product_id(self):
        # to format name into: "[product_code] product_name"
        res = super()._onchange_product_id()
        desc = ""
        if self.product_id:
            product_lang = self.product_id.with_context(
                lang=self.requisition_id.purchase_ids.partner_id.lang,
                partner_id=self.requisition_id.purchase_ids.partner_id.id,
            )
            self.name = product_lang.display_name
            if product_lang.description_purchase:
                self.name += '\n' + product_lang.description_purchase
        return res
