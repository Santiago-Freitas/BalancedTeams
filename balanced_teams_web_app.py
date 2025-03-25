from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_players(file):
    players = []
    try:
        stream = file.stream.read().decode("utf-8").splitlines()
        reader = csv.reader(stream)
        for row in reader:
            if len(row) != 2:
                continue
            name, rate = row
            try:
                players.append((name, float(rate)))
            except ValueError:
                continue
    except Exception as e:
        print(f"Error reading file: {e}")
    return sorted(players, key=lambda x: x[1], reverse=True)

def balance_teams(players, num_teams):
    teams = [[] for _ in range(num_teams)]
    team_rates = [0] * num_teams
    for player in players:
        min_team = team_rates.index(min(team_rates))
        teams[min_team].append(player)
        team_rates[min_team] += player[1]
    return teams

@app.route('/', methods=['GET', 'POST'])
def index():
    teams = None
    if request.method == 'POST':
        file = request.files['file']
        num_teams = int(request.form['num_teams'])
        players = load_players(file)
        if players:
            teams = balance_teams(players, num_teams)
    return render_template('index.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)
