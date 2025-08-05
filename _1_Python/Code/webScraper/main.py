import get_weather_data_selenium
# import get_weather_data_requests


if __name__ == "__main__":
    print("Welcome to the Weather Data Scraper!")
    print("This program fetches weather data from world-weather.info using Selenium.")
    
  
    options = input("Choose the method to Print weather data : \n1. Print to Text File\n2. Print to JSON File\n3. Print to Console\nEnter your choice (1/2/3): ")
    options = int(options.strip())

    while options not in [1, 2, 3]:
        options = input("Invalid choice. Please enter 1, 2, or 3: ")
        options = int(options.strip())

    match options:
        case 1: 
            get_weather_data_selenium.get_weather_data_txt()
        case 2:
            get_weather_data_selenium.get_weather_data_json()
        case 3:
            data = get_weather_data_selenium.get_weather_data_selenium()
            if data:
                for num, city, temp, condition in data:
                    print(f"City #{num}: {city}, Temperature: {temp}°C, Condition: {condition}")
            else:
                print("No weather data to display.")
        case _:
            print("Invalid option selected. Please choose 1, 2, or 3.") 
            
    print("Thank you for using the Weather Data Scraper!")
    print("Goodbye!")        
            
            
        
           