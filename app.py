# imports
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema


# initialise flask object
app = Flask(__name__)

# Create home route
@app.route('/')
def home():
    return 'Hello world'

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)