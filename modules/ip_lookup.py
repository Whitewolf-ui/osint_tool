import requests

def lookup_ip(ip: str) -> dict:
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = r.json()
        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "org": data.get("org"),
            "timezone": data.get("timezone"),
            "loc": data.get("loc"),
        }
    except Exception as e:
        return {"error": str(e)}
