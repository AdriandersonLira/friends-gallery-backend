from flask import jsonify
from flask_restx import Resource

from werkzeug.security import check_password_hash
import datetime
import jwt

from src.server.instance import server
from src.server.response import responseApp

app, api, db = server.app, server.api, server.db

@api.route('/session')
class Session(Resource):
  def post(self):    
    try:
      user = api.payload
      # Find User by email
      dbResponse = dict(db.users.find_one({"email": user["email"]}))
      dbResponse["_id"] = str(dbResponse["_id"])
      
      if not check_password_hash(dbResponse["password"], user["password"]):
        return responseApp({ "message": "Invalid credentials." }, 403)
      
      payload = {
        "_id": dbResponse["_id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
      }

      token = jwt.encode(payload, app.secret_key, algorithm='HS256')
      
      response = {
        "token": token
          # jwt.decode(token, app.secret_key, algorithms=['HS256'])
      }
      
      return jsonify(response)
    except Exception as e:
      print(e)
      return responseApp({ "message": "User not found." }, 404) 
    
  # def delete(self, idUser):
  #   session.clear()
