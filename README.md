# CMIFC - Catch Me If You Can! 

###### **Advanced Headless Selenium Stealth Agent for Evidence Collection**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://selenium.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

 
> A fully human-like browser automation agent with advanced hardware fingerprint spoofing capabilities.

---

## ⚠️ Critical warning

This project contains code designed to alter or mask browser fingerprints and to bypass bot detection techniques.
Do **not** use this code to access systems you do not own or do not have explicit, written permission to test!
Illegal or unethical use is strictly prohibited. You accept full responsibility for any actions taken with this code.

## Purpose & intended use

* For security research, QA, authorized penetration testing, red/blue team training, and education.
* Not for abuse. Not for bypassing access controls!

---


##  Overview

CMIFC (Catch Me If You Can) is an advanced stealth scraping framework designed to bypass sophisticated anti-bot detection systems. It combines hardware fingerprint spoofing, human-like behavior simulation, and comprehensive browser automation concealment.

## 👑 Features 👑

###  Advanced Stealth Technology
- **Hardware Fingerprint Spoofing**: Consistent WebGL, CPU, and memory profiling
- **CDP-based Concealment**: Chrome DevTools Protocol optimizations
- **Canvas Fingerprinting Protection**: Randomized pixel noise injection
- **WebGL Debug Removal**: Blocks `WEBGL_debug_renderer_info` detection
- **Automation Flag Elimination**: Removes all Selenium/WebDriver traces

###  Human Behavior Simulation
- **Page-Type Specific Behavior**: Different patterns for forums, articles, generic sites
- **Realistic Scroll Patterns**: Irregular scrolling with micro-movements and pauses
- **Natural Click Delays**: Pre- and post-click timing variations
- **Reading Simulation**: Variable pause durations mimicking human reading speeds

###  Browser Environment Spoofing
- **Dynamic User-Agent Rotation**: Windows, Mac, Linux profiles
- **Language Localization**: German/English language preferences
- **Hardware Consistency**: Platform-specific hardware profiles
- **Plugin Simulation**: Realistic browser plugin arrays

##  Requirements

```bash
pip install selenium
```

**System Requirements:**
- Chrome/Chromium browser
- ChromeDriver (compatible with your Chrome version)
- Python 3.8+

## 🛠️ Installation
1. ***Download CMIFC.py**
2. **Install ChromeDriver:**
   - Download from [ChromeDriver website](https://chromedriver.chromium.org/)
   - Ensure it's in your PATH or specify the path in the script

3. **Verify installation:**
```bash
python CMIFC.py
```

##  Usage

### Basic XPath Extraction
```python
from CMIFC import stealth_xpath_extraction

# Extract XPaths from a website
xpaths = stealth_xpath_extraction("https://example.com", page_type="article")

for item in xpaths:
    print(f"XPath: {item['xpath']}")
    print(f"Tag: {item['tag']}")
    print(f"Text: {item['text']}")
```

### Custom Stealth Driver
```python
from CMIFC import create_stealth_driver, human_like_behavior

driver = create_stealth_driver()
try:
    driver.get("https://target-site.com")
    human_like_behavior(driver, "forum")
    # Your automation code here
finally:
    driver.quit()
```

### Stealth Testing
```python
from CMIFC import test_stealth_detection

# Test your stealth configuration
test_stealth_detection("https://bot.sannysoft.com")
```

##  Configuration

### Page Type Behaviors
- **`forum`**: Quick scanning with back-scrolls and irregular pauses
- **`article`**: Slow, methodical reading with long pauses
- **`generic`**: Standard browsing with random scroll patterns

### Hardware Profiles
The script automatically selects appropriate hardware profiles based on User-Agent:
- **Windows**: Intel hardware, 4-16GB RAM
- **Mac**: Apple Silicon/AMD, 8-32GB RAM  
- **Linux**: Generic Mesa/X.org, 2-8GB RAM

##  Advanced Features

### Human-Like Click Simulation
```python
from CMIFC import human_like_click

element = driver.find_element("xpath", "//button")
human_like_click(driver, element)
```

### Custom Behavior Patterns
```python
def custom_behavior(driver):
    # Implement your own human behavior simulation
    pass
```

##  Stealth Verification

The script includes comprehensive testing to verify stealth effectiveness:

```python
test_stealth_detection()
```

**Expected Output:**
```
🔍 CMIFC Stealth Test Results:
  Webdriver detected: None
  Chrome runtime: True
  Hardware Concurrency: 8
  Device Memory: 16
  ✅ Stealth Mode: ACTIVATED and CONSISTENT.
```

## ⚠️ Legal & Ethical Usage ⚠️

**Important Disclaimer:**
- This tool is designed for **ethical security research**, **penetration testing**, and **authorized data collection**
- Always respect `robots.txt`, terms of service, and applicable laws
- Obtain proper authorization before testing any systems
- The authors are not responsible for misuse of this tool

### Intended Use Cases
- ✅ Security research and penetration testing
- ✅ Authorized web application testing
- ✅ Competitive analysis (where permitted)
- ✅ Academic research
- ✅ Evidence collection for legal purposes

### Prohibited Use Cases
- ❌ Unauthorized scraping
- ❌ Denial of service attacks
- ❌ Credential stuffing
- ❌ Fraudulent activities
- ❌ Violating terms of service

##  Detection Avoidance

CMIFC employs multiple layers of concealment:

1. **Browser Automation Flags**: Complete removal of WebDriver indicators
2. **Hardware Consistency**: Matching User-Agent with hardware capabilities
3. **Behavioral Patterns**: Human-like interaction timing and patterns
4. **Fingerprint Spoofing**: Canvas, WebGL, and audio context protection
5. **Network Characteristics**: Realistic browser fingerprinting

##  Troubleshooting

### Common Issues

1. **ChromeDriver Version Mismatch**
   ```bash
   # Check Chrome version
   google-chrome --version
   # Download matching ChromeDriver version
   ```

2. **Headless Detection**
   - Use `--headless=new` flag for modern headless mode
   - Ensure all stealth optimizations are applied

3. **Performance Optimization**
   - Limit element processing with `elements[:80]`
   - Adjust random delay ranges for your use case


##  Acknowledgments

- Selenium WebDriver team for robust browser automation
- Chrome DevTools Protocol for advanced browser control
- Security researchers advancing anti-bot detection

---

**Catch Me If You Can!** 

*For educational and authorized security research purposes only.*

### Note

The modular file is only an example of how to build a headless bot that works like a human. The parsing of data is limited to extracting XPath and CSS selectors to analyze sites with your external tools. Against Kiddies!

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
