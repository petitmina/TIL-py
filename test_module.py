import module
module.price(3)
module.price_morning(4)
module.price_soldier(5)

import module as mv # as는 별명을 만든다
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from module import *
price(3)
price_morning(4)
price_soldier(5)

from module import price, price_morning
price(5)
price_morning(6)