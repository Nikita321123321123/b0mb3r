from service import Service


class Karusel(Service):
    async def run(self):
        await self.post(
            "https://app.karusel.ru/api/v1/phone/", data={"phone": self.formatted_phone}
        )
