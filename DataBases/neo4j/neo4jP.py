from neo4j.v1 import GraphDatabase, basic_auth


class neo4jPython():

    def connectLocalHost(self):
       driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "test10"))
       self.session = driver.session()

    def clearBase(self):
        self.connectLocalHost()
        print("Clear data base")
        self.session.run("MATCH (n)OPTIONAL MATCH (n)-[r]-()DELETE n,r")

    def createPersons(self,personsList):
       self.connectLocalHost()
       print("Create Persons with data: ",personsList)
       for person in personsList:
            self.session.run("CREATE (a:Person{FirstName: {fname}, LastName: {lname}})",
                  {"fname": person[0], "lname": person[1]})

    def createShows(self, showsList):
        self.connectLocalHost()
        print("Create Show with data: ", showsList)
        for show in showsList:
            self.session.run("CREATE (a:Show {Title: {title}})",
                             {"title": show})
    def createGroups(self):
        self.connectLocalHost()
        print("Create groups")
        self.session.run("CREATE (a:Group {Name: 'Shows'})")
        self.session.run("CREATE (a:Group {Name: 'Persons'})")


    def getPerson(self,personsList):
        resultList = []
        for person in personsList:
            query = "MATCH (a:Person) WHERE a.FirstName =" +"\""+person[0]+"\""+ " RETURN a.FirstName AS FirstName, a.LastName AS LastName"
            print(query)
            result = self.session.run(query)
            resultList.append(result)
        for res in resultList:
            self.displayRecords(res)

    def displayRecords(self,result):
        print("Person data")
        for record in result:
             print("%s %s" % (record["FirstName"], record["LastName"]))

    def addCharacterRelations(self,personFName, show):
        self.connectLocalHost()
        query = "MATCH (p:Person {FirstName:'"+personFName+"'}), (s:Show {Title:'"+show+"'})CREATE (p)-[:CHARACTER_FROM]->(s)"
        print(query)
        self.session.run(query)

    def addGroupRelations(self, persons, shows):

        for peson in persons:
            self.connectLocalHost()
            query = "MATCH (p:Person {FirstName:'" + peson[0] + "'}), (g:Group {Name:'Persons'})CREATE (p)-[:BELONGS_TO_GROUP]->(g)"
            print(query)
            self.session.run(query)

        for show in shows:
            self.connectLocalHost()
            query = "MATCH (s:Show {Title:'" + show + "'}), (g:Group {Name:'Shows'})CREATE (s)-[:BELONGS_TO_GROUP]->(g)"
            print(query)
            self.session.run(query)


def main():

   persons = [("Homer","Simpson"),("Rick","Sanchez"),("Sterling","Archer")]
   shows = ["Rick & Morty", "Simpsons","Archer"]

   neo4j_ = neo4jPython()
   neo4j_.clearBase()
   neo4j_.createPersons(persons)
   neo4j_.createShows(shows)

   neo4j_.createGroups()

   neo4j_.addGroupRelations(persons,shows)

   neo4j_.addCharacterRelations(persons[0][0],shows[1])
   neo4j_.addCharacterRelations(persons[1][0], shows[0])
   neo4j_.addCharacterRelations(persons[2][0], shows[2])

   neo4j_.getPerson(persons[0:2])

if __name__ == "__main__":
    main()

