from flask import Flask

app = Flask(__name__)

# default 
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'hello :)'

# add user
@app.route('/add_user/')
def add_user():
    return

# update user


# get user list 

# get user profile



#post /store data: {name :}
@app.route('/store')
def get_stores():
    return 'hi'


#post /store/<name> data: {name :}/item
@app.route('/store/<string:name>/item' )
def create_item_in_store(name):
    return name

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8888)