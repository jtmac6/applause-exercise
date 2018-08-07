import argparse
import sqlite3
from sqlite3 import Error


def main():
    parser = argparse.ArgumentParser(description='Query for testers')
    parser.add_argument("--country", "-c", action="append", required=False,
                        help="The country where a tester is located.")
    parser.add_argument("--device", "-d", action="append", required=False, help="The Device that the tester can test.")
    # If the user doesn't supply any arguments, args.country and args.device will be None
    args = parser.parse_args()

    print("Criteria: {0} {1}".format(
        ["Country=\"" + x + "\"" for x in args.country] if args.country else "Country=\"all\"",
        ["Device=\"" + x + "\"" for x in args.device] if args.device else "Device=\"all\""))
    print("Results:")
    matches = match_testers(args.country, args.device)
    for match in matches:
        print("Id: {0:<3} Name: {1:22} Country: {2:5} Experience: {3}".format(match[0], match[1] + " " + match[2],
                                                                              match[3], match[4]))


def create_connection():
    try:
        conn = sqlite3.connect("testers.db")
        return conn
    except Error as e:
        print(e)
    return None


def match_testers(country, device):
    conn = create_connection()
    cur = conn.cursor()

    where_lst = []
    if country:
        if "all" not in country:
            where_lst.append("testers.country in ({0})".format(", ".join(["\'" + x + "\'" for x in country])))
    if device:
        if "all" not in device:
            where_lst.append("devices.description in ({0})".format(", ".join(["\'" + y + "\'" for y in device])))

    where_clause = "where {0}".format(" and ".join(where_lst)) if len(where_lst) > 0 else ""

    query = "select testers.testerId, testers.firstName, testers.lastName, testers.country, count(bugs.bugId) as xp\
                from testers\
                join tester_device on tester_device.testerId = testers.testerId\
                join devices on devices.deviceId = tester_device.deviceId\
                join bugs on bugs.testerId = testers.testerId and bugs.deviceId = tester_device.deviceId\
                {0}\
                group by testers.testerId\
                order by xp desc, testers.testerId".format(where_clause)

    cur.execute(query)
    rows = cur.fetchall()
    return rows


if __name__ == '__main__':
    main()
