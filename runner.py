import asyncio
import logging

class AsyncRunner:
    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.logger = logging.getLogger(__name__)

    async def _run_task(self, task, interval):
        try:
            await asyncio.sleep(interval)
            await task.execute()
        except Exception as e:
            self.logger.error(f"Error executing task {task.name}: {e}")
            raise

    async def run_concurrently(self):
        tasks = [
            self._run_task(task, interval)
            for task, interval in self.scheduler.get_tasks()
        ]
        await asyncio.gather(*tasks)