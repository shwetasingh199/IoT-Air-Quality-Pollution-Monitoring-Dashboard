def classify_air_quality(aqi):

    if aqi <= 50:

        return "Good"

    elif aqi <= 100:

        return "Moderate"

    elif aqi <= 200:

        return "Poor"

    return "Hazardous"