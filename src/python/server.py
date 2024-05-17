import os.path
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

file_json = 'users.json'

app = Flask(__name__)
# Разрешает CORS (совместное использование ресурсов между источниками) для всех маршрутов
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


@app.route('/user_data', methods=['GET'])
def get_data():
    print("get_data")
    email = request.args.get('email')
    password = request.args.get('password')
    users_data = extract()
    user = next((user for user in users_data if user['email'] == email and user['password'] == password), None)
    if user:
        data = {
            'message': 'Hello from Flask!',
            'status': 'success',
            'user': user
        }
    else:
        data = {
            'message': 'Unauthorized',
            'status': 'fail'
        }
    return jsonify(data)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Получаем данные из тела POST-запроса
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # Обрабатываем данные, например, проверяем их
        print(f"email: {email}\npassword: {password}")

        if check_email(email, password):
            print("success!!!")
            return jsonify({'success': True, 'message': 'Login successful'}), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid email or password'})


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        # Получаем данные из тела POST-запроса
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        print(f"email: {email}\npassword: {password}")

        if name and email and password:
            exist_email, users_data = check_email(email)
            if not exist_email:
                # Создаем новый словарь с данными пользователя
                user_data = {'email': email, 'name': name, 'password': password}

                # Добавляем нового пользователя в список
                users_data.append(user_data)
                # Сохраняем обновленные данные в файл JSON
                with open(file_json, 'w') as file:
                    json.dump(users_data, file, indent=4)

                return jsonify({'success': True, 'message': 'Data saved successfully'}), 200
            else:
                return jsonify({'error': 'Пользователь с указанным email уже существует'})
        else:
            return jsonify({'error': 'Ошибка на стороне пользователя'})


def extract():
    users_data = []
    # Получаем данные из json
    if os.path.exists(file_json):
        with open(file_json, 'r') as f:
            users_data = json.load(f)
            # print("extract: ", users_data)
    return users_data


def check_email(email_to_check, password=None):
    """ проверка на существование в базе email """
    users_data = extract()
    for user in users_data:
        if user.get('email') == email_to_check:
            # print("user.get('email'), user.get('password')", user.get('email'), user.get('password'))
            if password:
                return user.get('password') == password
            return True, None
    return False, users_data


def show_data():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    user_data = {'email': email, 'name': name, 'password': password}
    print("user_data", user_data)
    users_data = json.dumps(user_data)
    print("users_data", users_data)
    user_from_json = json.loads(users_data)
    print("user_from_json", type(user_from_json))


if __name__ == '__main__':
    app.run(debug=True)
