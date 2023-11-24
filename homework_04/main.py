"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.models import session, Base, async_engine, User, Post
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(
        session: AsyncSession,
        name: str,
        username: str,
        email: str,
        id: int | None = None,
) -> User:
    user = User(id=id, name=name, username=username, email=email)
    session.add(user)
    await session.commit()
    return user


async def create_post(
        session: AsyncSession,
        title: str,
        body: str,
        user_id: int,
        id: int | None = None,
) -> Post:
    post = Post(id=id, title=title, body=body, user_id=user_id)
    session.add(post)
    await session.commit()
    return post


async def async_main():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with session:
        for user_data in users_data:
            await create_user(
                session,
                name=user_data["name"],
                username=user_data["username"],
                email=user_data["email"],
                id=user_data["id"],
            )

        for post_data in posts_data:
            await create_post(
                session,
                title=post_data["title"],
                body=post_data["body"],
                user_id=post_data["userId"],
                id=post_data["id"],
            )


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
