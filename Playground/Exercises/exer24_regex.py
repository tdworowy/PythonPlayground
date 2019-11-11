input_data = ['riya riya@gmail.com',
              'julia julia@julia.me',
              'julia sjulia@gmail.com',
              'julia julia@gmail.com',
              'samantha samantha@gmail.com',
              'tanya tanya@gmail.com']

input_data2 = [
'riya riya@gmail.com',
'julia julia@julia.me',
'julia sjulia@gmail.com',
'julia julia@gmail.com',
'samantha samantha@gmail.com',
'tanya tanya@gmail.com',
'riya ariya@gmail.com',
'julia bjulia@julia.me',
'julia csjulia@gmail.com',
'julia djulia@gmail.com',
'samantha esamantha@gmail.com',
'tanya ftanya@gmail.com',
'riya riya@live.com',
'julia julia@live.com',
'julia sjulia@live.com',
'julia julia@live.com',
'samantha samantha@live.com',
'tanya tanya@live.com',
'riya ariya@live.com',
'julia bjulia@live.com',
'julia csjulia@live.com',
'julia djulia@live.com',
'samantha esamantha@live.com',
'tanya ftanya@live.com',
'riya gmail@riya.com',
'priya priya@gmail.com',
'preeti preeti@gmail.com',
'alice alice@alicegmail.com',
'alice alice@gmail.com',
'alice gmail.alice@gmail.com'
]
import  re
def get_name(data: [str]):
     result = []
     for line in data:
         name = line[: line.rindex(" ")]
         if "@gmail.com" in line and name in line[line.rindex(" "):]:
             result.append(name)
     return sorted(result)


def get_name_regex(data: [str]):
    result = []
    pattern = re.compile("@gmail.com")
    for line in data:
        name = line[: line.rindex(" ")]
        if pattern.findall(line) and name in line[line.rindex(" "):]:
            result.append(name)
    return sorted(result)

if __name__ == "__main__":
    for name1,name2 in zip(get_name(input_data2),get_name_regex(input_data2)):
        print(name1,name2)