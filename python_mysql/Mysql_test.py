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
        # create_ratings_table_query = """
        # CREATE TABLE ratings (
        #     movie_id INT,
        #     reviewer_id INT,
        #     rating DECIMAL(2,1),
        #     FOREIGN KEY(movie_id) REFERENCES movies(id),
        #     FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
        #     PRIMARY KEY(movie_id, reviewer_id)
        # )
        # """
        # # if we want to create single table at one time we can use this 
        # with connection.cursor() as cursor:
        #     cursor.execute(create_ratings_table_query)
        #     connection.commit()
        # # # but if multiple table 
        # with connection.cursor() as cursor:
        #     cursor.execute(create_movies_table_query)
        #     cursor.execute(create_reviewers_table_query)
        #     cursor.execute(create_ratings_table_query)
        #     connection.commit()

        # # to fecth a table: equivalent to DESCRIBE <table_name>;
        # show_table_query = "Describe movies"
        # with connection.cursor() as cursor:
        #     cursor.execute(show_table_query)
        #     result = cursor.fetchall()
        #     for row in result:
        #         print(row)

        # # modifying table schema using ALTER Statment
        alter_table_query = """ ALTER TABLE movies 
        MODIFY COLUMN collection_in_mil DECIMAL(4,1);
        """
        show_table_query = "DESCRIBE movies"
        with connection.cursor() as cursor:
            cursor.execute(alter_table_query)
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            print("Movie table shema after chang")
            for row in result:
                print(row)

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