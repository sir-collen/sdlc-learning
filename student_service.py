class StudentService:

    def __init__(self):
        self.students = []

    def register_student(self, name, phone):

        if not phone:
            raise ValueError("Phone number cannot be empty")

        for student in self.students:
            if student["phone"] == phone:
                raise ValueError("Phone number already exists")

        self.students.append({
            "name": name,
            "phone": phone
        })

        return True