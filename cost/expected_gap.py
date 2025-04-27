from .norm import gamma, psi
from .Course import Course


def expected_gap(
    course: Course,
    alpha: float,
    avg_credit: float,
    max_credit: float,
    total_slots: float,
) -> float:
    d_credit = max_credit - avg_credit
    d_coursework = course.max_score - course.avg_score
    weighted = (1 - alpha) * d_credit + alpha * psi(d_coursework)
    return gamma(course.credit_hours * weighted, total_slots)
