# Copyright 2025 Akretion France (https://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "L10n FR Chorus Service Direct",
    "summary": "Direct selection of Chorus service on customer invoices",
    "version": "17.0.1.0.0",
    "category": "French Localization",
    "author": "Akretion",
    "maintainers": ["alexis-via"],
    "website": "https://github.com/akretion/chorus-extra-addons",
    "license": "AGPL-3",
    "depends": ["l10n_fr_chorus_account"],
    "data": [
        "views/account_move.xml",
        "views/res_partner.xml",
        ],
    "post_init_hook": "chorus_service_direct_data_mig",
    "installable": True,
}
