"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
DB_ECHO = False

async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)

Session = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

session: AsyncSession = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=False)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=False)
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )
    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )
