from nitric.application import Nitric
from nitric.resources import api, collection, ApiOptions

from middle import runfirst

publicApi = api("public", ApiOptions(
    middleware=[runfirst],
))

@publicApi.get("/profiles")
async def get_profiles(ctx):
    print("This should run second ...")

    ctx.res.body = "hello"


Nitric.run()
