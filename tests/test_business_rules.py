from business_rules import (
    calculate_bean_cost,
    get_bulk_discount,
    calculate_shipment_total,
    requires_prepayment,
    needs_pallet,
    total_shipped,
    largest_shipment,
    format_shipment_line,
)


def test_calculate_bean_cost():
    assert round(calculate_bean_cost(10.0, 67), 2) == 670.00


def test_calculate_bean_cost_zero_bags():
    assert round(calculate_bean_cost(15.0, 0), 2) == 0.00


def test_get_bulk_discount_under_small_discount_no_partner():
    assert round(get_bulk_discount(19, False), 2) == 0.00


def test_get_bulk_discount_under_small_discount_partner():
    assert round(get_bulk_discount(19, True), 2) == 0.00


def test_get_bulk_discount_small_discount_exact_no_partner():
    assert round(get_bulk_discount(20, False), 2) == 0.09


def test_get_bulk_discount_small_discount_exact_partner():
    assert round(get_bulk_discount(20, True), 2) == 0.13


def test_get_bulk_discount_under_large_discount_no_partner():
    assert round(get_bulk_discount(79, False), 2) == 0.09


def test_get_bulk_discount_under_large_discount_partner():
    assert round(get_bulk_discount(79, True), 2) == 0.13


def test_get_bulk_discount_large_discount_exact_no_partner():
    assert round(get_bulk_discount(80, False), 2) == 0.14


def test_get_bulk_discount_large_discount_exact_partner():
    assert round(get_bulk_discount(80, True), 2) == 0.18


def test_calculate_shipment_total_under_threshold_shipping_fee():
    assert round(calculate_shipment_total(10.0, 10, partner=False), 2) == 135.00


def test_calculate_shipment_total_at_threshold_no_shipping_fee():
    assert round(calculate_shipment_total(25.0, 10, partner=False), 2) == 250.00


def test_calculate_shipment_total_over_threshold_no_shipping_fee():
    assert round(calculate_shipment_total(30.0, 10, partner=False), 2) == 300.00


def test_requires_prepayment_below_threshold():
    assert requires_prepayment(1499.00) is False


def test_requires_prepayment_at_threshold():
    assert requires_prepayment(1500.00) is True


def test_requires_prepayment_above_threshold():
    assert requires_prepayment(1504.00) is True


def test_needs_pallet_both_below_threshold():
    assert needs_pallet(59, 699.00) is False


def test_needs_pallet_bags_above_threshold_total_below_threshold():
    assert needs_pallet(61, 699.00) is False


def test_needs_pallet_bags_below_threshold_total_above_threshold():
    assert needs_pallet(59, 1500.00) is False


def test_needs_pallet_both_above_threshold():
    assert needs_pallet(61, 1500.00) is True


def test_total_shipped_short_list():
    short_shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 15, "partner": False},
    ]
    assert total_shipped(short_shipments) == 320.00


def test_largest_shipment_short_list():
    short_shipments = [
        {"buyer": "Small", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "Big", "bag_price": 16.00, "bags": 15, "partner": False},
    ]
    assert largest_shipment(short_shipments) == "Big"


def test_largest_shipment_tie():
    tied_shipments = (
        {"buyer": "First Before", "bag_price": 10.00, "bags": 1000, "partner": False},
        {"buyer": "Second", "bag_price": 10.00, "bags": 150, "partner": False},
        {"buyer": "First After", "bag_price": 10.00, "bags": 1000, "partner": False},
        {"buyer": "Third", "bag_price": 10.00, "bags": 15, "partner": False},
    )
    assert largest_shipment(tied_shipments) == "First Before"


def test_largest_shipment_empty_list():
    assert largest_shipment([]) == ""
