import aiohttp


class Service:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    client = aiohttp.ClientSession()

    def __init__(self, phone, phone_code):
        self.phone = phone
        self.phone_code = phone_code
        self.formatted_phone = self.phone_code + self.phone

        self.client.headers = {"User-Agent": self.user_agent}

    async def post(self, *args, **kwargs):
        await self.client.post(*args, **kwargs)

    async def get(self, *args, **kwargs):
        await self.client.post(*args, **kwargs)

    async def options(self, *args, **kwargs):
        await self.client.options(*args, **kwargs)
