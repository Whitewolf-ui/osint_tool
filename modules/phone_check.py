import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def check_phone(phone: str) -> dict:
    try:
        parsed = phonenumbers.parse(phone, None)
        valid = phonenumbers.is_valid_number(parsed)
        return {
            "valid": valid,
            "country": geocoder.description_for_number(parsed, "en"),
            "carrier": carrier.name_for_number(parsed, "en"),
            "timezone": list(timezone.time_zones_for_number(parsed)),
            "international_format": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "local_format": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
        }
    except Exception as e:
        return {"error": str(e), "tip": "Include country code e.g. +2348012345678"}
