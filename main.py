from task import Task
from scheduler import Scheduler
from runner import AsyncRunner
import asyncio

def say_hello():
    print("Hello, world!")

def print_time():
    from time import ctime
    print(f"Current time: {ctime()}")

def print_date():
    from datetime import date
    print(f"Current date: {date.today()}")

async def long_running_task():
    print("Starting long running task")
    await asyncio.sleep(5)
    print("Long running task completed")

async def count_numbers():
    for i in range(1, 10):
        print(f"Counting: {i}")
        await asyncio.sleep(1)

if __name__ == "__main__":
    # Create tasks
    task1 = Task("Greeting", say_hello)
    task2 = Task("Show Time", print_time)
    task3 = Task("Show Date", print_date)
    task4 = Task("Long Running Task", long_running_task)
    task5 = Task("Count Numbers", count_numbers)

    # Schedule tasks
    scheduler = Scheduler()
    scheduler.add_task(task1, interval=2)
    scheduler.add_task(task2, interval=3)
    scheduler.add_task(task3, interval=4)
    scheduler.add_task(task4, interval=5)
    scheduler.add_task(task5, interval=6)

    # Run tasks
    runner = AsyncRunner(scheduler)
    try:
        asyncio.run(runner.run_concurrently())
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting.")
    except Exception as e:
        print(f"An error occurred: {e}")
