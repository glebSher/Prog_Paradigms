# Реализовать с использованием функциональной парадигмы процедуру normalization,
# которая выполняет нормализацию полученного массива по приведенной формуле
# нормализованного значения элемента, где
# ○ x_norm - нормализованное значение элемента
# ○ x - исходное значение элемента
# ○ x_max, x_min - максимальное и минимальное значение в массиве

def normalize(data):
    min_value = min(data)
    max_value = max(data)

    def normalize_element(x):
        return (x - min_value) / (max_value - min_value)

    return list(map(normalize_element, data))
