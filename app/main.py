import os
import sys

path2dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
sys.path.append(path2dir)

from fastapi import FastAPI  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from fastapi.staticfiles import StaticFiles  # noqa: E402

from app.bookings.router import router as router_bookings  # noqa: E402
from app.hotels.router import router as router_hotels  # noqa: E402
from app.hotels.rooms.router import router as router_rooms  # noqa: E402
from app.images.router import router as router_images  # noqa: E402
from app.pages.router import router as router_pages  # noqa: E402
from app.users.router import router_auth, router_users  # noqa: E402


app = FastAPI()

app.mount(
    path="/static",
    app=StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_bookings)

app.include_router(router_images)


origins = [
    "https://mysite.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


app.include_router(router_pages)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
