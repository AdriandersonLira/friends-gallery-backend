from flask_restx import Resource

from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

from src.server.auth import jwtRequired
from src.server.instance import server
from src.server.response import responseApp

api, db = server.api, server.db

@api.route('/gallery')
class Gallery(Resource):
  @jwtRequired
  def post(self, current_user):
    try:
      gallery = api.payload
      
      # Encrypt the password
      gallery["password"] = generate_password_hash(gallery["password"])
      
      # Check for existing name
      if db.galleries.find_one({ "name": gallery["name"] }):
        return responseApp({
          "message": "This name already in use",
        }, 400)
        
      gallery["admins"] = dict(gallery["admins"])
      
      # Checking if the amount of admins is between 1 and 2
      quant = len(gallery["admins"])
      if quant != 1 and quant != 2:
        return responseApp({
          "message": "The amount of admins to be 1 or 2",
        }, 400)
      
      # Checking if the admin exists as a user
      for key, value in gallery["admins"].items():
        if not db.users.find_one({"_id":  ObjectId(value)}):
          return responseApp({ "message": "Could not find user." }, 400)
        
      # Insert gallery
      dbResponse = db.galleries.insert_one(gallery)
      
      return responseApp({
          "message": "Gallery created", 
          "id": f"{dbResponse.inserted_id}"
        }, 200)
    except Exception as e:
      print(e)
      return responseApp({ "message": "Cannot create gallery" }, 400)

@api.route('/gallery/<id>')
class GalleryId(Resource):
  @jwtRequired
  def get(self, id, current_user):
    try:
      dbResponse = dict(db.galleries.find_one({"_id": ObjectId(id)}))
      
      dbResponse["_id"] = str(dbResponse["_id"])
      
      del dbResponse["password"]
      
      return responseApp(dbResponse, 200)
    except Exception as e:
      print(e)
      return responseApp({ "message": "Cannot read gallery" }, 400)
  
  @jwtRequired
  def patch(self, id, current_user):
    try:
      request = api.payload
      
      # Check for existing name
      if "name" in request:
        if db.galleries.find_one({ "name": request["name"] }):
          return responseApp({
            "message": "This name already in use",
          }, 400)
          
      if "admins" in request:
        request["admins"] = dict(request["admins"])
      
        # Checking if the amount of admins is between 1 and 2
        quant = len(request["admins"])
        if quant != 1 and quant != 2:
          return responseApp({
            "message": "The amount of admins to be 1 or 2",
          }, 400)
          
        # Checking if the admin exists as a gallery
        for key, value in request["admins"].items():
          if not db.users.find_one({"_id":  ObjectId(value)}):
            return responseApp({ "message": "Could not find user." }, 400)
          
      dbResponse = db.galleries.update_one(
        {"_id": ObjectId(id)},
        {"$set": request}
      )
      print(dbResponse.modified_count)
      if dbResponse.modified_count == 1:
        return responseApp({ 
          "message": "Gallery updated" 
        }, 200) 
        
      return responseApp({
        "message": "Nothing to update" 
      }, 404)
    except Exception as e:
      print(e)
      return responseApp({ "message": "Cannot update gallery" }, 400)
  
  @jwtRequired
  def delete(self, id, current_user):
    try:
      dbResponse = db.galleries.delete_one({ "_id": ObjectId(id) })
        
      if dbResponse.deleted_count == 1:
        return responseApp({ "message": "Gallery deleted" }, 200)
      
      return responseApp({ "message": "Gallery not found" }, 404)
    except Exception as e:
      print(e)
      return responseApp({ "message": "Cannot delete gallery" }, 500)