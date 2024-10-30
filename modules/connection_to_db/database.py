from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()


DATABASE_URL=os.getenv("DATABASE_URL")
DATABASE_URL_AUTH=os.getenv("DATABASE_URL_AUTH")

engine_auth = create_async_engine(DATABASE_URL_AUTH, echo=True)
engine = create_async_engine(DATABASE_URL, echo=True)


async_session_auth = sessionmaker(
    engine_auth, class_=AsyncSession, expire_on_commit=False
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


# Dependency
async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session

        
async def get_async_session_auth() -> AsyncSession:
    async with async_session_auth() as session:
        yield session
        
