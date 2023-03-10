from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
from models.note import Note
from api.note import router


app = FastAPI()


app.include_router(router)



async def init(client: AsyncIOMotorClient, db_name: str) -> None:
    """
    Initialize master database connection.
    """

    # Initialize beanie with the Product document class and a database
    await init_beanie(
        database=client[db_name],
        document_models=[Note],
        allow_index_dropping=True,
    )


DATABASE_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(DATABASE_URL)





@app.on_event("startup")
async def configure_db_and_routes(db_name: str = "note_db") -> None:
    """
    Executed on application startup.
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Initialize database connection
    await init(client=client, db_name=db_name)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=True)
