from numpy.fft import fft

from is_lucky import is_lucky

if __name__ == "__main__":
    x = [0, 1, 2, 3]
    y = fft(x)
    print(y)

# alt + enter
from homework import my_max, my_max3

print(my_max(1, 5))
print(my_max3(1, 2, 3))
print(is_lucky("213213"))

import homework as hw
print(hw.my_abs(-213))

# from bmi import * - tak nie robić
# __init__.py dodaje sie jako modul do paczek, zeby wiadomo ze to paczka
