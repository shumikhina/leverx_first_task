class Joiner:

    @staticmethod
    def join_rooms_with_students(rooms: list, students: list) -> list:
        result = []
        for room in rooms:
            result.append({**room, 'students': [student for student in students if student['room'] == room['id']]})
        return result
