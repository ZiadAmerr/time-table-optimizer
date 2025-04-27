class Course:
    __slots__ = ("credit_hours", "avg_score", "max_score")

    def __init__(self, credit_hours: float, avg_score: float, max_score: float = 100):
        self.credit_hours = credit_hours
        self.avg_score = avg_score
        self.max_score = max_score
