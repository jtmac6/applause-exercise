# applause-exercise
A tester matching coding exercise for Applause

# Design

I chose to implement this coding exercise as a simple command line program.  The structure of the input seemed well suited to a command line interface and using argparse made it easy to read in user input.  Initially, I thought about reading directly from the csv files and storing the data in memory, but I knew that wouldn't be a very scalable design. If the dataset were to grow substantially, I'd risk overflowing my stack. I also knew that the act of matching the testers to the given criteria would be well suited to a formal database query. The csv files were also already structured in a way that mimicked a relational database, so for these reasons, I chose to build a Sqlite database from the csv files using the csvs-to-sqlite tool. My program would then assemble a query based the user's input. Since I was taking user input and concatenating it into my query string, I made sure to account for potential sql injection vulnerabilities and used sqlite3's execute parameters to sanitize the input.

# Installation:

1. Create a virtual environment.
  
    ```
    python3 -m pip install --user virtualenv          #macOS and Linux
    py -m pip install --user virtualenv               #Windows
    ```
    ```
    python3 -m virtualenv venv                        #macOS and Linux
    py -m virtualenv venv                             #Windows
    ```
2. Activate your virtual environment
    ```
    source venv/bin/activate                          #macOS and Linux
    .\venv\Scripts\activate                           #Windows
    ```
    
# Rebuilding the Database
Usually I wouldn't version control a self-contained database in a project, but since the corresponding csv data files are already included and this is a small data set, I've included a prebuilt database for convenience.  If you'd like to edit the csv files and rebuild the database to test different data, you can do so by doing the following:

1. Install csvs-to-sqlite.
```pip install csvs-to-sqlite```

2. Build the sqlite database from the given csv files.
```csvs-to-sqlite bugs.csv devices.csv tester_device.csv testers.csv testers.db```

Note: The tests in test_test_matcher.py assume expected values from the original data set.

# Usage

 ```
    python tester_matcher.py --help
    usage: tester_matcher.py [-h] [--country COUNTRY] [--device DEVICE]

    A program that matches testers to the given search criteria.

    optional arguments:
      -h, --help            show this help message and exit
      --country COUNTRY, -c COUNTRY
                            The country where a tester is located.
      --device DEVICE, -d DEVICE
                            The Device that the tester can test.
```

# Examples:

1. Single argument value: ```tester_matcher.py --country "US" --device "iPhone 4"```
```
    Criteria: Country="US" Device="iPhone 4"
    Results:
    Id: 4   Name: Taybin Rutkin          Country: US    Experience: 66
    Id: 1   Name: Miguel Bautista        Country: US    Experience: 23
```

2. Query using the full list of devices and/or countries with "all": ```tester_matcher.py -c "all" -d "all"```
```
    Criteria: Country="all" Device="all"
    Results:
    Id: 4   Name: Taybin Rutkin          Country: US    Experience: 125
    Id: 7   Name: Lucas Lowry            Country: JP    Experience: 117
    Id: 8   Name: Sean Wellington        Country: JP    Experience: 116
    Id: 1   Name: Miguel Bautista        Country: US    Experience: 114
    Id: 6   Name: Stanley Chen           Country: GB    Experience: 110
    Id: 5   Name: Mingquan Zheng         Country: JP    Experience: 109
    Id: 3   Name: Leonard Sutton         Country: GB    Experience: 106
    Id: 9   Name: Darshini Thiagarajan   Country: GB    Experience: 104
    Id: 2   Name: Michael Lubavin        Country: US    Experience: 99
```
3. Multiple argument values: ```tester_matcher.py -c "JP" -c "GB" -d "Galaxy S3" -d " Galaxy S4" -d "Nexus 4"```
```
    Criteria: Country="JP" Country="GB" Device="Galaxy S3" Device=" Galaxy S4" Device="Nexus 4"
    Results:
    Id: 3   Name: Leonard Sutton         Country: GB    Experience: 55
    Id: 7   Name: Lucas Lowry            Country: JP    Experience: 53
    Id: 9   Name: Darshini Thiagarajan   Country: GB    Experience: 28
    Id: 8   Name: Sean Wellington        Country: JP    Experience: 23
    Id: 5   Name: Mingquan Zheng         Country: JP    Experience: 13
```
# Tests
Tests are included in test_tester_matcher.py

To run: 

```pip install pytest```

```pytest```
