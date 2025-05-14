def parse_forecast(forecast_data):
    location = forecast_data["location"]["name"]
    country = forecast_data["location"]["country"]
    forecast_days = forecast_data["forecast"]["forecastday"]
    
    weather_report = {
        "location": f"{location}, {country}",
        "forecast": []
    }
    
    for day in forecast_days:
        date = datetime.strptime(day["date"], "%Y-%m-%d").strftime("%A, %b %d")
        max_temp = day["day"]["maxtemp_c"]
        min_temp = day["day"]["mintemp_c"]
        condition = day["day"]["condition"]["text"]
        
        daily_forecast = {
            "date": date,
            "condition": condition,
            "max_temp": max_temp,
            "min_temp": min_temp
        }
        
        weather_report["forecast"].append(daily_forecast)
    
    return weather_report
