r'''
Regex Implementation:

'''


import re # import re is a Module Function

# re.findall(pattern, string)
r'''
Use Case: Extraction. Returns a list of all non-overlapping matches.
"Find all the email addresses in this text and give them to me in a list.
'''

text = "Contact support@company.com for pricing, usually around $29.99. #promo"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
prices = re.findall(r'\$\d+\.\d{2}', text)

print(emails) # Output: ['support@company.com']
print(prices) # Output: ['$29.99']



#########################

# re.sub(pattern, repl, string)
r'''
Use Case: Replacement/Cleaning. Replaces all matches with a new string.
"Find all non-digit characters in this phone number and replace them with nothing (delete them)."
'''

raw_phone = " (555) 123-4567 "
# Step 1: Remove all non-digit characters
digits_only = re.sub(r'[^\d]', '', raw_phone) # '5551234567'
# Step 2: Format using capturing groups (optional but clean)
formatted_phone = re.sub(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', digits_only)
print(formatted_phone) # Output: '555-123-4567'




#########################

# re.split(pattern, string)
r'''
Use Case: Splitting. Splits a string by the occurrences of the pattern.
"Split this line of text wherever you see a comma, space, or semicolon."
'''

messy_text = "   This    text has   too many   spaces.   "
clean_text = re.sub(r'\s+', ' ', messy_text).strip()
print(clean_text) # Output: "This text has too many spaces."
# .strip() removes leading/trailing spaces after the substitution.



#########################
# Learning the Regex Pattern/ Core Syntax: 
r'''
Symbol	        Meaning & Usage	        Example	        Matches
.	Any single character (except a newline)	a.c	abc, a c, a-c
\d	            Any digit (0-9)	        \d\d	        42, 00, 99
\w	Any word character (a-z, A-Z, 0-9, _)	\w\w\w	Abc, xyz, A_1
\s	Any whitespace (space, tab, newline)	hello\sworld	hello world
[abc]	Character Set: matches one of the characters inside	[cb]at	cat, bat
[a-z]	Character Range: matches one character in the range	[a-z]at	cat, bat, zat
[^abc]	Negated Set: matches any character NOT listed	[^cb]at	rat, hat, mat
*	0 or more of the previous character/group	a*b	b, ab, aaab
+	1 or more of the previous character/group	a+b	ab, aaab (not b)
?	0 or 1 of the previous character/group (makes it optional)	a?b	b, ab
{3}	Exactly 3 of the previous character/group	a{3}	aaa
{2,4}	Between 2 and 4 of the previous character/group	a{2,4}	aa, aaa, aaaa
^	Start of the string or line	^Hello	Hello world (but not World, Hello)
$	End of the string or line	world$	Hello world (but not wold peace)
`	`	Alternation / OR	`cat	dog`	cat, dog
( )	Capturing Group: groups patterns and "captures" the text for extraction	(abc)+	abc, abcabc
'''


# 2. The "How to Study" Plan: Build Patterns like Legos
r'''Building the Pattern for Getting the Numbers'''
ph_land_line_number = "02-8555-1234" # Level 1 
ph_phone_number = "0917-555-1234" # Level 1 
phone_number_ph = "+63 917-555-1234" # Level 3 

# How many Digit in terms of ph_phone_number? 11 Digit
# Pattern: \d\d\d\d\d\d\d\d\d\d\d
# d is digit the ones, tens, hundreds 
# Better: \d{11} (using the quantifier {11} for "exactly 11 digits")
# I think the quantifier is \d{} or {}




