"""Classes for melon orders."""
from random import choice
from datetime import datetime
#we will be using datetime.weekday() and datetime.time() for get_base_price()


class AbstractMelonOrder(object):
    """Super class for general melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """need to find rush hour"""
        random_base_price = choice(range(5, 10))
        if (datetime.now().hour in range(8, 11) and
                datetime.now().weekday() in range(5)):
            random_base_price += 4
        return random_base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()  # I want THIS INSTANCES method!(.self)

        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact that an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """sub class for government orders with no tax"""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False
        self.tax = 0

    def mark_inspection(self, status):
        """Record the fact that an order has been shipped."""

        self.passed_inspection = status


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
