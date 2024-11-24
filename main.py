from task import Task
from scheduler import Scheduler
from runner import Runner

def say_hello():
    print("Hello, world!")

def print_time():
    from time import ctime
    print(f"Current time: {ctime()}")

if __name__ == "__main__":
    # Create tasks
    task1 = Task("Greeting", say_hello)
    task2 = Task("Show Time", print_time)

    # Schedule tasks
    scheduler = Scheduler()
    scheduler.add_task(task1, interval=2) # Run after 2 seconds
    scheduler.add_task(task2, interval=3) # Run after 3 seconds

    # Run tasks
    runner = Runner(scheduler)
    runner.run()