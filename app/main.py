import os
import sys

path2dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
sys.path.append(path2dir)

from fastapi import FastAPI  # noqa: E402

from app.bookings.router import router as router_bookings  # noqa: E402
from app.hotels.router import router as router_hotels  # noqa: E402
from app.hotels.rooms.router import router as router_rooms  # noqa: E402
from app.users.router import router_auth, router_users  # noqa: E402


app = FastAPI()

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_bookings)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
