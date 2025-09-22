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
 """
Для проверки работоспособности кода
if __name__ == "__main__":
    # Проверка simple_probability
    print("simple_probability(2, 4) =", simple_probability(2, 4))  # 0.5

    # Проверка logical_or
    print("logical_or(2, 3, 10) =", logical_or(2, 3, 10))  # 0.5

    # Проверка logical_and
    print("logical_and(2, 3, 10, 5) =", logical_and(2, 3, 10, 5))  # 0.12

    # Проверка expected_value
    values = (1, 2, 3)
    probs = (0.2, 0.3, 0.5)
    print("expected_value(values, probs) =", expected_value(values, probs))  # 2.3

    # Проверка conditional_probability
    pairs = ((1, 1), (1, 0), (0, 1), (1, 1))
    print("conditional_probability(pairs) =", conditional_probability(pairs))  
    # A=1 три раза, среди них дважды B=1 → 2/3 = 0.666...

    # Проверка bayesian_probability
    print("bayesian_probability(0.5, 0.8) =", bayesian_probability(0.5, 0.8))  
    # P(A)=0.5, P(B|A)=0.8 → ~0.8
 """
