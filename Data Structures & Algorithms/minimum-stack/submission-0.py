class MinStack:
    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.values.append(val)

        min_val = min(val, self.min_values[-1] if self.min_values else float('inf'))

        self.min_values.append(min_val)

    def pop(self) -> None:
        self.min_values.pop()

        return self.values.pop()
        

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.min_values[-1]
        
