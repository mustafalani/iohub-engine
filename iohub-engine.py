#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of iohub.
#
# iohub is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# iohub is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with iohub. If not, see <http://www.gnu.org/licenses/>.
#
# ------------------------------------------------------------------------------

import os
import sys
import sqlite3
from sqlite3 import Error


# Check database and create db file if missing
def create_db_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"./sqlite/db/ioengine.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS channels (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        channel_id integer NOT NULL,
                                        FOREIGN KEY (channel_id) REFERENCES channels (id)
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS presets (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    preset_id integer NOT NULL,
                                    FOREIGN KEY (preset_id) REFERENCES presets (id)
                                );"""

    # create a database connection
    conn = create_db_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
