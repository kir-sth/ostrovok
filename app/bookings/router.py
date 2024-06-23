from fastapi import APIRouter, Depends, status
from pydantic import TypeAdapter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingsInfo, SNewBooking
from app.exceptions import RoomCannotBeBookedException
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_bookings(
    user: Users = Depends(get_current_user)
) -> list[SBookingsInfo]:
    return await BookingDAO.find_all_with_images(user_id=user.id)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_booking(
    booking: SNewBooking,
    user: Users = Depends(get_current_user),
) -> SNewBooking:
    booking = await BookingDAO.add(
        user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to
    )
    if not booking:
        raise RoomCannotBeBookedException
    booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
    return booking


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_booking(
    booking_id: int,
    user: Users = Depends(get_current_user),
) -> None:
    await BookingDAO.delete(id=booking_id, user_id=user.id)
