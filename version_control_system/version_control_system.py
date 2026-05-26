import sys
import os
import hashlib
import shutil

def get_hash(files):
    hasher = hashlib.sha1()
    for f in sorted(files):
        if os.path.exists(f):
            with open(f, "rb") as file:
                while chunk := file.read(8192):
                    hasher.update(chunk)
    return hasher.hexdigest()

def ensure_vcs_dir():
    if not os.path.exists("vcs"):
        os.mkdir("vcs")
    if not os.path.exists("vcs/commits"):
        os.mkdir("vcs/commits")
    for f in ["config.txt", "index.txt", "log.txt"]:
        if not os.path.exists(f"vcs/{f}"):
            open(f"vcs/{f}", "a", encoding="utf-8").close()

def handle_config(args):
    if len(args) == 1:
        with open("vcs/config.txt", "r", encoding="utf-8") as f:
            content = f.read().strip()
            print(f"The username is {content}." if content else "Please, tell me who you are.")
    else:
        with open("vcs/config.txt", "w", encoding="utf-8") as f:
            f.write(args[1])
            print(f"The username is {args[1]}.")

def handle_add(args):
    if len(args) == 1:
        with open("vcs/index.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("Add a file to the index.")
            else:
                print("Tracked files:")
                for line in lines:
                    print(line.strip())
    else:
        filename = args[1]
        if os.path.exists(filename):
            with open("vcs/index.txt", "r", encoding="utf-8") as f:
                tracked = [line.strip() for line in f]
            if filename not in tracked:
                with open("vcs/index.txt", "a", encoding="utf-8") as f:
                    f.write(filename + "\n")
            print(f"The file '{filename}' is tracked.")
        else:
            print(f"Can't find '{filename}'.")

def handle_commit(message):
    if not message:
        return print("Message was not passed.")
    with open("vcs/index.txt", "r", encoding="utf-8") as f:
        tracked = [line.strip() for line in f if line.strip()]
    if not tracked:
        return print("Nothing to commit.")
    
    current_hash = get_hash(tracked)
    last_hash = ""
    if os.path.exists("vcs/log.txt"):
        with open("vcs/log.txt", "r", encoding="utf-8") as f:
            line = f.readline()
            if line and line.startswith("commit"):
                last_hash = line.split()[1]

    if current_hash == last_hash:
        return print("Nothing to commit.")

    path = f"vcs/commits/{current_hash}"
    os.makedirs(path, exist_ok=True)
    for f in tracked:
        shutil.copy(f, path)
    
    with open("vcs/config.txt", "r", encoding="utf-8") as f:
        author = f.read().strip()
    
    with open("vcs/log.txt", "r", encoding="utf-8") as f:
        old_log = f.read()
    with open("vcs/log.txt", "w", encoding="utf-8") as f:
        f.write(f"commit {current_hash}\nAuthor: {author}\n{message}\n\n" + old_log)
    print("Changes are committed.")

def handle_log():
    if not os.path.exists("vcs/log.txt") or os.stat("vcs/log.txt").st_size == 0:
        print("No commits yet.")
    else:
        with open("vcs/log.txt", "r", encoding="utf-8") as f:
            print(f.read().strip())

def handle_checkout(args):
    if len(args) == 1:
        return print("Commit id was not passed.")
    commit_id = args[1]
    commit_path = f"vcs/commits/{commit_id}"
    if not os.path.exists(commit_path):
        return print("Commit does not exist.")
    for filename in os.listdir(commit_path):
        shutil.copy(os.path.join(commit_path, filename), ".")
    print(f"Switched to commit {commit_id}.")

def main():
    ensure_vcs_dir()
    commands = {
        "config": "Get and set a username.",
        "add": "Add a file to the index.",
        "log": "Show commit logs.",
        "commit": "Save changes.",
        "checkout": "Switch between commits and restore a previous file state."
    }
    args = sys.argv[1:]
    
    if not args or args[0] == "--help":
        print("These are VCS commands:")
        for cmd, desc in commands.items():
            print(f"{cmd:10} {desc}")
    elif args[0] == "config":
        handle_config(args)
    elif args[0] == "add":
        handle_add(args)
    elif args[0] == "commit":
        handle_commit(args[1] if len(args) > 1 else None)
    elif args[0] == "log":
        handle_log()
    elif args[0] == "checkout":
        handle_checkout(args)
    else:
        print(f"'{args[0]}' is not a VCS command.")

if __name__ == "__main__":
    main()
