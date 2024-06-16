# neo4j

from neo4j import GraphDatabase, basic_auth


class Neo:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            "bolt://localhost:7687", auth=basic_auth("neo4j", "test10")
        )

    def clear_base(self):
        session = self.driver.session()
        print("Clear data base")
        session.run("MATCH (n)OPTIONAL MATCH (n)-[r]-()DELETE n,r")

    def create_people(self, people_list):
        session = self.driver.session()
        print("Create Persons with data: ", people_list)
        for person in people_list:
            session.run(
                "CREATE (a:Person{FirstName: {fname}, LastName: {lname}})",
                {"fname": person[0], "lname": person[1]},
            )

    def create_shows(self, shows_list):
        session = self.driver.session()
        print("Create Show with data: ", shows_list)
        for show in shows_list:
            session.run("CREATE (a:Show {Title: {title}})", {"title": show})

    def create_groups(self):
        session = self.driver.session()
        print("Create groups")
        session.run("CREATE (a:Group {Name: 'Shows'})")
        session.run("CREATE (a:Group {Name: 'Persons'})")

    def get_person(self, people_List):
        result_list = []
        session = self.driver.session()
        for person in people_List:
            query = (
                "MATCH (a:Person) WHERE a.FirstName ="
                + '"'
                + person[0]
                + '"'
                + " RETURN a.FirstName AS FirstName, a.LastName AS LastName"
            )
            print(query)
            result = session.run(query)
            result_list.append(result)
        for res in result_list:
            self.display_records(res)

    def display_records(self, result):
        print("Person data")
        for record in result:
            print("%s %s" % (record["FirstName"], record["LastName"]))

    def add_character_relations(self, person_first_name, show):
        session = self.driver.session()
        query = (
            "MATCH (p:Person {FirstName:'"
            + person_first_name
            + "'}), (s:Show {Title:'"
            + show
            + "'})CREATE (p)-[:CHARACTER_FROM]->(s)"
        )
        print(query)
        session.run(query)

    def add_group_relations(self, people, shows):

        for person in people:
            session = self.driver.session()
            query = (
                "MATCH (p:Person {FirstName:'"
                + person[0]
                + "'}), (g:Group {Name:'Persons'})CREATE (p)-[:BELONGS_TO_GROUP]->(g)"
            )
            print(query)
            session.run(query)

        for show in shows:
            session = self.driver.session()
            query = (
                "MATCH (s:Show {Title:'"
                + show
                + "'}), (g:Group {Name:'Shows'})CREATE (s)-[:BELONGS_TO_GROUP]->(g)"
            )
            print(query)
            session.run(query)


def main():
    people = [
        ("Homer", "Simpson"),
        ("Rick", "Sanchez"),
        ("Morty", "Sanchez"),
        ("Sterling", "Archer"),
    ]
    shows = ["Rick & Morty", "Simpsons", "Archer"]

    neo4j_ = Neo()
    neo4j_.clear_base()
    neo4j_.create_people(people)
    neo4j_.create_shows(shows)

    neo4j_.create_groups()

    neo4j_.add_group_relations(people, shows)

    neo4j_.add_character_relations(people[0][0], shows[1])
    neo4j_.add_character_relations(people[1][0], shows[0])
    neo4j_.add_character_relations(people[2][0], shows[0])
    neo4j_.add_character_relations(people[3][0], shows[2])

    neo4j_.get_person(people[0:3])


if __name__ == "__main__":
    main()
