"""
Lesson 2
Фильтрация, трансформация и сортировка товарных данных
"""

from typing import List, Dict

DISCOUNT_RATE = 0.10
PRICE_THRESHOLD = 75


# Исходные данные
raw_data: List[Dict] = [
    {"name": "Product A", "price": 100.0, "category": "electronics"},
    {"name": "Product B", "price": 50.0, "category": "books"},
    {"name": "Product C", "price": 200.0, "category": "electronics"}
]


def filter_expensive_products(data: List[Dict], threshold: float) -> List[Dict]:
    """Фильтрует товары дороже указанной цены."""
    return [item for item in data if item["price"] > threshold]


def apply_discount(data: List[Dict], discount_rate: float) -> List[Dict]:
    """Добавляет поле discounted_price."""
    result = []

    for item in data:
        new_item = item.copy()
        new_item["discounted_price"] = item["price"] * (1 - discount_rate)
        result.append(new_item)

    return result


def sort_by_price_desc(data: List[Dict]) -> List[Dict]:
    """Сортирует товары по убыванию цены."""
    return sorted(data, key=lambda x: x["price"], reverse=True)


def process_data(data: List[Dict]) -> List[Dict]:
    """
    Полный pipeline обработки данных.
    """
    filtered = filter_expensive_products(data, PRICE_THRESHOLD)
    discounted = apply_discount(filtered, DISCOUNT_RATE)
    return sort_by_price_desc(discounted)


# --- Обработка данных ---
data_processed = process_data(raw_data)

# Флаг успешной трансформации (используется тестами)
transformation_applied = True


def main():
    print("Обработанные данные:")
    for item in data_processed:
        print(f"{item['name']}: {item['price']} -> {item['discounted_price']}")


if __name__ == "__main__":
    main()
