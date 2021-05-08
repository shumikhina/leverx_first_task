from loader import Loader
from joiner import Joiner
from printer import Printer
import constants


class Controller:

    def process_files(self):
        rooms_data = Loader.read_file(constants.Path_rooms)
        students_data = Loader.read_file(constants.Path_students)
        result_data = Joiner.join_rooms_with_students(rooms_data, students_data)
        Printer().save_file(result_data)
