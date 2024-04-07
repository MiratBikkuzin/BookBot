from aiohttp import ClientSession


class AiohttpSingleton:
    session = None

    async def __new__(cls, *args, **kwargs):
        if not cls.session:
            cls.session = ClientSession()
        return cls