from enum import Enum

from mongoengine import *


class PaymentMethodEnums(Enum):

    def __init__(self):
        _payment_methods = [
            "Visa",
            "Mastercard",
            "Discover",
            "American Express",
            "Apple Pay",
            "Google Pay",
            "Android Pay"
        ]

        for i, payment_method in enumerate(_payment_methods):
            self.setattr(self, payment_method, i)


class PaymentMethods(Document):

    payment_methods = [
        "Visa",
        "Mastercard",
        "Discover",
        "American Express",
        "Apple Pay",
        "Google Pay",
        "Android Pay"
    ]

