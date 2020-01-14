from service import Service


class MailRuCloud(Service):
    async def run(self):
        await self.post(
            "https://cloud.mail.ru/api/v2/notify/applink",
            json={
                "phone": "+" + self.formatted_phone,
                "api": 2,
                "email": "email",
                "x-email": "x-email",
            },
        )
