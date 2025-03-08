from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
import asyncio

router = APIRouter()

# רשימה לניהול כל החיבורים הפתוחים
active_connections: List[WebSocket] = []

class ConnectionManager:
    """מנהל חיבורים עבור WebSockets"""
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """מתחבר ל-WebSocket ושומר את החיבור"""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """סוגר חיבור ומסיר אותו מהרשימה"""
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        """שולח הודעה לכל המשתמשים המחוברים"""
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                self.disconnect(connection)

# יצירת מנהל חיבורים
manager = ConnectionManager()

@router.websocket("/ws/parking")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket לעדכוני חניות בזמן אמת"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = {"message": f"Received: {data}"}
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
