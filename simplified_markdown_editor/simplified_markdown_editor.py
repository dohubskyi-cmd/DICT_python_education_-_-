elif choice == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(result_text)
            break
