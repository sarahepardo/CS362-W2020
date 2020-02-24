import unittest


class MyTestCase(unittest.TestCase):
    def test__init__(self,id,first_name,last_name):
        s = Student(123,"Sara","Smith")
        self.assert_(self)
        self.assertEqual(id, 123)
        self.assertTrue(first_name,"Sara")
        self.assertTrue(last_name,"Smith")

    def test_get_full_name(self):
        fn = "Frankie Nickles"
        self.assertTrue(first_name,"Frankie")
        self.assertTrue(last_name,"Nickels")

    def test_submit_assignment(self,assignment):
        self.assertContains(assignment)

    #def test_get_assignments(self):
    #def test_get_assignment(self,name):
    #def test_get_average(self):
    #def test_submit_assignment(self,assignment):
    #def test_remove_assignment(self):







if __name__ == '__main__':
    unittest.main()
