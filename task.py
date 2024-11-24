import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class Task:
    def __init__(self, name, action):
        self.name = name
        self.action = action # A callable function

    def execute(self):
        logging.info(f"Executing task {self.name}")
        self.action()