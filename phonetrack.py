import phonenumbers
import requests
from phonenumbers import geocoder

# Function to get address with PIN code using Google Maps Geocoding API
def get_address_from_phone_number(phone_number):
    # Get the location description for the phone number (country, region)
    location = geocoder.description_for_number(phone_number, "en")
    
    # Use Google Geocoding API to get address details
    api_key = 'YOUR_GOOGLE_API_KEY'  # Replace with your Google API key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    # Query the API with the location (e.g., city, country)
    response = requests.get(base_url, params={
        'address': location,
        'key': api_key
    })
    
    # Check if the API call was successful
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            address = data['results'][0]['formatted_address']
            pin_code = None
            for component in data['results'][0]['address_components']:
                if 'postal_code' in component['types']:
                    pin_code = component['long_name']
                    break
            return f"Address: {address}\nPIN Code: {pin_code if pin_code else 'Not available'}"
        else:
            return "No address found."
    else:
        return "Error with API request."

# Parse phone numbers
phone_number1 = phonenumbers.parse("+917028431113")
phone_number2 = phonenumbers.parse("+918766583935")
phone_number3 = phonenumbers.parse("+918788325371")
phone_number4 = phonenumbers.parse("+919765606483")

# Get address with PIN code for each phone number
print("\nPhone Numbers Location with Address and PIN Code\n")
print(get_address_from_phone_number(phone_number1))
print(get_address_from_phone_number(phone_number2))
print(get_address_from_phone_number(phone_number3))
print(get_address_from_phone_number(phone_number4))
