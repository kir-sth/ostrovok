import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from fastapi import FastAPI

from app.bookings.router import router as router_bookings


app = FastAPI()
app.include_router(router_bookings)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
