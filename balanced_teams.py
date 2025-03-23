import csv
import itertools

def load_players(file_path):
    # print(f"Loading players from file: {file_path}")
    players = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 2:
                print(f"Skipping invalid row: {row}")
                continue  # Skip invalid rows
            name, rate = row
            try:
                players.append((name, float(rate)))
            except ValueError:
                print(f"Skipping row with invalid rating: {row}")
                continue  # Skip rows with invalid ratings
    # print(f"Loaded {len(players)} valid players.")
    return sorted(players, key=lambda x: x[1], reverse=True)

def balance_teams(players, num_teams):
    print()
    print(f"Balancing {len(players)} players into {num_teams} teams.")
    teams = [[] for _ in range(num_teams)]
    team_rates = [0] * num_teams
    
    for player in players:
        min_team = team_rates.index(min(team_rates))
        # print(f"Assigning player {player} to team {min_team+1}.")
        teams[min_team].append(player)
        team_rates[min_team] += player[1]
    
    # print("Final team distributions:")
    # for i, team in enumerate(teams, 1):
        # print(f"Team {i} total rating: {team_rates[i-1]}")
    
    return teams

def main():
    # Input file should be a CSV with two columns: Name,Rating (e.g., Daniel,100).
    file_path = input("Enter the file path containing players and ratings: ") 
    num_teams = int(input("Enter the number of teams: "))
    
    players = load_players(file_path)
    if not players:
        print("No valid players found in the file.")
        return
    
    teams = balance_teams(players, num_teams)
    
    for i, team in enumerate(teams, 1):
        print(f"\nTeam {i}:")
        for name, rate in team:
            print(f"  {name} - {rate}")
        print(f"  Total rating: {sum(player[1] for player in team)}")
    print()

if __name__ == "__main__":
    main()
