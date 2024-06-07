import uvicorn
from fastapi import FastAPI, Depends

from app.schemas import HotelsSearchArgs, HotelSchema, BookingSchema
from app.bookings.router import router as router_bookings


app = FastAPI()
app.include_router(router_bookings)


@app.get("/hotels")
async def get_hotels(
    hotels_search_args: HotelsSearchArgs = Depends(),
) -> list[HotelSchema]:
    hotels = [
        {
            "address": "Ул. Гагарина, 1",
            "name": "Super Hotel",
            "stars": 5
        }
    ]
    return hotels


@app.post("/booking")
async def add_booking(
    booking: BookingSchema
):
    pass


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
