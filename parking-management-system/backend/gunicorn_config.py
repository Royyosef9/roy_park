bind = "0.0.0.0:8000"  # מאזין על כל הכתובות בפורט 8000
workers = 4  # מספר תהליכים במקביל (לפי כמות הליבות בשרת)
worker_class = "uvicorn.workers.UvicornWorker"  # משתמש ב-Uvicorn לניהול ה-API
timeout = 120  # מגביל זמן תגובה של שרתים
loglevel = "info"  # רמת הלוגים
