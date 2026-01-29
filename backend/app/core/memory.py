from collections import deque
from typing import Dict

class SessionMemory:
    def __init__(self, max_turns: int = 5):
        self.history = deque(maxlen=max_turns)

    def add(self, question: str, answer: str):
        self.history.append((question, answer))

    def get_context(self) -> str:
        return "\n".join([f"Human: {q}\nAI: {a}" for q, a in self.history])

# Memory manager to hold multiple sessions in RAM
class MemoryManager:
    def __init__(self):
        self.sessions: Dict[str, SessionMemory] = {}

    def get_session(self, session_id: str) -> SessionMemory:
        if session_id not in self.sessions:
            self.sessions[session_id] = SessionMemory()
        return self.sessions[session_id]

memory_manager = MemoryManager()