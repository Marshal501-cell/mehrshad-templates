# قالب‌ها در جنگو با MDUI

پروژه تکلیف «templateها در جنگو»: نمایش چهار صفحه ساخته‌شده با کتابخانه MDUI در مسیرهای مناسب جنگو.

## صفحه‌ها

| صفحه | مسیر |
| --- | --- |
| خانه | `/` |
| درباره ما | `/about/` |
| تماس با ما | `/contact/` |
| ثبت‌نام | `/register/` |
| ورود | `/login/` |
| پنل ادمین | `/admin/` |

ثبت‌نام، کاربر جدید می‌سازد و ورود با همان حساب انجام می‌شود. فرم تماس پیام را در دیتابیس ذخیره می‌کند و پیام «پیام شما با موفقیت ثبت شد.» را یک بار نشان می‌دهد. اطلاعات تماس صفحه تماس فرضی است.

## نیازمندی‌ها

- Python 3.12 یا جدیدتر (تست‌شده با Python 3.15.2)
- Django 5.0 (تست‌شده با Django 5.0.14)
- دیتابیس SQLite (داخل خود پایتون است؛ نصب جدا نمی‌خواهد)
- کتابخانه MDUI نسخه 2.1.5 داخل خود پروژه است (`static/css/mdui.css` و `static/js/mdui.global.js`) و اینترنت لازم ندارد.

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

ساخت سوپر یوزر برای پنل ادمین (اختیاری):

```powershell
python manage.py createsuperuser
```

## تست‌ها

```powershell
python manage.py test
```

## ساختار پروژه

```
Mehrshad-Templates/
├── config/          تنظیمات و مسیرهای اصلی پروژه
├── pages/           اپ صفحه‌ها: مدل، ویو، قالب و تست
├── static/          فایل‌های MDUI و CSS اختصاصی
├── README.md
└── manage.py
```
