from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

app = FastAPI()

# toggle flag
is_down = False

# router
users_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@app.get("/toggle")
def toggle():

    global is_down

    is_down = not is_down

    return {
        "is_down": is_down
    }


@users_router.get("/")
def get_users():

    if is_down:

        return JSONResponse(
            content={
                "error": "backend down"
            },
            status_code=500
        )

    return {
        "users": [
            {
                "id": 1,
                "name": "Adwiteek"
            },
            {
                "id": 2,
                "name": "Utkarsh"
            }
        ]
    }


@users_router.get("/{user_id}")
def get_user(user_id: int):

    if is_down:

        return JSONResponse(
            content={
                "error": "backend down"
            },
            status_code=500
        )

    return {
        "id": user_id,
        "name": f"user-{user_id}"
    }


# include router
app.include_router(users_router)

@app.get("/")
def root():

    return {
        "message": "API running"
    }