# Indonesia UMKM All-in-One Business & Compliance Engine

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Bundle: 7--in--1 UMKM](https://img.shields.io/badge/Bundle-7--in--1%20Indonesian%20Suite-red.svg)](https://airiv.id)

The definitive, all-in-one Indonesian business, regulatory, and commerce meta-engine built specifically for **Odoo 18.0 Community Edition**. Provides a 1-click installation package bundling all 7 specialized Indonesian localization modules into a unified executive control center.

---

## 7 Core Pillars Included

1. **DJP Coretax & e-Faktur 4.0 (`airiv_tax_indonesia`)**: PPN 12% statutory calculations, DPP Nilai Lain, 16-digit NIK/NPWP validation, and NSFP tax number management.
2. **SAK EMKM Accounting (`airiv_accounting_indonesia`)**: Standard IAI SAK EMKM chart of accounts, Laporan Laba Rugi, Laporan Posisi Keuangan (Neraca), and PPh Final UMKM 0.5% (PP 55/2022).
3. **Indonesian Payroll & PPh 21 TER (`airiv_payroll_indonesia`)**: Monthly TER Rates (Categories A, B, C under PP 58/2023), statutory BPJS Ketenagakerjaan & Kesehatan calculations, and DJP e-Bupot 21/26 batch export.
4. **Tri-Gateway Payment Rails (`airiv_payment_indonesia`)**: Midtrans Snap, Xendit Invoice, and PayPal REST API v2 for seamless IDR and cross-border checkout.
5. **Indonesian Shipping Aggregator (`airiv_delivery_indonesia`)**: Direct Biteship & RajaOngkir API integration supporting 10+ local couriers (JNE, J&T, SiCepat, GoSend) and automated waybill (*Nomor Resi*) synchronization.
6. **WhatsApp Business Messaging (`airiv_whatsapp_indonesia`)**: Automated WhatsApp dispatch for order confirmations, Biteship tracking URLs, and customer invoices via Fonnte REST API and WAHA Docker with an Offline Sandbox Simulator.
7. **Retail & F&B Point of Sale (`airiv_pos_indonesia`)**: Dynamic on-screen QRIS display, 58mm/80mm ESC/POS thermal receipts with statutory PPN 12% breakdown, and 1-click WhatsApp digital receipt delivery.

---

## Validated Commercial Benchmark (End-to-End Scrutinized)

The complete Indonesian UMKM meta-engine was verified under live Odoo 18.0 Community conditions:

1. **8-Module Registry Discovery**: Verified all 8 modules installed and operational (`airiv_tax_indonesia`, `airiv_payroll_indonesia`, `airiv_delivery_indonesia`, `airiv_payment_indonesia`, `airiv_whatsapp_indonesia`, `airiv_pos_indonesia`, `airiv_accounting_indonesia`, `airiv_umkm_indonesia`).
2. **Master Onboarding Wizard**: Configured store NPWP 16/NIK `3171012345670001`, 80mm thermal receipt width, PPN 12% compliance, and WhatsApp Sandbox Mode in a single transaction.
3. **Statutory Tax & Accounting**: Verified PPN 12% calculation (DPP Rp 1.000.000 $\rightarrow$ PPN Rp 120.000) and SAK EMKM Laporan Laba Rugi & Posisi Keuangan (Neraca) generation.
4. **Payroll & PPh 21 TER**: Computed Gross Rp 15.000.000 with TER A (6% = Rp 900.000) and statutory BPJS (Rp 520.423), resulting in Take-Home-Pay of Rp 13.579.577,00.
5. **POS & Dynamic QRIS**: Processed POS order with dynamic QRIS payment and dispatched WhatsApp digital receipt.
6. **Logistics & Gateway Rails**: Validated Midtrans, Xendit, and Biteship automated courier synchronization.

---

## Installation & Odoo Configuration Guide

1. **Deploy Module**:
   Place `airiv_umkm_indonesia` inside your Odoo `custom_addons` directory (all 7 sub-modules will be resolved automatically).

2. **Activate Module**:
   * Navigate to **Apps > Update Apps List**.
   * Search for `Indonesia UMKM All-in-One Business & Compliance Engine` and click **Activate**.

3. **Run 1-Click Setup Wizard**:
   * Open the **UMKM Center** app from the App Drawer.
   * Click **Panduan Setup Wizard** to configure company NPWP 16/NIK, thermal receipt width, and WhatsApp mode in under 2 minutes.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (100% Native, App Drawer Integrated) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | All 7 AIRIV Indonesian Modules + Community Base |
| **Server Overhead** | Zero (Native ORM, direct browser & REST streams) |
