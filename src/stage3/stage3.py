available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line"]
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

    text = input("Text: ")
    return f"#" * level + " " + text + "\n"

def format_plain():
    text = input("Text: ")
    return text

def format_bold():
    text = input("Text: ")
    return f"**{text}**\n"


while True:
    user_input = input("Choose a formatter: ")
    text = ""
    if user_input not in available_formatters and user_input not in special_commands:
        print("Unknown formatting type or command")
        continue

    else:
        match user_input:
            case "plain": text += format_plain()
            case "bold": text += format_bold()
            case "header": text += format_header()


    print(text)


