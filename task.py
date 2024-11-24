import logging
import asyncio
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class Task:
    def __init__(self, name, action):
        self.name = name
        self.action = action # A callable function
        self.is_async = asyncio.iscoroutinefunction(action)
    async def execute(self):
        logging.info(f"Executing task {self.name}")
        if self.is_async:
            await self.action()
        else:
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, self.action)