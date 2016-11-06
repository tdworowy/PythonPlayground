while True:
    reply = input("Enter digit")
    if reply == "stop":break
    try:
        num = int(reply)
    except:
        print("Error")
    else:
        print(int(reply)*2)
print("End")