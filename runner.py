import time

class Runner:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def run(self):
        """Run tasks in sequence based on their interval"""
        for task, interval in self.scheduler.get_tasks():
            time.sleep(interval)
            task.execute()