from models import Team
from models import Player
from models import Game
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy import or_

class PlayerObject(SQLAlchemyObjectType):
    class Meta:
        model = Player
        interfaces = (graphene.relay.Node, )


class TeamObject(SQLAlchemyObjectType):
    class Meta:
        model = Team
        interfaces = (graphene.relay.Node, )


class GameObject(SQLAlchemyObjectType):
    class Meta:
        model = Game
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    # Expose all attributes for players, teams, and games based on their model
    all_players = SQLAlchemyConnectionField(PlayerObject)
    all_teams = SQLAlchemyConnectionField(TeamObject)
    all_games = SQLAlchemyConnectionField(GameObject)

    # Get a specific player (expects player name)
    get_player = graphene.Field(PlayerObject, name = graphene.String())
    # Get a game (expects game id)
    get_game = graphene.Field(GameObject, id = graphene.Int())
    # Get all games a team has played (expects team id)
    get_team_games = graphene.Field(lambda: graphene.List(GameObject), team = graphene.Int())
    # Get all players who play a certain position (expects position name)
    get_position = graphene.Field(lambda: graphene.List(PlayerObject), position = graphene.String())

    # Resolve our queries
    def resolve_get_player(parent, info, name):
        query = PlayerObject.get_query(info)
        return query.filter(Player.name == name).first()

    def resolve_get_game(parent, info, id):
        query = GameObject.get_query(info)
        return query.filter(Game.id == id).first()

    def resolve_get_team_games(parent, info, team):
        query = GameObject.get_query(info)
        return query.filter(or_(Game.winner_id == team, Game.loser_id == team)).all()
    
    def resolve_get_position(parent, info, position):
        query = PlayerObject.get_query(info)
        return query.filter(Player.position == position).all()


schema = graphene.Schema(query=Query)