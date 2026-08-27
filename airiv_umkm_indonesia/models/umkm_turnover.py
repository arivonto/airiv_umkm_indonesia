# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date

class AirivUmkmTurnover(models.Model):
    _name = 'airiv.umkm.turnover'
    _description = 'Buku Peredaran Bruto Bulanan UMKM (PP 55/2022)'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'year desc, month desc, id desc'

    name = fields.Char(string="Nomor Referensi", compute="_compute_name", store=True)
    year = fields.Selection([
        (str(y), str(y)) for y in range(2023, 2035)
    ], string="Tahun Pajak", default=lambda self: str(date.today().year), required=True, tracking=True)
    
    month = fields.Selection([
        ('01', 'Januari'), ('02', 'Februari'), ('03', 'Maret'),
        ('04', 'April'),   ('05', 'Mei'),      ('06', 'Juni'),
        ('07', 'Juli'),    ('08', 'Agustus'),  ('09', 'September'),
        ('10', 'Oktober'), ('11', 'November'), ('12', 'Desember')
    ], string="Masa Pajak (Bulan)", default=lambda self: f"{date.today().month:02d}", required=True, tracking=True)
    
    company_id = fields.Many2one('res.company', string="Perusahaan / UMKM", default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one('res.currency', string="Mata Uang", related='company_id.currency_id', readonly=True)
    
    taxpayer_type = fields.Selection([
        ('op', 'Orang Pribadi (Fasilitas Bebas Pajak s/d 500 Jt)'),
        ('badan', 'Badan Usaha (PT / CV / Koperasi)'),
    ], string="Tipe Wajib Pajak", default='op', required=True, tracking=True)

    gross_turnover = fields.Monetary(string="Omzet Bruto Bulan Ini", required=True, tracking=True)
    cumulative_turnover_prior = fields.Monetary(string="Omzet Kumulatif Sebelumnya", compute="_compute_tax_calculation", store=True)
    non_taxable_portion = fields.Monetary(string="Porsi Bebas Pajak (s/d 500 Jt)", compute="_compute_tax_calculation", store=True)
    taxable_dpp = fields.Monetary(string="Dasar Pengenaan Pajak (DPP)", compute="_compute_tax_calculation", store=True)
    tax_rate = fields.Float(string="Tarif PPh Final", default=0.5, readonly=True)
    tax_amount = fields.Monetary(string="Kewajiban PPh Final 0.5%", compute="_compute_tax_calculation", store=True)

    billing_code = fields.Char(string="Kode Billing DJP (e-Billing)", tracking=True)
    ntpn = fields.Char(string="NTPN (Nomor Transaksi Penerimaan Negara)", tracking=True)
    payment_date = fields.Date(string="Tanggal Setor / Bayar", tracking=True)

    state = fields.Selection([
        ('draft', 'Draft (Pencatatan)'),
        ('calculated', 'Dihitung'),
        ('billed', 'Kode Billing Terbit'),
        ('paid', 'Lunas / Disetor'),
    ], string="Status Pembayaran", default='draft', required=True, tracking=True)

    @api.depends('year', 'month', 'company_id')
    def _compute_name(self):
        month_names = {
            '01': 'JAN', '02': 'FEB', '03': 'MAR', '04': 'APR',
            '05': 'MEI', '06': 'JUN', '07': 'JUL', '08': 'AGU',
            '09': 'SEP', '10': 'OKT', '11': 'NOV', '12': 'DES'
        }
        for rec in self:
            m_label = month_names.get(rec.month, rec.month or '')
            rec.name = f"UMKM/{rec.year}/{m_label}"

    @api.depends('gross_turnover', 'year', 'month', 'taxpayer_type', 'company_id')
    def _compute_tax_calculation(self):
        for rec in self:
            if not rec.year or not rec.month:
                rec.cumulative_turnover_prior = 0.0
                rec.non_taxable_portion = 0.0
                rec.taxable_dpp = 0.0
                rec.tax_amount = 0.0
                continue

            prior_records = self.search([
                ('company_id', '=', rec.company_id.id),
                ('year', '=', rec.year),
                ('month', '<', rec.month),
                ('id', '!=', rec.id or 0)
            ])
            prior_turnover = sum(r.gross_turnover for r in prior_records)
            rec.cumulative_turnover_prior = prior_turnover

            if rec.taxpayer_type == 'op':
                threshold = 500000000.0
                if prior_turnover >= threshold:
                    rec.non_taxable_portion = 0.0
                    rec.taxable_dpp = rec.gross_turnover
                elif (prior_turnover + rec.gross_turnover) <= threshold:
                    rec.non_taxable_portion = rec.gross_turnover
                    rec.taxable_dpp = 0.0
                else:
                    rec.non_taxable_portion = threshold - prior_turnover
                    rec.taxable_dpp = (prior_turnover + rec.gross_turnover) - threshold
            else:
                rec.non_taxable_portion = 0.0
                rec.taxable_dpp = rec.gross_turnover

            rec.tax_amount = rec.taxable_dpp * 0.005

    def action_calculate(self):
        self._compute_tax_calculation()
        self.write({'state': 'calculated'})

    def action_mark_billed(self):
        self.write({'state': 'billed'})

    def action_mark_paid(self):
        self.write({'state': 'paid'})
