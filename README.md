# GraphQL Quidditch Manager

This application demonstrates how we can use Flask to build a GraphQL API that can create and return **flexible and meaningful data**. First we'll setup our backend using Flask and an SQLite database. Next we'll bring in GraphQL to build an API that will allow us to interact with quidditch teams, players, and games. Finally we'll see how we can use [Auth0 rules](https://auth0.com/docs/rules) to integration different authorization models.

# Getting Started

First install [Python](https://www.python.org/downloads/) if it's not already on your machine (Python 3 in this example).

Next clone this repo and enter into the root folder.

```bash
git clone https://github.com/hollylawly/flask-graphql-quidditch
cd flask-graphql-quidditch
```

Setup a virtual environment (not necessary, but recommended) so that the dependencies are all together and there are no conflicts.

For Mac/Linux:
```bash
python3 -m venv env
```

For Windows:
```bash
py -3 -m venv env
```

Activate the virtual environment

For Windows:

```bash
env\Scripts\activate
```

Mac or Linux use:

```bash
. env/bin/activate
```

Install our dependencies

```bash
pip install -r requirements.txt
```

Populate the database with our mock data. First open up a Python shell by typing `python` in your terminal. Then paste in the following and press enter:

```bash

from database import Base, engine, db_session
from models import Team, Player, Game
Base.metadata.create_all(bind=engine)

team1 = Team(name='Gryffindor', rank=1)
db_session.add(team1)
team2 = Team(name='Slytherin', rank=2)
db_session.add(team2)
team3 = Team(name='Ravenclaw', rank=4)
db_session.add(team3)
team4 = Team(name='Hufflepuff', rank=3)
db_session.add(team4)

player1 = Player(name='Harry Potter', year=2, position='Seeker', on_team=team1)
db_session.add(player1)
player2 = Player(name='Draco Malfoy', year=2, position='Seeker', on_team=team2)
db_session.add(player2)
player3 = Player(name='Oliver Wood', year=4, position='Captain', on_team=team1)
db_session.add(player3)
player4 = Player(name='Vincent Crabbe', year=2, position='Beater', on_team=team2)
db_session.add(player4)
player5 = Player(name='Cho Chang', year=2, position='Seeker', on_team=team3)
db_session.add(player5)
player6 = Player(name='Cedric Diggory', year=4, position='Captain', on_team=team4)
db_session.add(player6)
player7 = Player(name='Roger Davies', year=3, position='Captain', on_team=team3)
db_session.add(player7)
player8 = Player(name='Gregory Goyle', year=2, position='Beater', on_team=team2)
db_session.add(player8)
player9 = Player(name='Katie Bell', year=4, position='Chaser', on_team=team1)
db_session.add(player9)
player10 = Player(name='Zacharias Smith', year=3, position='Chaser', on_team=team4)
db_session.add(player10)

game1 = Game(level='Practice', winner_id=1, loser_id=2)
db_session.add(game1)
game2 = Game(level='Practice', winner_id=4, loser_id=1)
db_session.add(game2)
game3 = Game(level='Practice', winner_id=1, loser_id=3)
db_session.add(game3)
game4 = Game(level='Practice', winner_id=2, loser_id=4)
db_session.add(game4)
game5 = Game(level='Practice', winner_id=2, loser_id=3)
db_session.add(game5)
game6 = Game(level='Practice', winner_id=3, loser_id=4)
db_session.add(game6)
game7 = Game(level='First', winner_id=1, loser_id=2)
db_session.add(game7)
game8 = Game(level='First', winner_id=4, loser_id=3)
db_session.add(game8)
game9 = Game(level='Final', winner_id=1, loser_id=4)
db_session.add(game9)

db_session.commit()
```

Then press `ctrl` + `Z` to exit.

Next just start the server with:

```bash
python app.py
```

View the GraphQL IDE at http://localhost:5000/graphql

## Example queries:

Paste these on the left-hand side and you can see the result on the right-hand side

### Get all players

```
{
    allPlayers {
        edges {
            node {
                name
                position
            }
        }
    }
}
```

### Get player where name is "Harry Potter"

```
{
    getPlayer(name: "Harry Potter") {
        name
        position
        teamName {
            name
            rank
        }
    }
}
```

To exit and deactivate the virtual environment:

```bash
deactivate
```