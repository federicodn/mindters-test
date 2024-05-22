from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/search_user', methods=['GET'])
def search_user():
    user_id = request.args.get('user_id')
    conn = get_db_connection()
    cur = conn.execute('select * from users where user_id = ?', [user_id])
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user is None:
        return jsonify({'error_message': f'No user with id {user_id}',
                        'error_code': 'xxxx'})

    return jsonify({"name": user['user_name'],
                    "age": user['user_age']})