import os
from playwright.sync_api import sync_playwright

def take_screenshots():
    os.makedirs("screenshots", exist_ok=True)
    html_dir = os.path.abspath("html_pages")
    files = sorted([f for f in os.listdir(html_dir) if f.endswith(".html")])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for filename in files:
            file_path = f"file://{os.path.join(html_dir, filename)}"
            screenshot_path = os.path.join("screenshots", filename.replace(".html", ".png"))
            print(f"Taking screenshot of {filename}...")
            page.goto(file_path)
            # Wait a bit for external resources if any (like YouTube or Maps iFrames)
            page.wait_for_timeout(2000)
            page.screenshot(path=screenshot_path)
        browser.close()

if __name__ == "__main__":
    take_screenshots()
