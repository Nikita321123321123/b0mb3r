import inspect
import os
import sys
import traceback
import webbrowser
import asyncio
import aiohttp.client_exceptions
import pkg_resources
from aiohttp import web

country_codes = {"7": "ru", "375": "by", "380": "ua"}
required_params = ["number_of_cycles", "phone_code", "phone"]
os.chdir(os.path.join(pkg_resources.get_distribution("b0mb3r").location, "b0mb3r"))

app = web.Application()
routes = web.RouteTableDef()


def main():
    webbrowser.open("http://127.0.0.1:8080/", new=2, autoraise=True)
    app.add_routes(routes)
    app.add_routes([web.static("/static", "static")])
    web.run_app(app, host="127.0.0.1", port=8080)


def load_services():
    services = os.listdir("services")
    service_classes = {}
    sys.path.insert(0, "services")

    for service in services:
        if service.endswith(".py") and service != "service.py":
            module = __import__(service[:-3])
            for member in inspect.getmembers(module, inspect.isclass):
                if member[1].__module__ == module.__name__:
                    service_classes[module] = member[0]

    return service_classes


async def attack(number_of_cycles: int, phone_code: str, phone):
    for _ in range(number_of_cycles):
        for module, service in load_services().items():
            try:
                await getattr(module, service)(phone, phone_code).run()
            except aiohttp.client_exceptions.ClientError:
                continue


@routes.get("/")
async def index(_):
    with open("templates/index.html", "r", encoding="utf-8") as template:
        response = template.read().replace("services_count", str(len(load_services())))
        return web.Response(text=response, content_type="text/html")


@routes.post("/attack/start")
async def start_attack(request):
    try:
        loop = asyncio.get_running_loop()
        data = await request.post()
        if len(data.items()) == 0:
            data = await request.json()

        for required_param in required_params:
            if required_param not in data:
                print(required_param, await request.post(), await request.json())
                return web.json_response(
                    {
                        "success": False,
                        "error_code": 400,
                        "error_description": f"You need to specify {required_param}.",
                    },
                    status=400,
                )
        phone = data["phone"].replace("-", "").replace(" ", "")

        number_of_cycles = int(data["number_of_cycles"])
        if int(number_of_cycles) < 1:
            return web.json_response(
                {
                    "success": False,
                    "error_code": 400,
                    "error_description": "The minimum value for number_of_cycles is 1.",
                },
                status=400,
            )

        phone_code = data["phone_code"]
        if phone_code not in country_codes.keys():
            return web.json_response(
                {
                    "success": False,
                    "error_code": 400,
                    "error_description": "This phone_code is not supported.",
                },
                status=400,
            )

        loop.create_task(attack(number_of_cycles, phone_code, phone))

        return web.json_response({"success": True})
    except Exception as error:
        formatted_error = f"{type(error).__name__}: {error}"
        return web.json_response(
            {
                "success": False,
                "error_code": 500,
                "error_description": formatted_error,
                "traceback": traceback.format_exc(),
            },
            status=500,
        )


if __name__ == "__main__":
    main()
