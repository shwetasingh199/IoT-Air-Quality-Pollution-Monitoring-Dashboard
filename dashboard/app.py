import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# -------------------------------
# IMPORT API CLIENT
# -------------------------------

try:
    from api_client import get_air_quality
except Exception as e:
    st.error(f"Import Error: {e}")
    st.stop()

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="IoT Air Quality Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -------------------------------
# PATHS
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sensor_logs.csv"

# -------------------------------
# TITLE
# -------------------------------

st.title("🌍 IoT Air Quality & Pollution Monitoring Dashboard")

# -------------------------------
# SIDEBAR
# -------------------------------

mode = st.sidebar.radio(
    "Select Mode",
    [
        "Simulation Mode",
        "Live AQI Mode"
    ]
)

# ==================================================
# LIVE AQI MODE
# ==================================================

if mode == "Live AQI Mode":

    st.header("🌍 Global Live Air Quality Monitoring")

    city = st.text_input(
        "Enter Any City Name",
        value="Delhi"
    )

    if st.button("Get Air Quality"):

        air_data = get_air_quality(city)
        st.write(air_data)
        

        if air_data is None:

            st.error("City not found or API Error")
            st.stop()

        aqi = air_data["aqi"]
        pm25 = air_data["pm25"]
        pm10 = air_data["pm10"]
        co = air_data["co"]
        temperature = air_data.get("temperature", "N/A")
        humidity = air_data.get("humidity", "N/A")

        # AQI Status

        if aqi == 1:
            status = "Good"
            recommendation = "Air quality is excellent."
        elif aqi == 2:
            status = "Fair"
            recommendation = "Acceptable air quality."
        elif aqi == 3:
            status = "Moderate"
            recommendation = "Sensitive people should reduce outdoor activity."
        elif aqi == 4:
            status = "Poor"
            recommendation = "Avoid prolonged outdoor exposure."
        else:
            status = "Very Poor"
            recommendation = "Stay indoors if possible."

        st.subheader(f"📍 Location: {city}")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "AQI",
            aqi
        )

        if temperature != "N/A":
            temp_display = round(float(temperature), 2)
        else:
            temp_display = "N/A"

        if humidity != "N/A":
            humidity_display = round(float(humidity), 2)
        else:
            humidity_display = "N/A"

        col2.metric(
            "Temperature °C",
            temp_display
        )

        col3.metric(
            "Humidity %",
        humidity_display
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "PM2.5",
            round(pm25, 2)
        )

        col5.metric(
            "PM10",
            round(pm10, 2)
        )

        col6.metric(
            "CO",
            round(co, 2)
        )

        st.success(f"Status: {status}")

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=aqi,
                title={"text": f"{city} AQI"},
                gauge={
                    "axis": {"range": [1, 5]},
                    "steps": [
                        {"range": [1, 2], "color": "green"},
                        {"range": [2, 3], "color": "yellow"},
                        {"range": [3, 4], "color": "orange"},
                        {"range": [4, 5], "color": "red"}
                    ]
                }
            )
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

        pollutant_df = pd.DataFrame(
            {
                "Pollutant": [
                    "PM2.5",
                    "PM10",
                    "CO"
                ],
                "Value": [
                    pm25,
                    pm10,
                    co
                ]
            }
        )

        fig = px.bar(
            pollutant_df,
            x="Pollutant",
            y="Value",
            title="Pollutant Concentration"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("💡 Health Recommendation")

        st.info(recommendation)

# ==================================================
# SIMULATION MODE
# ==================================================

else:

    st.header("🧪 Simulated IoT Monitoring")

    if not DATA_FILE.exists():

        st.error(
            f"CSV file not found:\n{DATA_FILE}"
        )

        st.stop()

    try:

        df = pd.read_csv(DATA_FILE)

    except Exception as e:

        st.error(f"CSV Read Error: {e}")
        st.stop()

    if df.empty:

        st.warning("No data available.")
        st.stop()

    latest = df.iloc[-1]

    aqi = latest["aqi"]
    temperature = latest["temperature"]
    humidity = latest["humidity"]
    status = latest["status"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Current AQI", int(aqi))
    col2.metric("Temperature °C", round(float(temperature), 2))
    col3.metric("Humidity %", round(float(humidity), 2))
    col4.metric("Status", status)

    st.divider()

    # -------------------------------
    # AQI Gauge
    # -------------------------------

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=aqi,
            title={"text": "AQI Gauge"},
            gauge={
                "axis": {"range": [0, 500]},
                "steps": [
                    {"range": [0, 50], "color": "green"},
                    {"range": [50, 100], "color": "yellow"},
                    {"range": [100, 200], "color": "orange"},
                    {"range": [200, 500], "color": "red"}
                ]
            }
        )
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    # -------------------------------
    # CHARTS
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:

        fig_aqi = px.line(
            df,
            x="timestamp",
            y="aqi",
            title="AQI Trend"
        )

        st.plotly_chart(
            fig_aqi,
            use_container_width=True
        )

    with col2:

        fig_temp = px.line(
            df,
            x="timestamp",
            y="temperature",
            title="Temperature Trend"
        )

        st.plotly_chart(
            fig_temp,
            use_container_width=True
        )

    fig_humidity = px.line(
        df,
        x="timestamp",
        y="humidity",
        title="Humidity Trend"
    )

    st.plotly_chart(
        fig_humidity,
        use_container_width=True
    )

    # -------------------------------
    # PIE CHART
    # -------------------------------

    status_counts = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = [
        "Status",
        "Count"
    ]

    fig_pie = px.pie(
        status_counts,
        names="Status",
        values="Count",
        title="Pollution Distribution"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    # -------------------------------
    # ALERT PANEL
    # -------------------------------

    st.subheader("🚨 Alert Panel")

    if status == "Hazardous":

        st.error(
            "⚠ Hazardous Air Quality Detected"
        )

    elif status == "Poor":

        st.warning(
            "⚠ Poor Air Quality Detected"
        )

    else:

        st.success(
            "✅ Air Quality Acceptable"
        )

    # -------------------------------
    # DATA TABLE
    # -------------------------------

    st.subheader("Sensor Data")

    st.dataframe(
        df.tail(100),
        use_container_width=True
    )

    # -------------------------------
    # DOWNLOAD
    # -------------------------------

    with open(DATA_FILE, "rb") as file:

        st.download_button(
            label="📥 Download CSV Report",
            data=file,
            file_name="sensor_logs.csv",
            mime="text/csv"
        )