from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import random
import json

app = FastAPI(title="لوحة التحكم", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def generate_chart_data():
    """Generate realistic-looking sales data for the past 7 days"""
    days = []
    sales = []
    visits = []
    today = datetime.now()
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        days.append(day.strftime("%a"))
        sales.append(random.randint(8000, 25000))
        visits.append(random.randint(400, 1200))
    return days, sales, visits


def generate_recent_orders():
    names = ["أحمد محمد", "سارة علي", "خالد عبدالله", "منى حسن", "عمر يوسف",
             "ريم الأحمد", "فيصل النصر", "نورة السالم"]
    products = ["MacBook Pro", "iPhone 15", "iPad Air", "AirPods Pro", "Apple Watch", "iMac"]
    statuses = ["مكتمل", "قيد المعالجة", "تم الشحن", "ملغي"]
    status_colors = {"مكتمل": "success", "قيد المعالجة": "warning", "تم الشحن": "info", "ملغي": "danger"}

    orders = []
    for i in range(8):
        status = random.choice(statuses)
        orders.append({
            "id": f"#ORD-{random.randint(1000,9999)}",
            "name": random.choice(names),
            "product": random.choice(products),
            "amount": f"{random.randint(500, 5000):,} ر.س",
            "status": status,
            "color": status_colors[status],
            "date": (datetime.now() - timedelta(hours=random.randint(1, 48))).strftime("%Y/%m/%d")
        })
    return orders


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    days, sales, visits = generate_chart_data()
    orders = generate_recent_orders()

    stats = {
        "total_revenue": f"{random.randint(80000, 150000):,}",
        "total_orders": random.randint(1200, 2500),
        "total_customers": random.randint(8000, 15000),
        "conversion_rate": f"{random.uniform(3.5, 8.2):.1f}",
        "revenue_change": f"+{random.uniform(8, 25):.1f}",
        "orders_change": f"+{random.uniform(5, 18):.1f}",
        "customers_change": f"+{random.uniform(3, 12):.1f}",
        "conversion_change": f"+{random.uniform(0.5, 2.5):.1f}",
    }

    return templates.TemplateResponse("index.html", {
        "request": request,
        "stats": stats,
        "orders": orders,
        "chart_days": json.dumps(days),
        "chart_sales": json.dumps(sales),
        "chart_visits": json.dumps(visits),
        "current_time": datetime.now().strftime("%A، %d %B %Y"),
    })


@app.get("/api/refresh-stats")
async def refresh_stats():
    days, sales, visits = generate_chart_data()
    return {
        "total_revenue": f"{random.randint(80000, 150000):,}",
        "total_orders": random.randint(1200, 2500),
        "total_customers": random.randint(8000, 15000),
        "conversion_rate": f"{random.uniform(3.5, 8.2):.1f}",
        "chart_days": days,
        "chart_sales": sales,
        "chart_visits": visits,
    }
