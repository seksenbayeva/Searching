from flask import Flask, jsonify, render_template
import json
app = Flask(__name__)

# Функция для загрузки данных из JSON-файла
def load_data():
    with open('emp.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Маршрут для отображения страницы сотрудников
@app.route('/')
def index():
    return render_template('index.html')  # Отобразить HTML-шаблон из папки templates

# Маршрут для получения всех сотрудников
@app.route('/get_employees_json')
def get_employees_json():
    try:
        with open('emp.json', 'r', encoding='utf-8') as file:
            employees_data = json.load(file)
        return jsonify(employees_data)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

# Маршрут для получения информации о конкретном сотруднике по ID
@app.route('/employee/<int:employee_id>')
def employee(employee_id):
    return render_template('employee.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
