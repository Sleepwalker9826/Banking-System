print("For banker's use")
Acc_1 = float(input("Enter the amount in account number 1 : "))
Acc_2 = float(input("Enter the amount in account number 2 : "))
Acc_3 = float(input("Enter the amount in account number 3 : "))
Acc_4 = float(input("Enter the amount in account number 4 : "))
Acc_5 = float(input("Enter the amount in account number 5 : "))
pwd1 = 123
pwd2 = 234
pwd3 = 345
pwd4 = 456
pwd5 = 567
for a in range (1000):
    print("1 = Deposit money to an account")
    print("2 = Check balance")
    print("3 = Take Money")
    print("4 = Total of Money in the Bank")
    print("5 = Transfer Money from one ccount to another")
    Q1 = int(input("What do you want to do today? : "))
    if Q1 == 1:
        print("You can deposit money here.")
        Q1_1 = int(input("Enter Account Number : "))
        if Q1_1 == 1:
            Q2_1 = int(input("Enter the amount to be deposited : "))
            Acc_1 = (Acc_1 + Q2_1)
            print("Your balance is", Acc_1)
        elif Q1_1 == 2:
            Q2_1 = int(input("Enter the amount to be deposited : "))
            Acc_2 = (Acc_2 + Q2_1)
            print("Your balance is", Acc_2)
        elif Q1_1 == 3:
            Q2_1 = int(input("Enter the amount to be deposited : "))
            Acc_3 = (Acc_3 + Q2_1)
            print("Your balance is", Acc_3 )
        elif Q1_1 == 4:
            Q2_1 = int(input("Enter the amount to be deposited : "))
            Acc_4 = (Acc_4 + Q2_1)
            print("Your balance is", Acc_4)
        else:
            Q2_1 = int(input("Enter the amount to be deposited : "))
            Acc_5 = (Acc_5 + Q2_1)
            print("Your balance is", Acc_5 )
    elif Q1 == 2:
        print("You can check balance here")
        Q1_2 = int(input("Enter Account Number : "))
        if Q1_2 == 1:
            print("Your balance is", Acc_1)
        elif Q1_2 == 2:
            print("Your balance is", Acc_2)
        elif Q1_2 == 3:
            print("Your balance is", Acc_3)
        elif Q1_2 == 4:
            print("Your balance is", Acc_4)
        else:
            print("Your balance is", Acc_5)
    elif Q1 == 3:
        print("You can take money here")
        Q1_3 = int(input("Enter account number : "))
        pwd = int(input("Enter Password : "))
        if (Q1_3 == 1 and pwd == pwd1) or (Q1_3 == 2 and pwd == pwd2) or (Q1_3 == 3 and pwd == pwd3) or (Q1_3 == 4 and pwd == pwd4) or (Q1_3 == 5 and pwd == pwd5):
            if Q1_3 == 1:
                Q2_1 = float(input("Enter the amount to be taken : "))
                if Acc_1 >= Q2_1:
                    Acc_1 = Acc_1 - Q2_1
                    print("Your balance is", Acc_1)
                else:
                    print("No enough money in your account")
            elif Q1_3 == 2:
                Q2_1 = float(input("Enter the amount to be taken : "))
                if Acc_2 >= Q2_1:
                    Acc_2 = Acc_2 - Q2_1
                    print("Your balance is", Acc_2)
                else:
                    print("No enough money in your account")
            elif Q1_3 == 3:
                Q2_1 = float(input("Enter the amount to be taken : "))
                if Acc_3 >= Q2_1:
                    Acc_3 = Acc_3 - Q2_1
                    print("Your balance is", Acc_3 )
                else:
                    print("No enough money in your account")
            elif Q1_3 == 4:
                Q2_1 = float(input("Enter the amount to be taken : "))
                if Acc_4 >= Q2_1:
                    Acc_4 = Acc_4 - Q2_1
                    print("Your balance is", Acc_4)
                else:
                    print("No enough money in your account")
            else:
                Q2_1 = float(input("Enter the amount to be taken : "))
                if Acc_5 >= Q2_1:
                    Acc_5 = Acc_5 - Q2_1
                    print("Your balance is", Acc_5 )
                else:
                    print("No enough money in your account")
        else:
            print("Invalid Responce. Please recheck")
    elif Q1 == 4:
        print("The remainder in the bank is", Acc_1 + Acc_2 + Acc_3 + Acc_4 + Acc_5)
    elif Q1 == 5:
        tr_acc = int(input("Enter the account number to take : "))
        if tr_acc == 1 or 2 or 3 or 4 or 5:
            pwd_tr = int(input("Enter the password : "))
            if (tr_acc == 1 and pwd_tr == pwd1) or (tr_acc == 2 and pwd_tr == pwd2) or (tr_acc == 3 and pwd_tr == pwd3) or (tr_acc == 4 and pwd_tr == pwd4) or (tr_acc == 5 and pwd_tr == pwd5):
                de_acc = int(input("Enter the account to transfer : "))
                amount = float(input("Enter the amount to be transfered : "))
                if (tr_acc != de_acc):
                    if tr_acc == 1:
                        Acc_1 = Acc_1 - amount
                        print("Remainder in the account you took money from:", Acc_1)
                    elif tr_acc == 2:
                        Acc_2 = Acc_2 - amount
                        print("Remainder in the account you took money from:", Acc_2)
                    elif tr_acc == 3:
                        Acc_3 = Acc_3 - amount
                        print("Remainder in the account you took money from:", Acc_3)
                    elif tr_acc == 4:
                        Acc_4 = Acc_4 - amount
                        print("Remainder in the account you took money from:", Acc_4)
                    else:
                        Acc_5 = Acc_5 - amount
                        print("Remainder in the account you took money from:", Acc_5)
                    if de_acc == 1:
                        Acc_1 = Acc_1 + amount
                        print("Remainder in the account you transferred to:", Acc_1)
                    elif de_acc == 2:
                        Acc_2 = Acc_2 + amount
                        print("Remainder in the account you transferred to:", Acc_2)
                    elif de_acc == 3:
                        Acc_3 = Acc_3 + amount
                        print("Remainder in the account you transferred to:", Acc_3)
                    elif de_acc == 4:
                        Acc_4 = Acc_4 + amount
                        print("Remainder in the account you transferred to:", Acc_4)
                    elif de_acc == 5:
                        Acc_5 = Acc_5 + amount
                        print("Remainder in the account you transferred to:", Acc_5)
                else:
                    print("You can't transfer money from one account to itself")
            else:
                print("Invalid Responce")        
        else:
            print("Account Unavailable")
    else:
        ("Invalid Responce")
print("Thanks for using my services...")