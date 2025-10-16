# Stealth Scraper — README

**sss.py — Stealth Scraper Script (Like a Batmobile)**

> **Critical legal notice — read this before anything else.**

---

## Project summary

A compact Python testbed for browser fingerprint research and authorized red/blue team exercises. Short, pragmatic, and a bit cheeky. Use only with explicit permission.

## ⚠️ Critical warning

This project contains code designed to alter or mask browser fingerprints and to bypass simple detection techniques.
Do **not** use this code to access systems you do not own or do not have explicit, written permission to test.
Illegal or unethical use is strictly prohibited. You accept full responsibility for any actions taken with this code.

## Purpose & intended use

* For security research, QA, authorized penetration testing, red/blue team training, and education.
* Not for abuse. Not for bypassing access controls.

## Safe / Compliance mode (recommended)

Set a runtime flag to disable all stealth features. Use this for sensitive tests or when you lack full permissions.

**Example (environment variable):**

```bash
export SSS_SAFE_MODE=1      # Unix
set SSS_SAFE_MODE=1         # Windows (cmd)
```

**Example (python snippet):**

```python
import os
SAFE_MODE = os.getenv("SSS_SAFE_MODE") == "1"

if SAFE_MODE:
    # minimal, non-evasive driver
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    def create_stealth_driver():
        opts = Options()
        opts.add_argument("--window-size=1920,1080")
        return webdriver.Chrome(options=opts)
else:
    from sss import create_stealth_driver
```

## Quick features

* Create a Chrome WebDriver with optional stealth tweaks.
* Inject CDP scripts to modify fingerprint surfaces (unless SAFE_MODE).
* Simulate simple human interactions: scrolling and random delays.
* Helpers: `create_stealth_driver()`, `stealth_xpath_extraction(url)`, `test_stealth_detection(url)`.

## Requirements

* Python 3.8+
* Google Chrome and matching chromedriver.
* `selenium` Python package.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate       # or .venv\Scripts\activate on Windows
pip install --upgrade pip
pip install selenium
```

Place a matching `chromedriver` in your PATH or use a driver manager.

## Quick start (safe)

Run tests only against endpoints you control or where you have authorization.

```bash
SSS_SAFE_MODE=1 python sss.py
```

### Usage (brief)

```python
from sss import create_stealth_driver, stealth_xpath_extraction

driver = create_stealth_driver()
try:
    driver.get("https://example.com")    # only authorized targets
    data = stealth_xpath_extraction("https://example.com")
    print(len(data))
finally:
    driver.quit()
```

### Note

The modular sss.py is only an example of how to build a headless bot that works like a human. The parsing of data is limited to extracting XPath and CSS selectors to analyze sites with your external tools. Against Kiddies!

## Consent / Permission template

Copy-paste this into an email or doc when requesting testing permission.

```
Permission for Browser Testing and Data Collection

This document grants [Your Name / Organization] permission to perform browser testing and data access on [Target Domain / URL], limited to the scope defined below.

Scope:
- Automated browsing for research and testing.
- Collection of basic page metadata and DOM structure.
- No attempts to access authenticated areas, private user data, or bypass controls.

Duration:
- From [start date] to [end date].

Signed:
[Target Owner Name], [Title]
[Signature or Email Confirmation]
[Date]
```

## Audit & reporting (short)

* Keep screenshots, request logs, and timestamps.
* Preserve written consent.
* If you find a vulnerability, follow coordinated disclosure.

## Ethics & best practice

* Stop immediately if requested by the target owner.
* Minimize load. Respect rate limits and crawl-delay.
* Prefer APIs over scraping when possible.

## Limitations

* Experimental. Results vary by Chrome version and target site.
* Not a guaranteed bypass for modern anti-bot systems.
* Headless mode may reduce site functionality.

## Liability, Warranty & Indemnity (READ CAREFULLY)

### No Warranty

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. THE AUTHORS, MAINTAINERS, CONTRIBUTORS, AND DISTRIBUTORS DISCLAIM ALL WARRANTIES, INCLUDING BUT NOT LIMITED TO IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.

### No Liability

IN NO EVENT SHALL THE AUTHORS, MAINTAINERS, CONTRIBUTORS, OR DISTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR CONSEQUENTIAL DAMAGES, LOSS OF PROFITS, LOSS OF DATA, INTERRUPTION OF BUSINESS, OR ANY OTHER DAMAGES WHATSOEVER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, ARISING OUT OF OR IN CONNECTION WITH THE USE OR MISUSE OF THIS SOFTWARE.

### Permitted Use Only (Strict)

This project is intended solely for lawful security research, authorized penetration testing, red/blue team training, and educational use. You must obtain **explicit, written permission** from the owner of any systems you test. Do not use this software to access systems, data, or content you are not authorized to access.

### Indemnity

By using this software you agree to indemnify, defend, and hold harmless the authors, maintainers, contributors, and distributors from and against any claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys’ fees) arising from or related to your use, misuse, or distribution of the software.

### Export & Legal Compliance

You are responsible for ensuring compliance with all applicable laws, regulations, and export controls in your jurisdiction and the jurisdiction of any target.

### Auditability & Consent

Keep written proof of consent when conducting tests. Maintain logs, timestamps, and contact information of the authorizing party. If requested by an owner or authority, you must provide evidence of authorization.

### No Professional Advice

This text is a template only and does not constitute legal advice. Consult a qualified attorney for a binding liability strategy.

## Contributor Agreement (short)

By submitting code, documentation, issues, or other contributions to this repository you confirm:

1. You have the right to contribute the content.
2. You grant the project a perpetual, worldwide, non-exclusive, royalty-free license to use your contribution.
3. You agree that your contribution does not violate any law or third-party right.
4. You agree to the Liability & Indemnity section above and will indemnify the project for claims arising from your contributions.

If you do not accept these terms, do not submit a contribution.

## Permission checklist (for targets)

Copy into your permission email or attach to requests.

* Target domain / IPs:
* Allowed actions: (e.g., crawl public pages, collect DOM, no auth bypass)
* Time window:
* Rate limits:
* Contact person (name + email):
* Written confirmation (attach email or signed doc)

## License & Attribution

Code credits: Volkan Sah (2023–2025). MIT license
