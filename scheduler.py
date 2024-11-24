class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, interval):
        """Add a task with a delay interval (in seconds)"""
        self.tasks.append((task ,interval))
    
    def get_tasks(self):
        """Get all tasks"""
        return self.tasks
