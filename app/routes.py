from flask import Blueprint, jsonify
from app.models import User

main  = Blueprint('main', __name__)
################################################################################################################
@main.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()  # 查詢所有用戶
    result = []
    for user in users:  # 將資料轉換為 JSON 格式
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    return jsonify(result)  # 返回 JSON 格式的結果

@main.route('/')
def hello_world():
  return "Hello, World! Flask connected to MySQL!"
################################################################################################################