def generate_google_maps_url(latitude, longitude, zoom):
    base_url = "https://www.google.com/maps/search/?api=1"
    location_string = f"{latitude},{longitude}"
    zoom_string = f"&zoom={zoom}"
    return f"{base_url}&query={location_string}{zoom_string}"

# Example usage
latitude = -35.473469
longitude = 149.012375
zoom = 15
url = generate_google_maps_url(latitude, longitude, zoom)
print(url)