
# WEATHER APP 🌦️

A Python-based weather application built with Flask and OpenWeatherMap API featuring real-time weather data, dynamic backgrounds, and location-based forecasts.

## Features

### ✅ Core Features
- Real-time weather data from OpenWeatherMap API
- Location-based weather information (city search)
- Dynamic background changes based on weather conditions
- Current weather display (temperature, humidity, wind speed)
- Weather description with appropriate icons
- Responsive design for all devices

### 🎨 User Interface
- Modern gradient backgrounds matching weather conditions
- Clean, intuitive interface with weather cards
- Smooth animations and transitions
- Responsive layout for mobile and desktop
- Error handling for invalid locations

## Technologies Used
- **Backend**: Flask (Python web framework)
- **Weather API**: OpenWeatherMap
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with weather-based gradients
- **Environment**: Python-dotenv for configuration

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- OpenWeatherMap API key (free tier available)

### Installation Steps
1. Clone the project:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure environment variables:
   Create a `.env` file with:
   ```env
   API_KEY=your_openweathermap_api_key
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Access the application:
   Open your browser and go to: `http://localhost:5000`

## App Navigation

### Getting Started
1. Enter a city name in the search bar
2. View current weather conditions
3. See dynamic background change based on weather

### Features in Detail
- **Weather Display**:
  - Current temperature with feels-like
  - Humidity and wind speed
  - Atmospheric pressure
  - Weather description (sunny, rainy, etc.)

- **Dynamic Backgrounds**:
  - Sunny: Warm orange gradient
  - Rainy: Cool blue gradient
  - Cloudy: Gray gradient
  - Stormy: Dark gradient
  - Snowy: Light white gradient

## Project Structure
```
weather-app/
├── app.py                 # Main Flask application
├── static/
│   └── style.css          # Application styles
├── templates/
│   └── index.html         # Main weather interface
└── .env                   # Environment configuration
```

## API Integration
The app uses OpenWeatherMap's Current Weather Data API:
- Endpoint: `https://api.openweathermap.org/data/2.5/weather`
- Parameters: `q={city}&appid={API_KEY}&units=metric`

## Testing
### Functional Testing
1. Test with valid city names
2. Test with invalid city names (verify error handling)
3. Test responsive design on different devices
4. Verify background changes match weather conditions

### Common Issues
- **API Not Responding**:
  - Verify your API key is correct
  - Check your internet connection
  - Ensure you haven't exceeded API limits

- **Background Not Changing**:
  - Check weather condition codes in console
  - Verify CSS classes are being applied

## Future Enhancements
### Planned Features
- 5-day weather forecast
- Hourly weather predictions
- Location detection via browser geolocation
- Temperature unit toggle (Celsius/Fahrenheit)
- Severe weather alerts
- Air quality index display

### Technical Improvements
- Add caching for API responses
- Implement proper error pages
- Add loading animations
- Improve mobile responsiveness
- Add PWA capabilities

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License
This project is open source and available under the MIT License.

## Support
If you encounter any issues:
- Check the browser console for errors
- Review the Flask application logs
- Create an issue with detailed information
```
