"""
CMIFC.py - Catch Me If You Can! (Stealth Scraper Script)
Copyright (c) 2023-2025 Volkan Sah

# Advanced Headless Selenium Stealth Agent for evidence collection.
# Fully human-like behavior and advanced hardware fingerprint spoofing.
# Motto: Catch me if you can!
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

def enhance_stealth(driver):
    """Applies advanced stealth optimizations with consistent hardware spoofing via CDP."""
    
    # Define plausible hardware profiles based on common User Agents
    hardware_profiles = {
        'windows': {
            'webgl_vendor': 'Intel Inc.',
            'webgl_renderer': 'Intel Iris OpenGL Engine',
            'platform': 'Win32',
            'hardware_concurrency': random.choice([4, 6, 8, 12]),
            'device_memory': random.choice([4, 8, 16])
        },
        'mac': {
            'webgl_vendor': 'Apple Inc.',
            'webgl_renderer': random.choice(['Apple M1 Pro', 'AMD Radeon Pro']),
            'platform': 'MacIntel',
            'hardware_concurrency': random.choice([8, 10, 12]),
            'device_memory': random.choice([8, 16, 32])
        },
        'linux': {
            # More generic, but still masked values for X11/Linux
            'webgl_vendor': 'Mesa/X.org',
            'webgl_renderer': 'llvmpipe (LLVM 11.0.1, 256 bits)',
            'platform': 'Linux x86_64',
            'hardware_concurrency': random.choice([2, 4, 8]),
            'device_memory': random.choice([2, 4, 8])
        }
    }
    
    # Determine the current profile based on the selected User-Agent (from options)
    current_ua = driver.execute_script("return navigator.userAgent")
    if "Windows" in current_ua:
        profile = hardware_profiles['windows']
    elif "Macintosh" in current_ua:
        profile = hardware_profiles['mac']
    else:
        profile = hardware_profiles['linux']
        
    # 1. CDP Command: Set platform consistently (fixes the largest anti-bot flag)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": current_ua,
        "platform": profile['platform']
    })

    # 2. CDP Command: Inject ALL JavaScript patches in ONE GO (eliminates redundancy and race conditions)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': f'''
        // --- Core Stealth: Remove WebDriver Flag ---
        Object.defineProperty(navigator, 'webdriver', {{
            get: () => undefined,
        }});
        
        // --- Automation Flags (Redundant but Safe) ---
        Object.defineProperty(navigator, '__webdriver_evaluate', {{ get: () => false }});
        Object.defineProperty(navigator, '__selenium_evaluate', {{ get: () => false }});
        Object.defineProperty(navigator, '__webdriver_script_function', {{ get: () => false }});
        
        // --- Hardware Spoofing (Consistent with UA) ---
        Object.defineProperty(navigator, 'hardwareConcurrency', {{
            get: () => {profile['hardware_concurrency']},
        }});
        Object.defineProperty(navigator, 'deviceMemory', {{
            get: () => {profile['device_memory']},
        }});
        
        // --- WebGL Spoofing (Critical for consistency) ---
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {{
            if (parameter === 37445) {{ // GL_VENDOR
                return '{profile['webgl_vendor']}';
            }}
            if (parameter === 37446) {{ // GL_RENDERER
                return '{profile['webgl_renderer']}';
            }}
            return getParameter.call(this, parameter);
        }};
        
        // --- WebGL Debug Info Removal ---
        const getExtension = WebGLRenderingContext.prototype.getExtension;
        WebGLRenderingContext.prototype.getExtension = function(name) {{
            if (name === 'WEBGL_debug_renderer_info') {{
                return null;
            }}
            return getExtension.call(this, name);
        }};
        
        // --- Canvas Fingerprinting with Noise ---
        const toDataURL = HTMLCanvasElement.prototype.toDataURL;
        HTMLCanvasElement.prototype.toDataURL = function(type) {{
            const context = this.getContext('2d');
            if (this.width > 0 && this.height > 0) {{
                const imageData = context.getImageData(0, 0, this.width, this.height);
                for (let i = 0; i < imageData.data.length; i += 4) {{
                    // Add subtle random noise (0.1% chance)
                    if (Math.random() < 0.001) {{
                        imageData.data[i] = Math.random() * 255;
                        imageData.data[i + 1] = Math.random() * 255;
                        imageData.data[i + 2] = Math.random() * 255;
                    }}
                }}
                context.putImageData(imageData, 0, 0);
            }}
            return toDataURL.call(this, type);
        }};
        
        // --- Standard Browser Properties Spoofing ---
        if (!window.chrome) {{ window.chrome = {{ runtime: {{}}, loadTimes: function() {{}}, csi: function() {{}} }}; }}
        Object.defineProperty(navigator, 'plugins', {{ get: () => [{{0: {{type: "application/pdf"}}, name: "Chrome PDF Plugin"}}] }});
        Object.defineProperty(navigator, 'languages', {{ get: () => ['de-DE', 'de', 'en-US', 'en'] }});
        const originalQuery = window.navigator.permissions.query;
        window.navigator.permissions.query = (p) => (p.name === 'notifications' ? Promise.resolve({{ state: Notification.permission }}) : originalQuery(p));
        Object.defineProperty(Notification, 'permission', {{ get: () => 'default' }});
        
        console.log('CMIFC Advanced Stealth Mode activated.');
        '''
    })

def human_like_behavior(driver, page_type="forum"):
    """Simulates human behavior based on page type to avoid bot pattern detection."""
    
    # Random initial delay (human needs time to orient)
    time.sleep(random.uniform(1.5, 4.0))
    
    if page_type == "forum":
        _forum_behavior(driver)
    elif page_type == "article":
        _reading_behavior(driver)
    else:
        _generic_browsing(driver)

def _forum_behavior(driver):
    """Simulates forum user behavior: quick scan, random back-scroll, irregular pauses."""
    
    # 1. Initial quick scroll
    initial_scroll = random.randint(300, 800)
    driver.execute_script(f"window.scrollTo(0, {initial_scroll});")
    time.sleep(random.uniform(0.8, 1.8))
    
    # 2. Back-scroll (typical human: "Did I miss anything?")
    if random.random() > 0.3:
        back_scroll = random.randint(50, 200)
        driver.execute_script(f"window.scrollBy(0, -{back_scroll});")
        time.sleep(random.uniform(0.3, 0.7))
    
    # 3. Irregular continued scrolling with reading pauses
    scroll_steps = random.randint(3, 8)
    current_position = initial_scroll
    
    for step in range(scroll_steps):
        scroll_amount = random.randint(200, 500)
        current_position += scroll_amount
        
        # Smooth scrolling simulation (can be slower, up to 0.3s)
        driver.execute_script(f"window.scrollTo({{ top: {current_position}, behavior: 'smooth' }});")
        
        # Random pause between scrolls (simulating reading/distraction)
        time.sleep(random.uniform(0.5, 2.5))
        
        # Occasional micro-scroll back
        if random.random() > 0.7:
            micro_back = random.randint(10, 50)
            driver.execute_script(f"window.scrollBy(0, -{micro_back});")
            time.sleep(random.uniform(0.1, 0.3))

def _reading_behavior(driver):
    """Simulates article reading behavior: slower, more uniform scrolls, long pauses."""
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    
    scroll_position = 0
    while scroll_position < total_height - viewport_height:
        scroll_step = random.randint(150, 300) # Smaller steps like actual reading
        scroll_position += scroll_step
        
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        
        # Longer pauses while "reading"
        read_time = random.uniform(1.5, 4.0)
        time.sleep(read_time)

def _generic_browsing(driver):
    """Simple human browsing behavior for generic pages."""
    scroll_actions = random.randint(2, 5)
    for i in range(scroll_actions):
        scroll_y = random.randint(200, 600)
        driver.execute_script(f"window.scrollBy(0, {scroll_y});")
        time.sleep(random.uniform(0.5, 1.5))

def human_like_click(driver, element):
    """Simulates a human click with pre- and post-delays and scroll into view."""
    # Pre-click delay (targeting)
    time.sleep(random.uniform(0.3, 1.2))
    
    # Bring element into viewport smoothly
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(random.uniform(0.2, 0.5))
    
    # Perform click
    element.click()
    
    # Post-click delay (waiting for page load/response)
    post_click_delay = random.uniform(1.5, 3.5)
    time.sleep(post_click_delay)

def create_stealth_driver():
    """Creates a maximally concealed Chrome Driver with integrated CDP optimizations."""
    
    options = Options()
    
    # === Headless & Display ===
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    
    # === Security & Sandbox (for servers) ===
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # === Stealth & Anti-Detection Flags ===
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-automation")
    options.add_argument("--disable-extensions")
    # ... other standard stealth arguments retained
    
    # === Realistic User Agents ===
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    options.add_argument(f"--user-agent={random.choice(user_agents)}")
    
    # === Further Concealment Options ===
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # === Language & Location ===
    options.add_argument("--lang=de-DE")
    options.add_argument("--accept-lang=de-DE,de;q=0.9,en;q=0.8")
    
    # === WebDriver Properties Overrides (Prefs) ===
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
    
    # CRITICAL: CDP Stealth optimizations immediately after driver creation
    enhance_stealth(driver)
    
    return driver

def stealth_xpath_extraction(url, page_type="generic"):
    """XPath Extraction with fully integrated stealth and human-like behavior."""
    driver = create_stealth_driver()
    
    try:
        # Initial delay before navigation
        time.sleep(random.uniform(2, 5))
        
        driver.get(url)
        
        # Wait until page loaded
        driver.implicitly_wait(10)
        
        # Simulate human-like behavior based on page type
        human_like_behavior(driver, page_type)
        
        # Extract XPaths with human-like pauses
        elements = driver.find_elements("xpath", "//*[@id or text() or @class]")
        xpaths = []
        
        for i, element in enumerate(elements[:80]): # Limit for performance
            # Random delay between element processing
            if i % random.randint(3, 8) == 0:
                time.sleep(random.uniform(0.1, 0.4))
            
            try:
                # JavaScript to generate robust XPaths
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
                
                if xpath and len(xpath) < 500: # Avoid overly long XPaths
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

def test_stealth_detection(url="https://httpbin.org/headers"):
    """Tests if the stealth mode is functioning correctly."""
    driver = create_stealth_driver()
    
    try:
        driver.get(url)
        
        # Test for key detection vectors
        webdriver_detected = driver.execute_script("return navigator.webdriver")
        chrome_runtime = driver.execute_script("return window.chrome && window.chrome.runtime")
        hardware_concurrency = driver.execute_script("return navigator.hardwareConcurrency")
        device_memory = driver.execute_script("return navigator.deviceMemory")
        
        print(f"🔍 CMIFC Stealth Test Results:")
        print(f"  Webdriver detected: {webdriver_detected}") # Should be undefined/None
        print(f"  Chrome runtime: {chrome_runtime}") # Should be an object
        print(f"  Hardware Concurrency: {hardware_concurrency}") # Should be masked
        print(f"  Device Memory: {device_memory}") # Should be masked
        print(f"  User-Agent: {driver.execute_script('return navigator.userAgent')}")
        print(f"  Platform (JS Check): {driver.execute_script('return navigator.platform')}")
        
        if webdriver_detected is None and chrome_runtime:
            print(" Stealth Mode: ACTIVATED and CONSISTENT.")
        else:
            print("❌ Stealth Mode: FAILED.")
            
    finally:
        driver.quit()

if __name__ == "__main__":
    print("🚀 CMIFC Agent - Advanced Concealment System Activated (The Batmobile)")
    
    # Test the Stealth Mode
    test_stealth_detection()
    
    # Test XPath Extraction
    print("\n🎯 Starting XPath Extraction Test...")
    url = "https://httpbin.org/html"
    xpaths = stealth_xpath_extraction(url, page_type="article")
    
    print(f" Found: {len(xpaths)} XPaths")
    for item in xpaths[:8]:
        print(f"📍 {item['xpath']}")
        if item['text']:
            print(f"    Text: {item['text']}")
        if item['id']:
            print(f"    ID: #{item['id']}")
        print("---")
