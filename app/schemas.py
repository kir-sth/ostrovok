from datetime import date
from fastapi import Query
from pydantic import BaseModel
from typing import Optional


class HotelSchema(BaseModel):
    address: str
    name: str
    stars: int


class HotelsSearchArgs():
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(default=None, ge=1, le=5),
        has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class BookingSchema(BaseModel):
    room_id: int
    date_from: date
    date_to: date
