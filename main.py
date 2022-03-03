from src.server.instance import server

from src.controllers.user import *
from src.controllers.session import *
from src.controllers.moment import *
from src.controllers.gallery import *

api = server.api

api.add_resource(User, '/user')
api.add_resource(UserId, '/user/<id>')

api.add_resource(Session, '/session')

api.add_resource(Moment, '/moment')

api.add_resource(Gallery, '/gallery')


if __name__ == '__main__':
  server.run()