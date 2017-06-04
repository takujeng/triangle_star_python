while True:
    print ("how many stars row: ")
    try:
        stars_row = int(input("> "))
    except:
        print("it's not a number")
        break
    for i in range(1,stars_row+1):
        for j in range (1,i+1):
            print ("*",end=" ")
        print("")
    print("want to insert print star again? (input y or n)")
    choose = input("> ")
    if choose=="y":
        continue
    elif choose=="n":
        break