from Playground.rootDirectory import get_root_directory


def get_to_append(i):
    return """{
	  "firstName" : "firstName%s",
	  "lastName" : "lastName%s",
	  "email" : "employee1@cream.local",
	  "login" : "employee%s",
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
						"itemCodes": ["Bulgarian","Catalan","Croatian","Czech","Danish","Dutch","English","Estonian","Finnish","French", "German","Greek","Hungarian","Italian","Hungarian","Italian","Japanese","Latvian","Lithuanian","Norwegian","Polish","Portuguese","Romanian","Russian","Slovak","Slovenian","Spanish"]
					}, {
						"dictionaryCode": "Service",
						"itemCodes": ["Audit_Services","Complaints_Mitigation","Content_Management","Conversion_Services","Customer_Services","Customer_Verification","Incident_Coordination","Campaign_Services","Police_Request_Handling","Product_Testing","Promotion_Services","Risk_Services","VIP_Hosting_Services"]
					},
					{
					  "dictionaryCode": "Shop",
					  "itemCodes":["ACF","binguez.com","BORGATA","bwin.be","bwin.com","bwin.es","bwinfr","empirepoker.com","gamebookers.com","getminted","GiocoDigitale","intralot.it","party.com","party.dk","party.es","party.fr","party.it","party.net","PartyPokerNJ","pmu.fr","Premium"]
					}
					]
			},},
	""" % (i, i, i)


def extend_employ(file, range_):
    file.write("[ ")
    add_string = ""
    for i in range(range_[0], range_[1]):
        add_string = add_string + get_to_append(str(i))

    add_string = add_string + " ]"
    file.write(add_string)


if __name__ == '__main__':
    # file = open("C:/PLIKI/Load_tests/users_with_traits2.txt",'a')
    file = open(get_root_directory() + "\\users_with_No_traits.json", 'w+')

    extend_employ(file, (1, 2000))
