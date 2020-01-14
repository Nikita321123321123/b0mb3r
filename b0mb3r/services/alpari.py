from service import Service
import random
import string


class Alpari(Service):
    async def run(self):
        email = "".join(random.choice(string.ascii_letters) for _ in range(6))
        await self.post(
            "https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
            json={
                "client_type": "personal",
                "email": f"{email}@gmail.ru",
                "mobile_phone": self.formatted_phone,
                "deliveryOption": "sms",
            },
        )
