# Balanced Teams Generator

This script takes as input a CSV file containing player names and their ratings.

## Example

### **Players.csv**
```
Daniel,100
Nael,95
Roshaan,98
```

### **Running the script**
```sh
python3 balanced_teams.py
```

#### **Example input/output**
```
Enter the file path containing players and ratings: players.csv
Enter the number of teams: 4
```

You will get back a list of balanced teams.

```
Balancing X players into Y teams.

Team 1:
  Daniel - 100.0
  Arian - 99.0
  Total rating: 522.0

Team 2:
  Bardia - 100.0
  Roshaan - 98.0
  Total rating: 520.0

Team 3:
  Andres - 100.0
  Nael - 95.0
  Total rating: 523.0

Team 4:
  Cesar - 100.0
  Ivaan - 93.0
  Total rating: 515.0
```
