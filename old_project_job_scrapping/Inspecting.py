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