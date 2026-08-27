# -*- coding: utf-8 -*-
{
    'name': 'Indonesia UMKM All-in-One Business & Compliance Engine',
    'version': '18.0.1.0.0',
    'category': 'Localization/Indonesia',
    'summary': 'Unified Indonesian ERP Bundle for UMKM: DJP Coretax, SAK EMKM, PPh 21 TER, Biteship, QRIS POS & WhatsApp',
    'description': """
The Definitive Indonesian UMKM All-in-One Business, Accounting & Regulatory Meta-Engine for Odoo 18 Community Edition.
Bundles and seamlessly synchronizes all 7 AIRIV Indonesian enterprise modules:
1. DJP Coretax & e-Faktur 4.0 Compliance (PPN 12%, DPP Nilai Lain, NSFP Pool)
2. Indonesian SAK EMKM Accounting & Financial Reports (Neraca & Laba Rugi)
3. Indonesian Payroll & PPh 21 TER (PP 58/2023, BPJS TK & Kes, e-Bupot 21/26)
4. Tri-Gateway Payment Rails (Midtrans Snap, Xendit Invoice, PayPal REST API v2)
5. Indonesian Shipping Aggregator (Biteship & RajaOngkir 10+ Couriers & Resi Sync)
6. WhatsApp Business Messaging Engine (Fonnte & WAHA Offline Sandbox)
7. Retail & F&B Point of Sale (Dynamic QRIS, 58/80mm Thermal Receipts, WA Struk)

Features a 1-Click Unified Setup Wizard to configure store NPWP 16/NIK, payment rails, shipping origin, and WhatsApp messaging in under 2 minutes.
Zero External Server Overhead - 100% Odoo 18 Community Native - Always Free ($0.00).
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'base',
        'account',
        'sale',
        'stock',
        'point_of_sale',
        'airiv_tax_indonesia',
        'airiv_payroll_indonesia',
        'airiv_delivery_indonesia',
        'airiv_payment_indonesia',
        'airiv_whatsapp_indonesia',
        'airiv_pos_indonesia',
        'airiv_accounting_indonesia',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/umkm_onboarding_wizard_views.xml',
        'views/umkm_dashboard_views.xml',
        'views/umkm_menu_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
