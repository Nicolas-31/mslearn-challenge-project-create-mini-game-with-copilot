import unittest
import app  # Import your main application file

class TestApp(unittest.TestCase):
    def test_determine_winner(self):
        self.assertEqual(app.determine_winner('rock', 'scissors'), 'user')
        self.assertEqual(app.determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(app.determine_winner('rock', 'rock'), 'tie')
        
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            app.determine_winner('invalid', 'rock')

if __name__ == "__main__":
    unittest.main()