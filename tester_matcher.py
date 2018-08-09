import argparse
import sqlite3
from sqlite3 import Error


def main():
    """
    Parses command line arguments, matches testers, and prints the results
    :return: None
    """

    parser = argparse.ArgumentParser(description='A program that matches testers to the given search criteria.')
    parser.add_argument("--country", "-c", action="append", required=False,
                        help="The country where a tester is located.")
    parser.add_argument("--device", "-d", action="append", required=False, help="The Device that the tester can test.")

    args = parser.parse_args()

    print("Criteria: {0} {1}".format(
        "".join(["Country=\"" + x + "\"" for x in args.country]) if args.country else "Country=\"all\"",
        "".join(["Device=\"" + x + "\"" for x in args.device]) if args.device else "Device=\"all\""))
    print("Results:")

    matches = match_testers(args.country, args.device)

    if len(matches)<1:
        print("There were no testers that matched the search criteria.")
    else:
        for match in matches:
            print("Id: {0:<3} Name: {1:22} Country: {2:5} Experience: {3}".format(match[0], match[1] + " " + match[2],
                                                                              match[3], match[4]))


def create_connection():
    """
    Creates the connection to the database.
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect("testers.db")
        return conn
    except Error as e:
        print(e)
    return None


def match_testers(country, device):
    """
    Assembles and runs a database query that matches testers to the search criteria provided by the user.
    :param country: The list of country parameters
    :param device: The list of device parameters
    :return: A list of tuples representing rows in the database.
    """
    conn = create_connection()
    cur = conn.cursor()
    where_clause, country_clause, device_clause = "", "", ""

    # Assemble the individual parts of the where clause
    if country:
        if "all" not in country:
            country_clause = "testers.country in ({0})".format(','.join('?' * len(country))) if len(country) > 0 else ""

        else:
            country = []
    else:
        country = []

    if device:
        if "all" not in device:
            device_clause = "devices.description in ({0})".format(','.join('?' * len(device))) if len(
                device) > 0 else ""
        else:
            device = []
    else: device = []

    # Put the parts together
    if country_clause != "" or device_clause != "":

        where_clause += "where "

        # Just Country
        if country_clause != "" and device_clause == "":
            where_clause += country_clause

        # Just Device
        elif country_clause == "" and device_clause != "":
            where_clause += device_clause

        # Both
        else:
            where_clause += country_clause + " and " + device_clause

    # Add the where clause to the query
    query = "select testers.testerId, testers.firstName, testers.lastName, testers.country, count(bugs.bugId) as xp\
                from testers\
                join tester_device on tester_device.testerId = testers.testerId\
                join devices on devices.deviceId = tester_device.deviceId\
                join bugs on bugs.testerId = testers.testerId and bugs.deviceId = tester_device.deviceId\
                {0}\
                group by testers.testerId\
                order by xp desc, testers.testerId".format(where_clause)

    # Run the query with the combined list to prevent sql injections
    combined_list = country + device
    cur.execute(query, combined_list)
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    main()
