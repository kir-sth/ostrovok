import uvicorn
from fastapi import FastAPI, Depends
from schemas import HotelsSearchArgs, HotelSchema, BookingSchema


app = FastAPI()


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
