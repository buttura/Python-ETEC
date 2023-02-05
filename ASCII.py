ascii = {"A": [" ______     ", "/\  _  \    ", "\ \ \L\ \   ", " \ \  __ \  ", "  \ \ \/\ \ ", "   \ \_\ \_\ ", "    \/_/\/_/"],
         "B": [" ____      ", "/\  _`\    ", "\ \ \L\ \  ", " \ \  _ <' ", "  \ \ \L\ \ ", "   \ \____/", "    \/___/ "]}


l = str(input("Digite uma palavra: ")).upper()
for i in range(len(l)):
    if l[i] in ascii:
        for x in range(len(ascii[l[i]])):
            print(ascii[l[i]][x])
    else:
        print("", end="")
