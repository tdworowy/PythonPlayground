def echo(message):
    print(message)

def indirect(func,arg):
        func(arg)

if __name__ == "__main__":

    indirect(echo,"Test!!")


    schedule = [(echo,"Spam"),(echo,"Spam2")]
    for func,arg in schedule:
        func(arg)