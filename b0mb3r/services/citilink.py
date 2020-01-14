from service import Service


class Citilink(Service):
    async def run(self):
        await self.post(
            "https://www.citilink.ru/registration/confirm/phone/+"
            + self.formatted_phone
            + "/"
        )
