# -------------------------------
# STRING METHODS
# -------------------------------
# name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")

# length = len(name)
# index = name.find(" ")
# name = name.capitalize() #làm cho ptu đầu tiên viết hoa các ptu phía sau in thường
# name = name.upper()
# name = name.lower()
# result = name.isdigit() 
# result = name.isalpha() # trả về true-false ,  nếu trong chuỗi tất cả các kí tự đề là chữ .
# result = phone_number.count(" ")
# phone_number = phone_number.replace("-", "")

# -------------------------------
#        EXERCISE
# -------------------------------
username = input("Enter a username: ")

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")