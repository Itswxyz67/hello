import os
from playwright.sync_api import sync_playwright

def screenshot_python():
    output_dir = "python_outputs"
    screenshot_dir = "python_screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    files = sorted([f for f in os.listdir(output_dir) if f.endswith(".txt")])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(device_scale_factor=2)
        page = context.new_page()
        for filename in files:
            name = filename[:-4]
            with open(os.path.join(output_dir, filename), "r") as f:
                content = f.read()

            # Simple terminal-like HTML
            html_content = f"""
            <html>
            <body style="background-color: black; color: #FFFFFF; font-family: 'Courier New', monospace; padding: 30px; white-space: pre-wrap; font-size: 18px;">
{content}
            </body>
            </html>
            """
            page.set_content(html_content)
            screenshot_path = os.path.join(screenshot_dir, name + ".png")
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot taken for {name}")
        browser.close()

if __name__ == "__main__":
    screenshot_python()
