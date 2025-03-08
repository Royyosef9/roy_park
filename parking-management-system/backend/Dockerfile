# משתמשים ב-Image רשמי של Python 3.10
FROM python:3.10

# מגדירים משתני סביבה
ENV PYTHONUNBUFFERED=1 \
    APP_HOME=/app

# מגדירים תיקיית עבודה
WORKDIR $APP_HOME

# מעתיקים את הקבצים ל-Docker
COPY . $APP_HOME

# מתקינים את כל התלויות
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# מפעילים את Gunicorn עם Uvicorn
CMD ["gunicorn", "-c", "gunicorn_config.py", "app.main:app"]
