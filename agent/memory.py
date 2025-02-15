# agent/memory.py

from utils.logger import logger

class Memory:
    def __init__(self):
        self.memory = []

    def add_interaction(self, query, response):
        """Store past interactions for multi-turn reasoning."""
        self.memory.append({"query": query, "response": response})
        logger.info(f"Stored interaction in memory: {self.memory[-1]}")