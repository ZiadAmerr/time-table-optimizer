from bisect import bisect_right

_thresholds = [3, 7, 11, 14, 17, 20, 24, 27, 30, 33, 40]
_values = [0, 0, 0.3, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 4]


def psi(x: float) -> float:
    return _values[bisect_right(_thresholds, x)]


def gamma(x: float, total_slots: float) -> float:
    gap = x / total_slots * 6 + 1
    return max(1, min(gap, 7))
