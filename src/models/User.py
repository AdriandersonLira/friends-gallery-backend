from flask_restx import fields

from src.server.instance import server

User = server.api.model('User', {
  '_id': fields.String(description='User ID.'),
  'nickname': fields.String(required=True, max_length=20, description='User nickname.'),
  'email': fields.String(required=True, description='User email.'),
  'password': fields.String(required=True, description='User password.')
})