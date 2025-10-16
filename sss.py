"""
sss.py - Stealth Scraper Script (The Batmobile)
Copyright (c) 2023-2025 Volkan Sah
# Selenium Stealth Setup like a pro!
# catch me if you can!
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random

def enhance_stealth(driver):
    """Zusätzliche Stealth-Optimierungen via CDP - SOFORT nach Driver-Erstellung"""
    
    # CDP Commands für erweiterte Tarnung - Wird vor Seitenladung ausgeführt
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
        // WebDriver Flag komplett entfernen
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined,
        });
        
        // Chrome Runtime properties simulieren
        if (!window.chrome) {
            window.chrome = {
                runtime: {},
                loadTimes: function() {},
                csi: function() {},
                app: {}
            };
        }
        
        // Plugins array modifizieren für Realismus
        Object.defineProperty(navigator, 'plugins', {
            get: () => [
                {0: {type: "application/pdf", suffixes: "pdf", description: "Portable Document Format"}, name: "Chrome PDF Plugin", filename: "internal-pdf-viewer"},
                {0: {type: "application/x-google-chrome-pdf", suffixes: "pdf", description: "Portable Document Format"}, name: "Chrome PDF Viewer", filename: "mhjfbmdgcfjbbpaeojofohoefgiehjai"},
                {0: {type: "application/x-nacl", suffixes: "", description: "Native Client Executable"}, name: "Native Client", filename: "internal-nacl-plugin"}
            ],
        });
        
        // Languages property für deutsche Lokalisierung
        Object.defineProperty(navigator, 'languages', {
            get: () => ['de-DE', 'de', 'en-US', 'en'],
        });
        
        // Permissions API patchen
        const originalQuery = window.navigator.permissions.query;
        window.navigator.permissions.query = (parameters) => (
            parameters.name === 'notifications' ?
                Promise.resolve({ state: Notification.permission }) :
                originalQuery(parameters)
        );
        
        // Notification permissions setzen
        Object.defineProperty(Notification, 'permission', {
            get: () => 'default',
        });
        
        // WebGL Vendor und Renderer maskieren
        const getParameter = WebGLRenderingContext.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {
            if (parameter === 37445) {
                return 'Intel Inc.';
            }
            if (parameter === 37446) {
                return 'Intel Iris OpenGL Engine';
            }
            return getParameter(parameter);
        };
        
        // Canvas Fingerprinting protection
        const toDataURL = HTMLCanvasElement.prototype.toDataURL;
        HTMLCanvasElement.prototype.toDataURL = function(type) {
            const context = this.getContext('2d');
            context.fillText('Stealth Mode', 10, 10);
            return toDataURL.call(this, type);
        };
        
        console.log('Stealth mode activated');
        '''
    })
    
    # Zusätzliche CDP Optimierungen
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": driver.execute_script("return navigator.userAgent"),
        "platform": "Win32"
    })
    
    # Automations-Flags entfernen
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
        // Weitere Automation Flags entfernen
        Object.defineProperty(navigator, 'webdriver', { get: () => false });
        Object.defineProperty(navigator, '__webdriver_evaluate', { get: () => false });
        Object.defineProperty(navigator, '__selenium_evaluate', { get: () => false });
        Object.defineProperty(navigator, '__webdriver_script_function', { get: () => false });
        Object.defineProperty(navigator, '__webdriver_script_func', { get: () => false });
        Object.defineProperty(navigator, '__webdriver_script_fn', { get: () => false });
        '''
    })

def create_stealth_driver():
    """Erstellt einen maximal getarnten Chrome Driver mit integrierten CDP-Optimierungen"""
    
    options = Options()
    
    # === Headless & Display ===
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    
    # === Security & Sandbox (für Server) ===
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # === Stealth & Anti-Detection ===
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-automation")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-component-extensions-with-background-pages")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-renderer-backgrounding")
    
    # === Realistische User Agents ===
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    options.add_argument(f"--user-agent={random.choice(user_agents)}")
    
    # === Weitere Tarnungs-Optionen ===
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # === Language & Location ===
    options.add_argument("--lang=de-DE")
    options.add_argument("--accept-lang=de-DE,de;q=0.9,en;q=0.8")
    
    # === WebDriver Properties überschreiben ===
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
        "webrtc.multiple_routes_enabled": False,
        "webrtc.nonproxied_udp_enabled": False,
        "intl.accept_languages": "de-DE,de"
    })
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    #  WICHTIG: CDP Stealth-Optimierungen SOFORT nach Driver-Erstellung 
    enhance_stealth(driver)
    
    return driver

def stealth_xpath_extraction(url):
    """XPath Extraction mit vollständig integriertem Stealth"""
    driver = create_stealth_driver()
    
    try:
        # Zufällige Verzögerung vor Seitenaufruf
        import time
        time.sleep(random.uniform(1, 3))
        
        driver.get(url)
        
        # Warte bis Seite geladen
        driver.implicitly_wait(10)
        
        # Simuliere menschliches Verhalten
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 3);")
        time.sleep(random.uniform(0.3, 1.2))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 1.5);")
        time.sleep(random.uniform(0.2, 0.8))
        
        # XPaths extrahieren
        elements = driver.find_elements("xpath", "//*[@id or text() or @class]")
        xpaths = []
        
        for element in elements[:100]:  # Begrenze für Performance
            try:
                xpath = driver.execute_script("""
                function getElementXPath(element) {
                    if (element.id !== '')
                        return '//*[@id=\"' + element.id + '\"]';
                    if (element === document.body)
                        return '/html/body';
                    
                    var ix = 0;
                    var siblings = element.parentNode.childNodes;
                    
                    for (var i = 0; i < siblings.length; i++) {
                        var sibling = siblings[i];
                        if (sibling === element)
                            return getElementXPath(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + (ix + 1) + ']';
                        if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
                            ix++;
                    }
                }
                return getElementXPath(arguments[0]);
                """, element)
                
                if xpath and len(xpath) < 500:  # Vermeide zu lange XPaths
                    xpaths.append({
                        'xpath': xpath,
                        'tag': element.tag_name,
                        'text': element.text.strip()[:80] if element.text else '',
                        'id': element.get_attribute('id'),
                        'classes': element.get_attribute('class')
                    })
                    
            except Exception as e:
                continue
                
        return xpaths
        
    finally:
        driver.quit()

# Test-Funktion
def test_stealth_detection(url="https://httpbin.org/headers"):
    """Testet ob der Stealth-Modus funktioniert"""
    driver = create_stealth_driver()
    
    try:
        driver.get(url)
        
        # Teste ob Webdriver erkannt wird
        webdriver_detected = driver.execute_script("return navigator.webdriver")
        chrome_runtime = driver.execute_script("return window.chrome && window.chrome.runtime")
        
        print(f"   Stealth Test Results:")
        print(f"   Webdriver detected: {webdriver_detected}")
        print(f"   Chrome runtime: {chrome_runtime}")
        print(f"   User-Agent: {driver.execute_script('return navigator.userAgent')}")
        
        if webdriver_detected is None and chrome_runtime:
            print("✅ Stealth Mode: AKTIVIERT")
        else:
            print("❌ Stealth Mode: FEHLGESCHLAGEN")
            
    finally:
        driver.quit()

if __name__ == "__main__":
    # Teste den Stealth-Modus
    test_stealth_detection()
    
    # XPath Extraction testen
    print("\n Starte XPath Extraction...")
    url = "https://httpbin.org/html"
    xpaths = stealth_xpath_extraction(url)
    
    print(f"✅ Gefunden: {len(xpaths)} XPaths")
    for item in xpaths[:8]:
        print(f"📍 {item['xpath']}")
        if item['text']:
            print(f"   Text: {item['text']}")
        if item['id']:
            print(f"   ID: #{item['id']}")
        print("---")
