import math
from decimal import Decimal
n=Decimal("2.7182818284590452353602875")
st ="1.0000000000000000000000000"
print(n.quantize(Decimal(st[:int(input()) + 2])))
