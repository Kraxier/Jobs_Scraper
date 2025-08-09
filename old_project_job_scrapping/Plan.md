🔍 What You Can Scrape
Most job board data available publicly is technically scrapable. Typical elements include:

Job title

Company name

Location (city, country, remote status)

Posting date (e.g., “2 days ago”)

Job description

Employment type (full‑time, part‑time, contract)

Salary range (if disclosed)

Application URL/link

Requirements/qualifications

Tags/categories (e.g., Developer, Customer Service)

On some platforms (e.g., Kalibrr, OnlineJobs.ph), you might also scrape:

Resume snippets or skill matrices

Assessment results (Kalibrr)

Employer ratings or chat metadata (Bossjob)

⚖️ Legal & Ethical Guidelines
Redditors shared common wisdom about scraping:

“Follow the robots.txt rules…Scraping is not illegal, just respect the website's property. Abusive scrapper gets IP banned.” 
reddit.com
reddit.com
en.wikipedia.org
+7
reddit.com
+7
businesstips.ph
+7
allremote.jobs
+13
ph.theasianparent.com
+13
medium.com
+13
seekersnewsgh.com
+2
allremote.jobs
+2
virtualstaffer.ph
+2
poeajobs.ph
+4
manatal.com
+4
virtualstaffer.ph
+4

“If the data is public, you can scrape it… Don't crash the site… Follow robots.txt.” 
reddit.com

And on LinkedIn:

“A court has ruled that it's legal to scrape publicly available data from LinkedIn… Legally ok… but they will ban your account.” 
reddit.com

Best Practices:
Respect robots.txt and Terms of Service

Throttle requests to avoid server overload

Avoid personal data (e.g., contact info, emails, private profiles)—that crosses into privacy/legality territory

Use rotating IPs/proxies if scraping at scale

Scraping is legal, but platform may retaliate (e.g., IP blocks, account suspension)

✅ Summary Table
Aspect	What to Scrape
Job meta	Titles, companies, locations, dates, job types
Job details	Descriptions, requirements, salary (if present)
Platform-specific	Embedded features (assessments, ratings, chat logs)

🛠️ Final Tips
Start small & polite: Scrape a few listings, respect delays.

Focus on publicly visible, non-personal data.

Use scraping frameworks like BeautifulSoup, Selenium or Ulixee (reddit user built one for JobsDB) 
reddit.com
bossjob.ph
+5
virtualstaffer.ph
+5
manatal.com
+5
reddit.com
en.wikipedia.org
+1
bossjob.ph
+1
reddit.com
.

Plan data format: JSON/CSV with fields like title, company, URL, etc.

Anticipate blocks: some platforms like LinkedIn are aggressive—expect captchas/IP stalls.



ret content (e.g., pricing engines, quoting calculators) may lead to misappropriation claims—as seen in the Compulife case 
reddit.com
+2
reuters.com
+2
reddit.com
+2
.

Respect Copyright and Intellectual Property

Factual data is generally okay, but copying long text, context, or design may breach copyright 
reddit.com
+3
datacamp.com
+3
scraperapi.com
+3
.

Comply with Privacy Laws (GDPR, CCPA, etc.)

Avoid scraping PII (like emails, names, phone numbers) unless you have a lawful basis or consent 
crawlxpert.com
+3
datacamp.com
+3
fiverr.com
+3
marqueedata.com
+2
fiverr.com
+2
bignewsnetwork.com
+2
.

Be Aware of Jurisdiction-Specific Rules

Laws vary across countries—e.g., GDPR in the EU, CCPA in California, CFAA in the U.S. 
hackernoon.com
+5
reddit.com
+5
reddit.com
+5
crawlxpert.com
+1
bignewsnetwork.com
+1
.

Remain Updated on Legal Precedents

Important cases include hiQ vs LinkedIn (allowed scraping of public profiles but settled terms issues) 
fiverr.com
+7
crawlxpert.com
+7
datacamp.com
+7
en.wikipedia.org
.

🤝 Ethical Best Practices
Minimize Impact on Servers

Use rate limiting (e.g., 1 request per 10–15 seconds), delays, and throttling to avoid overloading web servers 
bignewsnetwork.com
+6
fiverr.com
+6
scraperapi.com
+6
.

Scrape Only What You Need

Avoid “vacuum‑ing” entire sites. Focus on relevant data to reduce harm and storage bloat 
linkedin.com
+5
scraperapi.com
+5
fiverr.com
+5
.

Identify Your Crawler

Use a transparent User-Agent string and contact info—this builds trust and accountability 
linkedin.com
+6
scraperapi.com
+6
siberoloji.com
+6
.

Don’t Bypass Security Measures

Avoid CAPTCHAs, authentication walls, or anti-bot defenses—trying to get around them is likely illegal 
fiverr.com
.

Use APIs When Available

If a platform offers a public API, use that instead of scraping – it's more reliable and compliant 
crawlxpert.com
+1
linkedin.com
+1
datacamp.com
+2
scraperapi.com
+2
linkedin.com
+2
.

Attribute Sources, Respect Copyright

When using scraped data, credit the origin site, especially if you publish or repurpose content 
dev.to
+3
datacamp.com
+3
scraperapi.com
+3
.

Protect and Review Collected Data

Store data securely, anonymize sensitive info, set data retention policies, and handle deletion requests 
siberoloji.com
+1
vox.com
+1
.

Be Transparent and Accountable

Document your scraping approach and intentions. Be ready to justify your actions and comply with removal requests 
hackernoon.com
+4
siberoloji.com
+4
scraperapi.com
+4
.

Stay Informed on Changing Rules

Scraping norms, laws, and site policies evolve—review your methods regularly .

🇵🇭 Local Philippine Job Sites
• PhilJobNet
The official job-matching portal of the Philippine Department of Labor and Employment (DOLE). It’s free for both job seekers and employers, and only accredited firms can post openings — reducing scams. Offers job matching, labor-market trends, and career resources. 
Efren Nolasco
+15
PhilJobNet
+15
Seekers News GH
+15

• JobStreet Philippines
One of the longest-established and most widely used platforms in the country. With thousands of listings across sectors, advanced filters, job alerts, and company reviews, it's a go-to for many Filipinos. Now integrated into SEEK’s regional AI‑powered platform. 
Seekers News GH

• Kalibrr
Full-stack hiring platform headquartered in Makati. Features automated matching, assessments, profile-based job recommendations, and partnerships with government and top multinational companies. Ideal for both local and remote roles. 
Wikipedia

• Indeed Philippines (ph.indeed.com)
A global job search engine with localized coverage in the Philippines. Aggregates listings from company sites, recruiters, and job boards. Strong filtering tools, resume uploads, and alerts. 
Findojobs
+7
Vista Residences
+7
Efren Nolasco
+7

• Foundit.com.ph (formerly Monster Philippines)
Offers listings across industries along with career guides, salary insights, and resume services. Perfect for browsing and applying to mid to senior‑level positions.

• OnlineJobs.ph
Specializes in remote and virtual jobs for Filipino professionals. International employers post directly, and the platform ensures no salary deductions. Useful for VAs, content creators, support staff, and developers.

• WorkAbroad.ph
Focused on overseas employment opportunities via POEA-accredited agencies. Particularly helpful for OFWs looking for jobs in healthcare, engineering, hospitality, and more. 
ModernFilipina.ph
+3
Vista Residences
+3
Efren Nolasco
+3

• Trabaho.com
One of the earliest Philippine job portals, established in the mid‑1990s. Offers domestic and international job listings, company details, and job fair postings. 
Business Tips Philippines

🔎 Other Useful Platforms
BestJobs.ph – Known for a clean interface, fast search functionality, and easy job alerts. 
Reddit
+3
ModernFilipina.ph
+3
Reddit
+3

JobsDB Philippines – Another alternative to JobStreet with a straightforward search experience and job alerts. 
ModernFilipina.ph
+1
Wikipedia
+1

JobOpenings.ph – A purely Filipino-run platform with hundreds of thousands of job postings, especially from smaller companies. 
ModernFilipina.ph

Monster / Foundit – Continues to operate effectively under its new name, providing a reliable database of varied listings. 
Efren Nolasco
+1
Reddit
+1

LinkedIn – Though global, it’s heavily used by Filipino professionals. Great for networking, headhunter outreach, and job listings with filters like “remote” or “work from home.” 
Reddit
+10
Reddit
+10
Reddit
+10

💬 Insights from Filipinos on Reddit
Many Filipinos find JobStreet, Indeed, LinkedIn, and Kalibrr as reliable sources:

“Jobstreet – Indeed – LinkedIn – Kalibrr” 
Reddit
+6
Reddit
+6
Reddit
+6

“BestJobs.ph, Indeed, JobStreet, Appen…” 
Reddit
+11
Reddit
+11
ModernFilipina.ph
+11

For remote work, OnlineJobs.ph, Remote Staff, VirtualStaff.ph, Upwork, and Freelancer.com are often recommended:

“Remote Staff”, “OnlineJobs.ph”, “Upwork”, “Freelancer.com” 
Reddit
+1
Reddit
+1

Reddit users also suggest cross‑checking listings with official company websites or verifying via LinkedIn for legitimacy. Avoid job postings that ask for money or sensitive data.