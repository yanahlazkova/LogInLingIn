from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Разрешает CORS (совместное использование ресурсов между источниками) для всех маршрутов
CORS(app)

@app.route('/', methods=['POST'])
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


if __name__ == '__main__':
    app.run(debug=True)
