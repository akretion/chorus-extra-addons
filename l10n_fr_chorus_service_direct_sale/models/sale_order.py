# Copyright 2025 Akretion France (https://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fr_chorus_service_id = fields.Many2one(
        "chorus.partner.service",
        string="Chorus Service",
        ondelete="restrict",
        tracking=True,
        domain="[('partner_id', '=', commercial_partner_id)]",
    )
    # this module doesn't depend on l10n_fr_chorus_sale, that's why
    # I also define a related field of transmit method code here under another name
    service_direct_invoice_transmit_method_code = fields.Char(
        related="partner_invoice_id.customer_invoice_transmit_method_id.code",
    )

    def _prepare_invoice(self):
        """Copy Chorus service from sale order to invoice"""
        vals = super()._prepare_invoice()
        if (
                self.service_direct_invoice_transmit_method_code == 'fr-chorus' and
                self.fr_chorus_service_id):
            vals['fr_chorus_service_id'] = self.fr_chorus_service_id.id
        return vals
