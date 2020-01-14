from service import Service


class Qlean(Service):
    async def run(self):
        await self.post(
            "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
            json={"phone": self.formatted_phone},
        )
