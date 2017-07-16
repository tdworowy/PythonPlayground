import array

with open("Pulp-Simpson-Tee-Design-by-Stationjack-600x300.png", "rb") as imageFile:
    data = imageFile.read()
    print(data)

with open('newFile.png','ab') as file:
    x= list(data[0:20]) #don't work first 8 bites are png signature
    for char in data[20:]:
        if(char+2 > 255):
            x.append(255)
        else:
            x.append(char+2)
    print(x)
    y = array.array('B', x).tostring()
    print(y)
    file.write(y)
