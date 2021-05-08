import json
import xml.etree.cElementTree as xml
import constants


class Printer:

    def _choose_format(self):
        choice = None
        formats = {
            '1': self.save_json,
            '2': self.save_xml
        }
        while choice not in formats:
            choice = input(constants.Choice_format)
        return formats[choice]

    @staticmethod
    def save_json(data):
        with open('file.json', 'w') as file:
            json.dump(data, file)

    @staticmethod
    def save_xml(data):
        root = xml.Element('Rooms')
        for room in data:
            room_element = xml.SubElement(root, 'Room')
            xml.SubElement(room_element, 'Id').text = str(room['id'])
            xml.SubElement(room_element, 'Name').text = str(room['name'])
            students = xml.SubElement(room_element, 'Students')
            for student in room['students']:
                student_element = xml.SubElement(students, 'Student')
                xml.SubElement(student_element, 'Id').text = str(student['id'])
                xml.SubElement(student_element, 'Name').text = student['name']
                xml.SubElement(student_element, 'Room').text = str(student['room'])
        file_xml = xml.ElementTree(root)
        file_xml.write('file.xml')

    def save_file(self, data: list) -> None:
        chosen_format = self._choose_format()
        chosen_format(data)
