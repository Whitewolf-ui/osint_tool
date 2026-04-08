# ⚡ OSINT Dashboard

An Open Source Intelligence gathering tool built with Python and FastAPI.

## What it does
- 🌐 **IP Lookup** — location, ISP, timezone, coordinates
- 👤 **Username Search** — checks GitHub, Reddit, TikTok, Instagram, Twitter, Pinterest
- 📧 **Email Check** — validates format, extracts domain info
- 📱 **Phone Lookup** — carrier, country, timezone, number format

## Requirements
- Python 3.10+
- Kali Linux / any Linux distro

## Installation

git clone https://github.com/Whitewolf-ui/osint_tool.git
cd osint_tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Usage

uvicorn main:app --reload

Then open your browser at:
http://127.0.0.1:8000

## Project Structure

osint_tool/
├── modules/
│   ├── ip_lookup.py       # IP geolocation
│   ├── username_check.py  # Social media presence
│   ├── email_check.py     # Email validation
│   └── phone_check.py     # Phone number info
├── templates/
│   └── dashboard.html     # Web UI
├── main.py                # FastAPI app
├── requirements.txt       # Dependencies
└── README.md              # This file

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Web dashboard |
| GET | /lookup/ip?value= | IP lookup |
| GET | /lookup/username?value= | Username search |
| GET | /lookup/email?value= | Email check |
| GET | /lookup/phone?value= | Phone lookup |

## Built With
- FastAPI
- ipinfo.io - IP data
- phonenumbers - Phone parsing

## Author
Whitewolf-ui

## License
MIT
