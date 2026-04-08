import requests

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
}

def check_username(username: str) -> dict:
    results = {}
    for platform, url in PLATFORMS.items():
        try:
            full_url = url.format(username)
            r = requests.get(full_url, timeout=5, allow_redirects=True)
            results[platform] = {
                "url": full_url,
                "found": r.status_code == 200
            }
        except Exception as e:
            results[platform] = {"url": full_url, "found": False, "error": str(e)}
    return results
