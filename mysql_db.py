from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource 

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ginger94090@localhost/testdb"
db = SQLAlchemy(app)
api = Api(app) # new



class company(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        company_id = db.Column(db.String(120))
        #  is_ddb_client = db.Column(db.Integer,default=0)
        #  is_erp_client = db.Column(db.Integer,default=0)
        #  created_time = db.Column(db.Integer,default=0)
        #  updated_time = db.Column(db.Integer,default=0)
        def post(self):
            new_post = Post(
                company_id=request.json['company_id'],
            )
            db.session.add(new_post)
            db.session.commit()
            # return post_schema.dump(new_post)

        def __init__(self,company_id):
                 self.company_id = company_id
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

from flask_marshmallow import Marshmallow # new

ma = Marshmallow(app) # new

class PostSchema(ma.Schema):
        class Meta:
            fields = ("id", "username", "email")
            model = User

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

class com(Resource):
        def get(self):
            posts = User.query.all()
            return posts_schema.dump(posts)
        def post(self):
            new_post = User(
            username=request.json['username'],
            email=request.json['email']
            )
            db.session.add(new_post)
            db.session.commit()
            return post_schema.dump(new_post)

api.add_resource(com, '/posts/')
if __name__ == "__main__":
         app.run(debug=True)

# class test(db.Model):
#          id = db.Column(db.Integer, primary_key=True)
#          test = db.Column(db.String(80), unique=True)
#          def __init__(self, test):
#              self.test = test
        

# class PostCompany(Resource):
#     # new
#     def post(self):
#         new_post = company(
#             company_idt =request.json['company_id'],
#             # content=request.json['content']
#         )
#         db.session.add(new_post)
#         db.session.commit()
#         return post_schema.dump(new_post)

# api.add_resource(PostListResource, '/posts')


# admin2 = User('admin3', 'admin@example.com4')

# db.create_all() # In case user table doesn't exists already. Else remove it.    

# db.session.add(admin2)

# db.session.commit() # This is needed to write the changes to database

# User.query.all()

# tes2 = test('dafdsf')
# db.create_all()
# db.session.add(tes2)
# db.session.commit()
# test.query.all()


