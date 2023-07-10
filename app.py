from flask import Flask ,render_template, redirect, url_for, jsonify
from wtform_c import *
from model import * 
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager, login_user, current_user,  login_required, logout_user
from flask_socketio import SocketIO, send, join_room, leave_room
import time

app = Flask(__name__)
app.secret_key="replace_later"

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://hello_chat_database_user:vXIZVffkLlvKnfpJlt2ghOc5qFLfViu8@dpg-ciil4liip7vpels24nrg-a.oregon-postgres.render.com/hello_chat_database'
# db = SQLAlchemy(app)
db.init_app(app)

socketio= SocketIO(app)

# Predefined rooms for chat
ROOMS = ["lounge", "news", "games", "coding"]

# default
# flask-login ki jagah manage session bhi use kar sakte hai
login_man= LoginManager()
login_man.init_app(app)

@login_man.user_loader
def load_user(id):
    return User.query.get(int(id))
# id lene ke liye , query and filterby wala bhi use kar sakte yha

@app.route('/get_table_data', methods=['GET'])
def get_table_data():
    # Retrieve table data from the database
    table_data = retrieve_table_data_from_database()

    # Convert table data to JSON format
    json_data = jsonify(table_data)

    # Return the JSON response
    return json_data

def retrieve_table_data_from_database():
    # Code to retrieve the table data from the database
    # You can use your preferred database library here
    # Example using SQLAlchemy:
    table_data = message_history.query.all()
    print(table_data)
    return table_data



@app.route('/',methods =["GET","POST"])
def hello_world():
    form=Registrationform()
    if form.validate_on_submit():
        username= form.username.data
        password= form.password.data

        hashed_pswd= pbkdf2_sha256.hash(password)

        # # check username
        # user_object = User.query.filter_by(username=username).first()      ab jarurat nhi wtform me custom validator lga diye
        # if user_object:
        #     return "someone else has taken this"
        
        user1= User(username=username,password=hashed_pswd)
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('index.html',form=form)

@app.route('/login', methods=["GET","POST"])
def login():
    lform= LoginForm()
    if lform.validate_on_submit():
        user_object = User.query.filter_by(username=lform.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))
        # # login user lo current_user ke naam se use karte hai
        # if current_user.is_authenticated:                   --------authenticated use kyuki undermixin use kiye hai model.py me
        #    return "login successfully with flask login"
        
        
    
    return render_template('login.html',form=lform)


@app.route('/chat', methods=["GET","POST"])
@login_required
def chat():
    # restrict karne ke liye sirf login wale log hi access kare ya to login_required func lagao ya phir current_user.is_authenticated
    # if current_user.is_authenticated:                   --------authenticated use kyuki undermixin use kiye hai model.py me
        #    return "chat"
    # chat_object= message_history.query.filter_by(sender="user6").first()
    # chat_object= message_history.query.all()
    # json_data = jsonify(chat_object)
    # print(chat_object[1].message)
    # return render_template('chat.html',username=current_user.username, rooms=ROOMS, sender=chat_object.sender, message=chat_object.message, room=chat_object.room)
    return render_template('chat.html', username=current_user.username, rooms=ROOMS )

@app.route('/logout',methods=["GET"])
def logout():
    logout_user()
    return "logout sucessfully"

@socketio.on('incoming-msg')
def on_message(data):
    """Broadcast messages"""

    msg = data["msg"]
    username = data["username"]
    room = data["room"]
    # Set timestamp
    time_stamp = time.strftime('%b-%d %I:%M%p', time.localtime())
    send({"username": username, "msg": msg, "time_stamp": time_stamp}, room=room)

    # storing in database
    msg_history= message_history(sender=username,message=msg,room=room)
    db.session.add(msg_history)
    db.session.commit()


@socketio.on('join')
def on_join(data):
    """User joins a room"""

    username = data["username"]
    room = data["room"]
    join_room(room)

    # Broadcast that new user has joined
    send({"msg": username + " has joined the " + room + " room."}, room=room)


@socketio.on('leave')
def on_leave(data):
    """User leaves a room"""

    username = data['username']
    room = data['room']
    leave_room(room)
    send({"msg": username + " has left the room"}, room=room)


if __name__ == '__main__':
    app.run(debug=True)