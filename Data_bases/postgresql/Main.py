from Data_bases.postgresql.display import Display
from Data_bases.postgresql.PostgresConnection import PostgresConnection
from Data_bases.postgresql.querys import Query
from Data_bases.postgresql.XmlGenerator import XmlGenerator


def main():
    try:

        display_input = input("Display example pictures ? y/n ")
        connection_string = "NoSql", "User", "test10"
        con = PostgresConnection(*connection_string)
        q = Query(con.get_connection)
        xml = XmlGenerator(con.get_connection)

        q.init_load()
        q.custom_query("select * from workers")

        q.get_hierarchy_from("AGENT")
        q.get_hierarchy_from("HOMER")

        q.get_hierarchy_last("AGENT")
        q.get_hierarchy_last("HORSMAN")
        q.get_hierarchy_last("HOMER")

        q.get_hierarchy_exa("BOSS.AGENT.HORSMAN")
        q.get_hierarchy_exa("BOSS.AGENT")
        q.get_hierarchy_exa("BOSS")

        print("INSERT DATA")
        q.insertNewWorker("6", "SpongeBob", "SquarePants", "BOSS.SPONGE")
        q.insertNewPicturesLinks("a_56ad0355.jpg", "6")
        q.insert_new_pictures("6", "a_56ad0355.jpg")


        if display_input is 'y':
                ui = Display()
                pictures_list = [q.get_picture(1), q.get_picture(2), q.get_picture(3)]
                ui.display_pictures_fom_db(pictures_list)

                pictures_list = [q.get_picture_path(1), q.get_picture_path(2)]
                ui.display_pictures_via_path(pictures_list)

                pictures_list = [q.get_picture(6)]
                ui.display_pictures_fom_db(pictures_list)

                pictures_list = [q.get_picture_path(6)]
                ui.display_pictures_via_path(pictures_list)


        xml.export_to_xml(1)
        xml.export_to_xml(6)

        title= ("Title", "Rick and Morty")
        seasons = ("Seasons", "2")
        genre1 = ("Genre", "SF")
        genre2= ("Genre", "Comedy")
        xml.generate_xml("Sanchez", title, seasons, genre1, genre2)

        q.insert_xml("Sanchez", "1")
        title = ("Title", "Archer")
        seasons = ("Seasons", "7")
        genre1 = ("Genre", "Action")
        genre2 = ("Genre", "Comedy")
        xml.generate_xml("Archer", title, seasons, genre1, genre2)

        q.insert_xml("Archer", "2")


        q.get_genre_from_xml_be_id("1")
        q.get_genre_from_xml_be_id("2")
        q.get_genre_from_xml()

    except Exception as ex:
       print(ex)
    finally:
       q.custom_query("select * from workers")
       q.drop_table()

if __name__ == "__main__":
    main()
