# قالب‌ها در جنگو با MDUI

## نیازمندی‌ها

- Python 3.12 یا جدیدتر (تست‌شده با Python 3.15.2)
- Django 5.0 (تست‌شده با Django 5.0.14)
- دیتابیس SQLite (داخل خود پایتون است؛ نصب جدا نمی‌خواهد)
- کتابخانه MDUI نسخه 2.1.5 داخل خود پروژه است (`static/css/mdui.css` و `static/js/mdui.global.js`) و اینترنت لازم ندارد.

## ساختار پروژه

```
Mehrshad-Templates/
├── config/          تنظیمات و مسیرهای اصلی پروژه
├── pages/           اپ صفحه‌ها: مدل، ویو، قالب و تست
├── static/          فایل‌های MDUI و CSS اختصاصی
├── README.md
└── manage.py
```

## اجرا

```powershell
cd Mehrshad-Templates
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install "Django==5.0.*"
python manage.py migrate
python manage.py runserver
```

بعد در مرورگر باز کنید: `http://127.0.0.1:8000/`
