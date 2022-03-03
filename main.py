from flask import jsonify
from src.server.instance import server

from src.controllers.user import *
from src.controllers.session import *

api = server.api

api.add_resource(User, '/user')
api.add_resource(UserId, '/user/<id>')

api.add_resource(Session, '/session/')

if __name__ == '__main__':
  server.run()