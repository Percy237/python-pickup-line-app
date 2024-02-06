class Line:
    def __init__(self, line, prev=None, next=None) -> None:
        self.line = line
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"{self.line[:10]}"
