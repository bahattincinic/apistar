import asyncio

class AsyncioEventLoop(object):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
    
    def __call__(self):
        return self.loop


@contextlib.contextmanager
def get_event_loop(loop: AsyncioEventLoop):
    try:
        yield loop.loop
    finally:
        session.close()
