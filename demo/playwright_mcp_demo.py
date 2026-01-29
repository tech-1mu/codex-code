"""Playwright MCP demo script.

Launches Chromium, opens example.com, captures a screenshot, and prints the page title.
"""

import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


async def main() -> None:
    output_dir = Path("artifacts")
    output_dir.mkdir(exist_ok=True)
    screenshot_path = output_dir / "example.png"

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com", wait_until="domcontentloaded")
        await page.set_viewport_size({"width": 1280, "height": 720})
        await page.screenshot(path=str(screenshot_path), full_page=True)
        title = await page.title()
        await browser.close()

    print(f"Saved screenshot to {screenshot_path} (title: {title})")


if __name__ == "__main__":
    asyncio.run(main())
