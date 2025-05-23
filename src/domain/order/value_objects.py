from domain.base.value_object import ValueObject
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class OrderLine(ValueObject):
    orderid: str
    sku: str
    qty: int
