from flask_restx import Resource

from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

from src.server.auth import jwtRequired
from src.server.instance import server
from src.server.response import responseApp
# from src.models.User import User

app, api, db = server.app, server.api, server.db

@api.route('/user')
class User(Resource):
  # @api.marshal_list_with(User)
  # def get(self):
  #   try:
  #     data = list(db.users.find())
      
  #     for user in data:
  #       user["_id"] = str(user["_id"])
        
  #     return responseApp(data, 200)
  #   except Exception as e:
  #     print(e)
  #     return responseApp({ "message": "cannot read users" }, 500)
  
  # @api.expect(User, validation=True)
  # @api.marshal_with(User)
  def post(self):
    try:
      user = api.payload
      
      # Encrypt the password
      user["password"] = generate_password_hash(user["password"])
      
      # Check for existing email address
      if db.users.find_one({ "email": user["email"] }):
        return responseApp({
          "message": "Email address already in use",
        }, 400)
        
      # Insert User
      dbResponse = db.users.insert_one(user)
      
      return responseApp({
          "message": "user created", 
          "id": f"{dbResponse.inserted_id}"
        }, 200)
    except Exception as e:
      print(e)
      return responseApp({ "message": "cannot create user" }, 400)

@api.route('/user/<id>')
class UserId(Resource):
  @jwtRequired
  def get(self, id, current_user):
    try:
      dbResponse = dict(db.users.find_one({"_id": ObjectId(id)}))
      
      dbResponse["_id"] = str(dbResponse["_id"])
      
      return responseApp(dbResponse, 200)
    except Exception as e:
      print(e)
      return responseApp({ "message": "cannot read user" }, 500)
    
  def patch(self, id):
    try:
      request = api.payload
      dbResponse = db.users.update_one(
        {"_id": ObjectId(id)},
        {"$set": request}
      )
      
      if dbResponse.modified_count == 1:
        return responseApp({ 
          "message": "user updated" 
        }, 204) 
        
      return responseApp({
        "message": "nothing to update" 
      }, 404)
    except Exception as e:
      print(e)
      return responseApp({ "message": "cannot update user" }, 500)
    
  # def delete(self, id):
  #   try:
  #     dbResponse = db.users.delete_one({ "_id": ObjectId(id) })
        
  #     if dbResponse.deleted_count == 1:
  #       return responseApp({ "message": "user deleted" }, 200)
      
  #     return responseApp({ "message": "user not found" }, 404)
  #   except Exception as e:
  #     print(e)
  #     return responseApp({ "message": "cannot delete user" }, 500)