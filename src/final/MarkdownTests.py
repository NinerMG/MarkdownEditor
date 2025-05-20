import unittest
import subprocess

class TestStage5(unittest.TestCase):
    def run_markdown(self, user_inputs):
        """
        Uruchamia markdown.py z listą wejść jako symulacją interakcji z użytkownikiem.
        """
        process = subprocess.run(
            ["python", "markdown.py"],
            input="\n".join(user_inputs),
            capture_output=True,
            text=True
        )
        return process.stdout

    def test_help_command(self):
        output = self.run_markdown(["!help", "!done"])
        self.assertIn("Available formatters: plain bold italic header link inline-code new-line", output)
        self.assertIn("Special commands: !help !done", output)

    def test_unknown_command(self):
        output = self.run_markdown(["unknown", "!done"])
        self.assertIn("Unknown formatting type or command", output)

    def test_plain_formatter(self):
        output = self.run_markdown(["plain", "simple text", "!done"])
        self.assertIn("simple text", output)

    def test_bold_formatter(self):
        output = self.run_markdown(["bold", "bold text", "!done"])
        self.assertIn("**bold text**", output)

    def test_italic_formatter(self):
        output = self.run_markdown(["italic", "italic text", "!done"])
        self.assertIn("*italic text*", output)

    def test_inline_code_formatter(self):
        output = self.run_markdown(["inline-code", "x = 1", "!done"])
        self.assertIn("`x = 1`", output)

    def test_link_formatter(self):
        output = self.run_markdown(["link", "Link name", "http://example.com", "!done"])
        self.assertIn("[Link name](http://example.com)", output)

    def test_header_formatter_valid_level(self):
        output = self.run_markdown(["header", "2", "Title", "!done"])
        self.assertIn("## Title", output)

    def test_header_formatter_invalid_level_then_valid(self):
        output = self.run_markdown(["header", "9", "2", "Fixed Header", "!done"])
        self.assertIn("The level should be within the range of 1 to 6", output)
        self.assertIn("## Fixed Header", output)

    def test_new_line_formatter(self):
        output = self.run_markdown(["plain", "Line1", "new-line", "plain", "Line2", "!done"])
        self.assertIn("Line1\nLine2", output)  # nowa linia powinna rozdzielać

    def test_combination_output(self):
        output = self.run_markdown([
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

    def test_ordered_list_formatter(self):
        output = self.run_markdown([
            "ordered-list", "3",
            "First item",
            "Second item",
            "Third item",
            "!done"
        ])
        self.assertIn("1. First item", output)
        self.assertIn("2. Second item", output)
        self.assertIn("3. Third item", output)

    def test_unordered_list_formatter(self):
        output = self.run_markdown([
            "unordered-list", "2",
            "Item one",
            "Item two",
            "!done"
        ])
        self.assertIn("* Item one", output)
        self.assertIn("* Item two", output)

    def test_ordered_list_invalid_then_valid(self):
        output = self.run_markdown([
            "ordered-list", "0", "2",
            "Valid one",
            "Valid two",
            "!done"
        ])
        self.assertIn("The number of rows should be greater than zero", output)
        self.assertIn("1. Valid one", output)
        self.assertIn("2. Valid two", output)

    def test_unordered_list_invalid_then_valid(self):
        output = self.run_markdown([
            "unordered-list", "-1", "3",
            "A", "B", "C",
            "!done"
        ])
        self.assertIn("The number of rows should be greater than zero", output)
        self.assertIn("* A", output)
        self.assertIn("* B", output)
        self.assertIn("* C", output)

    def test_done_saves_output(self):
        output = self.run_markdown([
            "header", "1", "Test Title",
            "plain", " content",
            "!done"
        ])
        with open("output.md", "r") as file:
            saved = file.read()
        self.assertIn("# Test Title", saved)
        self.assertIn(" content", saved)