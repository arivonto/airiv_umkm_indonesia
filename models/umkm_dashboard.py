# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date

class AirivUmkmDashboard(models.Model):
    _name = 'airiv.umkm.dashboard'
    _description = 'Executive Dashboard UMKM & PP 55/2022 PPh Final 0.5%'
    _order = 'year desc, id desc'

    name = fields.Char(string="Dashboard Periode", compute="_compute_name", store=True)
    year = fields.Integer(string="Tahun Pajak", default=lambda self: date.today().year, required=True)
    company_id = fields.Many2one('res.company', string="Perusahaan / UMKM", default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one('res.currency', string="Mata Uang", related='company_id.currency_id', readonly=True)
    
    taxpayer_type = fields.Selection([
        ('op', 'Orang Pribadi (Bebas Pajak s/d Rp 500 Juta)'),
        ('badan', 'Badan Usaha / PT / CV (PPh 0.5% dari Omzet Pertama)'),
    ], string="Kategori Wajib Pajak", default='op', required=True)

    # Metric Cards (PP 55/2022)
    total_omzet_ytd = fields.Monetary(string="Total Omzet Bruto (YTD)", compute="_compute_metrics", store=True)
    omzet_bebas_pajak = fields.Monetary(string="Omzet Bebas Pajak (s/d 500 Jt)", compute="_compute_metrics", store=True)
    dpp_pph_final = fields.Monetary(string="Dasar Pengenaan Pajak (DPP)", compute="_compute_metrics", store=True)
    total_pph_final = fields.Monetary(string="Total Kewajiban PPh 0.5%", compute="_compute_metrics", store=True)
    
    threshold_progress = fields.Float(string="Utilisasi Threshold Bebas Pajak (%)", compute="_compute_metrics", store=True)
    is_threshold_exceeded = fields.Boolean(string="Threshold 500 Juta Terlampaui", compute="_compute_metrics", store=True)

    @api.depends('year', 'company_id')
    def _compute_name(self):
        for rec in self:
            rec.name = f"Dashboard UMKM Pajak {rec.year} - {rec.company_id.name}"

    @api.depends('year', 'taxpayer_type', 'company_id')
    def _compute_metrics(self):
        Turnover = self.env['airiv.umkm.turnover'].sudo()
        for rec in self:
            records = Turnover.search([
                ('company_id', '=', rec.company_id.id),
                ('year', '=', str(rec.year))
            ])
            
            gross = sum(r.gross_turnover for r in records)
            rec.total_omzet_ytd = gross
            
            if rec.taxpayer_type == 'op':
                non_taxable = min(gross, 500000000.0)
                dpp = max(0.0, gross - 500000000.0)
                rec.threshold_progress = min(100.0, (gross / 500000000.0) * 100.0) if gross > 0 else 0.0
                rec.is_threshold_exceeded = gross > 500000000.0
            else:
                non_taxable = 0.0
                dpp = gross
                rec.threshold_progress = 100.0
                rec.is_threshold_exceeded = True
                
            rec.omzet_bebas_pajak = non_taxable
            rec.dpp_pph_final = dpp
            rec.total_pph_final = dpp * 0.005

    @api.model
    def get_dashboard_data(self):
        current_year = date.today().year
        dashboard = self.search([
            ('company_id', '=', self.env.company.id),
            ('year', '=', current_year)
        ], limit=1)
        if not dashboard:
            dashboard = self.create({
                'year': current_year,
                'company_id': self.env.company.id
            })
        dashboard._compute_metrics()
        return {
            'id': dashboard.id,
            'year': dashboard.year,
            'total_omzet_ytd': dashboard.total_omzet_ytd,
            'omzet_bebas_pajak': dashboard.omzet_bebas_pajak,
            'dpp_pph_final': dashboard.dpp_pph_final,
            'total_pph_final': dashboard.total_pph_final,
            'threshold_progress': dashboard.threshold_progress,
            'is_threshold_exceeded': dashboard.is_threshold_exceeded,
            'taxpayer_type': dashboard.taxpayer_type,
        }
