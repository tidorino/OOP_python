from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def test_student_initialization_with_courses(self):
        courses = {'Python Advance': ['note1', 'note2']}
        student = Student('Student', courses)
        self.assertEqual('Student', student.name)
        self.assertEqual(courses, student.courses)

    def test_student_initialization_without_courses(self):
        courses = {}
        student = Student('Student', courses)
        self.assertEqual(courses, student.courses)

    def test_enroll__student_updates_course_notes_when_course_name_already_enrolled(self):
        course_name = 'Python Advance'
        courses = {course_name: ['note1', 'note2']}
        student = Student('Student', courses)

        result = student.enroll(course_name, ['note3', 'note4'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note1', 'note2', 'note3', 'note4'], student.courses[course_name])

    def test_enroll__student_add_new_course_and_notes_when_add_course_note_is_y(self):

        courses = {}
        student = Student('Student', courses)

        result = student.enroll('Python OOP', ['note3', 'note4'], 'Y')

        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue('Python OOP' in student.courses)
        self.assertEqual(['note3', 'note4'], student.courses['Python OOP'])

    def test_enroll__student_add_new_course_and_notes_when_add_course_note_empty_string_or_null(self):

        courses = {}
        student = Student('Student', courses)

        result = student.enroll('Python OOP', ['note3', 'note4'], '')

        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue('Python OOP' in student.courses)
        self.assertEqual(['note3', 'note4'], student.courses['Python OOP'])

    def test_enroll__student_add_new_course_to_courses_dict_if_adds_notes_are_different_y_or_empty_str(self):

        courses = {}
        student = Student('Student', courses)

        result = student.enroll('Python OOP', ['note1'], 'M')

        self.assertEqual('Course has been added.', result)
        self.assertTrue('Python OOP' in student.courses)
        self.assertEqual([], student.courses['Python OOP'])

    def test_add_notes__student_add_course_notes_if_course_name_already_in_dict(self):
        course_name = 'Python Advance'
        courses = {course_name: ['note1']}
        student = Student('Student', courses)

        result = student.add_notes(course_name, 'note3')

        self.assertEqual("Notes have been updated", result)
        self.assertTrue(course_name in student.courses)
        self.assertEqual(['note1', 'note3'], student.courses[course_name])

    def test_add_notes__student_cannot_add_course_notes_if_course_name_not_in_dict_expect_to_raise(self):
        course_name = 'Python Advance'
        courses = {}
        student = Student('Student', courses)

        with self.assertRaises(Exception) as ex:
            student.add_notes(course_name, 'note3')
        self.assertEqual('Cannot add notes. Course not found.',  str(ex.exception))
        self.assertEqual({}, student.courses)

    def test_leave_course__student_remove_course_if_course_name_already_in_dict(self):
        course_name = 'Python Advance'
        courses = {course_name: []}
        student = Student('Student', courses)
        self.assertTrue(course_name in student.courses)

        result = student.leave_course(course_name)

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, student.courses)

    def test_leave_course__when_course_not_exists_expect_to_raise(self):
        course_name = 'Python Advance'
        courses = {course_name: []}
        student = Student('Student', courses)

        with self.assertRaises(Exception) as ex:
            student.leave_course('Python OOP')
        self.assertEqual('Cannot remove course. Course not found.',  str(ex.exception))
        self.assertEqual({course_name: []}, student.courses)


if __name__ == '__main__':
    main()
