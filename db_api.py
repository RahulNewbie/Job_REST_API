import sqlite3
from sqlite3 import Error
import constants

# Global variable declaration
ID = 1


def connect_to_database():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param: None
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(constants.DB_FILE)
    except Error as e:
        print(e)
    return conn


def insert_to_db(title, desc, company, location, category):
    """
    inserts the records in the database
    """
    global ID
    con = connect_to_database()
    cur = con.cursor()
    try:
        cur.execute("SELECT count(*) FROM job_data_table")
        num_of_job_offer = cur.fetchall()
        print(int(str(num_of_job_offer[0][0])))
        # Incrementing sequence for the record identifier
        ID = int(str(num_of_job_offer[0][0])) + constants.INCREMENT
        cur.execute(r"INSERT INTO job_data_table "
                    "(Id,Title,Description,Company,Location,"
                    "Job_Category) "
                    "VALUES (?, ?, ?, ?,?, ?)",
                    (ID, title, desc, company, location, category,))
        print("database insertion finished")
    except Error as err:
        print("Error happened while inserting "
              "data into database " + str(err))
    con.commit()
    con.close()


def select_all_job_offer():
    """
    Query all rows in the screenshot table
    :param: None
    :return: All rows of the table
    """
    conn = connect_to_database()
    cur = conn.cursor()
    # Select All the records from the Database
    cur.execute("SELECT * FROM job_data_table")
    rows = cur.fetchall()
    return rows


def update_job_offer(id, title=None, desc=None,
                     company=None, location=None, job_catagory=None):
    """
    Update job offer by providing the job id and update fields
    """
    conn = connect_to_database()
    cur = conn.cursor()
    try:
        if title is not None:
            cur.execute("UPDATE job_data_table "
                        "set Title = ? WHERE Id = ?", (title, id,))
        if desc is not None:
            cur.execute("UPDATE job_data_table "
                        "set Description = ? WHERE Id = ?", (desc, id,))
        if company is not None:
            cur.execute("UPDATE job_data_table "
                        "set Company = ? WHERE Id = ?", (company, id,))
        if location is not None:
            cur.execute("UPDATE job_data_table "
                        "set Location = ? WHERE Id = ?", (location, id,))
        if job_catagory is not None:
            cur.execute("UPDATE job_data_table "
                        "set Job_Category = ? WHERE Id = ?", (job_catagory, id,))
        conn.commit()
        conn.close()
    except Error as err:
        return "Error while updating jon offer"


def get_location_category():
    """
    Query all rows in the screenshot table
    :param: None
    :return: All rows of the table
    """
    conn = connect_to_database()
    cur = conn.cursor()
    # Select All the records from the Database
    # group by location and category
    cur.execute("SELECT Location, Job_Category  "
                "FROM job_data_table GROUP BY Location,Job_Category")
    rows = cur.fetchall()
    return str(rows)
