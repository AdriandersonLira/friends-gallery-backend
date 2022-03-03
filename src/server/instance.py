from flask import Flask
from flask_restx import Api
from pymongo import MongoClient

class Server():
  def __init__(self):
    self.app = Flask(__name__)
    self.app.secret_key = b'\x8d*\xf1u\xef\xa5\x13P\x1e\xe48\x13\xfeZ\x03\x13'
    self.api = Api(self.app, 
      version='1.0',
      title='Sample Friends Gallery API',
      description='A sample friends gallery API',
      doc='/docs'
    )
    try:
      self.client = MongoClient('mongodb://localhost:27017/')
      self.db = self.client["gallery"]
    except:
      print("ERROR - Cannot connect to db")
    
  def run(self):
    self.app.run(
      debug=True
    )
    
server = Server()
