from service import Service


class Plink(Service):
    async def run(self):
        await self.post(
            "https://plink.tech/register/", json={"phone": self.formatted_phone}
        )
