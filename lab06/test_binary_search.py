import unittest
from Binary_Search import Student, binary_search


class TestStudent(unittest.TestCase):
    """Test cases for the Student class"""

    def setUp(self):
        """Create test student objects"""
        self.student1 = Student(1, "Alice", 3.8)
        self.student2 = Student(2, "Bob", 3.5)
        self.student3 = Student(3, "Charlie", 4.0)

    def test_student_initialization(self):
        """Test that student is initialized with correct values"""
        self.assertEqual(self.student1.get_name(), "Alice")
        self.assertEqual(self.student1.get_ID(), 1)
        self.assertEqual(self.student1.get_GPA(), 3.8)

    def test_student_get_name(self):
        """Test get_name method"""
        self.assertEqual(self.student1.get_name(), "Alice")
        self.assertEqual(self.student2.get_name(), "Bob")

    def test_student_get_id(self):
        """Test get_ID method"""
        self.assertEqual(self.student1.get_ID(), 1)
        self.assertEqual(self.student3.get_ID(), 3)

    def test_student_get_gpa(self):
        """Test get_GPA method"""
        self.assertAlmostEqual(self.student1.get_GPA(), 3.8)
        self.assertEqual(self.student3.get_GPA(), 4.0)


class TestBinarySearch(unittest.TestCase):
    """Test cases for the binary_search function"""

    def setUp(self):
        """Create a sorted list of students for testing"""
        self.students = [
            Student(1, "Alice", 3.8),
            Student(2, "Bob", 3.5),
            Student(3, "Charlie", 4.0),
            Student(4, "Diana", 3.9),
            Student(5, "Eve", 3.7),
        ]
        # Sort by name as the main function does
        self.students.sort(key=lambda x: x.get_name())

    def test_binary_search_found_first(self):
        """Test finding the first element"""
        result, comparisons, index = binary_search(self.students, "Alice")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_name(), "Alice")
        self.assertEqual(index, 0)

    def test_binary_search_found_last(self):
        """Test finding the last element"""
        result, comparisons, index = binary_search(self.students, "Eve")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_name(), "Eve")
        self.assertEqual(index, 4)

    def test_binary_search_found_middle(self):
        """Test finding a middle element"""
        result, comparisons, index = binary_search(self.students, "Charlie")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_name(), "Charlie")

    def test_binary_search_not_found(self):
        """Test when element is not found"""
        result, comparisons, index = binary_search(self.students, "Zack")
        self.assertIsNone(result)
        self.assertEqual(index, -1)

    def test_binary_search_comparisons_single_element(self):
        """Test that comparisons are counted correctly with single element"""
        single_student = [Student(1, "Alice", 3.8)]
        result, comparisons, index = binary_search(single_student, "Alice")
        self.assertIsNotNone(result)
        self.assertEqual(comparisons, 1)

    def test_binary_search_empty_list(self):
        """Test binary search with empty list"""
        result, comparisons, index = binary_search([], "Alice")
        self.assertIsNone(result)
        self.assertEqual(index, -1)

    def test_binary_search_case_sensitive(self):
        """Test that search is case-sensitive"""
        result, comparisons, index = binary_search(self.students, "alice")
        self.assertIsNone(result)  # Should not find "alice" (lowercase)

    def test_binary_search_returns_student_object(self):
        """Test that the returned object is a Student instance"""
        result, comparisons, index = binary_search(self.students, "Bob")
        self.assertIsInstance(result, Student)

    def test_binary_search_comparisons_logged(self):
        """Test that comparisons count is greater than 0 when searching"""
        result, comparisons, index = binary_search(self.students, "Bob")
        self.assertGreater(comparisons, 0)


class TestBinarySearchEdgeCases(unittest.TestCase):
    """Test edge cases for binary search"""

    def test_search_with_duplicate_names(self):
        """Test binary search behavior with duplicate names"""
        students = [
            Student(1, "Alice", 3.8),
            Student(2, "Alice", 3.5),
            Student(3, "Bob", 4.0),
        ]
        students.sort(key=lambda x: x.get_name())
        result, comparisons, index = binary_search(students, "Alice")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_name(), "Alice")

    def test_search_with_special_characters(self):
        """Test binary search with special characters in names"""
        students = [
            Student(1, "Alice-Marie", 3.8),
            Student(2, "Bob O'Brien", 3.5),
        ]
        students.sort(key=lambda x: x.get_name())
        result, comparisons, index = binary_search(students, "Bob O'Brien")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_name(), "Bob O'Brien")


if __name__ == "__main__":
    unittest.main()
