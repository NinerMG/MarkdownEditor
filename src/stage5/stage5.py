available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code",
                        "new-line", "ordered-list", "unordered-list"]
special_commands = ["!help", "!done"]

def format_header():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            else:
                print("The level should be within the range of 1 to 6")
        except ValueError:
            print("Please enter a valid number")

    input_text = input("Text: ")
    return "\n" + "#" * level + " " + input_text + "\n"

def format_plain():
    input_text = input("Text: ")
    return input_text

def format_bold():
    input_text = input("Text: ")
    return f"**{input_text}**"

def format_italic():
    input_text = input("Text: ")
    return f"*{input_text}*"

def format_inline_code():
    input_text = input("Text: ")
    return f"`{input_text}`"

def format_new_line():

    return "\n"

def format_link():
    input_label = input("Label: ")
    input_url = input("URL: ")
    return f"[{input_label}]({input_url})"

def format_ordered_list():
    while True:
        try:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            else:
                print("The number of rows should be greater than zero")
        except ValueError:
            print("Please enter a valid number")

    lines = [input(f"Row#{x + 1}: ") for x in range(rows)]
    return "\n".join([f"{i + 1}. {line}" for i, line in enumerate(lines)]) + "\n"

def format_unordered_list():
    while True:
        try:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            else:
                print("The number of rows should be greater than zero")
        except ValueError:
            print("Please enter a valid number")
    lines = [input(f"Row#{x + 1}: ") for x in range(rows)]
    return "\n".join([f"* {line}" for line in lines]) + "\n"

def save_to_file(string_to_save):
    with open("output.md", "w") as file:
        file.write(string_to_save)

text = ""
while True:
    user_input = input("Choose a formatter: ")

    if user_input not in available_formatters and user_input not in special_commands:
        print("Unknown formatting type or command")
        continue
    elif user_input in special_commands:
        if user_input == "!help":
            print(f"Available formatters: {' '.join(available_formatters)}")
            print(f"Special commands: {' '.join(special_commands)}")
        elif user_input == "!done":
            save_to_file(text)
            print("Markdown saved to output.md")
            break

    else:
        match user_input:
            case "plain": text += format_plain()
            case "bold": text += format_bold()
            case "italic": text += format_italic()
            case "header": text += format_header()
            case "inline-code": text += format_inline_code()
            case "new-line": text += format_new_line()
            case "link": text += format_link()
            case "ordered-list": text += format_ordered_list()
            case "unordered-list": text += format_unordered_list()

    print(text)


