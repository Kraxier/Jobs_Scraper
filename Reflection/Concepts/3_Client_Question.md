# Client Intake Q&A — Web Scraping / Data Project

Use this during the kickoff call or first client message. Ask for explicit answers or examples (URLs, screenshots).

---

## Project Overview

**Q1. What is the main goal of this project?**  
(e.g., price monitoring, lead generation, market research, content aggregation, competitive intelligence)

**Q2. Who will use the data and how will it be used?**  
(e.g., internal dashboard, Excel analysis, ML model, public website, API feed)

**Q3. Is this a one-time data pull or an ongoing/recurring feed?**  
(one-off, daily, hourly, weekly)


---

## Data Specifics

**Q4. Which websites / pages / endpoints should we scrape?**  
(Please provide sample URLs or a short list)
#### Understanding : Pretty much self Explanatory 

**Q5. What specific fields do you want collected?**  
(e.g., title, price, availability, SKU, rating, date, description, images, links)
#### Understanding : Circulating to the goal
**Q6. Do you need historical data (backfill) or only future snapshots?**  
(If historical, how far back?)
#### Understanding: To Understand How far back do i need to scrape for historical analysis thing 

**Q7. What format do you want the data in?**  
(CSV, JSON, SQL dump, Google Sheets, API endpoint, database)
#### Understanding: Depends on the client want 

**Q8. How many records / pages do you expect initially and per update?**  
(estimate: hundreds, thousands, millions)
#### Understanding: Depends on the Data Volume of how much they really want

---

## Technical & Access

**Q9. Are the pages static HTML or JavaScript-rendered?**  
(examples help us verify)
#### Understanding: To know the complexity of the website 

**Q10. Do you have an API or feed we could use instead?**  
(If yes, please provide docs/keys)

**Q11. Do we need to log in or use credentials to access content?**  
(If yes, provide a test account or describe auth flow)
#### Understanding: Testing an account for a content thing 

**Q12. Are there rate limits, CAPTCHAs, or anti-bot protections you’re aware of on these sites?**
#### Understanding: To know the complexity of the anti bot thing that i'm going to do 

---

## Legal, Privacy & Compliance

**Q13. Are you authorized to collect/use this data?**  
(Have you reviewed the sites’ terms of service / robots.txt, or should we check?)
#### Understanding: To not cross the border and remain ethical and also following the law

**Q14. Is there any PII, confidential, or restricted data involved?**  
(If yes, specify what and desired handling)

---

## Deliverables, Timeline & Budget

**Q15. What are your expected deliverables and format?**  
(e.g., raw data, cleaned dataset, ETL pipeline, dashboard, API)
#### Understanding: To know the output of the client want but i  think mostly cleaned dataset and raw data, i had no idea of dashboard,api and ETL piple

**Q16. What is your desired timeline and turnaround?**  
(start date, deadlines, milestones)
#### Understanding: Providing the Milestone of my own thing to get the job done properly 

**Q17. What is your budget or price range for the job?**  
(optional but helps scope realistic options)
#### Understanding: to know my worth ehheehhe 
---

## Maintenance & Support

**Q18. Do you want ongoing monitoring and maintenance (fix broken selectors, adapt to site changes)?**  
(yes/no — if yes, how frequently should we review)
#### Understanding: to be able to know when to fix if already done in the project 

**Q19. Who will be the main point of contact and preferred communication channel?**  
(email, Slack, Teams, Upwork chat)
#### Understanding: To have a better communication to a client 
---

## Acceptance Criteria & Testing

**Q20. How will you judge the job as “done”?**  
(e.g., 95% coverage of required fields, data freshness within X hours, sample dataset verification)
#### Understanding: to know the expectation of the client or meet their needs man to be able to deliver what they want

---

# Example Kickoff Message to Client

Hi **[Client Name]**,

Thanks — to scope this properly I put together a short questionnaire. Could you please answer or provide examples for the items below?

1. Project goal: [e.g., price monitoring for 3 competitor sites]  
2. Target websites / sample URLs: [...]  
3. Data fields required: [...]  
4. Frequency: [one-time / daily / hourly]  
5. Delivery format: [CSV / JSON / DB / API]  
6. Any login/auth required? [yes/no — if yes, please provide test creds]  
7. Any legal/usage constraints I should know about?  
8. Desired timeline and budget range:  
9. Who will be the point of contact?  

If you prefer, we can do a 30-min call and I’ll draft a one-page discovery summary & a quick prototype sample for your approval.

Thanks — I’ll use your answers to prepare a short plan and a milestone-based quote.

---

# Quick Acceptance Criteria (Template)

- **Scope:** Scrape the following pages: [list]. Collect fields: [list].  
- **Frequency:** [e.g., daily at 02:00 UTC].  
- **Delivery format:** [CSV + DB].  
- **Quality targets:** ≥95% of records include required fields.  
- **Acceptance test:** Client will verify a random sample of 100 records within 3 business days.  
- **Maintenance:** [e.g., 30 days bug-fix warranty, ongoing monitoring available at $X/month].  

---

# Internal Checklist (Before Starting)

- [ ] Client approved discovery summary  
- [ ] Sample URLs received  
- [ ] Required fields prioritized (must-have vs nice-to-have)  
- [ ] Auth credentials/test account (if required)  
- [ ] Robots.txt / ToS checked and compliance note recorded  
- [ ] Milestones & payment schedule agreed  
- [ ] Acceptance criteria defined  
