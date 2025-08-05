
"""
get_weather_data_selenium.py

This script uses Selenium and BeautifulSoup to fetch and parse weather data from world-weather.info.

Features:
- Uses Selenium to automate Chrome, set cookies, and fetch the weather page with temperatures in Celsius.
- Extracts city names, temperatures, and weather conditions using regex from the resorts section.
- Saves weather data in both tabular text and JSON formats, including fetch timestamp.

Usage:
- Ensure ChromeDriver is installed and available.
- Run the script directly to save weather data as JSON (default), or call get_weather_data_txt() for text output.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from datetime import datetime
import re
from tabulate import tabulate
import json

def get_weather_data_selenium():

    """
    Fetches weather data from world-weather.info using Selenium and BeautifulSoup.
    Sets the 'celsius' cookie to ensure temperatures are in Celsius.
    Returns a zip object of (number, city, temperature, condition) for each resort.
    """
    url = "https://world-weather.info/"
    options = Options()
    options.add_argument('--headless')  # Run Chrome in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(options=options)
    print("Opening page with Selenium...")
    driver.get(url)
    time.sleep(2)  # Wait for initial page load
    # Set the celsius cookie
    driver.add_cookie({"name": "celsius", "value": "1"})
    driver.refresh()
    time.sleep(3)  # Wait for page to reload with cookie

    page_source = driver.page_source
    driver.quit()

    # Save the HTML for inspection
    with open(r".\webScraper\selenium_weather_response.html", "w",encoding="utf-8") as f:
        f.write(page_source)

    # Parse with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    resorts = soup.find("div", id="resorts")
    if resorts:
        cities = re.findall(r'\/">([\w+\s]+)<\/a><span>', str(resorts))
        temps = re.findall(r'>([\+-]\d+)<span', str(resorts))
        temps = [int(temp) for temp in temps]  # Convert to integers
        conditions = re.findall(r'title="([\w\s]+)"><\/', str(resorts))
        num_resorts = len(cities)
        numbering = [x for x in range(1, num_resorts + 1)]
        weather_data = zip(numbering,cities, temps, conditions)
        return weather_data
    else:
        print("Resorts section not found.")
    print("Done.")
    



def get_weather_data_txt():   

    """
    Fetches weather data and saves it as a formatted text table with timestamp.
    """
    data = get_weather_data_selenium()
    if data:
        with open(r".\webScraper\weather_data.txt", "w", encoding="utf-8") as file:
            file.write(f"Weather data fetched on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("#" + "-" * 50 + "\n")
            table = tabulate(data, headers=["#","City", "Temperature (°C)", "Condition"], tablefmt="double_grid")
            file.write(table)
        print("Weather data saved to weather_data.txt")
    else:
        print("No weather data to save.") 
        
        
        

def get_weather_data_json():

    """
    Fetches weather data and saves it as a JSON file with timestamp.
    """
    data = get_weather_data_selenium()
    if data:
        # Convert to a list of dictionaries for JSON format
        weather_list = [{f"City #{num}": city, "Temperature (°C)": temp, "Condition": condition} for num, city, temp, condition in data]
        # Prepare the JSON object with date and weather data
        json_data = {
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "weather": weather_list
        }
        with open(r".\webScraper\weather_data.json", "w", encoding="utf-8") as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
        print("Weather data saved to weather_data.json")
    else:
        print("No weather data to save.")        
    

if __name__ == "__main__":
    
    get_weather_data_json()
    
    
    


