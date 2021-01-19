def switchFiles():
    file = input("File name 1: ")
    file2 = input("File name 2: ")
    with open (file, 'r')as a:
        dataa = a.read()
    with open (file2, 'r')as b:
        datab = b.read()
    with open (file, 'w') as a:
        a.write(datab)
    with open (file2, 'w') as b:
        b.write(dataa)
    print(dataa)
    print(datab)
switchFiles()