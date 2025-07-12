def outfitRecommendation(temp,condition):
    if temp > 30:
        advice = "It's hot 🌞. Wear light clothes like shorts and a t-shirt."
    elif 20 <= temp <= 30:
        advice = "Nice weather 🌤️. Wear something comfortable."
    elif 10 <= temp < 20:
        advice = "It's cool 🍂. Wear a hoodie or light jacket."
    else:
        advice = "It's cold 🧥. Wear warm clothes and maybe a scarf!"

    if "Rain" in condition:
        advice += " Also, carry an umbrella ☔️."
    elif "Snow" in condition:
        advice += " Wear boots and gloves ❄️."

    return advice
    