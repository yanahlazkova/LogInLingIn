import os.path

from flask import Flask, request, jsonify
from flask_cors import CORS
import json

file_json = 'users.json'

app = Flask(__name__)
# Разрешает CORS (совместное использование ресурсов между источниками) для всех маршрутов
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Получаем данные из тела POST-запроса
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # Обрабатываем данные, например, проверяем их
        print(f"email: {email}\npassword: {password}")
        if email == 'ecovod2003@ukr.net' and password == '111':
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
        if name and email and password:
            # Извлекаем данные из файла JSON
            users_data = extract()

            if len(users_data):
                exists_email = check_data(users_data, email)
                print("exitst_email", len(exists_email))
                if len(exists_email) == 0:
                    # Создаем новый словарь с данными пользователя
                    user_data = {'email': email, 'name': name, 'password': password}

                    # Добавляем нового пользователя в список
                    users_data.append(user_data)

                    # Сохраняем обновленные данные в файл JSON
                    with open(file_json, 'w') as file:
                        json.dump(users_data, file)

                    return jsonify({'message': 'Data saved successfully'}), 200
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
            # users_json = json.loads(users_data)
            print("extract: ", users_data)

    return users_data


def check_data(users_data, search_email):
    print("check: ", users_data)
    filtered_data = filter(lambda user: user['email'] == search_email, users_data)
    print("filtered", list(filtered_data))
    return list(filtered_data)


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
