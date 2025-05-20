import unittest
import subprocess

class TestStage1(unittest.TestCase):
    def test_output_contains_expected_lines(self):
        result = subprocess.run(["python", "stage1.py"], capture_output=True, text=True)
        output = result.stdout

        self.assertIn("# The Beatles Favorite Songs", output)
        self.assertIn("**rock band**", output)
        self.assertIn("* *John Lennon*", output)
        self.assertIn("***Let It Be***", output)
        self.assertIn("~~Ob-La-Di, Ob-La-Da~~", output)

class TestStage2(unittest.TestCase):
    def run_stage2(self, user_inputs):
        """
        Uruchamia stage2.py z listą wejść (user_inputs) jako symulacją interakcji z użytkownikiem.
        """
        process = subprocess.run(
            ["python", "stage2.py"],
            input="\n".join(user_inputs),
            capture_output=True,
            text=True
        )
        return process.stdout

    def test_help_command(self):
        output = self.run_stage2(["!help", "!done"])
        self.assertIn("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line", output)
        self.assertIn("Special commands: !help !done", output)

    def test_unknown_command(self):
        output = self.run_stage2(["unknown-command", "!done"])
        self.assertIn("Unknown formatting type or command", output)

    def test_known_formatter(self):
        output = self.run_stage2(["plain", "!done"])
        self.assertNotIn("Unknown formatting type or command", output)
        self.assertIn("Choose a formatter:", output)

    def test_multiple_valid_inputs(self):
        output = self.run_stage2(["header", "ordered-list", "unordered-list", "!done"])
        self.assertNotIn("Unknown formatting type or command", output)
        self.assertEqual(output.count("Choose a formatter:"), 4)

    def test_exit_command(self):
        output = self.run_stage2(["!done"])
        self.assertTrue(output.strip().endswith("Choose a formatter:"))
