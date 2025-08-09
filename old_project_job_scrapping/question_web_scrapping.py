r'''
I know from the fact that Web Scrapping can have a lawsuit because you can get information from the website 

I learned about Human Mimicing , User Agent Rotation, and also Rotating Proxy and like that but the problem here lies on is this illegal? 
Is Web Scrapping Illegal? 
    What is that i'm getting into? 

     
'''


r'''
Some Key Factor in Determining Legality 

1. Website's Terms of Service (ToS):
    * The most common factor. If a website's ToS explicitly prohibits scraping
    (e.g., clauses against automated access, data extraction, or bots), 
    scraping it likely violates the contract and can be grounds for legal action (breach of contract).
    * Ignoring a clearly stated prohibition in the robots.txt file (especially Disallow: /) 
    also signals violation of the site's terms.

    # I think i needed to Investigate the robots.txt files and i quite learned how to do something with the robot.txt files
    figuring out if it is Disallow 

2. The Type of Data Scraped 
    * Copyrighted Content: Scraping and republishing substantial amounts of copyrighted text, images, code, etc., without permission/license/fair use justification is likely copyright infringement.
    # This make Sense for image and code but the copyrighted "Text" i had no idea

    * Personal Data (PII): Scraping personal information (emails, phone numbers, private profiles, financial data) is heavily regulated under laws like GDPR (EU), CCPA/CPRA (California), and others. Scraping PII without consent and a lawful basis is highly likely to be illegal.
    # I think there are in Upwork or any Freelancer site where i needed to gather emails i think this is not part of that because
    # maybe they used the Business Contact instead of Personal Information

    * Confidential/Proprietary Data: Accessing data behind logins (without authorization) or marked confidential is illegal under laws like the CFAA (Computer Fraud and Abuse Act) in the US and similar computer misuse laws elsewhere.
    # Accessing Data Behind Logins which make total sense and i get teach that log in and maitaining the sessions really matter but accessing data behind login 
    # This is really complex 

3. How You Scrape
    Overloading Servers: Sending too many requests too quickly can disrupt the website's normal operation (Denial of Service), potentially violating the CFAA or similar laws prohibiting unauthorized access that damages systems.
    # this is Actually i can Implement Properly

    Bypassing Security/Logins: Hacking passwords, circumventing paywalls, or evading technical barriers (like IP blocking) is almost certainly illegal under computer fraud laws (CFAA).
    # There are Concept of Rotate Proxy so i had no idea into doing this stuff but i know hacking passwordi s bad 

    * Masking Identity: Using techniques solely to avoid detection might be seen as evidence of intent to circumvent terms or access unauthorized data.
    # This is a Gray Area for me because There are Concept of "Rotate User Agent", Mimicing Human Behavior, and Rotating Proxies

4. Jurisdiction & Purpose:
    * Laws differ significantly by country/region (e.g., CFAA in the US, GDPR in EU, CASL in Canada).
    # Maybe Investigating in the Philippines Law if I'm going Deeper into this 

    * Fair Use (Copyright): In some jurisdictions (like the US), scraping for purposes like news reporting, criticism, comment, teaching, scholarship, or research might qualify as fair use, potentially protecting limited use of copyrighted material. This is complex and fact-specific.
    # Understanding the Copyright thing 

    * Public vs. Non-Public Data: Scraping truly publicly accessible data (data visible without login or special access) generally has a stronger legal footing than scraping non-public data. The landmark US case hiQ Labs v. LinkedIn affirmed this principle, but it's not absolute and depends on other factors like ToS.
    # Sticking with the Public Data will be my best chance and also i needed to manage to ToS

Landmark Case: hiQ Labs v. LinkedIn (US)
    * This case significantly influenced the landscape. The court ruled that scraping publicly available data from LinkedIn (data visible without a login) likely did not violate the CFAA.

    * Crucially: This case focused on CFAA violations, not on copyright or breach of contract. Websites can still use copyright claims or breach of ToS arguments against scrapers, even for public data. The ruling also emphasized that scraping shouldn't harm the website's servers.
    '''

# Best Practices for (Potentially) Legal Scraping

r'''
1. Read & Respect robots.txt: This file indicates the site owner's preferences for crawlers. While not legally binding by itself, ignoring it is poor etiquette and can be used as evidence in a breach of ToS claim.
# Can i Automate This instead of Reading Everything i needed a bot that will read the robot.txt

2. Review Terms of Service (ToS) Thoroughly: If the ToS explicitly forbids scraping, respect it. Proceeding anyway carries significant legal risk.
# Some Website have here but if i carry it i hope i get blocked not go to court

3.Scrape Publicly Accessible Data Only: Avoid anything behind logins, paywalls, or requiring special permissions.
# This is my Best Shot ofcourse

4. Be Gentle: Limit request rates to avoid overloading servers. Use delays between requests.
# I can do this properly

5. Identify Your Bot: Use a clear user agent string identifying your bot and providing contact information.
# I don't know 

6. Respect Copyright: Don't republish substantial amounts of copyrighted content verbatim without permission or a solid fair use justification.
# I needed to fix this in terms of Github because i always upload there 

7. Avoid Personal Data (PII): Unless you have explicit consent and comply with data protection laws (GDPR, CCPA, etc.), steer clear of scraping personal information.
# Yep Roger on this 

8. Consider the Purpose: Non-commercial, research, or transformative use has a stronger fair use argument than commercial republication.
# Transformative Use i think this is the Result of Data Analyzing 
# Commercial Republication I had no idea what this means 
# What does it mean by Non Commericial? 


'''

# I definitely Need some time for this 
# Research on 
r'''
What is Robot.txt
Can i Automate Reading the Disallow Section?
What is Copywright 

Relearning the Book 

'''