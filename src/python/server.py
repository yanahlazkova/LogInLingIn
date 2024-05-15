from flask import Flask, request, jsonify
from flask_cors import CORS
import json

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

        # Обрабатываем данные, например, проверяем их
        print(f"email: {email}\npassword: {password}")
        if email == 'ecovod2003@ukr.net' and password == '111':
            print("success!!!")
            save_data()
            return jsonify({'success': True, 'message': 'SignUp successful'}), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid email or password'})


def save_data():
    if request.method == 'POST':
        data = request.json  # Получаем данные в формате JSON из запроса
        # Сохраняем полученные данные в файле на сервере
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return jsonify({'message': 'Data saved successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
