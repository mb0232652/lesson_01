
from Address import Address
from Mailing import Mailing

to_address = Address(121212,"Браслав", "Костюшко", "14", "27")
from_address = Address(232323, "Минск", "Свободы", "27", "27")

my_package = Mailing(to_address, from_address, 270, 1313)

print(my_package)
