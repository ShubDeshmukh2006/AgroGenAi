🎯 Overview
AgriGenie AI is a full-stack intelligent farming platform built to bridge the technology gap for Indian farmers. It combines machine learning, natural language processing, and real-time data to deliver actionable farming insights — in the farmer's own language.
The Problem

Indian farmers lose ₹50,000+ crore annually due to wrong crop selection and pest damage
70% of farmers cannot access agricultural advisory in their native language
Government schemes worth ₹1.5 lakh crore go unclaimed due to lack of awareness

Our Solution
A unified AI platform that speaks the farmer's language — literally — with voice support in 8 Indian languages, ML-powered crop recommendations, and real-time weather intelligence.

✨ Key Features
🌱 AI Crop Recommendation Engine

Gaussian suitability scoring algorithm analyzing soil pH, NPK levels, temperature, rainfall, and humidity
Predicts expected yield and estimated profit per crop
Recommends top crops ranked by suitability score for the farmer's specific conditions

🎙️ Multilingual Voice Assistant

Supports 8 Indian languages: English, Hindi (हिन्दी), Marathi (मराठी), Bengali (বাংলা), Telugu (తెలుగు), Tamil (தமிழ்), Gujarati (ગુજરાતી), Urdu (اردو)
Speech-to-text input using SpeechRecognition
Text-to-speech responses using gTTS
Automatic language detection with langdetect

🌤️ Real-Time Weather Dashboard

Live weather data including temperature, humidity, rainfall, and wind
Location-based forecasting using geopy
Irrigation scheduling recommendations based on weather patterns

🐛 Pesticides & Disease Guide

Comprehensive pest and disease identification
Safe pesticide product recommendations
Application guidelines and safety precautions

🏛️ Government Schemes Portal

Database of active agricultural schemes (subsidies, loans, insurance, training, equipment)
Eligibility checker and application tracking
Direct links to official application forms
Application status management (Pending → Approved → Completed)

📄 PDF Report Generation

Hospital-grade agricultural reports using ReportLab
Crop recommendation reports with suitability analysis
Exportable farm data summaries

🔐 User Authentication System

Secure farmer registration and login
Personal farm profile management
History tracking for recommendations and applications


🏗️ Tech Stack
Backend
TechnologyPurposeDjango 4.2Core web framework & ORMDjango REST FrameworkRESTful API endpointsNumPyGaussian ML suitability scoringOpenAI APIAI-powered farming advisorygTTSText-to-speech in 8 languagesSpeechRecognitionVoice input processinglangdetectAutomatic language detectionReportLabProfessional PDF generationpytesseractOCR for document scanninggeopyLocation & weather servicesMatplotlibData visualization
Frontend
TechnologyPurposeDjango TemplatesServer-side renderingBootstrapResponsive UI frameworkJavaScriptInteractive voice interface
Database
EnvironmentDatabaseDevelopmentSQLiteProductionPostgreSQL-ready

📁 Project Structure
AgriGenieAi/
├── agrigenie/
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── apps/
│   ├── crops/               # Crop recommendation engine
│   │   ├── ai.py            # Gaussian yield prediction ML model
│   │   ├── models.py        # Crop & recommendation data models
│   │   ├── views.py         # Recommendation logic & API
│   │   └── utils.py         # CropRecommendationEngine
│   ├── voice/               # Multilingual voice assistant
│   │   ├── views.py         # 8-language response system
│   │   └── urls.py          # Voice assistant endpoints
│   ├── weather/             # Weather dashboard
│   ├── pesticides/          # Pesticide & disease guide
│   ├── schemes/             # Government schemes portal
│   │   ├── models.py        # GovernmentScheme & Application models
│   │   └── views.py         # Scheme listing & application tracking
│   └── exports/             # PDF report generation
├── templates/               # HTML templates for all modules
├── requirements.txt         # Python dependencies
├── manage.py                # Django management CLI
└── add_crops.py             # Database seeding script

🚀 Quick Start
Prerequisites

Python 3.11+
pip
Git

Installation
bash# 1. Clone the repository
git clone https://github.com/ShubDeshmukh2006/AgriGenieAi.git
cd AgriGenieAi

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env and add your API keys:
# OPENAI_API_KEY=your_openai_key
# SECRET_KEY=your_django_secret_key

# 5. Run database migrations
python manage.py migrate

# 6. Seed crop database
python add_crops.py

# 7. Start the development server
python manage.py runserver
Visit http://localhost:8000 to access AgriGenie AI.

🔧 Environment Variables
Create a .env file in the root directory:
envSECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
OPENAI_API_KEY=your-openai-api-key

⚠️ Never commit your .env file or API keys to GitHub.


📊 ML Model — Gaussian Crop Suitability
AgriGenie uses a custom Gaussian suitability scoring algorithm to recommend crops:
python# Suitability score based on optimal growing conditions
score = exp(-0.5 * ((value - optimal) / tolerance)²)
Input Parameters:

Soil pH
Nitrogen (N), Phosphorus (P), Potassium (K) levels
Temperature (°C)
Rainfall (mm)
Humidity (%)

Output:

Suitability score per crop (0–100%)
Expected yield (tonnes/hectare)
Estimated profit (₹/hectare)
Ranked crop recommendations


🌍 Supported Languages
LanguageCodeScriptEnglishenLatinHindihiदेवनागरीMarathimrमराठीBengalibnবাংলাTeluguteతెలుగుTamiltaதமிழ்GujaratiguગુજરાતીUrduurاردو

🛣️ Roadmap

 Mobile app (React Native)
 Deploy on AWS EC2 with RDS
 Real-time crop market prices API
 Satellite imagery analysis for farm health
 WhatsApp bot integration for offline farmers
 Multi-user farm management dashboard


👨‍💻 Author
Shubham Manoj Deshmukh

📍 Khopoli, Maharashtra, India
🎓 B.E. Computer Engineering (2nd Year)
🐍 Python Certified — 100% Score, Disha Computer Institute
☁️ AWS Cloud Practitioner (In Progress)
🔗 GitHub: @ShubDeshmukh2006


📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

🙏 Acknowledgments

OpenAI for GPT API powering the agricultural advisory
Django community for the excellent web framework
Indian farmers — the true inspiration behind this project
