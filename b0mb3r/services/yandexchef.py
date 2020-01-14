from service import Service


class YandexChef(Service):
    async def run(self):
        await self.post(
            "https://api.chef.yandex/api/v2/auth/sms", json={"phone": self.phone},
        )
