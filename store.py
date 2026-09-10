"""Simple checkout calculator for an online store.

TODO(team): implement the pricing rule(s) assigned to you in the README.
"""


def loyalty_discount(subtotal:float):
    if subtotal > 50:
        return subtotal * 0.9

def tax(subtotal:float):
    return subtotal * 1.08

def shipping(subtotal:float):
    return subtotal + 5.0

def calculate_total(
    subtotal, apply_discount=False, apply_tax=False, apply_shipping=False
):
    """Calculate the final total a customer pays for their cart."""


    if apply_discount:
        subtotal = loyalty_discount(subtotal)

    if apply_tax:
        subtotal = tax(subtotal)

    if apply_shipping:
        subtotal = shipping(subtotal)
    
    
    total = subtotal

    return total


if __name__ == "__main__":
    example_subtotal = 100.0
    print(
        f"Total for a ${example_subtotal:.2f} cart: ${calculate_total(example_subtotal):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with discount: ${calculate_total(example_subtotal, True, False):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with tax: ${calculate_total(example_subtotal, False, True):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with discount and tax: ${calculate_total(example_subtotal, True, True):.2f}"
    )
