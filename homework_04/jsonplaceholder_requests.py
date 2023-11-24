"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from aiohttp import ClientSession

URL = "https://jsonplaceholder.typicode.com/"
USERS_DATA_URL = f"{URL}/users"
POSTS_DATA_URL = f"{URL}/posts"


async def fetch_api_data(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def fetch_users_data():
    return await fetch_api_data(USERS_DATA_URL)


async def fetch_posts_data():
    return await fetch_api_data(POSTS_DATA_URL)
