from fastapi import APIRouter
from sqlalchemy import Select

from app.database import async_session_maker
from app.bookings.models import Bookings


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)

@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = Select(Bookings)
        result = await session.execute(query)
        print(result)

@router.get("/{booking_id}")
def get_booking(booking_id):
    pass
