# Copyright 2025 Akretion France (https://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "L10n FR Chorus Service Direct Sale",
    "summary": "Direct selection of Chorus service on sale orders",
    "version": "17.0.1.0.0",
    "category": "French Localization",
    "author": "Akretion",
    "maintainers": ["alexis-via"],
    "website": "https://github.com/akretion/chorus-extra-addons",
    "license": "AGPL-3",
    "depends": [
        "l10n_fr_chorus_service_direct",
        "sale_commercial_partner",
    ],
    "data": [
        "views/sale_order.xml",
    ],
    "installable": True,
    'auto_install': True,
}
