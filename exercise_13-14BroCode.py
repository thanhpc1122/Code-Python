email = input("nhập vào email của bạn : ")

email_index = email.index('@')

firstEmail = email[:email_index]
lastEmail = email[email_index + 1:]

print(f"phần trước tên email là : {firstEmail} , tên miền của email là {lastEmail} .")