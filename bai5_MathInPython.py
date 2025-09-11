import math

# Làm tròn xuống (floor) và làm tròn lên (ceil)
print(math.floor(3.7))   # 3
print(math.floor(-3.7))  # -4
print(math.ceil(3.2))    # 4
print(math.ceil(-3.2))   # -3

# Cắt phần thập phân (trunc = giống int())
print(math.trunc(3.9))   # 3
print(math.trunc(-3.9))  # -3

# Căn bậc hai
print(math.sqrt(16))     # 4.0

# Lũy thừa
print(math.pow(2, 3))    # 8.0 (trả về float)
print(2 ** 3)            # 8 (int)

# Giai thừa
print(math.factorial(5)) # 120

# Ước số chung lớn nhất
print(math.gcd(12, 18))  # 6

# Giá trị tuyệt đối (chuyên dùng cho float)
print(math.fabs(-5.7))   # 5.7

# Số pi và e
print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045

# Logarit
print(math.log(8, 2))    # 3.0 (log cơ số 2 của 8)
print(math.log10(1000))  # 3.0 (log cơ số 10 của 1000)

# Hàm lượng giác (đơn vị radian)
print(math.sin(math.pi/2)) # 1.0
print(math.cos(math.pi))   # -1.0
print(math.tan(math.pi/4)) # 0.9999999999999999 ≈ 1.0

# Chuyển đổi độ ↔ radian
print(math.radians(180))   # 3.141592653589793 (π)
print(math.degrees(math.pi/2)) # 90.0

#kt xem nó có phải Vô cực or NaN ko?
print(math.isfinite(5))     # True
print(math.isinf(math.inf)) # True
print(math.isnan(math.nan)) # True
print(math.isnan(5))        # False

print(math.isinf(-math.inf))  # True
print(math.isinf(1000))       # False

