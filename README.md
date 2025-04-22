# 🐾 Pupdater – pip manager for Django Admin

**Pupdater** is a pluggable Django admin app that allows you to view, check, and upgrade installed Python packages en Requirements.txt directly from the Django admin interface.

## Features
- View all installed packages with metadata
- Highlight outdated packages
- Update packages with a single click (superuser-only)
- Save and compare snapshots of your environment
- Export snapshots to JSON, CSV, TXT or XLSX
- Compare two snapshots side-by-side
- Compare current environment to `requirements.txt` and manage differences
- Integrated with Jazzmin (if available), but works standalone

## Installation

1. Install via pip:
```bash
pip install git+https://github.com/WilkoRi/pupdater.git
