import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

class ShoppingCartTest(unittest.TestCase):
    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("banana - 5 - 200", output[1])
        self.assertEqual("pear - 5 - 0", output[2])

    def test_print_total(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("Total - 1200", output[3])

    def test_print_inorder(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        sc.add_item("apple", 4)
        sc.add_item("apple", 2)
        sc.add_item("banana", 2)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("banana - 5 - 200", output[1])
        self.assertEqual("pear - 5 - 0", output[2])
        self.assertEqual("apple - 4 - 100", output[3])
        self.assertEqual("apple - 2 - 100", output[4])
        self.assertEqual("banana - 2 - 200", output[5])
        self.assertEqual("Total - 2200", output[6])

    def test_formatting(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        sc.add_item("apple", 4)
        sc.add_item("apple", 2)
        sc.add_item("banana", 2)
        with Capturing() as output:
            sc.print_receipt("{price} - {item} - {quantity}")
        self.assertEqual("100 - apple - 2", output[0])
        self.assertEqual("200 - banana - 5", output[1])
        self.assertEqual("0 - pear - 5", output[2])
        self.assertEqual("100 - apple - 4", output[3])
        self.assertEqual("100 - apple - 2", output[4])
        self.assertEqual("200 - banana - 2", output[5])
        self.assertEqual("Total - 2200", output[6])
    
unittest.main(exit=False)
