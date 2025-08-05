import requests
from bs4 import BeautifulSoup

# This script uses requests to fetch the weather data page from world-weather.info
# and prints the page source for inspection. You can then parse the HTML with BeautifulSoup.

##### Important Note : this script is not using Selenium, it uses requests to fetch the page.
##### It is a simpler and more efficient way to get the data if the page does not require JavaScript to render.
##### the response in this code keeps gettimg 403 Forbidden error, so it is not working.




def get_weather_data_requests():

    url = "https://world-weather.info/"
    header = { "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
              "Accept-Encoding": "gzip, deflate, br",
              "referer": "https://world-weather.info/",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
              "Accept-Language": "en-US,en;q=0.5",
              "cookie": "user_city=14; celsius=1",
              "authority" : "world-weather.info",
              } 

    print("Before request...")
    try:
        response = requests.get(url, headers=header, timeout=10)
        print("After request...")
    except Exception as e:
        print(f"Request failed: {e}")
        exit(1)
    
        
    if response.status_code == 200:
        print("Successfully fetched the weather data page.")
        soup = BeautifulSoup(response.content, 'html.parser')
        # Here you would extract specific weather data from the soup object
        print("Fetching weather data from:", url ,"........")
        print("Weather data page content fetched successfully.")
        print("#" + "-" * 50)
        
        resorts = soup.find("div", id="resorts")
        
        if resorts:
            with open("resorts.txt", "w") as file:
                file.write(resorts.string)
        
        
    else:
        print(f"Failed to fetch the weather data page. Status code: {response.status_code}")
        



if __name__ == "__main__":
    get_weather_data_requests() 
    
           
         
         
