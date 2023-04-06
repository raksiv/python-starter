from nitric.application import Nitric
from nitric.resources import api, ApiOptions

from middle import run_first

publicApi = api("public", ApiOptions(
    middleware=[run_first],
))


@publicApi.get("/profiles")
async def get_profiles(ctx):
    print("This should run second ...")

    ctx.res.body = "hello"


Nitric.run()