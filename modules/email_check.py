import re
import requests

def check_email(email: str) -> dict:
    result = {}
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    result["valid_format"] = bool(re.match(pattern, email))
    
    if not result["valid_format"]:
        result["error"] = "Invalid email format"
        return result

    domain = email.split("@")[1]
    result["domain"] = domain

    try:
        r = requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=demo", timeout=5)
        data = r.json()
        result["disposable"] = data.get("data", {}).get("disposable", "unknown")
        result["smtp_valid"] = data.get("data", {}).get("smtp_server", "unknown")
    except:
        result["disposable"] = "unknown"
        result["smtp_valid"] = "unknown"

    return result
