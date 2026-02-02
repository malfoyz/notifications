__all__ = ("setup_database", "cleanup_db", "client")

import pytest
from httpx import AsyncClient, ASGITransport
from tortoise import Tortoise

from app.main import app

DB_URL = "sqlite://:memory:"


@pytest.fixture(scope="session", autouse=True)
async def setup_database():
    await Tortoise.init(
        db_url=DB_URL,
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()


@pytest.fixture(autouse=True)
async def cleanup_db():
    yield
    for model in Tortoise.apps.get("models").values():
        await model.all().delete()


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client
