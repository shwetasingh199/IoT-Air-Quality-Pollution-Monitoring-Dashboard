def generate_alert(aqi):

    if aqi > 300:

        return (
            True,
            "WARNING: Hazardous Air Quality"
        )

    return (
        False,
        "Safe"
    )