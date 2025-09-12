'''Viết chương trình kiểm tra một mật khẩu hợp lệ khi:
Có độ dài từ 8 ký tự trở lên
Chứa ít nhất một chữ số
Không chứa khoảng trắng " "
👉 Gợi ý: dùng and, not in, any(char.isdigit() for char in password). '''

def tuDuyCpp(inputPasswork):
    checkLen = False
    checkNum = False
    checkSpace = False

    while checkLen == False or checkNum == False or checkSpace == False:
        if (len(inputPasswork) < 8  ):
            print("error : phải có ít nhất 8 kí tự trở lên.")
            inputPasswork = input("nhập vào paswork :")
        else:
            checkLen = True

        if checkNum != True and len(inputPasswork) >= 8:
            for i in range(0,len(inputPasswork)):
                if inputPasswork[i] >= '0' and inputPasswork[i] <= '9' :
                    checkNum = True
                    break
        if(checkNum == False and len(inputPasswork) >=8):
            print("error: không có kí tự số nào trong pass work")
            inputPasswork = input("nhập vào paswork :")


        checkSpace = True
        for i in range(0,len(inputPasswork)):
            if inputPasswork[i] == ' ':
                print("lỗi có kí tự ' ' trong passwork. ")
                inputPasswork = input("nhập vào paswork :")
                checkSpace = False
                break
                
        
        if checkLen != False and checkNum != False and checkSpace != False:
            print(f"mật khẩu {inputPasswork} hợp lệ")
            break


inputPasswork = input("nhập vào paswork :")

tuDuyCpp(inputPasswork)


    
