#!/usr/bin/python3.7

# Author: Ginger Fan
# Date:   Dec 4, 2020

import sys
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse
from flask_marshmallow import Marshmallow
import datetime
from sqlalchemy import or_
from sqlalchemy.dialects.mysql import TINYINT

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'hello :)'

# Connect to local mysql server
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://debian-sys-maint:KM5fObUGBIC3zEQ9@localhost/testdb"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ginger:"+sys.argv[1]+"@localhost/testdb"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ginger94090@localhost/testdb"
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
api = Api(app)
ma = Marshmallow(app)
parser = reqparse.RequestParser()


class ResponseData():
    STATUS_FAIL = 0
    STATUS_SUCCESS = 1

    CODE_LACK_OF_ESSENTIAL_COLUMN = 1  # 缺少必要欄位
    CODE_DATA_ALREADY_EXIST = 2       # 資料己存在
    CODE_DATABASE_ERROR = 3           # 資料庫或伺服器異常

    @classmethod
    def get(cls, status='', code='', message='', result=''):
        messageDict = {}
        messageDict[cls.CODE_LACK_OF_ESSENTIAL_COLUMN] = 'Lack of essential column'
        messageDict[cls.CODE_DATA_ALREADY_EXIST] = 'Data already exist'
        messageDict[cls.CODE_DATABASE_ERROR] = 'Database error'

        returnDict = {}
        returnDict.update({'status': status} if status != '' else {})
        returnDict.update({'code': code} if code != '' else {})
        returnDict.update(
            {'message': messageDict[code]} if code in messageDict else {})
        returnDict.update({'result': result} if result != '' else {})
        return returnDict

####### SCHEMA ##########


class User(db.Model):
    db.create_all()
    MAX_STRING_LENGTH = 120
    uid = db.Column(db.VARCHAR(MAX_STRING_LENGTH), primary_key=True)
    country = db.Column(db.VARCHAR(MAX_STRING_LENGTH))
    role = db.Column(db.VARCHAR(MAX_STRING_LENGTH))
    is_invited = db.Column(TINYINT, default=0)
    job_type = db.Column(db.VARCHAR(MAX_STRING_LENGTH))
    is_ddg_user = db.Column(TINYINT, default=0)
    is_ddb_user = db.Column(TINYINT, default=0)
    is_ddg_buy = db.Column(TINYINT, default=0)
    company_id = db.Column(db.VARCHAR(MAX_STRING_LENGTH))
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
        self.created_time = datetime.datetime.now()
        self.updated_time = datetime.datetime.now()

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


class Company(db.Model):
    MAX_STRING_LENGTH = 120
    company_id = db.Column(db.VARCHAR(MAX_STRING_LENGTH), primary_key=True)
    company_name = db.Column(db.VARCHAR(MAX_STRING_LENGTH))
    is_ddb_client = db.Column(TINYINT, default=0)
    is_erp_client = db.Column(TINYINT, default=0)
    created_time = db.Column(db.DateTime)
    updated_time = db.Column(db.DateTime)

    def __init__(self, company_id, company_name, is_ddb_client, is_erp_client,
                 created_time, updated_time):
        self.company_id = company_id if company_name != '' else ''
        self.company_name = company_name if company_name != '' else ''
        self.is_ddb_client = is_ddb_client if is_ddb_client != 0 else 0
        self.is_erp_client = is_erp_client if is_erp_client != 0 else 0
        self.created_time = created_time
        self.updated_time = updated_time

    def __repr__(self):
        return '<Company %r>' % self.company_id


class CompanySchema(ma.Schema):
    class Meta:
        fields = ("company_id", "company_name", "is_ddb_client",
                  "is_erp_client", "created_time", "updated_time")
        model = Company


class User_client(db.Model):
    db.create_all()
    MAX_STRING_LENGTH = 120
    uid = db.Column(db.VARCHAR(MAX_STRING_LENGTH), primary_key=True)
    cid = db.Column(db.VARCHAR(MAX_STRING_LENGTH))
    created_time = db.Column(db.DateTime)

    def __init__(self, uid, cid, created_time):
        self.uid = uid
        self.cid = cid
        self.created_time = datetime.datetime.now()

    def __repr__(self):
        return '<User_client %r>' % self.uid


####### SQL API ##########

class User_All(Resource):
    def get(self):
        try:
            posts = User.query.all()
            return ResponseData.get(status=ResponseData.STATUS_SUCCESS, result=posts_user.dump(posts))
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)


class Compnay_All(Resource):
    def get(self):
        try:
            posts = Company.query.all()
            return ResponseData.get(status=ResponseData.STATUS_SUCCESS, result=posts_company.dump(posts))
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)


class Company_detail(Resource):
    def get(self, idorname):
        try:
            post = db.session.query(Company).filter(
                or_(Company.company_id == idorname, Company.company_name == idorname)).first()
            return ResponseData.get(status=ResponseData.STATUS_SUCCESS, result=post_company.dump(post))
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)


class User_detail(Resource):
    def get(self, uid):
        try:
            post = db.session.query(User).filter_by(uid=uid).first()
            return ResponseData.get(status=ResponseData.STATUS_SUCCESS, result=post_user.dump(post))
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)


class User_One(Resource):
    def post(self):
        try:
            exists_user = db.session.query(User.uid).filter_by(
                uid=request.json['uid']).scalar() is not None

            if 'uid' not in request.json.keys():
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            if not request.json['uid'] or request.json['uid'] == " " or request.json['uid'].isspace()  :
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            new_post = User(
                uid=request.json['uid'],
                country=request.json['country'] if 'country' in request.json.keys(
                ) else '',
                role=request.json['role'] if 'role' in request.json.keys(
                ) else '',
                is_invited=request.json['is_invited'] if 'is_invited' in request.json.keys(
                ) else 0,
                job_type=request.json['job_type'] if 'job_type' in request.json.keys(
                ) else '',
                is_ddg_user=request.json['is_ddg_user'] if 'is_ddg_user' in request.json.keys(
                ) else 0,
                is_ddb_user=request.json['is_ddb_user'] if 'is_ddb_user' in request.json.keys(
                ) else 0,
                is_ddg_buy=request.json['is_ddg_buy'] if 'is_ddg_buy' in request.json.keys(
                ) else 0,
                company_id=request.json['company_id'] if 'company_id' in request.json.keys(
                ) else '',
                register_time=datetime.datetime.now(),
                created_time=datetime.datetime.now(),
                updated_time=datetime.datetime.now()
            )
            if exists_user:
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATA_ALREADY_EXIST)
            else:
                db.session.add(new_post)
                db.session.commit()
                result = {'uid': request.json['uid']}
                return ResponseData.get(status=ResponseData.STATUS_SUCCESS)
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)

    def put(self):
        try:
            if 'uid' not in request.json.keys():
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            if not request.json['uid'] or request.json['uid'] == " " or request.json['uid'].isspace() :
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            admin = User.query.filter_by(uid=request.json['uid']).first()
            for key in request.json.keys():
                if key == 'uid':
                    pass
                else:
                    setattr(admin, key, request.json[key])
                    db.session.commit()
            return ResponseData.get(status=ResponseData.STATUS_SUCCESS)
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)


class Company_One(Resource):
    def post(self):
        try:
            if 'company_name' not in request.json.keys():
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            if not request.json['company_name'] or request.json['company_name'] == " " or request.json['company_name'].isspace() :
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            cou = db.session.query(Company).count()+1
            num = 'company-'+str(cou)
            new_post = Company(
                company_id=num,
                company_name=request.json['company_name'],
                is_ddb_client=request.json['is_ddb_client'] if 'is_ddb_client' in request.json.keys(
                ) else 0,
                is_erp_client=request.json['is_erp_client'] if 'is_erp_client' in request.json.keys(
                ) else 0,
                created_time=datetime.datetime.now(),
                updated_time=datetime.datetime.now()
            )
            exists_company = db.session.query(Company.company_name).filter_by(
                company_name=request.json['company_name']).scalar() is not None

            if exists_company:
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATA_ALREADY_EXIST)
            else:
                db.session.add(new_post)
                db.session.commit()
                result = {'company_id': num}
                return ResponseData.get(status=ResponseData.STATUS_SUCCESS, result=result)
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)

    def put(self):
        try:
            if 'company_name' not in request.json.keys():
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            if not request.json['company_name'] or request.json['company_name'] == " " or request.json['company_name'].isspace():
                return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_LACK_OF_ESSENTIAL_COLUMN)
            admin = Company.query.filter_by(
                company_name=request.json['company_name']).first()
            for key in request.json.keys():
                if key == 'company_name':
                    pass
                else:
                    setattr(admin, key, request.json[key])
                    db.session.commit()
            return ResponseData.get(status=ResponseData.STATUS_SUCCESS)
        except:
            return ResponseData.get(status=ResponseData.STATUS_FAIL, code=ResponseData.CODE_DATABASE_ERROR)


if __name__ == "__main__":

    post_user = UserSchema()
    posts_user = UserSchema(many=True)

    post_company = CompanySchema()
    posts_company = CompanySchema(many=True)

    db.create_all()
    api.add_resource(User_One, '/user')
    api.add_resource(User_detail, '/user/<uid>')
    api.add_resource(User_All, '/user/list')

    api.add_resource(Company_One, '/company')
    api.add_resource(Company_detail, '/company/<idorname>')
    api.add_resource(Compnay_All, '/company/list')

    app.run(debug=True, host='0.0.0.0', port=8888)
