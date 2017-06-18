def echo(message):
    print(message)

def indirect(func,arg):
        func(arg)

indirect(echo,"Test!!")


schedule = [(echo,"Spam"),(echo,"Spam2")]
for func,arg in schedule:
    func(arg)