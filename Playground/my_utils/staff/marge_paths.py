def marge_strings(string1, string2):
    list1 = string1.split(";")
    list2 = string2.split(";")
    list3 = [element for element in list1 if element not in list2]
    list3.extend(list2)
    return (
        str(list3)
        .replace("[", "")
        .replace("]", "")
        .replace("\\\\", "\\")
        .replace("'", "")
        .replace(",", ";")
    )


if __name__ == "__main__":
    string1 = "C:\\Users\Tomasz\AppData\Roaming\cabal\bin;C:\\Users\Tomasz\AppData\Roaming\local\\bin;C:\\Users\Tomasz\AppData\Local\Programs\Python\Python35-32\Scripts\;C:\\Users\Tomasz\AppData\Local\Programs\Python\Python35-32\;D:\Program Files\Docker Toolbox;%USERPROFILE%\AppData\Local\Microsoft\WindowsApps;D:\Google_drive\Python\SeleniumPython\chromedriver;D:\Android\sdk\\tools;D:\Android\sdk\platform-tools;C:\Program Files\Java\jdk1.8.0_121\\bin;C:\Program Files\MySQL\MySQL Server 5.7\\bin;D:\Python\Scripts;C:\maven\\apache-maven-3.3.9\\bin;D:\Python;D:\Python\Lib;C:\Program Files\Docker Toolbox;"
    string2 = "C:\\ProgramData\Oracle\Java\javapath;C:\\PROGRA~2\\Groovy\GROOVY~1.10\\bin;C:\WINDOWS\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\WindowsPowerShell\\v1.0\;C:\Program Files (x86)\\NVIDIA Corporation\PhysX\Common;C:\Program Files (x86)\GtkSharp\\2.12\\bin;C:\Program Files\dotnet\\"
    print(marge_strings(string2, string1))
