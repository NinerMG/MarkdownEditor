available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
special_commands = ["!help", "!done"]

while True:
    user_input = input("Choose a formatter: ")

    if user_input not in available_formatters and user_input not in special_commands:
        print("Unknown formatting type or command")
        continue

    else:
        if user_input in available_formatters:
            pass
        elif user_input in special_commands:
            if user_input == "!help":
                print(f"Available formatters: {' '.join(available_formatters)}")
                print(f"Special commands: {' '.join(special_commands)}")
            elif user_input == "!done":
                break