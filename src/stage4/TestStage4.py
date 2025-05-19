import unittest
import subprocess

class TestStage3(unittest.TestCase):
    def run_stage4(self, user_inputs):
        """
        Uruchamia stage4.py z listą wejść jako symulacją interakcji z użytkownikiem.
        """
        process = subprocess.run(
            ["python", "stage4.py"],
            input="\n".join(user_inputs),
            capture_output=True,
            text=True
        )
        return process.stdout

    def test_help_command(self):
        output = self.run_stage4(["!help", "!done"])
        self.assertIn("Available formatters: plain bold italic header link inline-code new-line", output)
        self.assertIn("Special commands: !help !done", output)

    def test_unknown_command(self):
        output = self.run_stage4(["unknown", "!done"])
        self.assertIn("Unknown formatting type or command", output)

    def test_plain_formatter(self):
        output = self.run_stage4(["plain", "simple text", "!done"])
        self.assertIn("simple text", output)

    def test_bold_formatter(self):
        output = self.run_stage4(["bold", "bold text", "!done"])
        self.assertIn("**bold text**", output)

    def test_italic_formatter(self):
        output = self.run_stage4(["italic", "italic text", "!done"])
        self.assertIn("*italic text*", output)

    def test_inline_code_formatter(self):
        output = self.run_stage4(["inline-code", "x = 1", "!done"])
        self.assertIn("`x = 1`", output)

    def test_link_formatter(self):
        output = self.run_stage4(["link", "Link name", "http://example.com", "!done"])
        self.assertIn("[Link name](http://example.com)", output)

    def test_header_formatter_valid_level(self):
        output = self.run_stage4(["header", "2", "Title", "!done"])
        self.assertIn("## Title", output)

    def test_header_formatter_invalid_level_then_valid(self):
        output = self.run_stage4(["header", "9", "2", "Fixed Header", "!done"])
        self.assertIn("The level should be within the range of 1 to 6", output)
        self.assertIn("## Fixed Header", output)

    def test_new_line_formatter(self):
        output = self.run_stage4(["plain", "Line1", "new-line", "plain", "Line2", "!done"])
        self.assertIn("Line1\nLine2", output)  # nowa linia powinna rozdzielać

    def test_combination_output(self):
        output = self.run_stage4([
            "header", "1", "Title",
            "plain", " text ",
            "bold", "bold",
            "italic", "italic",
            "new-line",
            "inline-code", "code",
            "!done"
        ])
        self.assertIn("# Title", output)
        self.assertIn(" text **bold**", output)
        self.assertIn("*italic*", output)
        self.assertIn("`code`", output)
        self.assertIn("\n", output)  # sprawdzenie, czy są nowe linie
