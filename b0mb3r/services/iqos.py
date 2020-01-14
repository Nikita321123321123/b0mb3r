from service import Service


class Iqos(Service):
    async def run(self):
        await self.post(
            "https://ube.pmsm.org.ru/esb/iqos-phone/validate",
            json={"phone": self.phone},
        )
