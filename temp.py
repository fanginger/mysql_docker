from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource ,reqparse
from flask_marshmallow import Marshmallow 
# from flask_restful import reqparse

app = Flask(__name__)

# 連線到本機端mysql server
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ginger94090@127.0.0.1/testdb"
db = SQLAlchemy(app)
api = Api(app) 
ma = Marshmallow(app)

parser = reqparse.RequestParser()




class user(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     uid = db.Column(db.String(120))
     country = db.Column(db.String(120))
     # role = db.Column(db.String(120))
     # is_invited = db.Column(db.Integer,default=0)
     # job_type = db.Column(db.String(120))
     # is_ddg_user = db.Column(db.Integer,default=0)
     # is_ddb_user = db.Column(db.Integer,default=0)
     # is_ddg_buy = db.Column(db.Integer,default=0)
     # company_id = db.Column(db.String(120))
     # register_time = db.Column(db.DateTime)
     # created_time = db.Column(db.DateTime)
     # updated_time = db.Column(db.DateTime)
     def __init__(self,uid,country):
#      def __init__(self,uid,country,role,is_invited,job_type,is_ddg_user,is_ddb_user,is_ddg_buy,\
# company_id,register_time,created_time,updated_time):
               self.uid = uid
               self.country = country
               #   self.role = role
               #   self.is_invited = is_invited
               #   self.job_type = job_type
               #   self.is_ddg_user = is_ddg_user
               #   self.is_ddb_user = is_ddb_user
               #   self.is_ddg_buy = is_ddg_buy
               #   self.company_id = company_id
               #   self.register_time = register_time
               #   self.created_time = created_time
               #   self.updated_time = updated_time
               
     def __repr__(self):
             return '<User %r>' % self.uid

class UserSchema(ma.Schema):
        class Meta:
#             fields = ("id", "uid,country","role","is_invited","job_type","is_ddg_user","is_ddb_user","is_ddg_buy",\
# "company_id","register_time","created_time","updated_time")
          fields = ('id','uid','country')
          model = user

post_user = UserSchema()
posts_user = UserSchema(many=True)

class User_All(Resource):
     db.create_all()
     def get(self):
          posts = user.query.all()
          return {'status': '0',
            'data': posts_user.dump(posts)
          }
     # def get(self, uid):
     #      post = user.query.get_or_404(uid)

     #      return post_user.dump(post)
     # def post(self):
     #      parser.add_argument('uid', required=True, help='status:1, uid  is required')
     #      args = parser.parse_args()
     #      new_post = user(
     #      # uid=request.json['uid'],
     #      uid = args['uid'],
     #      country=request.json['country'],
     #      )
     #      db.session.add(new_post)
     #      db.session.commit()
     #      return {
     #        'status': '0',
     #        'data': post_user.dump(new_post)
     #      }
          # return post_user.dump(new_post)

# api.add_resource(UserResource, '/user/<string:uid>')
# api.add_resource(UserResource, '/user/',endpoint='s')
api.add_resource(User_All, '/user/list/',endpoint='userlist')



class User_One(Resource):
     def post(self):
          parser.add_argument('uid', required=True, help='status:1, uid  is required')
          args = parser.parse_args()
          new_post = user(
          # uid=request.json['uid'],
          uid = args['uid'],
          country=request.json['country'],
          )
          db.session.add(new_post)
          db.session.commit()
          return {
          'status': '0',
          'data': post_user.dump(new_post)
          }
     # def put(self):

api.add_resource(User_One, '/user/',endpoint='user')

if __name__ == "__main__":
         app.run(debug=True)