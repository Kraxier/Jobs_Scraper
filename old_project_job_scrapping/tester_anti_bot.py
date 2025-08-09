import random
from pathlib import Path
from playwright.sync_api import sync_playwright

# Known anti-bot keywords in request URLs
ANTI_BOT_KEYWORDS = [
    "perimeterx", "datadome", "arkoselabs", "hcaptcha",
    "recaptcha", "cf_chl", "bot-detect", "shape", "humansecurity",
    "fingerprintjs", "mouseflow"
]

# Folder for screenshots
Path("screenshots").mkdir(exist_ok=True)

def log_request(request):
    req_url = request.url.lower()
    if any(keyword in req_url for keyword in ANTI_BOT_KEYWORDS):
        print(f"[POSSIBLE ANTI-BOT] {req_url}")
    else:
        print(f"[Request] {req_url}")

def fast_bot_mode(page):
    print("\n🚀 Running FAST BOT MODE")
    for i in range(5):
        page.mouse.move(100 + i * 50, 200)
        page.mouse.click(100 + i * 50, 200)

def slow_human_mode(page):
    print("\n🕵️ Running SLOW HUMAN MODE")
    for i in range(5):
        x, y = 100 + i * 50, 200
        page.mouse.move(x, y, steps=random.randint(10, 30))  # smooth movement
        page.wait_for_timeout(random.randint(500, 1500))  # thinking delay
        page.mouse.click(x, y, delay=random.randint(50, 200))  # slower click
        page.wait_for_timeout(random.randint(800, 2000))  # read time

def run_test(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # --- Fast bot test ---
        page = browser.new_page()
        page.on("request", log_request)
        print(f"\nVisiting {url} in FAST mode...")
        page.goto(url, wait_until="load")
        fast_bot_mode(page)
        page.wait_for_timeout(5000)  # observe site reaction
        page.screenshot(path="screenshots/fast_mode.png")
        page.close()

        # --- Slow human test ---
        page = browser.new_page()
        page.on("request", log_request)
        print(f"\nVisiting {url} in SLOW mode...")
        page.goto(url, wait_until="load")
        slow_human_mode(page)
        page.wait_for_timeout(5000)  # observe site reaction
        page.screenshot(path="screenshots/slow_mode.png")
        page.close()

        browser.close()

if __name__ == "__main__":
    run_test("https://ph.jora.com/j?sp=homepage&trigger_source=homepage&q=Mechatronics&l=")


r'''
Quick summary (one-liner)
The script opens the same job-search page twice, once doing fast bot-like interactions and once doing slow human-like interactions, logs every network request (and flags known anti-bot vendor URLs), and saves screenshots so you can see whether different behaviors trigger blocks/CAPTCHAs or different content.

Step-by-step explanation of the code and concepts
Imports and constants

random — used to add variability to movement/delays in slow mode (so behavior is not perfectly repetitive).

Path("screenshots").mkdir(...) — creates a folder to save screenshots of each run.

ANTI_BOT_KEYWORDS — a list of strings we consider “suspicious” (PerimeterX, Datadome, reCAPTCHA, etc.).
Concept: many anti-bot tools load JS from predictable URL paths; matching those URLs is a quick heuristic that “this site includes anti-bot/tracking code.”

log_request(request)

This function runs for every network request the page makes.

It lowercases the request URL and prints either [POSSIBLE ANTI-BOT] <url> (if it contains any keyword) or [Request] <url>.

Concept: network requests reveal what the site is doing (analytics, ads, bot protection). If a request goes to recaptcha or perimeterx, the site is loading that vendor’s JavaScript — evidence the vendor is present.

Interaction modes (fast vs slow)

fast_bot_mode(page):

Moves the mouse and clicks quickly with no waits — simulates a naive bot that performs instant actions.

Concept: fast, deterministic actions are low-entropy and often detected by behavior-based systems.

slow_human_mode(page):

Moves the mouse with steps (multi-step movement = smoother), waits random short periods, clicks with random delay, and waits more — simulates human reading and clicking patterns.

Concept: human interactions have jitter, pauses, and smooth movement; mimicking that can avoid behavior-triggered blocks.

run_test(url)

sync_playwright() context manager starts Playwright and ensures cleanup.

browser = p.chromium.launch(headless=False) launches a real browser window (not headless) — important because headless mode is often fingerprinted.

For each mode it:

new_page() and page.on("request", log_request) attach the network logger.

page.goto(url, wait_until="load") navigates to the page and waits for the browser load event (this waits until basic resources are loaded; not the same as waiting for all XHRs to finish).

Runs the interaction mode (fast or slow).

page.wait_for_timeout(5000) holds the session to observe any post-interaction effects (CAPTCHA popups or redirects).

page.screenshot(path="...") saves what the page looked like after the interaction.

page.close() then moves to the next test.

Finally it browser.close().

What each API call implies / why it matters
page.on("request", ...) — hooks into all network requests so you can inspect vendor URLs, timing, and detect anti-bot scripts.

wait_until="load" — waits for the document load event; sometimes you want networkidle or a wait_for_selector for the specific content instead.

page.mouse.move(x, y, steps=n) — if steps>1 Playwright generates intermediate coordinates producing smooth movement.

page.mouse.click(x, y, delay=d) — delay simulates the time the user keeps mouse button down; both delay and random waits make the action less bot-like.

page.screenshot(...) — visual evidence to compare whether a CAPTCHA or block appeared.

How to read your logs (the ones you pasted)
You posted many [Request] lines and a couple of [POSSIBLE ANTI-BOT] https://www.google.com/recaptcha/api2/aframe. Here’s what that tells us:

Lots of analytics / ad / tracking requests (google-analytics, googlesyndication, clarity.ms, cloudflareinsights, doubleclick, etc.)

This is normal for many modern sites: ads + analytics + session recording.

Presence alone ≠ blocking. It just means the site collects metrics and loads tracking scripts.

cdn-cgi/rum (Cloudflare RUM) and cloudflareinsights:

Cloudflare RUM is a Real User Monitoring script. Presence of Cloudflare tooling does not necessarily mean bot blocking — but Cloudflare also offers bot management on top of that.

[POSSIBLE ANTI-BOT] https://www.google.com/recaptcha/api2/aframe

The script flagged a reCAPTCHA URL. That means the page includes reCAPTCHA assets (often used for forms or when suspicious behavior is detected).

Important nuance: including reCAPTCHA JS does not mean every user sees a CAPTCHA. Many sites load the library for safety and only render the widget in certain flows or after suspicious events.

You saw no immediate block or redirect in logs and your fast run finished and produced the screenshot (so the page rendered). That means: even though reCAPTCHA code is present on the site, your run did not trigger an active block or forced CAPTCHA page.

So — is this site “heavily protected”? (based on your run)
Evidence of vendor scripts (reCAPTCHA, Cloudflare, Clarity, Google ad/analytics) → the site includes tracking and protection libraries.

But your fast mode did not get blocked or forced into CAPTCHA (you still got page requests and screenshots), which implies behavioral protection is not aggressively blocking your simple fast run.

Therefore: not heavily protected in behavioral terms. It has protection tooling available (reCAPTCHA etc.) that may trigger in some flows or if the site detects other patterns, but your quick test suggests moderate/low enforcement.

Limitations of this diagnostic (what it DOESN’T guarantee)
The script is a heuristic, not definitive:

It only looks for a small set of keywords — sites can use other vendors or custom endpoints you don’t flag.

It doesn’t inspect response content to detect soft blocks (pages that look normal but serve reduced or obfuscated data).

It clicks at fixed screen coordinates — if those hits don’t hit meaningful elements, the site might not see the same interaction data as a human clicking a real button.

Some protections trigger after sustained scraping (multiple pages / sessions). Running two quick visits may not trigger those.

Headedness: you used headless=False (good). Some protections still detect automation via more advanced fingerprinting (webRTC, fonts, WebGL, navigator properties). This script won’t detect fingerprinting directly.

Practical next steps (no code; actionable checklist)
Compare screenshots: check visually if any mode shows a CAPTCHA or an empty/placeholder result area.

Search the page DOM (manually in DevTools) for iframe or elements that reference "recaptcha" — if an iframe with recaptcha appears, that widget could appear conditionally.

Run several trials (different times / multiple pages): some protections trigger only after repeated fast requests.

Add content checks (conceptually): confirm the page contains the job titles/elements you expect — if the HTML is missing data in fast mode but appears in slow, that suggests behavior enforcement.

Watch for subtle blocks: look for responses with HTTP 403/429, or pages that render but with reduced content or error messages.

If you need more certainty: capture page.content() (HTML) after each run and compare; or capture network response codes to detect 403/429.

One last thing — what the logs specifically show you now
The site loads lots of analytics and ad/tracking scripts (normal).

It loads reCAPTCHA assets — so the capability to show CAPTCHA exists.

Your run didn’t trigger a visible CAPTCHA or block in fast mode, so behavioral detection is present as a library but the site did not (yet) actively block you.
'''