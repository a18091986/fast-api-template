from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from core.config import settings

class DatabaseHelper:

    def __init__(self, url: str, 
                 echo: bool = False, 
                 echo_pool: bool = False,
                 pool_size: int = 10,
                 max_overflow: int = 20
                 ) -> None:
        self.engine: AsyncEngine = create_async_engine(url=url, 
                                          echo=echo, 
                                          echo_pool=echo_pool,
                                          pool_size=pool_size,
                                          max_overflow=max_overflow)
        
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=self.engine, 
                                                                                    autocommit=False,
                                                                                    autoflush=False,
                                                                                    expire_on_commit=False)
        
    async def dispose(self):
        await self.engine.dispose()
    

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

db_helper = DatabaseHelper(url=str(settings.db.url),
                           echo=settings.db.echo,
                           echo_pool=settings.db.echo_pool,
                           pool_size=settings.db.pool_size,
                           max_overflow=settings.db.max_overflow)
