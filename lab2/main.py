from sqlalchemy import create_engine, MetaData, Table, select


def connect_to_database(db_type,
                        user,
                        password,
                        db_url,
                        port,
                        db_name):

    db_string = "".join([db_type, "://",
                         user, ":",
                         password, "@",
                         db_url, ":",
                         port, "/", db_name])
    print(db_string)

    return create_engine(db_string)


def unique_records(tables, columns):
    tabs = ",".join(list(tables))
    cols = ",".join(list(columns))

    return f"SELECT DISTINCT {tabs} FROM {cols}"


def limit_query(query, limit):
    return f"{query} LIMIT {limit}"


def min_query(table, column):
    return f"SELECT MIN({column}) FROM {table}"


def max_query(table, column):
    return f"SELECT MAX({column}) FROM {table}"


def in_query(columns, table_name, in_col, in_tuple):
    in_t = ",".join(in_tuple)
    col = ",".join(columns)
    return f"SELECT {col} FROM {table_name} WHERE {in_col} IN ({in_t})"


def staff_2_country():
    return """SELECT staff.first_name, staff.last_name, country.country
        FROM staff
        INNER JOIN address
            ON staff.address_id = address.address_id
        INNER JOIN city
            ON address.city_id = city.city_id
        INNER JOIN country
            ON city.country_id = country.country_id"""


def actor_2_language_2_film():
    return """SELECT actor.first_name, actor.last_name, film.title, language.name
        FROM actor
        INNER JOIN film_actor
            ON actor.actor_id = film_actor.actor_id
        INNER JOIN film
            ON film_actor.film_id = film.film_id
        INNER JOIN language
            ON film.language_id = language.language_id"""


def main():
    # zad1
    db = connect_to_database(db_type="postgres",
                              user="wbauer_adb",
                              password="adb2020",
                              db_url="pgsql-196447.vipserv.org",
                              port="5432",
                              db_name="wbauer_adb")
    # zad2
    actor2lang2film = db.execute(actor_2_language_2_film()).fetchall()
    staff2country = db.execute(staff_2_country()).fetchall()

    # zad3
    categories = db.execute(unique_records(
        tables=("name",), columns=("category",))).fetchall()

    # zad4
    limit2 = db.execute(limit_query(unique_records(
        tables=("name",), columns=("category",)), 2)).fetchall()

    # zad5
    youngest = db.execute(min_query("film", "title")).fetchall()
    oldest = db.execute(max_query("film", "title")).fetchall()

    # zad6
    in_q = db.execute(in_query(columns=("first_name", "last_name"),
                                   table_name="actor",
                                    in_col="first_name",
                                     in_tuple=("'Olympia'", "'Julia'", "'Ellen'"))).fetchall()
    print(in_q)
    


if __name__ == "__main__":
    main()
