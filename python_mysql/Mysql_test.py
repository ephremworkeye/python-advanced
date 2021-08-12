from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database='movie'
    ) as connection: # to create a connection and create a new database
        # # to create datbase
        # create_db_query = "CREATE DATABASE movie"
        # with connection.cursor() as cursor:
        #     cursor.execute(create_db_query)

        ## to create a table
        create_ratings_table_query = """
        CREATE TABLE ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_ratings_table_query)
            connection.commit()
except Error as e:
    print(e)

# but if we want to connect with existing database

# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "),
#         password=getpass("Enter password: "),
#         database="movie",
#     ) as connection:
#         print(connection)
# except Error as e:
#     print(e)