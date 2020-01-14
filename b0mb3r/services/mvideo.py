from service import Service


class MVideo(Service):
    async def run(self):
        await self.post(
            "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
            params={"pageName": "registerPrivateUserPhoneVerificatio"},
            data={
                "phone": self.formatted_phone,
                "recaptcha": "off",
                "g-recaptcha-response": "",
            },
        )
