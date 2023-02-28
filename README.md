# ds-test
This repository is used to generate test files for DataSurgeon

# Setup
```
pip install Faker
```

# Arguments
```
python3 ~/test.py -h                                                                                                                                                                                                             130 ⨯
usage: test.py [-h] [--output OUTPUT] [--size SIZE] [--speed SPEED]

DataSurgeon Test File Generator

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Name of the output file (default: test.txt)
  --size SIZE, -s SIZE  Size to create the test file in Gigabytes (Default: 5)
  --speed SPEED, -S SPEED
```

# Usage
```
python3 test.py
```
Below generates a 7GB test file 
```
python3 test.py -s 7
```
