# Copyright 2025 Akretion France (https://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

def chorus_service_direct_data_mig(env):
    chorus_srv_invoices = env['account.move'].search([
        ('move_type', 'in', ('out_invoice', 'out_refund')),
        ('transmit_method_code', '=', 'fr-chorus'),
        ('partner_id.fr_chorus_service_id', '!=', False),
        ])
    for invoice in chorus_srv_invoices:
        invoice.write({'fr_chorus_service_id': invoice.partner_id.fr_chorus_service_id})
    # unlink partners to chorus service
    srv_partners = env['res.partner'].with_context(active_test=False).search([('fr_chorus_service_id', '!=', False)])
    srv_partners.write({'fr_chorus_service_id': False})
    return
