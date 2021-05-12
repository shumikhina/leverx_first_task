class Joiner:

    @staticmethod
    def join_rooms_with_students(rooms: list, students: list) -> dict:
        result = {room['id']: {**room, 'students': []} for room in rooms}
        for student in students:
            result[student['room']]['students'].append(student)
        return result
