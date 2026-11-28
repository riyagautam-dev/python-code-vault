class InsufficientFundException(Exception):
    def __init__(self, arg):  # Constructor
            self.msg = arg 

class Account(Exception):
      def __init__(self, m):  # Constructor
              self.bal=m

      def withdraw(self,amount):
             if amount<self.bal:
              raise InsufficientFundException ("your ammount is more")
             else:
                
             
             
try:
      a1.ammount
              