# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

number_float = 34567.14159
number_int = -12345

print (f"{number_float : .2f}") 
print (f"{number_int :.3f}")
# 3.141590
#12345.000000
print (f"{number_float:10}")
print (f"{number_int:10}")
#   3.14159 
#     12345
print (f"{number_float:<11}")
print (f"{number_int:<11}")

print (f"a{number_float:>10}")
print (f"b{number_int:>10}")

print (f"a{number_float:^10}")
print (f"b{number_int:^10}")

print (f"c{number_float:+}")
print (f"d{number_int:+}")

print (f"E{number_float:,}")
print (f"F{number_int:,}")

print (f"G{number_float:%}")
print (f"H{number_int:%}")

print (f"I{number_float:=}")
print (f"K{number_int:=}")
