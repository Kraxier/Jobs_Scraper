# 🧠 The Ultimate Regex Fun-Sized Guide 🎉

Regex is like a super-powered "Find" for your text. It doesn't just look for words; it finds patterns. It's a mini-language that's supported in almost every programming language (Python, JavaScript, Java, etc.) and many text editors!

---

## ⚙️ 1. The Core Building Blocks

### 🔤 Literals (The Exact Match)  
The most basic search. `cat` will find the sequence "c" + "a" + "t".  

**Example:**  
`cat` in `"The cat in the hat"` → matches **"cat"**

---

### 🎭 Metacharacters (The Special Ones)  

These characters have magical powers and don't represent themselves.

- `.` : The **Wildcard** → matches any single character (except a newline).  
  - Example: `c.t` matches `"cat"`, `"cot"`, `"c@t"`.

- `^` : The **Starting Line** → asserts the pattern must be at the beginning.  
  - Example: `^Hello` matches `"Hello world"` but not `"World, hello"`.

- `$` : The **Finish Line** → asserts the pattern must be at the end.  
  - Example: `world$` matches `"Hello world"` but not `"worldly"`.

- `[]` : The **Character Set** → match any ONE character inside the brackets.  
  - Example: `[Cc][Aa][Tt]` matches `"cat"`, `"CAT"`, `"CaT"`.  
  - `[a-z]` matches any lowercase letter.  
  - `[0-9]` matches any digit.

---

### 🔢 Quantifiers (How Many Times?)  

They follow a character and tell it how many times to repeat.

- `*` : **0 or More** → be greedy!  
  - Example: `lo*l` matches `"ll"`, `"lol"`, `"lool"`.

- `+` : **1 or More** → at least one, please.  
  - Example: `lo+l` matches `"lol"`, `"lool"` but NOT `"ll"`.

- `?` : **0 or 1** → makes something optional.  
  - Example: `colou?r` matches both `"color"` and `"colour"`.

- `{m,n}` : **Between m and n times** → precise greed.  
  - Example: `\d{2,4}` matches `"12"`, `"123"`, `"1234"`.

---

### 📘 Character Classes (Shortcuts for Common Sets)

- `\d` : Any digit (0-9) → `[0-9]`  
- `\w` : Any word character (a-z, A-Z, 0-9, _) → `[a-zA-Z0-9_]`  
- `\s` : Any whitespace (space, tab, newline)  
- `\D`, `\W`, `\S` : The opposites (NOT a digit, NOT a word char, NOT whitespace)

---

### 👨‍👩‍👧‍👦 Groups & Capturing

- `( )` : **Capture Group** → groups a pattern and "captures" its match for later use.  
- `(?: )` : **Non-Capturing Group** → group but don't save the match.  
- `|` : The **OR Operator** → match one pattern or another.  

Example: `(apple|orange) pie` matches `"apple pie"` and `"orange pie"`.

---

## 🎯 The 20% That Gets You 80% of Results (Web Scraping Edition)

### 📧 1. Finding Emails
**Pattern:**  
```
[\w.-]+@[\w.-]+\.\w+
```

- `[\w.-]+` : Matches the name part (e.g., john.doe).  
- `@` : Literal @ symbol.  
- `[\w.-]+` : Matches the domain name (e.g., gmail).  
- `\.` : Escaped dot (a literal .).  
- `\w+` : Matches the TLD (e.g., com).  

✅ Matches: **john.doe@gmail.com**, **info@my-website.co.uk**

---

### 🌐 2. Grabbing URLs
**Pattern:**  
```
https?://[^\s"]+
```

- `https?` : Matches "http" or "https" (the `s` is optional).  
- `://` : Literal characters.  
- `[^\s"]+` : Matches one or more characters that are NOT whitespace or a double quote.  

✅ Matches: **https://www.example.com**, **http://localhost:8000/page.html**

---

### 💰 3. Extracting Prices
**Pattern:**  
```
\$\d+(?:\.\d{2})?
```

- `\$` : Escaped dollar sign (a literal $).  
- `\d+` : One or more digits for the whole number.  
- `(?:\.\d{2})?` : Optional cents (dot + 2 digits).  

✅ Matches: **$29**, **$150.99**, **$0.50**

---

### 🔗 4. Simple HTML Tag Attribute Extraction
⚠️ Warning: Regex can break on complex HTML. Use a proper parser (like BeautifulSoup) for reliable work. But for quick and dirty jobs:

- **Hrefs:**  
  ```
  href="([^"]+)"
  ```
  - `()` is the capture group.  
  - `[^"]+` means "match one or more characters that are NOT a double quote".  

  ✅ Example: `href="https://example.com"`

- **Image Sources:**  
  ```
  <img[^>]+src="([^"]+)"
  ```
  - `<img` : Literal start of tag.  
  - `[^>]+` : Matches all attributes inside the tag until...  
  - `src="([^"]+)"` : ...it finds the src attribute and captures its value.  

---

## 🧪 Quick Reference Cheat Sheet

| Pattern | Means | Example Matches |
|---------|-------|-----------------|
| `\d` | Digit | 1, 9 |
| `\d+` | One or more digits | 1, 123 |
| `\w` | Word Character | a, B, 3, _ |
| `\s` | Whitespace | " ", `\t` |
| `.` | Any Character | a, @, ! |
| `.*` | Anything (use carefully!) | cat, x@!4, the whole text |
| `[a-z]` | Lowercase Letter | a, z |
| `[A-Z]` | Uppercase Letter | A, Z |
| `[0-9]` | Digit | 0, 9 |
| `^Hi` | Starts with "Hi" | **Hi** there |
| `bye$` | Ends with "bye" | good**bye** |
| `a\|b` | a OR b | **a**pple, **b**anana |

---

## ⚠️ Final Word of Warning (Reprise!)

Regex is NOT a full HTML/XML parser! 🚫  
For structured web scraping, always use a dedicated tool like:

- **Python:** BeautifulSoup or lxml  
- **JavaScript:** Cheerio or DOMParser  

✅ Use Regex on the web for:
- 🔍 Post-processing text you've already extracted.  
- 📜 Parsing messy logs or raw text data.  
- 🎣 Quickly fishing for small, well-defined patterns in a large string.  

---

✨ Now go forth and pattern-match! You're powerful! 💥
