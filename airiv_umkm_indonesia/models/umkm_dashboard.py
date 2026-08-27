# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AirivUmkmDashboard(models.Model):
    _name = 'airiv.umkm.dashboard'
    _description = 'AIRIV Indonesian UMKM Executive Control Center'

    name = fields.Char(string="Dashboard Entity", default="AIRIV Indonesia UMKM Executive Center", required=True)
    company_id = fields.Many2one('res.company', string="Perusahaan", default=lambda self: self.env.company, required=True)

    # Status indicators for 7 core pillars
    tax_status = fields.Boolean(string="DJP Coretax & PPN 12%", default=True)
    accounting_status = fields.Boolean(string="SAK EMKM Financial Reports", default=True)
    payroll_status = fields.Boolean(string="PPh 21 TER & BPJS", default=True)
    payment_status = fields.Boolean(string="Midtrans / Xendit Gateways", default=True)
    delivery_status = fields.Boolean(string="Biteship Logistics", default=True)
    whatsapp_status = fields.Boolean(string="WhatsApp Notification Engine", default=True)
    pos_status = fields.Boolean(string="Dynamic QRIS & POS", default=True)
