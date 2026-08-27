# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class AirivUmkmOnboardingWizard(models.TransientModel):
    _name = 'airiv.umkm.onboarding.wizard'
    _description = 'Panduan Cepat Konfigurasi UMKM Indonesia'

    company_id = fields.Many2one('res.company', string="Perusahaan", default=lambda self: self.env.company, required=True)
    npwp_16 = fields.Char(string="NPWP 16 Digit / NIK Toko", default="0123456789012345", required=True)
    whatsapp_mode = fields.Selection([
        ('sandbox', 'Sandbox (Simulasi Gratis - Tanpa Kuota)'),
        ('production', 'Produksi (Fonnte API Token / WAHA Docker)'),
    ], string="Mode WhatsApp", default='sandbox', required=True)
    fonnte_token = fields.Char(string="Fonnte Token (Jika Produksi)")

    thermal_width = fields.Selection([
        ('58mm', '58 mm (Mobile Thermal EDC)'),
        ('80mm', '80 mm (Printer Struk Desktop)'),
    ], string="Ukuran Kertas Kasir POS", default='80mm', required=True)

    enable_qris = fields.Boolean(string="Aktifkan Dynamic QRIS", default=True)
    enable_ppn12 = fields.Boolean(string="Terapkan PPN 12% UU HPP", default=True)
    enable_sak_emkm = fields.Boolean(string="Gunakan Standar SAK EMKM", default=True)

    def action_apply_umkm_configuration(self):
        self.ensure_one()
        comp = self.company_id

        # 1. Update Company NPWP / NIK
        if hasattr(comp, 'vat'):
            comp.write({'vat': self.npwp_16})

        # 2. Update WhatsApp Configuration
        WAConfig = self.env.get('airiv.whatsapp.config')
        if WAConfig is not None:
            cfg = WAConfig.get_active_config()
            cfg.write({
                'environment': self.whatsapp_mode,
                'fonnte_api_token': self.fonnte_token if self.whatsapp_mode == 'production' else False,
            })

        # 3. Update POS Registers
        PosConfig = self.env.get('pos.config')
        if PosConfig is not None:
            for pcfg in PosConfig.search([]):
                pcfg.write({
                    'l10n_id_receipt_paper_width': self.thermal_width,
                    'l10n_id_store_npwp': self.npwp_16,
                    'l10n_id_show_tax_breakdown': self.enable_ppn12,
                })

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Konfigurasi UMKM Berhasil'),
                'message': _('Seluruh pengaturan bisnis Indonesia telah disinkronkan ke dalam sistem Odoo.'),
                'type': 'success',
                'sticky': False,
            }
        }
