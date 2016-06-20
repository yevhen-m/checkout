import logging
from collections import defaultdict


class Checkout:

    def __init__(self):
        self._items = defaultdict(int)
        self.total = 0

    def clear(self):
        self.total = 0
        self._items.clear()

    def __eq__(self, other):
        return self.total == other.total and self._items == other._items

    def calculate(self, item, quantity=1):
        try:
            getattr(self, '_add_item_{}'.format(item))(quantity)
        except AttributeError:
            fmt = 'Wrong item passed to Checkout calculate method: "{}"'
            logging.warning(fmt.format(item))
        return self.total

    def _add_item_A(self, quantity=1):
        self._items['A'] += 1
        self.total += 50
        if self._items['A'] >= 3:
            self._items['A'] -= 3
            # Discount for three items A
            self.total -= 20

    def _add_item_B(self, quantity=1):
        self._items['B'] += 1
        self.total += 30
        if self._items['B'] >= 2:
            self._items['B'] -= 2
            # Discount for two items B
            self.total -= 15

    def _add_item_C(self, quantity=0):
        self.total += round(199 * quantity)

    def _add_item_D(self, quantity=1):
        self._items['D'] += 1
        self.total += 120
        if self._items['D'] >= 2 and self._items['E']:
            self._items['D'] -= 2
            self._items['E'] -= 1
            # Item E is free for two items D
            self.total -= 90

    def _add_item_E(self, quantity=1):
        if self._items['D'] >= 2:
            # E is free if I've added two items D
            self._items['D'] -= 2
        else:
            self._items['E'] += 1
            self.total += 90
