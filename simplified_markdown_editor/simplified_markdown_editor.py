import sys

class MarkdownEditor:
    def __init__(self):
        self.formatters = [
            "plain", "bold", "italic", "header", "link", 
            "inline-code", "ordered-list", "unordered-list", "new-line"
        ]
        self.special_commands = ["!help", "!done"]
        self.full_content = []

    def show_help(self):
        print(f"Available formatters: {' '.join(self.formatters)}")
        print(f"Special commands: {' '.join(self.special_commands)}")

    def get_valid_int(self, prompt, error_msg, min_val, max_val=None):
        while True:
            try:
                val = int(input(prompt))
                if val < min_val or (max_val is not None and val > max_val):
                    print(error_msg)
                else:
                    return val
            except ValueError:
                print("Incorrect format. Please enter a number.")

    def add_header(self):
        level = self.get_valid_int("Level: ", "The level should be within the range of 1 to 6.", 1, 6)
        text = input("Text: ")
        self.full_content.append(f"{'#' * level} {text}\n")

    def add_list(self, list_type):
        n_rows = self.get_valid_int("Number of rows: ", "The number of rows should be greater than zero", 1)
        
        if self.full_content and not self.full_content[-1].endswith("\n\n"):
            if not self.full_content[-1].endswith("\n"):
                self.full_content.append("\n")
            self.full_content.append("\n")

        for i in range(1, n_rows + 1):
            row_text = input(f"Row #{i}: ")
            if list_type == "ordered-list":
                self.full_content.append(f"{i}. {row_text}\n")
            else:
                self.full_content.append(f"* {row_text}\n")
        
        self.full_content.append("\n")

    def run(self):
        while True:
            user_input = input("Choose a formatter: ").strip()

            if user_input == "!done":
                self.save_to_file()
                break
            elif user_input == "!help":
                self.show_help()
            elif user_input not in self.formatters:
                print("Unknown formatting type or command")
            else:
                self.process_formatter(user_input)
                print("".join(self.full_content))

    def process_formatter(self, formatter):
        if formatter == "header":
            self.add_header()
        elif formatter in ["ordered-list", "unordered-list"]:
            self.add_list(formatter)
        elif formatter == "new-line":
            self.full_content.append("\n\n")
        elif formatter == "link":
            label = input("Label: ")
            url = input("URL: ")
            self.full_content.append(f"[{label}]({url})")
        else:
            text = input("Text: ")
            if formatter == "plain":
                self.full_content.append(text)
            elif formatter == "bold":
                self.full_content.append(f"**{text}**")
            elif formatter == "italic":
                self.full_content.append(f"*{text}*")
            elif formatter == "inline-code":
                self.full_content.append(f"`{text}`")

    def save_to_file(self):
        with open("output.md", "w", encoding="utf-8") as f:
            f.write("".join(self.full_content))

if __name__ == "__main__":
    editor = MarkdownEditor()
    editor.run()
