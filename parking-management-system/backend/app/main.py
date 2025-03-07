from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user_routes, parking_routes
from .websockets import parking_ws
from .database import init_db
from .config import settings

# יוצרים את היישום של FastAPI
app = FastAPI(
    title="Parking Management System",
    description="API לניהול חניות בבניין עם GraphQL, WebSockets ו-Redis",
    version="1.0.0",
)

# מאפשרים קריאות מה-Frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ניתן להגביל לדומיינים ספציפיים בפרודקשן
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# מחברים את הנתיבים (Routes) ל-API
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(parking_routes.router, prefix="/parking", tags=["Parking"])
app.include_router(parking_ws.router, prefix="/ws", tags=["WebSockets"])

# אתחול מסד הנתונים בזמן עליית השרת
@app.on_event("startup")
async def startup_event():
    await init_db()
    print("✅ מסד הנתונים אותחל בהצלחה!")

# נקודת כניסה – אם רוצים לבדוק שה-API עובד
@app.get("/")
async def root():
    return {"message": "🚀 Parking Management API is running!"}
