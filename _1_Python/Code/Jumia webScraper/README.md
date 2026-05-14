# 🛒 Jumia Egypt Product Scraper

A lightweight Python web scraper that fetches a product page from **Jumia Egypt** and extracts product details — name and price — and prints them to the console.

Built as part of the **Hsoub AI Course** Python module.

---

## 📌 Features

- Sends an HTTP GET request with a custom **User-Agent** header to mimic a real browser
- Handles request exceptions gracefully with informative status messages
- Saves the raw HTML response to a local file (`Jumia_response.html`) for debugging
- Parses the HTML using **BeautifulSoup** and extracts product details via CSS class selectors
- Prints the extracted **product name** and **price** to the console

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| `Python 3.x` | Core programming language |
| `requests` | Sending HTTP GET requests |
| `BeautifulSoup4` | Parsing and navigating the HTML response |

---

## 📁 Project Structure

```
_1_Python/
│
└── webScraper/
    ├── jumia_get_product.py    # Main scraping script
    ├── Jumia_response.html     # Auto-generated HTML dump (for debugging)
    └── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MohamedNabil70/Hsoub_Ai_Course.git
cd Hsoub_Ai_Course/_1_Python/webScraper
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install requests beautifulsoup4
```

---

## 🚀 Usage

To scrape a different product, open `jumia_get_product.py` and update the `url` variable:

```python
url = "https://www.jumia.com.eg/your-target-product-page.html"
```

Then run the script:

```bash
python jumia_get_product.py
```

### Example Output

```
Before request...
After request...
200
Successfully fetched the web page.
Response URL ==>  https://www.jumia.com.eg/casio-fx991es-plus-2ed-thailand-107119084.html
##################################################
##################################################
Product Name: Casio FX-991ES Plus 2nd Edition Scientific Calculator
Product Price: EGP 1,299
##################################################
```

> The HTML response is also saved to `Jumia_response.html` in the same directory for manual inspection.

---

## 🔍 How It Works

### 1. `send_request(url, header, param=None)`
Sends a GET request with a browser-mimicking `User-Agent` header and a `timeout=10` safeguard. Prints the HTTP status code and final URL (after any redirects). Exits cleanly if the request fails.

### 2. HTML Dump
The raw response content is written to `Jumia_response.html` — useful for inspecting the page structure and debugging CSS selectors without re-fetching the page.

### 3. `display_product_details(soup)`
Uses `BeautifulSoup` to locate product details via known CSS classes:

| Field | Tag | CSS Class |
|---|---|---|
| Product Name | `<h1>` | `-fs20 -pts -pbxs` |
| Product Price | `<span>` | `-b -ubpt -tal -fs24 -prxs` |

Prints each field to the console, with a fallback message if an element isn't found.

---

## ⚠️ Notes & Limitations

- **CSS classes may change** — Jumia can update their front-end at any time, which may break the selectors. Inspect `Jumia_response.html` to find updated class names.
- **Anti-scraping measures** — If the status code is not `200`, Jumia may be rate-limiting or blocking the request. Try rotating headers or adding a delay.
- This script targets **a single product URL**. It does not handle pagination or category pages.

---

## 🔮 Potential Improvements

- [ ] Accept a product URL as a CLI argument (`argparse`)
- [ ] Scrape multiple products from a search results or category page
- [ ] Export extracted data to CSV or JSON
- [ ] Add retry logic for failed or non-200 responses
- [ ] Use `lxml` parser for faster HTML parsing

---

## 👤 Author

**Mohamed Nabil**  
Mechatronics & Robotics Engineer | AI & Computer Vision Enthusiast

- GitHub: [@MohamedNabil70](https://github.com/MohamedNabil70)
- LinkedIn: [linkedin.com/in/mohamednabil70](https://linkedin.com/in/mohamednabil70)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
