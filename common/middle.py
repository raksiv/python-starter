from nitric.faas import HttpMiddleware

async def run_first(ctx, nxt: HttpMiddleware):
    print("This should run first ...")
    return await nxt(ctx)