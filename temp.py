#!/usr/bin/python3.7

from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse
from flask_marshmallow import Marshmallow
import datetime

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'hello :)'


# 連線到本機端mysql server
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://debian-sys-maint:CEvAKvyX4MorUjFO@localhost/testdb"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ginger94090@localhost/testdb"
db = SQLAlchemy(app)
db.init_app(app)
api = Api(app)
ma = Marshmallow(app)
parser = reqparse.RequestParser()

####### SCHEMA ##########
class User(db.Model):
    uid = db.Column(db.String(120), primary_key=True)
    country = db.Column(db.String(120))
    role = db.Column(db.String(120))
    is_invited = db.Column(db.Integer, default=0)
    job_type = db.Column(db.String(120))
    is_ddg_user = db.Column(db.Integer, default=0)
    is_ddb_user = db.Column(db.Integer, default=0)
    is_ddg_buy = db.Column(db.Integer, default=0)
    company_id = db.Column(db.String(120))
    register_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime)
    updated_time = db.Column(db.DateTime)

    def __init__(self, uid, country, role, is_invited, job_type, is_ddg_user,
                 is_ddb_user, is_ddg_buy, company_id, register_time, created_time, updated_time):
        self.uid = uid
        self.country = country
        self.role = role
        self.is_invited = is_invited
        self.job_type = job_type
        self.is_ddg_user = is_ddg_user
        self.is_ddb_user = is_ddb_user
        self.is_ddg_buy = is_ddg_buy
        self.company_id = company_id
        self.register_time = register_time
        self.created_time = created_time
        self.updated_time = updated_time

    def __repr__(self):
        return '<User %r>' % self.uid

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "uid", 
            "country", 
            "role", 
            "is_invited", 
            "job_type",
            "is_ddg_user", 
            "is_ddb_user", 
            "is_ddg_buy", 
            "company_id", 
            "register_time", 
            "created_time", 
            "updated_time")
        model = User


class company(db.Model):
    MAX_STRING_LENGTH = 120
    company_id = db.Column(db.String(MAX_STRING_LENGTH), primary_key=True)
    company_name = db.Column(db.String(MAX_STRING_LENGTH))
    is_ddb_client = db.Column(db.Integer, default=0)
    is_erp_client = db.Column(db.Integer, default=0)
    created_time = db.Column(db.DateTime)
    updated_time = db.Column(db.DateTime)

    def __init__(self, company_id, company_name, is_ddb_client, is_erp_client,
                 created_time, updated_time):
        self.company_id = company_id
        self.company_name = company_name
        self.is_ddb_client = is_ddb_client
        self.is_erp_client = is_erp_client
        self.created_time = created_time
        self.updated_time = updated_time

    def __repr__(self):
        return '<Company %r>' % self.company_id

class CompanySchema(ma.Schema):
    class Meta:
        fields = ("company_id", "company_name", "is_ddb_client",
                  "is_erp_client", "created_time", "updated_time")
        model = company



####### SQL API ##########

class User_All(Resource):
    db.create_all()

    def get(self):
        posts = User.query.all()
        return {'status': '1',
                'result': posts_user.dump(posts)
                }


class Compnay_All(Resource):
    db.create_all()

    def get(self):
        posts = company.query.all()
        return {
            'status': '1',
            'result': posts_company.dump(posts)
        }

class User_One(Resource):
    def post(self):
        exists_company = db.session.query(user.uid).filter_by(
            uid=request.json['uid']).scalar() is not None

        new_post = user(
            uid=request.json['uid'],
            country=request.json['country'],
            role=request.json['role'],
            is_invited=request.json['is_invited'],
            job_type=request.json['job_type'],
            is_ddg_user=request.json['is_ddg_user'],
            is_ddb_user=request.json['is_ddb_user'],
            is_ddg_buy=request.json['is_ddg_buy'],
            company_id=request.json['company_id'],
            register_time=datetime.datetime.now(),
            created_time=datetime.datetime.now(),
            updated_time=datetime.datetime.now()
        )
        print(posts_user.dump(user.query.all()))
        if exists_company:
            return {
                'status': '0',
                'code': '2',
                'message': 'data already exsits'}
        else:
            db.session.add(new_post)
            db.session.commit()
            return {
                'status': '1'}

class Company_One(Resource):
    def post(self):
        # 1. 先辦別是否有 company_id
        # default 值
        # 2. 判別資料是否重複
        # 3. 防止資料data injection

        # for key in request.json.keys():
        #     print(key)
        # exists = db.session.query(company.company_id).filter_by(company_id=request.json['company_id']).scalar() is not None
        # print(exists)
        if 'company_id' in request.json.keys():
            return {
                'status': '0',
                'code': '1',
                'message': 'no company_id'
            }
        new_post = company(
            company_id=request.json['company_id'],
            company_name=request.json['company_name'],
            is_ddb_client=request.json['is_ddb_client'],
            is_erp_client=request.json['is_erp_client'],
            created_time=datetime.datetime.now(),
            updated_time=datetime.datetime.now()
        )
        exists_company = db.session.query(company.company_id).filter_by(
            company_id=request.json['company_id']).scalar() is not None

        if exists_company:
            return {
                'status': '0',
                'code': '2',
                'message': '資料已存在'}
        else:
            db.session.add(new_post)
            db.session.commit()
            return {
                'status': '1',
                'result': post_company.dump(request.json['company_id'])
            }

if __name__ == "__main__":
    post_user = UserSchema()
    posts_user = UserSchema(many=True)

    post_company = CompanySchema()
    posts_company = CompanySchema(many=True)

    api.add_resource(User_One, '/user/', endpoint='user')
    api.add_resource(Company_One, '/company/', endpoint='company')
    api.add_resource(Compnay_All, '/company/list/', endpoint='companylist')
    # api.add_resource(UserResource, '/user/<string:uid>')
    api.add_resource(User_All, '/user/list/', endpoint='userlist')

    app.run(debug=True, host='0.0.0.0', port=80)
