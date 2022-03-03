from functools import wraps
from flask import request, current_app

import jwt
from bson.objectid import ObjectId

from src.server.instance import server
from src.server.response import responseApp

app, api, db = server.app, server.api, server.db

def jwtRequired(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    token = None
    
    if 'authorization' in request.headers:
      token = request.headers['authorization']
      
    if not token:
      return responseApp(
        { "message": "You do not have permission to access this route" },
        403
      )
      
    if not "Bearer" in token:
      return responseApp({ "message": "Invalid Token" }, 401)
    
    try:
      token_pure = token.replace("Bearer ", "")
      decoded = jwt.decode(token_pure, app.secret_key, algorithms=['HS256'])
      current_user = dict(db.users.find_one({"_id": ObjectId(decoded["_id"])}))
      
      current_user["_id"] = str(current_user["_id"])
    except:
      return responseApp({ "message": "Invalid Token" }, 403)
    
    return f(current_user=current_user, *args, **kwargs)
  
  return wrapper