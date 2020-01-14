from service import Service


class AtPrime(Service):
    async def run(self):
        await self.post(
            "https://api.wowworks.ru/v2/site/send-code",
            json={"phone": self.formatted_phone, "type": 2},
        )
