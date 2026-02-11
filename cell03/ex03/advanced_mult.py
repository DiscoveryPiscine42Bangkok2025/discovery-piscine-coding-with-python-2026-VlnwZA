for n in range(1,15):
    i = 0
    result = ""
    while i <= 15:
        result = result + " " + str(i * n)
        i += 1
    print("Table de :" + result)