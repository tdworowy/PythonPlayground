from display import display
from postgresConection import postgresConection
from querys import query
from xmlGenerator import xmlGenerator


def main():
    try:

        displayInput = input("Display example pictures ? y/n ")
        conectionString = "NoSql", "User", "test10"
        con = postgresConection(*conectionString)
        q = query(con.getConection)
        xml = xmlGenerator(con.getConection)

        q.initLoad()
        q.customQuery("select * from workers")

        q.getHierarchyFrom("AGENT")
        q.getHierarchyFrom("HOMER")

        q.getHierarchyLast("AGENT")
        q.getHierarchyLast("HORSMAN")
        q.getHierarchyLast("HOMER")

        q.getHierarchyExa("BOSS.AGENT.HORSMAN")
        q.getHierarchyExa("BOSS.AGENT")
        q.getHierarchyExa("BOSS")

        print("INSERT DATA")
        q.insertNewWorker("6", "SpongeBob", "SquarePants", "BOSS.SPONGE")
        q.insertNewPicturesLinks("a_56ad0355.jpg", "6")
        q.insertNewPictures("6", "a_56ad0355.jpg")


        if(displayInput is 'y'):
                ui = display()
                picturesList = [q.getPicture(1),q.getPicture(2),q.getPicture(3)]
                ui.displayPicturesFomDB(picturesList)

                picturesList = [q.getPicturePath(1),q.getPicturePath(2)]
                ui.displayPicturesViaPath(picturesList)

                picturesList = [q.getPicture(6)]
                ui.displayPicturesFomDB(picturesList)

                picturesList = [q.getPicturePath(6)]
                ui.displayPicturesViaPath(picturesList)


        xml.exportToXML(1)
        xml.exportToXML(6)

        title= ("Title", "Rick and Morty")
        seasons = ("Seasons", "2")
        genre1 = ("Genre", "SF")
        genre2= ("Genre", "Comedy")
        xml.generateXML("Sanchez",title,seasons,genre1,genre2)

        q.insertXML("Sanchez","1")
        title = ("Title", "Archer")
        seasons = ("Seasons", "7")
        genre1 = ("Genre", "Action")
        genre2 = ("Genre", "Comedy")
        xml.generateXML("Archer", title, seasons, genre1, genre2)

        q.insertXML("Archer", "2")


        q.getGenreFromXMLBeID("1")
        q.getGenreFromXMLBeID("2")
        q.getGenreFromXML()

    except Exception as ex:
       print(ex)
    finally:
       q.customQuery("select * from workers")
       q.dropTable()

if __name__ == "__main__":
    main()
