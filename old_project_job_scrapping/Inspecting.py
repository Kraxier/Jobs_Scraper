# Inspection of the Website: or 🔹Manual Recon or Reconnaissance Phase
r'''
Exploring and Analyzing the Website is the Next Step 
'''

# Reflection in Understanding the Developer Tools:
    # There are Concept that i don't know yet What is the Used so Either I'm going to Focus if i only Encounter a Problem or Roadblocked instead of Absorbing All the Information
    # Too Much Overload in Information is Suck 


###################################### Understanding robot.txt ###########################################

r'''
1. Checking for robot.txt files:
    ✅ How to Identify the Location of robots.txt
    Per the Robots Exclusion Protocol(Documentation of Google Search Central), the location of a website’s robots.txt is always:
    https://<domain>/robots.txt
    📌 This file must live in the root of the domain, not in subdirectories.
    * The Documentation for the "Google Search Central"
    https://developers.google.com/search/docs/crawling-indexing/robots/intro

    Inside of https://ph.jora.com/robots.txt
    it Give me This part a Dictionary Term in term of python: 
        1. "User-agent:"
        2. "Disallow:"

    # Right now it give me this part 
    User-agent: *
    Disallow: /click

    # Chatgpt also Include the Sitemap: https://ph.jora.com/sitemap.xml
    i think this is the path of the website

    📌 What This Means:
    User-agent: * – Applies to all crawlers.
    Disallow: /click – Crawlers are not allowed to access any URLs that start with /click.
    Everything else is allowed. (I'm Safe)

    🔍 What's /click?
    This is usually a redirector or tracking endpoint (e.g., when someone clicks a job to go to an external site). 
    You’re not supposed to crawl or scrape this, which is fair because it might mess up their analytics or ad deals.
'''

###################################### Understanding Network Request (One of The DevTools) ###########################################

##### Research: 
##### Reflection:
# Currently It will not Affect the Workflow in term of Network Request I only think is Headers Part is only the Important thing
r'''
2. Using the Network Request:
    * Use browser developer tools (Network tab) to analyze:
            * Headers (e.g., User-Agent, Accept-Language, Sec-Fetch-*)
            * Cookies (e.g., __cf_bm for Cloudflare)
            * Dynamic tokens (CSRF, API keys)
            * JavaScript challenges (e.g., Cloudflare 5-second shield)

2.1 Understanding between Real Browser and Incognito Mode 
    Incognito Mode is for the Fresh User while the Real Browser i can go with Sessions and stuff 
 2. 📡 Network Tab
        Purpose: Monitor all HTTP requests (XHR/fetch, JS, CSS, images).
        Question: 
            1. What is XHR/Fetch, JS,CSS and Image 
        Use Cases:
            * Find hidden API endpoints serving data (look for XHR/Fetch requests).
            * Check request Headers (cookies, authentication tokens).
            * Analyze Response data (JSON, HTML, or XML payloads).
            * Filter requests by type (e.g., XHR, JS, Doc) or keyword.
            * Right-click a request → "Copy as cURL" to replicate in scripts.
        Reflection: 
            * I have some knowledge in this in terms of learning API Scrapping 
            * Every Time i click for the Job it Load Something 
                * I don't Know What kind of File is that 
                * Every Time I click there are Categories that i see
                    * Header
                    * Payload
                    * Preview
                    * Response
                    * Initiator
                    * Timing 
                    * Cookies 
                * I am Absolutely No Idea how i can use this 
            * There are "fetch" and "xhr" in term of HTTP Request 
            * every time i click in "fetch" type i see the Categories
            * Checking the Headers in term of "fetch"
                There are 2 Types of Header 
                    1. Response Header 
                    2. Request Header 
                What does it mean by This 2 type of Headers 
                What is the Relevance of this in term of Websrapping 
            * Analyzing Response Data Which is i can't see the JSON files only HTML 
            * Filtering Data there are no "JS" and "DOC" but there are certainly "xhr"
'''

######################################   🔍 Elements Tab  (One of The DevTools) ###########################################
r'''
    1. 🔍 Elements Tab 
        To Check for HTML Structure and CSS 
        Use Cases:
            Identify unique selectors (e.g., class, id, data-* attributes) for scraping.
            Verify dynamic changes to the DOM (e.g., content loaded via JavaScript).
            Right-click an element → "Copy" → Copy selector/XPath.
        
    Implementation:
        1. How To verify Whether it is Dynamic Changes? 
            [Knowledge in First Playwright JS]
        2. 
    Reflection:
        1. I'm Going to Scrape the 
            * Place
            * On Site
            Review(Optional)
            <p> Tag Problem with this is the Variation of How many P are in there
        2. IF i'm Going to Extract the <p> Tag Using some extraction 
            I Wonder How will i do that 
            * Maybe If they mention "Python" or "SQL" or "1-2" Experience 
            * Big Problem is the Text Extraction 

Basically Commonly Working in Extracting Data Later so I'm Going to think of this Later

'''
###################################### 📝 Console Tab (Ctrl+Shift+J / Cmd+Option+J) (One of The DevTools) ###########################################

r'''

Purpose: Execute JavaScript, debug, and view logs.
Use Cases:
    * Test CSS selectors: document.querySelectorAll(".product").
    * Check XPath: $x("//div[@class='price']").
    * Log errors (e.g., failed resource loads).

Reflection:
    I had no Idea how to Use This Dev Tools

'''

######################################📂 Sources Tab  (One of The DevTools) ###########################################

r'''

Purpose: Explore static files (HTML, JS, CSS).
Use Cases:
Review JavaScript for data-fetching logic.
Set breakpoints to debug dynamic content loading.

What is the use case of Static Files and how i can use that ?
'''

######################################📦 Application Tab(One of The DevTools) ###########################################

r'''
Purpose: Inspect stored data (cookies, localStorage, sessionStorage).
Use Cases:
Extract authentication tokens or session data.
Check localStorage for client-side data caching.
'''

######################################📱 Device Mode (Ctrl+Shift+M / Cmd+Shift+M) (One of The DevTools) ###########################################

r'''
Purpose: Emulate mobile devices and screen sizes.
Use Cases:
Test responsive layouts (may reveal hidden mobile-specific APIs).
'''



################## Research #############

r'''
1. Reconnaissance Phase
    Study the Protection:
        * Check robots.txt for allowed/disallowed paths. (Done)
        * Use browser developer tools (Network tab) to analyze:
            * Headers (e.g., User-Agent, Accept-Language, Sec-Fetch-*)
            * Cookies (e.g., __cf_bm for Cloudflare)
            * Dynamic tokens (CSRF, API keys)
            * JavaScript challenges (e.g., Cloudflare 5-second shield)

Identify Triggers:
Rapid requests, missing headers, headless browser signatures, or inconsistent mouse movements.

🧠 1. Understanding the Bot Protection Layers
Most modern anti-bot systems use multiple layers of detection:

a. IP Reputation
    Known bad IPs, VPNs, proxies, and data centers are often blocked.
    Too many requests from a single IP = rate-limiting or banning.
b. User-Agent & Headers Analysis
    Invalid or uncommon headers raise flags.
    Missing headers like Referer, Accept-Language, or User-Agent can be suspicious.
c. JavaScript Challenges
    Some sites require JS to run before granting access (e.g., Cloudflare's browser check).
d. Behavioral Analysis
    Tracks mouse movement, typing speed, scrolls, etc.
    Used heavily on login pages or checkout flows.
e. CAPTCHAs
    Google reCAPTCHA, hCaptcha, or puzzles to test for human interaction.

'''
r'''


Q: Are there legal or contractual restrictions (ToS, copyright, licensing)? Is the data sensitive or personal?
Answer:
Notes: Check Terms of Service, copyright, and data protection laws (e.g., GDPR). If data is personal or copyrighted, consult legal before scraping.

Q: What does robots.txt say? Any disallowed paths or crawl-delay directives?
Answer:
Notes: Always check https://<domain>/robots.txt. Respect disallow rules and crawl-delay where practical. If blocked but permitted through other channels, consider contacting site owners.

Q: Is there a sitemap (/sitemap.xml) or internal search that lists content? Are there RSS/feeds or APIs?
Answer:
Notes: Sitemaps and feeds are authoritative sources for URLs. APIs are preferable over scraping.


Q: Is the data present in HTML (static) or injected by JavaScript (client-rendered)? Show CSS selectors/XPath for each field if possible.
Answer:
Notes: Use “View source” vs DevTools Network/Elements. If data is in HTML responses or JSON blobs, prefer HTTP requests. If client-rendered, consider using the site’s API or a headless browser.

APIs & network endpoints
Q: Are there internal APIs used by the site (XHR/Fetch calls)? What are the request and response formats (URLs, parameters, headers)?
Answer:
Notes: Inspect Network tab for XHR/Fetch calls. Capture request URL, method (GET/POST), headers (auth, cookies), payload, and JSON response examples.


Authentication & sessions
Q: Does content require login? What auth type (form, OAuth, token)? How long do sessions last and what cookies are used?
Answer:
Notes: Document login flow, CSRF tokens, refresh tokens, multi-factor, and whether scraping an account violates ToS.

Rate limits & throttling
Q: Are there rate limits or anti-scraping responses (429, 403)? What is a safe request rhythm?
Answer:
Notes: Test politely. Start slow, observe HTTP codes and response times. Use exponential backoff, randomized delays, and obey crawl-delay if present.

Anti-bot protections
Q: Does the site use CAPTCHAs, WAFs (Cloudflare), JavaScript fingerprinting, or bot-detection services?
Answer:
Notes: Look for CAPTCHA pages, challenge responses, repeated 403/502 from security layers. If strong anti-bot measures exist, consider contacting the site or using official APIs.


Required headers, cookies, and emulation
Q: Which headers or cookies are necessary? Do you need to emulate a browser (User-Agent, Accept-Language, Referer)?
Answer:
Notes: Sites sometimes rely on headers or cookies to serve correct content. Reproduce minimal realistic headers; don’t fake identity to impersonate other users.


Throttling, concurrency & proxies
Q: Do you need proxies or distributed requests? How many concurrent connections are safe?
Answer:
Notes: Use proxies only when required and legally acceptable. Keep concurrency low and increase only after monitoring.
'''


r'''
# Web Scraping — Website Investigation Q\&A Form

> Use this Q\&A as a discovery checklist when preparing to scrape a website. Fill each "Answer" with the site's specific details. Below each question is a short explanation and suggested actions.

---

## 1) Project overview

**Q:** What is the goal of the scrape?

**Answer:**

**Notes:** Describe the business / research goal (eg. price monitoring, content aggregation, lead collection, sentiment analysis). This drives scope, frequency, and legal risk.

---

## 2) Target site identity

**Q:** What is the target website (domain + sections)? Provide example page URLs.

**Answer:**

**Notes:** List the base domain(s), subdomains, and 5–10 representative URLs to inspect.

---

## 3) Legal & ethical checks

**Q:** Are there legal or contractual restrictions (ToS, copyright, licensing)? Is the data sensitive or personal?

**Answer:**

**Notes:** Check Terms of Service, copyright, and data protection laws (e.g., GDPR). If data is personal or copyrighted, consult legal before scraping.

---

## 4) robots.txt and crawl policies

**Q:** What does `robots.txt` say? Any disallowed paths or crawl-delay directives?

**Answer:**

**Notes:** Always check `https://<domain>/robots.txt`. Respect disallow rules and crawl-delay where practical. If blocked but permitted through other channels, consider contacting site owners.

---

## 5) Sitemaps & discovery

**Q:** Is there a sitemap (`/sitemap.xml`) or internal search that lists content? Are there RSS/feeds or APIs?

**Answer:**

**Notes:** Sitemaps and feeds are authoritative sources for URLs. APIs are preferable over scraping.

---

## 6) Page types & templates

**Q:** What different page templates exist (listing pages, detail pages, pagination, search results)? How many templates?

**Answer:**

**Notes:** Identify distinct templates (e.g., product listing, product detail, blog post). Each template may need a different extraction rule.

---

## 7) URL patterns & pagination

**Q:** What are the URL schemes? How does pagination work (page numbers, offsets, cursors)?

**Answer:**

**Notes:** Recognize patterns to generate URL lists. Look for query parameters (`?page=2`, `offset=50`) or cursor tokens used by AJAX.

---

## 8) Data to extract

**Q:** List the exact data fields needed (field name, example, type — string/number/date/image/HTML).

**Answer:**

**Notes:** Be explicit (e.g., `product_name`, `price`, `currency`, `sku`, `availability`, `date_published`). Include sample expected formats.

---

## 9) Location of data on page

**Q:** Is the data present in HTML (static) or injected by JavaScript (client-rendered)? Show CSS selectors/XPath for each field if possible.

**Answer:**

**Notes:** Use “View source” vs DevTools Network/Elements. If data is in HTML responses or JSON blobs, prefer HTTP requests. If client-rendered, consider using the site’s API or a headless browser.

---

## 10) APIs & network endpoints

**Q:** Are there internal APIs used by the site (XHR/Fetch calls)? What are the request and response formats (URLs, parameters, headers)?

**Answer:**

**Notes:** Inspect Network tab for XHR/Fetch calls. Capture request URL, method (GET/POST), headers (auth, cookies), payload, and JSON response examples.

---

## 11) Authentication & sessions

**Q:** Does content require login? What auth type (form, OAuth, token)? How long do sessions last and what cookies are used?

**Answer:**

**Notes:** Document login flow, CSRF tokens, refresh tokens, multi-factor, and whether scraping an account violates ToS.

---

## 12) Rate limits & throttling

**Q:** Are there rate limits or anti-scraping responses (429, 403)? What is a safe request rhythm?

**Answer:**

**Notes:** Test politely. Start slow, observe HTTP codes and response times. Use exponential backoff, randomized delays, and obey `crawl-delay` if present.

---

## 13) Anti-bot protections

**Q:** Does the site use CAPTCHAs, WAFs (Cloudflare), JavaScript fingerprinting, or bot-detection services?

**Answer:**

**Notes:** Look for CAPTCHA pages, challenge responses, repeated 403/502 from security layers. If strong anti-bot measures exist, consider contacting the site or using official APIs.

---

## 14) Required headers, cookies, and emulation

**Q:** Which headers or cookies are necessary? Do you need to emulate a browser (User-Agent, Accept-Language, Referer)?

**Answer:**

**Notes:** Sites sometimes rely on headers or cookies to serve correct content. Reproduce minimal realistic headers; don’t fake identity to impersonate other users.

---

## 15) Throttling, concurrency & proxies

**Q:** Do you need proxies or distributed requests? How many concurrent connections are safe?

**Answer:**

**Notes:** Use proxies only when required and legally acceptable. Keep concurrency low and increase only after monitoring.

---

## 16) Data quality & validation

**Q:** How will you validate extracted data (schema checks, deduplication, sample checks)? What are acceptable error rates?

**Answer:**

**Notes:** Plan validation rules, required fields, type coercion, and fallback strategies for missing data.

---

## 17) Storage & format

**Q:** Where will scraped data be stored (CSV, JSON, DB)? What structure and retention policy?

**Answer:**

**Notes:** Consider normalization, unique keys, and whether to store raw HTML/JSON for audit.

---

## 18) Scheduling & update frequency

**Q:** How often should the site be scraped (one-time, hourly, daily)? Can you use incremental updates (only new/changed items)?

**Answer:**

**Notes:** Frequency should match data volatility and respect site load. Prefer incremental scraping using timestamps or ETags when possible.

---

## 19) Error handling & monitoring

**Q:** How will failures be handled (retries, alerts)? What metrics will you monitor (success rate, latency, HTTP errors)?

**Answer:**

**Notes:** Implement retries with backoff, logging, and alerts for rising error rates or blocks.

---

## 20) Testing plan

**Q:** How will you test the scraper (unit tests, integration, sample runs)? Which pages will be used as canonical test cases?

**Answer:**

**Notes:** Keep a test suite of representative pages and expected outputs. Re-run tests after any code or template changes.

---

## 21) Tech stack & tools

**Q:** What tools/frameworks will you use (requests/BeautifulSoup, Scrapy, Playwright, Selenium, Puppeteer, Headless Chrome)?

**Answer:**

**Notes:** Select tools based on complexity: static HTML -> requests + parser; dynamic JS -> Playwright or headless browser; large-scale -> Scrapy/rotating proxies.

---

## 22) Ethical contact & escalation

**Q:** If scraping is ambiguous or blocked, who will you contact at the site? What information will you include in the contact?

**Answer:**

**Notes:** Prepare a polite email explaining purpose, data needed, expected request rates, and offering to use an API or data feed.

---

## 23) Final risk checklist (quick binary checks)

* [ ] TOS allows scraping for this use
* [ ] Data is not personal/sensitive or you have consent
* [ ] robots.txt allows crawling of required paths
* [ ] No legal/contractual restrictions
* [ ] Anti-bot is manageable or site provides API
* [ ] Rate limits/account constraints identified

---

## Appendix: quick commands & inspection tips

* `curl -I https://example.com/page` — check headers and server responses
* `curl https://example.com/robots.txt` — view robots rules
* DevTools Network tab — find XHR/Fetch endpoints and JSON responses
* View page source vs Elements — spot client-rendered content
* Search for `sitemap.xml`, RSS feeds, or `/api/` endpoints
* Use `wget --mirror` or `httrack` for cautious local discovery (only when permitted)

---

*When you're ready, I can convert your completed Q\&A into an actionable scraping plan (URL generator, extraction rules, sample code) — tell me which target site and paste your answers.*

'''