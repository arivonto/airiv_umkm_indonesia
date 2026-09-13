# AIRIV UMKM Indonesia - PP 55/2022 Final PPh 0.5% & Omzet Ledger

[![Odoo](https://img.shields.io/badge/Odoo-18.0-714B67.svg)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-0f766e.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-AIRIV-0891b2.svg)](https://airiv.id)
[![GitHub Actions](https://github.com/arivonto/airiv_umkm_indonesia/actions/workflows/odoo-appstore-ci.yml/badge.svg?branch=18.0)](https://github.com/arivonto/airiv_umkm_indonesia/actions)
[![Apps Store Ready](https://img.shields.io/badge/Odoo%20Apps%20Store-ready-22c55e.svg)](https://apps.odoo.com/)

`airiv_umkm_indonesia` is an Indonesian UMKM turnover ledger and final income tax compliance module for Odoo 18 Community. It helps micro, small, and medium businesses record monthly gross turnover, track the annual Rp 500 million non-taxable threshold for individual taxpayers, calculate PPh Final 0.5%, and monitor e-Billing/NTPN payment evidence.

The module is built around practical Indonesian tax operations under PP 55/2022: monthly omzet recording, taxpayer type classification, automatic taxable base calculation, dashboard-level reconciliation, and payment status tracking.

## Core Capabilities

- Monthly gross turnover ledger for Indonesian UMKM taxpayers.
- Taxpayer type handling for individual taxpayers and business entities.
- Rp 500 million annual non-taxable turnover threshold for individual taxpayers.
- Automatic taxable base calculation when cumulative turnover exceeds the threshold.
- PPh Final 0.5% computation for eligible taxable turnover.
- e-Billing code and NTPN payment evidence fields.
- Payment state workflow from draft to calculated, billed, and paid.
- Executive dashboard for year-to-date turnover, tax base, tax obligation, and threshold progress.
- Native Odoo mail thread and activity tracking for turnover records.
- AIRIV OS-ready app identity, iconography, and store packaging.

## Architecture

```text
Monthly UMKM Turnover Entry
  |
  |-- taxpayer type
  |-- fiscal year and month
  |-- gross turnover
  |-- billing code and NTPN
  v
AIRIV UMKM Tax Calculation Layer
  |
  |-- cumulative prior turnover
  |-- Rp 500 million threshold logic
  |-- taxable DPP calculation
  |-- PPh Final 0.5% calculation
  v
Dashboard and Audit Layer
  |
  |-- year-to-date turnover
  |-- non-taxable portion
  |-- taxable base
  |-- total final income tax
  |-- payment status tracking
```

The module stays native to Odoo. It uses Odoo models, computed fields, standard views, access rules, and company currency handling without requiring an external tax engine.

## Feature & Workflow Automation

### 1. Monthly Turnover Recording

Users record gross turnover per fiscal month. Each record stores:

- fiscal year,
- fiscal month,
- taxpayer type,
- company,
- gross turnover,
- payment status,
- billing code,
- NTPN,
- payment date.

### 2. PP 55/2022 Threshold Calculation

For individual taxpayers, the module calculates the cumulative prior turnover in the same fiscal year and applies the Rp 500 million annual threshold. The taxable base is automatically split between:

- non-taxable turnover portion,
- taxable DPP portion,
- PPh Final 0.5% amount.

For business entities, the module treats the turnover as taxable from the first rupiah based on the selected taxpayer type.

### 3. Payment Evidence Workflow

The record state guides tax administration:

- `Draft` for initial turnover entry,
- `Calculated` after tax computation,
- `Billed` when e-Billing code is available,
- `Paid` after NTPN and payment date are confirmed.

### 4. Executive UMKM Dashboard

The dashboard aggregates current-year UMKM compliance indicators:

- total year-to-date gross turnover,
- non-taxable turnover portion,
- taxable DPP,
- total PPh Final obligation,
- threshold utilization percentage,
- threshold exceeded status.

## Technical Specifications

| Area | Specification |
| --- | --- |
| Odoo version | 18.0 Community |
| Module name | `airiv_umkm_indonesia` |
| License | LGPL-3 |
| Author | AIRIV |
| Website | https://airiv.id |
| Repository | https://github.com/arivonto/airiv_umkm_indonesia |
| Main models | `airiv.umkm.turnover`, `airiv.umkm.dashboard` |
| Business domain | Indonesian UMKM bookkeeping and PP 55/2022 final income tax |
| Tax rate | PPh Final 0.5% |
| Individual taxpayer threshold | Rp 500,000,000 annual gross turnover |
| Dependencies | `base`, `account`, `mail`, `airiv_os_core` |
| Store assets | `static/description/icon.png`, `static/description/banner.png`, `static/description/index.html` |

## Installation Guidance

1. Clone the repository on branch `18.0`.

```bash
git clone --branch 18.0 git@github.com:arivonto/airiv_umkm_indonesia.git
```

2. Add the module folder to your Odoo addons path.

```text
airiv_umkm_indonesia/airiv_umkm_indonesia
```

3. Restart Odoo and update the apps list.

4. Install **AIRIV UMKM Indonesia - PP 55/2022 Final PPh 0.5% & Omzet Ledger** from Apps.

5. Open **AIRIV UMKM Pajak** and start with the current fiscal year dashboard.

6. Create monthly turnover records before marking billing and payment evidence.

## Configuration Checklist

- Confirm the company currency is configured correctly.
- Choose the taxpayer type consistently: individual taxpayer or business entity.
- Enter monthly gross turnover in chronological order for the fiscal year.
- Review cumulative prior turnover before confirming the monthly calculation.
- Fill e-Billing code once generated in the official DJP channel.
- Fill NTPN and payment date after tax payment is completed.
- Reopen the dashboard to review year-to-date totals and threshold utilization.

## Repository Layout

```text
airiv_umkm_indonesia/
  __manifest__.py
  models/
    umkm_turnover.py
    umkm_dashboard.py
  security/
    ir.model.access.csv
  static/description/
    icon.png
    banner.png
    index.html
  views/
    umkm_turnover_views.xml
    umkm_dashboard_views.xml
    umkm_menu_views.xml
  wizard/
    umkm_onboarding_wizard.py
    umkm_onboarding_wizard_views.xml
```

## Contact Info

| Field | Details |
| --- | --- |
| Author | AIRIV |
| Website | https://airiv.id |
| GitHub | https://github.com/arivonto |
| Module repository | https://github.com/arivonto/airiv_umkm_indonesia |
| Odoo series | 18.0 |

## Quality Gate

This repository includes an Odoo Apps Store CI audit through GitHub Actions. The audit checks manifest metadata, required store assets, import safety, README presence, and Apps Store packaging readiness on branch `18.0`.
