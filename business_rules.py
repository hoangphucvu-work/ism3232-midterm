# business_rules.py
# Author: Hoang Phuc Vu

# Constant values according to the business rules, so that the business rules can be updated easily in this part

small_discount_bags: int = 20
large_discount_bags: int = 80

small_discount: float = 0.09
large_discount: float = 0.14
partner_bonus: float = 0.04

shipping_fee_threshold: float = 250
shipping_fee: float = 35

prepayment_threshold: float = 1500

pallet_bag_threshold: int = 60
pallet_total_threshold: float = 700

# End of constant values


def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Returns the bean cost before discount."""
    return bag_price * bags


def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Returns the discount rate based on the number of bags and whether the buyer is a partner."""
    if bags >= large_discount_bags:
        if partner is True:
            discount_rate = large_discount + partner_bonus
        else:
            discount_rate = large_discount
    elif bags >= small_discount_bags:
        if partner is True:
            discount_rate = small_discount + partner_bonus
        else:
            discount_rate = small_discount
    else:
        discount_rate = 0.0

    return discount_rate


def calculate_shipment_total(
    bag_price: float, bags: int, partner: bool = False
) -> float:
    """Returns the total cost of the shipment for one shipment"""

    bean_cost = calculate_bean_cost(bag_price, bags)
    discount_rate = get_bulk_discount(bags, partner)
    discounted_cost = bean_cost * (1 - discount_rate)

    if discounted_cost < shipping_fee_threshold:
        discounted_cost += shipping_fee
    return discounted_cost


def requires_prepayment(total: float) -> bool:
    """Returns True if the order requires prepayment, False otherwise."""
    return total >= prepayment_threshold


def needs_pallet(bags: int, total: float) -> bool:
    """Returns True if the order needs a freight pallet, False otherwise."""
    return bags > pallet_bag_threshold and total > pallet_total_threshold


def total_shipped(shipments: list) -> float:
    """Returns the sum of shipment totals for every shipment in the list."""
    grand_total = 0
    for shipment in shipments:
        grand_total += calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
    return grand_total


def largest_shipment(shipments: list) -> str:
    """Returns the buyer of the the shipment with the largest total cost."""
    if not shipments:
        return ""

    largest_buyer = ""
    max_total = -1.0

    for shipment in shipments:
        current_total = calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
        if current_total > max_total:
            max_total = current_total
            largest_buyer = shipment["buyer"]
    return largest_buyer


def format_shipment_line(
    buyer: str, grand_total: float, prepayment: bool, pallet: bool
) -> str:
    """Return one formatted report line for a shipment."""
    prepayment_str = "yes" if prepayment else "no"
    pallet_str = "yes" if pallet else "no"
    return f"{buyer}: ${grand_total:.2f} | prepayment: {prepayment_str} | pallet: {pallet_str}"
