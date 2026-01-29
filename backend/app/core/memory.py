from collections import deque

class SessionMemory:
    def __init__(self, max_turns: int = 5):
        self.history = deque(maxlen=max_turns)

    def add(self, question: str, answer: str):
        self.history.append((question, answer))

    def get_context(self) -> str:
        return "\n".join(
            f"Q: {q}\nA: {a}" for q, a in self.history
        )
