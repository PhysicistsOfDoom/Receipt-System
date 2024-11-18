from typing import Protocol, Literal

#Defining the pay literals
PayType = Literal["CASH", "CARD", "PHONE"]

class Payable(Protocol):
   def get_pay_type(self)->PayType:
      pass
   
   def set_pay_type(payment_method: PayType)->None:
      pass