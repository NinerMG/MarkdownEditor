import unittest
import subprocess

class TestMarkdownOutput(unittest.TestCase):
    def test_output_contains_expected_lines(self):
        result = subprocess.run(["python", "stage1.py"], capture_output=True, text=True)
        output = result.stdout

        self.assertIn("# The Beatles Favorite Songs", output)
        self.assertIn("**rock band**", output)
        self.assertIn("* *John Lennon*", output)
        self.assertIn("***Let It Be***", output)
        self.assertIn("~~Ob-La-Di, Ob-La-Da~~", output)