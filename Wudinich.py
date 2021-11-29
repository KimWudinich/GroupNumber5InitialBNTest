# this function (do again) ask the user if they want to conitue or exit the program
def again():

    yesorNo = input("Do you want to run the program again? ('Y' for yes, anything else to quit)\n ")
    if yesorNo.upper() == "Y":
        print()
        main()
    else:
        exit()

main()
