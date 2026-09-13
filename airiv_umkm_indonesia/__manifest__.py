# -*- coding: utf-8 -*-
{
    'name': 'AIRIV UMKM Indonesia - PP 55/2022 Final PPh 0.5% & Omzet Ledger',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'Buku Pembukuan Omzet UMKM, Threshold Bebas Pajak Rp 500 Juta, dan PPh Final 0.5% Sesuai PP 55/2022',
    'description': """
Modul Pembukuan dan Kepatuhan Pajak UMKM Indonesia Sesuai PP 55/2022:
- Pencatatan Omzet Bruto Bulanan (Wajib Pajak OP & Badan).
- Threshold Bebas Pajak Rp 500.000.000 per Tahun Pajak untuk Wajib Pajak Orang Pribadi.
- Perhitungan Otomatis PPh Final 0.5% atas Kelebihan Omzet di atas Rp 500 Juta.
- Executive Dashboard Rekonsiliasi & NTPN / Kode Billing DJP.
""",
    'author': 'AIRIV',
    'website': 'https://airiv.id',
    'url': 'https://github.com/arivonto/airiv_umkm_indonesia/blob/18.0/static/description/index.html',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'base',
        'account',
        'mail',
        'airiv_os_core',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/umkm_turnover_views.xml',
        'views/umkm_dashboard_views.xml',
        'views/umkm_menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
