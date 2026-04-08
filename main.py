import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from modules.ip_lookup import lookup_ip
from modules.username_check import check_username
from modules.email_check import check_email
from modules.phone_check import check_phone

app = FastAPI(title="OSINT Dashboard")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "dashboard.html")

@app.get("/lookup/ip")
def ip(value: str):
    return lookup_ip(value)

@app.get("/lookup/username")
def username(value: str):
    return check_username(value)

@app.get("/lookup/email")
def email(value: str):
    return check_email(value)

@app.get("/lookup/phone")
def phone(value: str):
    return check_phone(value)
