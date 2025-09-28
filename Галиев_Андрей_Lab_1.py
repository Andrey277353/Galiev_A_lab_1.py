# Galiev_A_lab_1.py

def simple_probability(m: int, n: int) -> float:
    """Простая вероятность: m / n"""
    if n == 0:
        return 0
    return m / n


def logical_or(m: int, k: int, n: int) -> float:
    """Вероятность OR для несовместных событий: (m + k) / n"""
    if n == 0:
        return 0
    return (m + k) / n


def logical_and(m: int, k: int, n: int, l: int) -> float:
    """Вероятность AND для совместных событий: (m/n) * (k/l)"""
    if n == 0 or l == 0:
        return 0
    return (m / n) * (k / l)


def expected_value(values: tuple, probabilities: tuple) -> float:
    """Математическое ожидание: сумма(values[i] * probabilities[i])"""
    if len(values) != len(probabilities):
        raise ValueError("Длины values и probabilities должны совпадать")
    return sum(v * p for v, p in zip(values, probabilities))


def conditional_probability(values: tuple) -> float:
    """
    Условная вероятность P(B=1 | A=1).
    values = ((a1, b1), (a2, b2), ...)
    """
    count_a1 = 0
    count_a1b1 = 0
    for a, b in values:
        if a == 1:
            count_a1 += 1
            if b == 1:
                count_a1b1 += 1
    if count_a1 == 0:
        return 0
    return count_a1b1 / count_a1


def bayesian_probability(a: float, ba: float) -> float:
    """
    Теорема Байеса.
    На вход: P(A) = a, P(B|A) = ba.
    Предположим P(B) = a*ba + (1-a)*(1-ba)  (если других данных нет).
    Возвращает P(A|B).
    """
    pb = a * ba + (1 - a) * (1 - ba)
    if pb == 0:
        return 0
    return (a * ba) / pb
    raise ValueError("Недостаточно данных: для P(A|B) нужно знать P(B) или P(B|¬A).")

