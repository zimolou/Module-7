
from datetime import datetime

class WeatherApp:
    API_KEY = "YOUR_API_KEY"  # Replace with actual API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/"
    
    def get_weather(self, location):
        url = f"{self.BASE_URL}weather?q={location}&appid={self.API_KEY}&units=metric"
        response = requests.get(url)
        return response.json()
    
    def get_forecast(self, location):
        url = f"{self.BASE_URL}forecast?q={location}&appid={self.API_KEY}&units=metric"
        response = requests.get(url)
        return response.json()
    
    def display_weather(self, data):
        if data.get('cod') != 200:
            print("Error:", data.get('message', 'Unknown error'))
            return
        
        print(f"\nCurrent Weather in {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C (Feels like {data['main']['feels_like']}°C)")
        print(f"Conditions: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} m/s")
    
    def display_forecast(self, data):
        if data.get('cod') != '200':
            print("Error:", data.get('message', 'Unknown error'))
            return
        
        print(f"\n5-Day Forecast for {data['city']['name']}:")
        for item in data['list'][::8]:  # Get one forecast per day
            date = datetime.fromtimestamp(item['dt'])
            print(f"\n{date.strftime('%A %b %d')}:")
            print(f"  Day: {item['main']['temp']}°C | {item['weather'][0]['description']}")
            print(f"  Wind: {item['wind']['speed']} m/s | Humidity: {item['main']['humidity']}%")

def main():
    app = WeatherApp()
    while True:
        location = input("\nEnter city name (or 'quit'): ")
        if location.lower() == 'quit':
            break
        
        print("\n1. Current Weather\n2. 5-Day Forecast")
        choice = input("Select: ")
        
        if choice == '1':
            data = app.get_weather(location)
            app.display_weather(data)
        elif choice == '2':
            data = app.get_forecast(location)
            app.display_forecast(data)

if __name__ == "__main__":
    main()
