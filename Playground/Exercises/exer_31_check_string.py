def check_str(s):
   rules = ["isalnum", "isalpha", "isdigit", "islower", "isupper" ]
   return [any(list(map(lambda ch: getattr(ch, rule)() ,s))) for rule in rules ]

if __name__ == '__main__':
    s ="123"
    for res in check_str(s):
        print(res)
