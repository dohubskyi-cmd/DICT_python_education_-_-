def main():
    formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
    special_commands = ["!help", "!done"]
    
    full_content = []

    while True:
        user_input = input("Choose a formatter: ")

        if user_input == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write("".join(full_content))
            break

        elif user_input == "!help":
            print(f"Available formatters: {' '.join(formatters)}")
            print(f"Special commands: {' '.join(special_commands)}")

        elif user_input not in formatters:
            print("Unknown formatting type or command")

        else:
            if user_input == "header":
                while True:
                    level = int(input("Level: "))
                    if 1 <= level <= 6:
                        break
                    print("The level should be within the range of 1 to 6.")
                text = input("Text: ")
                full_content.append(f"{'#' * level} {text}\n")

            elif user_input == "plain":
                text = input("Text: ")
                full_content.append(text)

            elif user_input == "bold":
                text = input("Text: ")
                full_content.append(f"**{text}**")

            elif user_input == "italic":
                text = input("Text: ")
                full_content.append(f"*{text}*")

            elif user_input == "inline-code":
                text = input("Text: ")
                full_content.append(f"`{text}`")

            elif user_input == "new-line":
                full_content.append("\n")

            elif user_input == "link":
                label = input("Label: ")
                url = input("URL: ")
                full_content.append(f"[{label}]({url})")

            elif user_input in ["ordered-list", "unordered-list"]:
                while True:
                    n_rows = int(input("Number of rows: "))
                    if n_rows > 0:
                        break
                    print("The number of rows should be greater than zero")
                
                for i in range(1, n_rows + 1):
                    row_text = input(f"Row #{i}: ")
                    if user_input == "ordered-list":
                        full_content.append(f"{i}. {row_text}\n")
                    else:
                        full_content.append(f"* {row_text}\n")

            print("".join(full_content))

if __name__ == "__main__":
    main()
