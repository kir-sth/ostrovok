from datetime import date, datetime, timedelta
from fastapi import Query, status

from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoomInfo
from app.hotels.router import router


@router.get("/{hotel_id}/rooms", status_code=status.HTTP_200_OK)
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(
        ...,
        description=f"Например, {datetime.now().date()}"
    ),
    date_to: date = Query(
        ...,
        description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"
    ),
) -> list[SRoomInfo]:
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms
