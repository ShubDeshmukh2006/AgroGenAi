# AgriGenie - Intelligent Agricultural Platform

**AgriGenie** is a comprehensive Django-based web platform designed to empower Indian farmers with intelligent agricultural solutions. The platform integrates AI-powered crop recommendations, weather insights, soil analysis, government scheme information, pesticide guidance, export market data, and a multilingual voice assistant to provide a complete farming solution ecosystem.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Application Modules](#application-modules)
- [Management Commands](#management-commands)
- [API Integrations](#api-integrations)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### 🔐 Authentication & User Management
- Custom user model with extended fields (phone, location, farm size, state, district)
- User registration, login, and profile management
- Multi-language support with language middleware
- Session-based authentication

### 🌾 Crop Management & Recommendations
- **Crop Database**: Comprehensive crop information including:
  - Scientific names, categories, seasons
  - Temperature and rainfall requirements
  - Soil pH preferences
  - Growing periods and yield data
  - Market prices
  - Suitable states/regions

- **AI-Powered Crop Recommendations**:
  - Intelligent crop recommendation engine using Gaussian suitability scoring
  - Multi-factor analysis (temperature, rainfall, soil pH, farm size)
  - Expected yield and profit predictions
  - Farm allocation optimization algorithms
  - Revenue visualization charts

- **Price Forecasting**:
  - Crop price forecasts by month/year
  - Climate impact analysis
  - Market trend indicators
  - Price change percentage tracking

### 🌤️ Weather Services
- Real-time weather data integration
- Weather dashboard with comprehensive metrics:
  - Temperature and feels-like temperature
  - Humidity and pressure
  - Wind speed and visibility
  - Weather conditions and descriptions
- Geo-location support (latitude/longitude)
- Weather forecast tracking
- Historical weather data storage

### 🌱 Soil Testing & Analysis
- **Soil Test Management**:
  - Comprehensive soil parameter input (pH, N-P-K, moisture, organic matter)
  - Automatic quality index calculation
  - Quality rating system (Poor → Excellent)
  - Personalized recommendations based on test results

- **Visualization & Reporting**:
  - Soil quality distribution pie charts
  - NPK composition visualizations
  - Historical test tracking
  - PDF report generation
  - OCR-based soil test form processing

### 💊 Pesticide Database
- Comprehensive pesticide information:
  - Categories (Insecticide, Herbicide, Fungicide, Nematicide, Rodenticide)
  - Active ingredients and descriptions
  - Target pests identification
  - Application methods and dosages
  - Safety precautions
  - Manufacturer details
  - Organic/non-organic classification
  - Price ranges

### 🏛️ Government Schemes
- **Scheme Management**:
  - Multiple scheme categories (Subsidy, Loan, Insurance, Training, Equipment, Technology)
  - Detailed eligibility criteria
  - Benefits and application processes
  - Required documents listing
  - Contact information and website links
  - Direct application form URLs

- **Application Tracking**:
  - User scheme applications
  - Application status tracking (Pending → Completed)
  - Personal information and farm details
  - Application history and notes

### 📦 Export Market Information
- Export service listings by country and product
- Demand level indicators (High/Medium/Low)
- Contact information for export services
- Export volume statistics
- Market share and growth potential data
- Visual charts and analytics

### 🎤 AI Voice Assistant
- **Multilingual Support**: English, Hindi, Tamil, Telugu, Bengali, Marathi, and more
- **Core Features**:
  - Text and voice input modes
  - Natural language conversation
  - Context-aware responses
  - Language auto-detection
  - Text-to-speech (TTS) using gTTS
  - Speech recognition capabilities
  - Conversation history management
  - Quick command templates

- **Agricultural Focus**:
  - Weather & climate queries
  - Crop management advice
  - Soil & fertilizer guidance
  - Government scheme information
  - Personalized recommendations

---

## 🛠️ Tech Stack

### Backend
- **Python 3.10+**
- **Django 4.2.7** - Web framework
- **Django REST Framework 3.14.0** - API development
- **django-cors-headers 4.3.1** - CORS handling

### Data Science & AI
- **NumPy 1.26.4** - Numerical computations for crop recommendations
- **OpenAI 1.101.0** - AI-powered conversations
- **langdetect 1.0.9** - Language detection
- **SpeechRecognition 3.10.0** - Voice input processing
- **gTTS 2.5.3** - Google Text-to-Speech
- **pyttsx3 2.90** - Offline TTS engine

### Data Visualization
- **Matplotlib 3.8.2** - Charts and graphs (crop revenue, soil quality)

### Geospatial & Utilities
- **geopy 2.4.1** - Geocoding and location services
- **pycountry 23.12.11** - Country data handling

### Document Processing
- **PyPDF2 3.0.1** - PDF manipulation
- **ReportLab 4.2.5** - PDF generation
- **pytesseract 0.3.13** - OCR for form processing
- **Pillow 10.1.0** - Image processing

### APIs & Networking
- **requests 2.31.0** - HTTP requests

### Configuration
- **python-decouple 3.8** - Environment variable management

### Database
- **SQLite** (default, development)
- Supports PostgreSQL, MySQL (production-ready)

### Frontend
- Django templates (HTML, CSS, JavaScript)
- Bootstrap (responsive design)
- Static file management

---

## 📁 Project Structure

```
agrigenie/
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── db.sqlite3                     # SQLite database (development)
├── README.md                      # Project documentation
│
├── agrigenie/                     # Main project package
│   ├── __init__.py
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Root URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
│
├── apps/                          # Application modules
│   ├── authentication/            # User authentication & profiles
│   │   ├── models.py              # CustomUser model
│   │   ├── views.py               # Auth views
│   │   ├── forms.py               # User forms
│   │   ├── urls.py                # Auth routes
│   │   ├── middleware.py          # Language middleware
│   │   └── templatetags/          # Custom template tags
│   │
│   ├── crops/                     # Crop management & recommendations
│   │   ├── models.py              # Crop, CropRecommendation, CropPriceForecast
│   │   ├── views.py               # Crop views
│   │   ├── ai.py                  # AI recommendation algorithms
│   │   ├── utils.py               # Utility functions
│   │   ├── visualization.py       # Chart generation
│   │   └── management/commands/   # Management commands
│   │       └── load_sample_crops.py
│   │
│   ├── weather/                   # Weather services
│   │   ├── models.py              # WeatherData, WeatherForecast
│   │   ├── views.py               # Weather dashboard
│   │   └── urls.py
│   │
│   ├── soil/                      # Soil testing & analysis
│   │   ├── models.py              # SoilTest model
│   │   ├── views.py               # Soil test views
│   │   ├── forms.py               # Soil test forms
│   │   ├── pdf_generator.py       # PDF report generation
│   │   └── visualization.py       # Soil quality charts
│   │
│   ├── pesticides/                # Pesticide database
│   │   ├── models.py              # Pesticide model
│   │   ├── views.py               # Pesticide views
│   │   └── management/commands/
│   │       └── populate_pesticides.py
│   │
│   ├── schemes/                   # Government schemes
│   │   ├── models.py              # GovernmentScheme, SchemeApplication
│   │   ├── views.py               # Scheme views
│   │   ├── forms.py               # Application forms
│   │   └── management/commands/
│   │       └── populate_schemes.py
│   │
│   ├── exports/                   # Export market info
│   │   ├── models.py              # ExportService model
│   │   ├── views.py               # Export views
│   │   └── urls.py
│   │
│   └── voice/                     # AI Voice Assistant
│       ├── models.py
│       ├── views.py               # Assistant views (unified, chat, voice)
│       └── urls.py
│
├── templates/                     # HTML templates
│   ├── base/                      # Base templates
│   │   ├── base.html
│   │   └── dashboard.html
│   ├── authentication/            # Auth templates
│   ├── crops/                     # Crop templates
│   ├── weather/                   # Weather templates
│   ├── soil/                      # Soil templates
│   ├── pesticides/                # Pesticide templates
│   ├── schemes/                   # Scheme templates
│   ├── exports/                   # Export templates
│   └── voice/                     # Voice assistant templates
│
└── static/                        # Static files (CSS, JS, images)
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10 or higher**
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **Virtual environment tool** (`venv` recommended)

### Installation Steps

#### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd agrigenie
```

#### 2. Create Virtual Environment

**Windows (PowerShell):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Environment Configuration

Create a `.env` file in the project root (optional, but recommended):

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (for production, use PostgreSQL/MySQL)
DATABASE_URL=sqlite:///db.sqlite3

# API Keys
WEATHER_API_KEY=your-weather-api-key
ELEVENLABS_API_KEY=your-elevenlabs-api-key
VAPI_API_KEY=your-vapi-api-key

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

**Note:** Update `agrigenie/settings.py` to use `python-decouple` for loading environment variables if needed.

#### 5. Database Setup

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

#### 6. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

#### 7. Load Sample Data (Optional)

```bash
# Load sample crops
python manage.py load_sample_crops

# Populate pesticides database
python manage.py populate_pesticides

# Populate government schemes
python manage.py populate_schemes
```

#### 8. Run Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to: **http://127.0.0.1:8000/**

---

## ⚙️ Configuration

### Django Settings

Key configuration options in `agrigenie/settings.py`:

- **SECRET_KEY**: Change in production! Use environment variables.
- **DEBUG**: Set to `False` in production.
- **ALLOWED_HOSTS**: Add your domain in production.
- **DATABASES**: Configure for PostgreSQL/MySQL in production.
- **TIME_ZONE**: Set to `Asia/Kolkata` (India Standard Time).
- **LANGUAGE_CODE**: Default language (`en-us`).

### Custom User Model

The project uses a custom user model (`apps.authentication.models.CustomUser`) with extended fields:
- Phone number
- Location
- Farm size
- State and district

### API Keys Configuration

Update the following in `settings.py` or via environment variables:

- **WEATHER_API_KEY**: For weather API integration
- **ELEVENLABS_API_KEY**: For text-to-speech services
- **VAPI_API_KEY**: For voice API (if used)

### Email Configuration

Configure SMTP settings for email functionality:
- Email backend
- SMTP host and port
- TLS/SSL settings
- Authentication credentials

---

## 📱 Application Modules

### Authentication (`apps.authentication`)

**Features:**
- User registration and login
- Profile management
- Custom user model with farm-specific fields
- Multi-language support via middleware
- Session management

**Templates:**
- `login.html` - User login
- `register.html` - User registration
- `profile.html` - User profile management

**Key Models:**
- `CustomUser` - Extended user model

---

### Crops (`apps.crops`)

**Features:**
- Crop database with comprehensive information
- AI-powered crop recommendations using Gaussian suitability scoring
- Yield and profit predictions
- Price forecasting with climate impact analysis
- Revenue visualization charts
- Farm allocation optimization

**Templates:**
- `crop_list.html` - Browse all crops
- `crop_detail.html` - Crop details
- `recommendation_form.html` - Get crop recommendations
- `recommendation_result.html` - View recommendation results

**Key Models:**
- `Crop` - Crop information
- `CropRecommendation` - User recommendation requests
- `RecommendedCrop` - Recommended crops with scores
- `CropPriceForecast` - Price forecasting data

**AI Algorithms:**
- Multi-factor suitability scoring (temperature, pH, rainfall)
- Yield prediction based on farm size and efficiency
- Profit calculation with cost estimation
- Greedy allocation optimization

---

### Weather (`apps.weather`)

**Features:**
- Real-time weather data
- Weather dashboard with comprehensive metrics
- Geo-location support
- Weather forecast tracking
- Historical weather data

**Templates:**
- `dashboard.html` - Weather dashboard

**Key Models:**
- `WeatherData` - Current weather information
- `WeatherForecast` - Forecast data

---

### Soil (`apps.soil`)

**Features:**
- Comprehensive soil test input
- Automatic quality index calculation
- Quality rating system
- Personalized recommendations
- Historical test tracking
- PDF report generation
- Soil quality visualizations
- OCR-based form processing

**Templates:**
- `test_form.html` - Submit soil test
- `report.html` - View test report
- `history.html` - Test history
- `pdf_tools.html` - PDF generation tools

**Key Models:**
- `SoilTest` - Soil test data with quality calculations

**Quality Rating System:**
- Excellent (≥90)
- Good (≥75)
- Moderate (≥60)
- Slightly Poor (≥40)
- Poor (<40)

---

### Pesticides (`apps.pesticides`)

**Features:**
- Comprehensive pesticide database
- Category-based organization
- Detailed application guidelines
- Safety precautions
- Organic/non-organic classification

**Templates:**
- `list.html` - Browse pesticides
- `detail.html` - Pesticide details

**Key Models:**
- `Pesticide` - Pesticide information

**Categories:**
- Insecticide
- Herbicide
- Fungicide
- Nematicide
- Rodenticide
- Other

---

### Schemes (`apps.schemes`)

**Features:**
- Government scheme database
- Category-based filtering
- Detailed eligibility and benefits
- Application tracking
- Status management
- Document requirements

**Templates:**
- `list.html` - Browse schemes
- `detail.html` - Scheme details
- `apply.html` - Apply for scheme
- `my_applications.html` - User applications
- `application_detail.html` - Application details

**Key Models:**
- `GovernmentScheme` - Scheme information
- `SchemeApplication` - User applications

**Categories:**
- Subsidy
- Loan
- Insurance
- Training
- Equipment
- Technology

**Application Status:**
- Pending → Submitted → Under Review → Approved/Rejected → Completed

---

### Exports (`apps.exports`)

**Features:**
- Export market information
- Country and product listings
- Demand level indicators
- Contact information
- Export statistics
- Market analytics

**Templates:**
- `list.html` - Export services list
- `detail.html` - Export service details

**Key Models:**
- `ExportService` - Export service information

---

### Voice Assistant (`apps.voice`)

**Features:**
- Multilingual AI assistant (English, Hindi, Tamil, Telugu, Bengali, Marathi, etc.)
- Text and voice input modes
- Natural language processing
- Context-aware conversations
- Language auto-detection
- Text-to-speech output
- Speech recognition
- Quick command templates
- Conversation history

**Templates:**
- `unified_assistant.html` - Main assistant interface
- `chatbot.html` - Chat interface
- `assistant.html` - Legacy assistant

**Endpoints:**
- `/voice/` - Unified assistant
- `/voice/chat/` - AI chat
- `/voice/voice/input/` - Voice input processing
- `/voice/voice/response/` - Voice response generation
- `/voice/languages/` - Supported languages
- `/voice/commands/` - Quick commands

---

## 🎯 Management Commands

### Available Commands

```bash
# Load sample crops data
python manage.py load_sample_crops

# Populate pesticides database
python manage.py populate_pesticides

# Populate government schemes
python manage.py populate_schemes
```

### Standard Django Commands

```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (production)
python manage.py collectstatic

# Run tests
python manage.py test

# Django shell
python manage.py shell
```

---

## 🔌 API Integrations

### Weather API
- **Provider**: Weather API (configured in settings)
- **Usage**: Real-time weather data and forecasts
- **API Key**: Set via `WEATHER_API_KEY` in settings

### OpenAI API
- **Provider**: OpenAI (for AI conversations)
- **Usage**: Agricultural assistant conversations
- **Configuration**: Set in voice assistant views

### ElevenLabs API
- **Provider**: ElevenLabs (for text-to-speech)
- **Usage**: Voice responses in assistant
- **API Key**: Set via `ELEVENLABS_API_KEY` in settings

### Google TTS (gTTS)
- **Provider**: Google Text-to-Speech
- **Usage**: Free alternative TTS for multilingual support

---

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run tests for a specific app:

```bash
python manage.py test apps.crops
python manage.py test apps.soil
```

---

## 🚢 Deployment

### Production Checklist

1. **Environment Variables:**
   - Set `DEBUG=False`
   - Configure `SECRET_KEY` via environment variable
   - Set `ALLOWED_HOSTS` with your domain(s)

2. **Database:**
   - Migrate from SQLite to PostgreSQL/MySQL
   - Update `DATABASES` in `settings.py`
   - Run migrations: `python manage.py migrate`

3. **Static Files:**
   ```bash
   python manage.py collectstatic --noinput
   ```
   - Configure web server (Nginx/Apache) to serve static files
   - Or use a CDN/service like AWS S3

4. **Media Files:**
   - Configure `MEDIA_ROOT` and `MEDIA_URL`
   - Set up proper file storage (local or cloud)

5. **Security:**
   - Use HTTPS
   - Configure CORS properly
   - Set secure cookie settings
   - Use environment variables for sensitive data

6. **Performance:**
   - Set up caching (Redis/Memcached)
   - Configure database connection pooling
   - Use a production WSGI server (Gunicorn/uWSGI)

7. **Monitoring:**
   - Set up error logging
   - Configure monitoring tools
   - Set up backups for database

### Deployment Platforms

- **Heroku**: Use `Procfile` and configure environment variables
- **AWS Elastic Beanstalk**: Configure `.ebextensions`
- **DigitalOcean App Platform**: Configure via dashboard
- **Docker**: Create `Dockerfile` and `docker-compose.yml`
- **VPS**: Use Gunicorn + Nginx

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes:**
   - Write clean, readable code
   - Add comments where necessary
   - Follow PEP 8 style guidelines
4. **Write/update tests** for your changes
5. **Commit your changes:**
   ```bash
   git commit -m "Add: description of your changes"
   ```
6. **Push to your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** with a clear description

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and modular

---

## 📄 License

This project is licensed under the MIT License (or your preferred license). See the LICENSE file for details.

---

## 🙏 Acknowledgments

- Django community for the excellent framework
- Contributors and open-source libraries that made this project possible
- OpenAI for AI capabilities
- All the farmers and agricultural experts who inspired this project

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team
- Check the documentation

---

## 🔮 Future Enhancements

- Mobile app (React Native/Flutter)
- Advanced ML models for predictions
- Integration with IoT sensors
- Real-time market price APIs
- Blockchain for supply chain tracking
- Farmer community features
- Advanced analytics dashboard
- SMS/WhatsApp notifications

---

**Built with ❤️ for Indian Farmers**
#   A g r i G e n i e A i  
 