# applause-exercise
A Tester matching exercise for Applause

# Installation:

1. Create a virtual environment.
  
    ```
    python3 -m pip install --user virtualenv          #macOS and Linux
    py -m pip install --user virtualenv               #Windows
    ```
    ```
    macOS and Linux: python3 -m virtualenv venv
    Windows: py -m virtualenv venv
    ```
2. Activate your virtual environment
    ```
    macOS and Linux: source venv/bin/activate
    Windows: .\venv\Scripts\activate
    ```
3. Install csvs-to-sqlite.
```pip install csvs-to-sqlite```

4. Build the database.
```csvs-to-sqlite bugs.csv devices.csv tester_device.csv testers.csv testers.db```

# How to Run:

1. Single argument value
```python tester_matcher.py --country "US" --device "iPhone 4"```

2 All
```python tester_matcher.py -c "all" -d "all"```

3. Multiple argument values
```python tester_matcher.py -c "US" -c "GB" -d "iPhone 4" -d "iPhone5"```
