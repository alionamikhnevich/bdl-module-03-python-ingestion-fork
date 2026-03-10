"""
Lesson 1
Исправление категорий товаров и расчёт стоимости партии с НДС
"""

# --- Константы ---
VAT_RATE = 0.2

# Инициализация переменных (категории перепутаны намеренно)
category_a = "Vegetables"
category_b = "Fruits"

price_per_unit_a = 150
quantity_a = 40


def calculate_total_value(price_per_unit: float, quantity: int, vat_rate: float) -> float:
    """
    Рассчитывает стоимость партии с НДС.
    """
    subtotal = price_per_unit * quantity
    total = subtotal * (1 + vat_rate)
    return total


# --- Исправление категорий ---
category_a, category_b = category_b, category_a


# --- Расчёт итоговой стоимости ---
total_value = calculate_total_value(price_per_unit_a, quantity_a, VAT_RATE)


def main():
    print("Текущая категория A:", category_a)
    print("Общая стоимость партии с НДС:", total_value)


if __name__ == "__main__":
    main()
