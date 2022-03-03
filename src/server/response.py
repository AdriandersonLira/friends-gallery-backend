from flask import Response
import json

def responseApp(data, statusCode=200):
  return Response(
    response=json.dumps(data),
    status=statusCode,
    mimetype="application/json"
  )