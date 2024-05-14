from flask import Flask, request
# url = "https://jsonplaceholder.typicode.com/users"
# respons = requests.get(url)
# if respons.status_code == 200:
#     data = respons.json()
#     for user in data:
#         print("=================\n")
#         print(user['name'], " = ", user['username'])
# else:
#     print("Request failed: ", respons.status_code)

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        # Получаем данные из POST-запроса
        email = request.form['email']
        password = request.form['password']

        # Теперь можно обработать эти данные или выполнить другие действия
        
        return f'Email: {email}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)
