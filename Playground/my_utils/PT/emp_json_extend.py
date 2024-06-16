from Playground.root_directory import get_root_directory

ToAppend = """{
  "firstName" : "firstName",
  "lastName" : "lastName",
  "email" : "employee2500@cream.local",
  "login" : "employee2500",
  "password" : "test10",
  "auth" : "LOCAL",
  "roles" : [ "employee", "seller", "casemanager", "businessadmin", "appadmin", "activitymanager", "campadmin", "productmanager", "servicemanager", "campviewer", "salesmanager", "sysadmin", "productowner" ],
  "lang": "en",
		"dictionaryCodes": {
			"groups": [
				{
					"dictionaryCode": "FuncArea",
					"itemCodes": ["1st_Line", "2nd_Line", "IT", "Training","Planning_&_Management_Information","Processes_and_Information","Project_&_Portfolio_Management","Quality_Management","Risk_Management","External"]
				}, {
					"dictionaryCode": "Lang",
					"itemCodes": ["BG","CA","HR","CS","DA","NL","EN","ET", "FI", "FR", "DE","EL","HU","IT","JP","LV","LT","NO","PL","PT","RO","RU","SK","SL","ES","SV","TR"]
				}, {
					"dictionaryCode": "Service",
					"itemCodes": ["audit","complaints","content","conversion","support","verification","incident","campaigns","police", "testing","promotion","risk","vip"]
				},
				{
				  "dictionaryCode": "Shop",
				  "itemCodes": ["ac","bc","bj","bb","bz","be","bf","ds"	,"ep","gb","gm","gd","ii","pp","dk","pe","fr","pi","pf","pj","pm","pr","sh","wt","wf","zy"]
				}
				]
		},},
"""


def clean(file):
    temp_string = file.read()
    temp_string = temp_string[:-4]
    file.write(temp_string)


def extend_employ(file, range_):
    clean(file)
    add_string = ""
    for i in range(range_[0], range_[1]):
        add_string = add_string + ToAppend.replace(
            "employee{x}".format(x=range_[0]), "employee" + str(i)
        )

    add_string = "[" + add_string + " ]"
    file.write(add_string)


if __name__ == "__main__":
    # file = open("C:/PLIKI/Load_tests/users_with_traits2.txt",'a')
    file = open(get_root_directory() + "\\users_with_traits2.json", "w+")

    extend_employ(file, (2500, 5000))
