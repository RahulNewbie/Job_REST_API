import csv
import sqlite3
import os
import constants


def job_insertion():
    """
    Read the CSV file and insert records in Database
    """
    con = sqlite3.connect(constants.DB_FILE)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS job_data_table (Id,Title,Description,Company,"
                "Location,Job_Category);")
    with open('job_listing.csv', 'rt') as fin:
        # csv.DictReader read line by line
        dr = csv.DictReader(fin)
        to_db = [(i['Id'], i['Title'], i['Description'],
                  i['Company'], i['Location'], i['Job_Category'])
                 for i in dr]

    cur.executemany("INSERT INTO job_data_table "
                    "(Id,Title,Description,Company,Location,"
                    "Job_Category) "
                    "VALUES (?, ?, ?, ?,?, ?);", to_db)
    print("database insertion finished")
    con.commit()
    con.close()


if __name__ == "__main__":
    job_insertion()
