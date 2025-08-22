# Client Intake — Fillable Form Template (Google Forms / Typeform)

Use this template to create a client intake form you can share in proposals or send to prospective clients. Below each field I indicate the recommended *question type* and whether it should be *required*.

---

## Form title
**Project Intake — Web Data / Scraping Project**

**Form description (subtitle):**
Please fill this form with as much detail as possible. If you'd rather, we can review this live in a 30‑minute kickoff call — select that option at the end.

---

### 1) Contact information
- **Full name** — *Short answer* — **Required**
- **Company / Organization** — *Short answer*
- **Email** — *Short answer* — **Required**
- **Phone / Slack / Preferred channel** — *Short answer*

### 2) Project overview
- **What is the main goal of this project?** — *Paragraph* — **Required**
  *Hint:* e.g., price monitoring, lead generation, market research.

- **Who will use the data and for what?** — *Paragraph* — **Optional**

- **Is this a one-time data pull or ongoing?** — *Multiple choice* — **Required**
  - One-time
  - Daily
  - Hourly
  - Weekly
  - Other (please specify)

### 3) Data & sources
- **Target websites / sample URLs** — *Paragraph* — **Required**
  *Please paste 5–10 representative URLs (or more). If you prefer, upload a list.*

- **Which fields do you need?** — *Checkboxes (multi-select) + "Other (specify)"* — **Required**
  - Title / Name
  - Price / Cost
  - Availability / Stock
  - SKU / Product ID
  - Rating / Reviews
  - Description / Specifications
  - Images (links)
  - Published date
  - Seller / Vendor
  - Contact information / leads
  - Link / URL
  - Other (please describe)

- **Do you need historical (backfill) data? If yes — how far back?** — *Short answer* — **Optional**

- **Approx. how many records/pages do you expect initially and per update?** — *Short answer* — **Required**
  *Example answer:* 10k initial, 1k/day updates.

### 4) Access & technical
- **Are the pages behind a login?** — *Multiple choice* — **Required**
  - No
  - Yes — basic login (username/password)
  - Yes — 2FA / OAuth / SSO (describe)

- **Do you have an API we can use instead?** — *Multiple choice* — **Required**
  - No
  - Yes — provide docs / keys (upload field or paste link)

- **Is the site heavily dynamic (content loads via JavaScript)?** — *Multiple choice* — **Required**
  - No (mostly static HTML)
  - Yes (dynamic / requires headless browser)
  - Not sure — please check (I will verify)

- **Known anti-bot protections (CAPTCHA, rate limits, IP blocks)?** — *Paragraph* — **Optional**

### 5) Legal & privacy
- **Do you have permission to collect/use this data?** — *Multiple choice* — **Required**
  - Yes
  - No / Unsure — please check

- **Does any of the data include PII or confidential information?** — *Multiple choice* — **Required**
  - No
  - Yes — describe how it should be handled

### 6) Deliverables, timeline, budget
- **Desired deliverables** — *Checkboxes* — **Required**
  - Raw CSV/JSON
  - Database dump (Postgres/MySQL)
  - Google Sheet
  - API endpoint
  - Dashboard (BI)
  - ETL pipeline (automated)
  - Prototype sample (5–10 records)
  - Other (specify)

- **Desired timeline / start date** — *Date + Short answer* — **Required**

- **Budget or price range (optional but helpful)** — *Short answer* — **Optional**

### 7) Maintenance & support
- **Do you want ongoing monitoring and maintenance?** — *Multiple choice* — **Required**
  - No — one-time only
  - Yes — monthly support
  - Yes — quarterly check-ins
  - Decide after prototype

- **Preferred point of contact and communication channel** — *Short answer* — **Required**

### 8) Acceptance & next steps
- **How will you consider this project "done"? (Acceptance criteria)** — *Paragraph* — **Required**
  *Examples:* 95% coverage of required fields, daily updates within 24 hours, sample dataset approved.

- **Would you like a 30-minute kickoff call to review these answers and get a prototype?** — *Multiple choice* — **Required**
  - Yes — please propose times
  - No — proceed by message

---

## Form settings & extras (Google Forms / Typeform tips)
- **Make contact fields required.**
- **Add a file-upload question** for clients who want to attach sample spreadsheets or lists of URLs.
- **Use conditional logic:** if user says login required → show additional fields to collect test credentials or auth details.
- **Add a final "review & confirm" screen** that asks for approval to proceed and agreement to your standard terms (e.g., privacy, ToS check).
- **Welcome screen:** short summary of how long the form takes ("~5–10 minutes").

---

# One‑Page Discovery Summary (Template)

Copy this one-page summary after the kickoff or when the client approves the form answers. Keep it short, single page, easy to approve.

```
Project: [Project Title]
Client: [Client Name / Company]
Prepared by: [Your Name]
Date: [YYYY-MM-DD]

----------------------
1) Project Goal (1–2 sentences)
[Concise statement of what success looks like.]

2) Priority Deliverables & Format
- Must-have fields: [title, price, url, timestamp]
- Nice-to-have: [images, seller, rating]
- Delivery: [CSV + Postgres dump + API]
- Frequency: [daily / one-time / hourly]

3) Data Sources (examples / sample URLs)
- Primary: [https://example.com/category/page1]
- Secondary: [https://example.com/shop/...]
- Notes: [login required / dynamic / known limits]

4) Scope & Constraints
- Includes: [list what you will collect]
- Excludes: [images processing, large historical backfills > X rows, ML labeling]
- Legal: [client confirms permission OR I will verify robots.txt and ToS]

5) Acceptance Criteria (what "done" means)
- At least X% records include required fields.
- Prototype sample (N rows) approved by client.
- Delivery format validated by client.

6) Milestones & Timeline
- Milestone 1 — Discovery & prototype: Deliver sample (5–10 records) — ETA: [date]
- Milestone 2 — Full scraping & data cleaning — ETA: [date]
- Milestone 3 — Automation & handover (cron/API) — ETA: [date]

7) Budget & Payment
- Estimated cost: [USD amount] (work to completion OR per milestone)
- Payment terms: [50% on prototype, 50% on delivery] or [net 15 after acceptance]

8) Maintenance & Warranty
- 30-day bug-fix warranty after delivery.
- Ongoing monitoring/maintenance available at $[X]/month.

9) Next steps / approval
- To proceed: Reply with ‘Approve’ or request changes. Upon approval I will schedule Milestone 1.

Signature: ____________________    Date: ___________
```

---

# How to use these templates
1. **Create the form** in Google Forms or Typeform using the question list above. Mark required fields and add conditional logic for login/auth.
2. **Send the form** to the client or paste the questions into your initial message. Offer a kickoff call as an alternative.
3. **After receiving answers**, paste them into the One‑Page Discovery Summary and send for approval.
4. **Build a quick prototype** (5–10 sample records) before full time/cost estimates.

---

# Optional: Example short message (for proposals / Upwork messages)

> Hi [Name],
>
> Thanks for your interest. To scope the work I created a short intake form — it takes about 5–10 minutes and will help me produce a prototype and a one‑page discovery plan. You can also opt for a 30‑minute kickoff call if you prefer. Please let me know which you prefer and I’ll send the form or schedule the call.

---

_End of templates._

