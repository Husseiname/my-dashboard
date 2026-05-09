# 🚀 لوحة التحكم - NovaDash

موقع لوحة تحكم متكامل مبني بـ FastAPI + Python

## 📁 هيكل المشروع

```
dashboard/
├── main.py              # الملف الرئيسي للتطبيق
├── requirements.txt     # المكتبات المطلوبة
├── templates/
│   └── index.html       # قالب HTML للواجهة
└── static/              # ملفات CSS/JS (اختياري)
```

## ⚙️ طريقة التشغيل

### 1. تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### 2. تشغيل الخادم
```bash
uvicorn main:app --reload
```

### 3. فتح المتصفح
```
http://localhost:8000
```

## 🌟 المميزات

- ✅ لوحة تحكم عربية كاملة (RTL)
- ✅ 4 بطاقات إحصاء تفاعلية
- ✅ رسم بياني للمبيعات والزيارات (Chart.js)
- ✅ رسم دائري لتوزيع الفئات
- ✅ جدول آخر الطلبات
- ✅ شريط تقدم أداء المنتجات
- ✅ زر تحديث البيانات (API endpoint)
- ✅ تصميم داكن احترافي
- ✅ متجاوب مع جميع الشاشات

## 🔌 API Endpoints

| المسار | الوصف |
|--------|-------|
| `GET /` | الصفحة الرئيسية |
| `GET /api/refresh-stats` | تحديث الإحصاءات |
| `GET /docs` | توثيق API التلقائي (Swagger) |

## 🛠️ التطوير

لإضافة صفحات جديدة:
```python
@app.get("/products", response_class=HTMLResponse)
async def products(request: Request):
    return templates.TemplateResponse("products.html", {"request": request})
```
