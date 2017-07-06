def getClassesNames(str):
	# temp = ','.join(str)
	temp = str.replace(".java", "")
	temp = temp.replace("[", "")
	temp = temp.replace("]", "")
	temp = temp.replace("'", "")

	return temp

if __name__ == '__main__':
	str = "['ActivityDefinitionTest.java', 'AppointmentsTest.java', 'BAM_Tests.java', 'CampaignsCategoriesTest.java', 'CampaignsResponsesTest.java', 'CampaignsTemplatesTest.java', 'CampaignsTest.java', 'CaseDefTest.java', 'CaseRulesTest.java', 'CasesTest.java', 'CommunicationsTest.java', 'ContactBook_AddOrganizationTest.java', 'ContactBook_AddPersonTest.java', 'ContactBook_AddResourceTest.java', 'ContactBook_EditOrganizationTest.java', 'ContactBook_EditPersonTest.java', 'ContactBook_EditResourceTest.java', 'ContactBook_MyContactsTest.java', 'ContractsTest.java', 'CreateMailBoxTest.java', 'DashboardsAdministrationTest.java', 'DashboardsHomeTest.java', 'DashboardTest.java', 'DictionariesTest.java', 'EmployeeTest.java', 'GenerateContactsTest.java', 'HotkeyTest.java', 'LoginTest.java', 'MainMenuTest.java', 'NotificationsTest.java', 'NumberSchemasTest.java', 'OrdersTest.java', 'ProductsTest.java', 'QuickAddTest.java', 'ReportsTest.java', 'RequestRulesTest.java', 'RequestsTest.java', 'SearchTest.java', 'SelectableColumnsTest.java', 'SendEmailTest.java', 'Tasks_AddTest.java', 'Tasks_ArchiveReopenTest.java', 'Tasks_EditTest.java', 'Tasks_MyTaskTest.java', 'Tasks_ToDoTaskTest.java', 'TeamTest.java', 'TraitsInheritTest.java', 'UserRolesTest.java', 'WorkflowTest.java']"
	print(getClasses(str))
