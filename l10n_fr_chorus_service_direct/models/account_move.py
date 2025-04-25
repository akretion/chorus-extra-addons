# Copyright 2025 Akretion France (https://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    fr_chorus_service_id = fields.Many2one(
        "chorus.partner.service",
        string="Chorus Service",
        ondelete="restrict",
        tracking=True,
        domain="[('partner_id', '=', commercial_partner_id)]",
    )
    # inherit of field present in l10n_fr_chorus_account
    chorus_service_code = fields.Char(
        related='fr_chorus_service_id.code')

    # inherit method from l10n_fr_chorus_account
    def _get_chorus_service(self):
        self.ensure_one()
        return self.fr_chorus_service_id
