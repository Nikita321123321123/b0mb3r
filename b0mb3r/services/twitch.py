from service import Service
import random
import string


class Twitch(Service):
    async def run(self):
        username = "".join(random.choice(string.ascii_letters) for _ in range(12))
        password = "".join(random.choice(string.printable) for _ in range(12))
        await self.post(
            "https://passport.twitch.tv/register?trusted_request=true",
            json={
                "birthday": {"day": 11, "month": 11, "year": 1999},
                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                "include_verification_code": True,
                "password": password,
                "phone_number": self.formatted_phone,
                "username": username,
            },
        )
