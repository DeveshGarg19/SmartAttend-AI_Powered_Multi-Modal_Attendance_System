import time
import sys
from playwright.sync_api import sync_playwright

def keep_alive(url):
    print(f"Connecting to Streamlit App: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            print("Page loaded. Waiting for app WebSocket connection...")
            time.sleep(10)

            # Check if Streamlit sleep page is showing
            content = page.content().lower()
            if "app has gone to sleep" in content or "get this app back up" in content or "wake up" in content:
                print("App was found sleeping! Looking for wake-up button...")
                # Search for typical Streamlit Cloud wake-up buttons
                buttons = page.query_selector_all("button")
                woke_up = False
                for btn in buttons:
                    txt = btn.inner_text().strip()
                    if "get this app back up" in txt.lower() or "wake" in txt.lower():
                        print(f"Clicking wake-up button: '{txt}'")
                        btn.click()
                        woke_up = True
                        break
                
                if woke_up:
                    print("Clicked wake-up button. Waiting 60s for app container to boot...")
                    time.sleep(60)
            else:
                print("App is alive and active! WebSocket session successfully registered.")
                
        except Exception as e:
            print(f"Error during ping: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    app_url = sys.argv[1] if len(sys.argv) > 1 else "https://smartattendai.streamlit.app"
    keep_alive(app_url)
