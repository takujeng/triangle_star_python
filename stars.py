
print ("how many stars row: ")
stars_row = int(input("> "))
for i in range(1,stars_row+1):
    for j in range (1,i+1):
        print ("*",end=" ")
    print("")