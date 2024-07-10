first = print("This is a flowchart for mira SSO")

third = " "
fourth = " "
fifth = " "
second = input("Do you have an account on this platfrom ? (yes or no)")
if second.lower() == "yes":
    third == input("input your username & password")
    print("WELCOME TO YOUR DASHBOARD")

elif second.lower() == "no":
    print("GO and create your account")
    third = input("Do you want to register with mira ? (yes or no)")
    if third.lower() == "yes":
        fourth = input("DO YOU HAVE A MIRA ACCOUNT ?")
        if fourth.lower() == "yes":
            print("LOGIN YOUR MIRA ACCOUNT HERE BELOW")
            fifth = input("INPUT YOUR MIRA EMAIL AND PASSWORD HERE")
            print("WELCOME TO YOUR DASHBOARD")
        elif fourth.lower() == "no":
            print("CLICK HERE TO CREATE A MIRA ACCOUNT")
            print("ENTER YOUR DETAILS BELOW")

            input("ENTER YOUR EMAIL HERE")
            input("ENTER YOUR PASSWORD")
            print("CONFIRM YOUR EMAIL BELOW")
            input("CONFIRM YOUR EMAIL HERE")
            print("WELCOME TO YOUR DASHBOARD")
        else:
            print(" invalid response ")
    elif third.lower() == "no":
        print("CLICK HERE TO CREATE AN ACCOUNT ON THIS PLATFORM")
        print("ENTER YOUR DETAILS BELOW")
        fourth = input("Email and password")
        input("VERIFY YOUR EMAIL")
        print("YOU MAY NOW LOGIN")
        print("WELCOME TO YOUR DASHBOARD")
    else:
        print("invalid response")

else:
    print("invalid response")
