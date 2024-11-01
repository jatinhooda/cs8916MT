from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to act as a "database"
students = []

# Endpoint to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Endpoint to retrieve a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    return jsonify(student) if student else ('Student not found', 404)

# Endpoint to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

# Endpoint to update an existing student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        data = request.get_json()
        student.update(data)
        return jsonify(student)
    else:
        return ('Student not found', 404)

# Endpoint to delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run()
