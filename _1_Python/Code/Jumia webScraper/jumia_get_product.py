"""
webScraper/jumia_get_product.py

This script fetches a product page from Jumia Egypt and extracts product details such as name and price.

Features:
- Sends an HTTP GET request to the specified Jumia product URL with a custom User-Agent header.
- Handles request exceptions and prints status information.
- Saves the HTML response to a file for inspection.
- Parses the HTML using BeautifulSoup to extract product name and price using known CSS classes.
- Prints extracted product details to the console.

Usage:
- Update the 'url' variable to the desired Jumia product page.
- Run the script to see product details printed and HTML saved for debugging.
"""

import requests
from bs4 import BeautifulSoup

# webScraper/jumia_get_product.py
# This script fetches a web page from Jumia Egypt and prints the status code and final URL

def send_request(url, header, param = None):
    """
    Sends an HTTP GET request to the given URL with headers and optional parameters.
    Prints request status and returns the response object.
    """
    print("Before request...")
    try:
        response = requests.get(url, headers=header, params=param, timeout=10)
        print("After request...")
    except Exception as e:
        print(f"Request failed: {e}")
        exit(1)

    print(response.status_code)

    if response.status_code == 200:
        print("Successfully fetched the web page.") 
    elif response.status_code == 404:
        print("Page not found (404).")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

    print("Response URL ==> " , response.url)  # Print the final URL after any redirects

    return response




####################################################################################



def display_product_details(soup):
    """
    Extracts and prints the product name and price from the BeautifulSoup object.
    """
    # Try to find the product title using only the id
    Product_name = soup.find("h1", class_="-fs20 -pts -pbxs")

    # Try to find the price using multiple strategies
    product_price = None
    # Try the most common price class
    price_span = soup.find("span", class_="-b -ubpt -tal -fs24 -prxs")

    if price_span:
        product_price = price_span


    print("Product Name:", Product_name.get_text(strip=True) if Product_name else "Product name not found")
    print("Product Price:", product_price.get_text(strip=True) if product_price else "Price not found")



# User-Agent header to mimic a browser
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}   
url = "https://www.jumia.com.eg/casio-fx991es-plus-2ed-thailand-107119084.html"
# filters = {"q" : "watches"}

response = send_request(url, header)

print("#" * 50  )  # Separator for clarity
####################################################################################
print("#" * 50  )  # Separator for clarity

# Save the HTML to a file for inspection (debugging purpose) 
with open("Jumia_response.html", "wb") as f:
    f.write(response.content)


# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

display_product_details(soup)

print("#" * 50  )  # Separator for clarity


