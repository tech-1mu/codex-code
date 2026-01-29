# Playwright MCP Demo

This demo shows a minimal Playwright script that launches Chromium, navigates to
`https://example.com`, captures a screenshot, and prints the page title.

## Run locally

1. Install Playwright (Python):

```bash
python -m pip install playwright
python -m playwright install
```

2. Run the demo script:

```bash
python demo/playwright_mcp_demo.py
```

The screenshot will be saved to `artifacts/example.png`.

## Run via MCP (Codex)

If you are running inside the Codex environment, you can use the MCP browser tool
with a script like this:

```python
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com")
        await page.screenshot(path="artifacts/example.png", full_page=True)
        await browser.close()
```

Pass the script to the `mcp__browser_tools__run_playwright_script` tool and include
`ports_to_forward: []` since this demo only visits a public URL.
