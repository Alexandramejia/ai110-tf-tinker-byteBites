import pytest
from models import (
    MenuItem,
    Customer,
    Order,
    Payment,
    filter_by_category,
    filter_by_max_price,
    sort_by_price,
    sort_by_popularity,
)


# --- Fixtures ---

@pytest.fixture
def menu_items():
    return [
        MenuItem("Spicy Burger", 8.99, "Burgers", 4.5),
        MenuItem("Classic Burger", 7.49, "Burgers", 3.8),
        MenuItem("Large Soda", 2.50, "Drinks", 3.0),
        MenuItem("Mango Shake", 4.75, "Drinks", 4.2),
        MenuItem("Brownie", 3.25, "Desserts", 4.8),
    ]

@pytest.fixture
def basic_order():
    order = Order("2026-06-12 12:00")
    burger = MenuItem("Spicy Burger", 8.99, "Burgers", 4.5)
    soda = MenuItem("Large Soda", 2.50, "Drinks", 3.0)
    order.add_item(burger, 2)
    order.add_item(soda, 1)
    return order


# --- Order total tests ---

def test_order_total_multiple_items_and_quantities(basic_order):
    # burger x2 ($8.99) + soda x1 ($2.50) = $20.48
    assert basic_order.total() == pytest.approx(20.48)

def test_order_total_single_item():
    order = Order("2026-06-12 12:00")
    item = MenuItem("Brownie", 3.25, "Desserts", 4.8)
    order.add_item(item, 1)
    assert order.total() == pytest.approx(3.25)

def test_empty_order_total_is_zero():
    order = Order("2026-06-12 12:00")
    assert order.total() == 0.0


# --- filter_by_category tests ---

def test_filter_by_category_returns_matching_items(menu_items):
    drinks = filter_by_category(menu_items, "Drinks")
    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)

def test_filter_by_category_no_matches_returns_empty_list(menu_items):
    result = filter_by_category(menu_items, "Sushi")
    assert result == []

def test_filter_by_category_empty_list_returns_empty_list():
    assert filter_by_category([], "Burgers") == []
