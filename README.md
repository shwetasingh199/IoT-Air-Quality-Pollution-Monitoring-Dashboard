# 🌍 IoT-Based Air Quality & Pollution Monitoring Dashboard

## 📌 Project Overview

The IoT-Based Air Quality & Pollution Monitoring Dashboard is a software-based environmental monitoring system that simulates IoT sensor readings and integrates real-time air quality information from OpenWeather APIs.

The system monitors:

* Air Quality Index (AQI)
* PM2.5 Concentration
* PM10 Concentration
* Carbon Monoxide (CO)
* Temperature
* Humidity

The collected data is visualized through an interactive Streamlit dashboard with charts, gauges, alerts, and analytics.

This project demonstrates how modern IoT monitoring systems can be designed for smart cities, environmental agencies, educational institutions, healthcare facilities, and industrial environments.

---

# 🎯 Problem Statement

Air pollution is one of the biggest environmental challenges worldwide.

Traditional monitoring stations are expensive and limited in coverage. Modern IoT-based systems provide a low-cost solution for collecting, analyzing, and visualizing environmental data in real time.

This project simulates an industry-oriented air quality monitoring solution capable of:

* Tracking environmental conditions
* Monitoring pollution levels
* Visualizing AQI trends
* Generating alerts
* Supporting environmental decision-making

---

# 🚀 Key Features

### Real-Time Air Quality Monitoring

* Live AQI monitoring using OpenWeather API
* Global city search support
* PM2.5 monitoring
* PM10 monitoring
* CO monitoring

### Environmental Monitoring

* Temperature tracking
* Humidity tracking
* Pollution classification

### Interactive Dashboard

* AQI Gauge
* KPI Cards
* Trend Analysis
* Pie Charts
* Alert Panels
* Data Tables

### Data Logging

* CSV storage
* Historical records
* Downloadable reports

### Simulation Module

* Simulated IoT sensor data generation
* AQI simulation
* Pollution event simulation
* Alert testing

---

# 🏗️ System Architecture

```text
OpenWeather API / Simulated Sensors
                │
                ▼
       Data Collection Layer
                │
                ▼
      AQI Classification Engine
                │
                ▼
       Data Storage (CSV)
                │
                ▼
        Streamlit Dashboard
                │
                ▼
       Analytics & Alerts
```

---

# 📂 Project Structure

```text
IoT-Air-Quality-Pollution-Monitoring-Dashboard/
│
├── arduino_code/
│
├── python_simulation/
│   ├── data_generator.py
│   ├── pollution_classifier.py
│   └── logger.py
│
├── dashboard/
│   ├── app.py
│   └── api_client.py
│
├── data/
│   └── sensor_logs.csv
│
├── outputs/
│
├── images/
│   ├── dashboard_home.png
│   ├── live_aqi_mode.png
│   ├── aqi_gauge.png
│   ├── pollution_chart.png
│   ├── alert_panel.png
│   ├── csv_logs.png
│   └── project_structure.png
│
├── circuit_diagram/
│
├── reports/
│
├── docs/
│
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── main.py
```

---

# 🧠 Workflow

```text
Generate / Fetch Data
          │
          ▼
AQI & Pollution Analysis
          │
          ▼
Classification Engine
          │
          ▼
CSV Data Logging
          │
          ▼
Dashboard Visualization
          │
          ▼
Alerts & Reporting
```

---

# 🌐 Live AQI Mode

The system fetches live air quality information from OpenWeather.

Users can search any city worldwide.

Examples:

* Delhi
* Mumbai
* Chandigarh
* London
* Paris
* Tokyo
* Sydney
* New York

Displayed Information:

* AQI
* PM2.5
* PM10
* CO
* Temperature
* Humidity
* Pollution Status

---

# 🧪 Simulation Mode

Simulation Mode generates virtual environmental readings.

Generated Parameters:

* AQI
* Temperature
* Humidity
* Pollution Status

Categories:

| AQI Range | Category  |
| --------- | --------- |
| 0 - 50    | Good      |
| 51 - 100  | Moderate  |
| 101 - 200 | Poor      |
| 201+      | Hazardous |

---

# 📊 Dashboard Features

### KPI Cards

Displays:

* AQI
* Temperature
* Humidity
* Pollution Status

### AQI Gauge

Visual indicator of pollution severity.

### Trend Analysis

Tracks:

* AQI Trends
* Temperature Trends
* Humidity Trends

### Distribution Analysis

Pollution category distribution chart.

### Alert System

Automatic warnings when:

* AQI becomes Poor
* AQI becomes Hazardous

---

# 📸 Screenshots

## Dashboard Home

<img width="1912" height="590" alt="Screenshot 2026-06-11 132658" src="https://github.com/user-attachments/assets/a709458a-53c8-4841-bd46-a2a1a152942b" />

---

## Live AQI Monitoring

<img width="1889" height="744" alt="Screenshot 2026-06-11 132838" src="https://github.com/user-attachments/assets/664b16a6-3535-4819-8f8c-b3fc5254710c" />

<img width="1498" height="516" alt="Screenshot 2026-06-11 132847" src="https://github.com/user-attachments/assets/7f8ae0ad-1806-46f5-bf63-be9ddcd8fecc" />

---

## AQI Gauge

<img width="1092" height="606" alt="Screenshot 2026-06-11 132856" src="https://github.com/user-attachments/assets/c41e5732-5aa9-4b00-b18e-180bbc1877c0" />


---

## Pollution Analytics

<img width="1871" height="843" alt="Screenshot 2026-06-11 132908" src="https://github.com/user-attachments/assets/302714d3-f307-4cdb-99f1-f90424f696b3" />


---

## CSV Logs

<img width="1891" height="795" alt="Screenshot 2026-06-11 132809" src="https://github.com/user-attachments/assets/bf7f39ce-6318-4ead-a503-fcfacc2607ab" />


---

# ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/IoT-Air-Quality-Pollution-Monitoring-Dashboard.git
```

Move into project folder

```bash
cd IoT-Air-Quality-Pollution-Monitoring-Dashboard
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

Create a `.env` file

```env
OPENWEATHER_API_KEY=YOUR_API_KEY
```

Example `.env.example`

```env
OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
```

---

# ▶️ Running the Project

Generate Simulation Data

```bash
python main.py
```

Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📈 Sample Output

```text
AQI: 78
Temperature: 31.5 °C
Humidity: 63 %
Status: Moderate
```

---

# 📋 Future Improvements

* MQTT Integration
* Multi-City Monitoring
* Interactive Maps
* AQI Forecasting using Machine Learning
* PDF Report Generation
* Email Alerts
* Telegram Notifications
* Real-Time Streaming

---

# 🎓 Learning Outcomes

Through this project, the following concepts were explored:

* IoT Architecture Design
* Environmental Monitoring
* AQI Analytics
* API Integration
* Data Visualization
* Dashboard Development
* Data Logging
* Streamlit Applications
* Python Programming
* Software-Based IoT Simulation

---

# 💼 Industry Relevance

Applications include:

* Smart Cities
* Environmental Monitoring Agencies
* Schools and Universities
* Healthcare Facilities
* Industrial Pollution Monitoring
* Smart Homes
* Research Organizations

---

# 👨‍💻 Author

**SHWETA SINGH**

**Developed as an Industry-Oriented IoT & Environmental Analytics Project for academic learning, portfolio development, and placement preparation.**

---

⭐ If you found this project useful, consider giving it a star.
