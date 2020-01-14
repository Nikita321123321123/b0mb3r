from service import Service
import random
import string


class Invitro(Service):
    async def run(self):
        password = "".join(random.choice(string.ascii_letters) for _ in range(6))
        await self.post(
            "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
            data={
                "password": password,
                "application": "lkp",
                "login": "+" + self.formatted_phone,
            },
        )
