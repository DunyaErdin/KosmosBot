from playwright.sync_api import sync_playwright
from colorama import Fore,Style,init
import random
from rich.console import Console
from rich.live import Live
from rich.text import Text
import time
import os

init(autoreset=True)

ascii_logo = [
    "██╗  ██╗ ██████╗ ███████╗███╗   ███╗ ██████╗ ███████╗██████╗  ██████╗ ████████╗",
    "██║ ██╔╝██╔═══██╗██╔════╝████╗ ████║██╔═══██╗██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝",
    "█████╔╝ ██║   ██║███████╗██╔████╔██║██║   ██║███████╗██████╔╝██║   ██║   ██║   ",
    "██╔═██╗ ██║   ██║╚════██║██║╚██╔╝██║██║   ██║╚════██║██╔══██╗██║   ██║   ██║   ",
    "██║  ██╗╚██████╔╝███████║██║ ╚═╝ ██║╚██████╔╝███████║██████╔╝╚██████╔╝   ██║   ",
    "╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝    ╚═╝   "
]

def show_logo():
    for line in ascii_logo:
        print(Fore.CYAN + line)

def colorful_signature():


    show_logo()

    print(Fore.CYAN)
    print(Fore.YELLOW + "👨‍💻  Işık Dünya Erdin - Yazılım Geliştirici" + Fore.RESET)
    print(Fore.MAGENTA + "💼  Python | Playwright | ASP.NET Core | C#" + Fore.RESET)
    print(Fore.BLUE + "🌍  Trakya Ruhuyla Kodlanmıştır" + Fore.RESET)
    print(Fore.LIGHTWHITE_EX + "🔗  GitHub   : " + Fore.LIGHTGREEN_EX + "https://github.com/DunyaErdin")
    print(Fore.LIGHTWHITE_EX + "📧  E-posta  : " + Fore.LIGHTGREEN_EX + "isikdunya5@gmail.com")
    print(Fore.LIGHTWHITE_EX + "📸  Instagram: " + Fore.LIGHTGREEN_EX + "https://instagram.com/thrakidunya")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)

    

def main():
    with sync_playwright() as p:
        browser =  p.chromium.launch_persistent_context(
            headless=False,
            user_data_dir=r"C:\playwright",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            channel="chrome",
            no_viewport=True,
            args=[
                "--disable-blink-features=AutomationControlled",  # Bot tespiti (navigator.webdriver) için
                "--disable-infobars",  # "Chrome is being controlled..." uyarısını engeller
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-web-security",
                "--disable-features=IsolateOrigins,site-per-process",
                "--start-maximized",  # Tarayıcıyı tam ekran başlatır
                "--window-position=0,0",
                "--window-size=1280,800",  # İnsansı viewport
                "--disable-background-timer-throttling",
                "--disable-backgrounding-occluded-windows",
                "--disable-renderer-backgrounding",
                "--mute-audio",  # Opsiyonel
                "--disable-popup-blocking",
                "--disable-extensions",  # Bazı botlara özel eklentiler devre dışı
                "--hide-scrollbars",
                "--lang=tr-TR",  # Dil ayarı
                "--blink-settings=imagesEnabled=true",  # Görsel içerikler yüklensin (insansı davranış)
            ])
        print("Browser Başlatıldı")
        print("context oluşturulyor...")
        
        print("Tarayıcı çalıştırılıyor...")
        print("Tarayıcıya context yapısı dahil ediliyor...")
        page =  browser.new_page()
        print("Bot tespiti azaltma işlemleri başlatılıyor...")
        page.add_init_script("""
        (() => {
            Object.defineProperty(navigator, 'WebDriver', { get: () => undefined });
            Object.defineProperty(navigator, 'languages', { get: () => ['tr-TR', 'tr'] });
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 4 });
            Object.defineProperty(navigator, 'mimeTypes',    { get: () => [1,2,3] });
            Object.defineProperty(navigator, 'platform',     { get: () => 'Win32' });
            Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });
            Object.defineProperty(navigator, 'maxTouchPoints',{ get: () => 1 });
            window.chrome = { runtime: {} };
            navigator.connection = { downlink: 10, effectiveType: "4g", rtt: 50, saveData: false, type: "wifi" };
            // Permissions API patch
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) =>
                parameters.name === 'notifications'
                ? Promise.resolve({ state: Notification.permission })
                : originalQuery(parameters);
            // WebGL Patch
            const getParameter = WebGLRenderingContext.prototype.getParameter;
            WebGLRenderingContext.prototype.getParameter = function(parameter) {
                if (parameter === 37445) return "Google Inc. (Intel)";
                if (parameter === 37446) return "ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x000046A8) Direct3D11 vs_5_0 ps_5_0, D3D11)";
                return getParameter.call(this, parameter);
            };
             const realCanPlayType = HTMLVideoElement.prototype.canPlayType;
            HTMLVideoElement.prototype.canPlayType = function(type) {
                if (/(mp4|h264|avc1)/i.test(type)) {
                 return "probably";
                }
             return realCanPlayType.call(this, type);
            };
        })();
""")

        
        print("İşlemler başarıyla tamamlandı.")
        print("Siteye gidiliyor...")
        page.goto("https://www.google.com/")
        page.wait_for_timeout(random.uniform(2,3))  # Gerçek kullanıcı gibi bekle
        page.goto("https://kosmosvize.com.tr/#", referer="https://www.google.com/")
        
        webgl_vendor = page.evaluate('''() => {
            const canvas = document.createElement('canvas');
            const gl = canvas.getContext('webgl');
            return gl.getParameter(gl.VENDOR);
        }''')
        print("WebGL Vendor:", webgl_vendor)
        value = page.evaluate("() => navigator.webdriver")
        print("navigator.webdriver:", value)
        
        print("Site başarıyla çalıştı.")
        print("Uygulama Çalıştırılıyor...")
        #os.system('cls' if os.name == 'nt' else 'clear')
        #colorful_signature()
        print("-----------------Kosmos Bota Hoşgeldiniz-----------------")
        start = input("Otomasyonu başlatmak için (Y) harfine tıklayın")
        
        if start.lower()=="y":
            
        
            page.wait_for_timeout(random.uniform(50,60))
            page.mouse.move(100, 200)
            page.wait_for_timeout(random.uniform(2,3))
            page.mouse.move(150, 220)
            page.wait_for_timeout(random.uniform(4,5))
            page.click("xpath=/html/body/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div/div[3]/div[1]/span/button")
            page.wait_for_timeout(random.uniform(2,5))
            page.mouse.move(100, 100)
            page.wait_for_timeout(2,3)
            
            page.keyboard.press("Tab")
            page.mouse.move(random.randint(100,150),random.randint(151,200))
            page.click("xpath=/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")
            page.wait_for_timeout(4,5)
            page.click("xpath=/html/body/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div/div[3]/div[2]/span/button")
            page.wait_for_timeout(2,3)
            page.mouse.move(100,200)
            for i in range(2):
                if i == 1:
                    page.locator("xpath=/html/body/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div/div[2]/div/div[3]/form/div/div[1]/fieldset/div/span/div/div[2]/header/span[3]").click()
                spans = page.locator("span.cell.day").all()
            
                for span in spans:
                     class_attr = span.get_attribute("class")
                     if class_attr and "disabled" not in class_attr  and "blank" not in class_attr:
                        text=span.inner_text()
                        print(f"Açık gün : {text}")
                        print("Açık gün bulundu")
                 

main()       
        