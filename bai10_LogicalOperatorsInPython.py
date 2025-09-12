# bai10_LogicalOperatorsInPython.py

# Toán tử logic trong Python: and, or, not

# Ví dụ với and
a = True
b = False

print(a and b)   # False (vì chỉ khi cả 2 đều True thì kết quả mới là True)
print(a and True)  # True (True AND True => True)
print(b and True)  # False (False AND True => False)

# Ví dụ với or
print(a or b)   # True (chỉ cần 1 cái True là True)
print(b or False)  # False (cả 2 đều False thì kết quả False)
print(b or True)   # True (1 cái True => True)

# Ví dụ với not
print(not a)  # False (ngược lại của True là False)
print(not b)  # True (ngược lại của False là True)

# Kết hợp các toán tử
x = 5
y = 10

print(x > 0 and y > 0)   # True (cả 2 điều kiện đều đúng)
print(x > 0 or y < 0)    # True (1 điều kiện đúng là True)
print(not (x > 0))       # False (x > 0 là True, đảo ngược lại là False)

# Thực hành với điều kiện trong if
if (x < 10 and y > 5):
    print("Điều kiện đúng")  # in ra vì 5 < 10 AND 10 > 5 => True
else:
    print("Điều kiện sai")

if (x < 0 or y < 0):
    print("Có số âm")
else:
    print("Không có số âm")  # in ra vì cả x và y đều dương

if not (y == 10):
    print("y không bằng 10")
else:
    print("y bằng 10")  # in ra vì y == 10
