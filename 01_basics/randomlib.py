import random
print(random.random())#0.0 se 1.0 ke beech float
print(random.uniform(1, 10))    # 1 se 10 tak float


print(random.randint(1, 10))


l1={"apple", "banana", "cherry"}
print(random.choice(list(l1)))


print(random.shuffle(list(l1)))
print(l1)


print(0.1+0.1+0.1-0.3)#5.551115123125783e-17
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))#0.0


