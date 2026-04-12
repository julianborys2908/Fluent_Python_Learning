test_list = [10, 20, 30, 40, 50, 60]

print(test_list[:2])
print(test_list[2:])
print(test_list[:3])
print(test_list[3:])

print("\n")

test_word = "bicycle"

print(test_word[::3])
print(test_word[::-1])
print(test_word[::-2])

print("\n")

invoice = """"
0.....6.................................40........52...55........
1909   Pimoroni PiBrella                  $17.50    3    $52.50
1489   6mm Tactile Switch x20             $4.95     2     $9.90
1510   Panavise Jr. - PV-201              $28.00    1    $28.00
1601   PiTFT Mini Kit 320x240             $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split("\n")[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


print("\n")

sliced_list = list(range(10))
print(sliced_list)

sliced_list[2:5] = [20, 30]
print(sliced_list)

del sliced_list[5:7]
print(sliced_list)

sliced_list[3::2] = [11, 22]
print(sliced_list)

sliced_list[2:5] = [100]
print(sliced_list)
