import os
import shutil

def scan_tool():
    try:
        filename = input("Enter a Filename: ")
        if not filename:
            print("You entered nothing, please try again")
        else:
            with open(filename, "r") as file:
                for line in file:
                    if "error" in line.lower():
                        print("Found Error:", line)
    except Exception as e:
        print("Something went wrong")
        print(e)

def backup_tool():
    try:
        source = input("Enter a source: ")
        backup = input("Enter a backup: ")
        if os.path.exists(source):
            if os.path.exists(backup):
                print("That folder already exists")
            else:
                shutil.copytree(source, backup)
                print("Folder was copied")
        else:
            print("Folder not found")
    except Exception as e:
        print("Something went wrong")
        print(e)

def cleanup_tool():
    try:
        folder = input("Enter a folder to clean: ")
        if not folder:
            print("You did not enter any folder")
        else:
            for file in os.listdir(folder):
                path = os.path.join(folder, file)
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                        print(f"Deleted file: {file}")
                except Exception as e:
                    print(f"Failed to delete {file}: {e}")
    except Exception as e:
        print("Something went wrong")
        print(e)

while True:
    print("-"*65)
    print("==== IT SUPPORT TOOLKIT ====")
    print("1.Backup files")
    print("2.Scan log")
    print("3.Cleaning")
    print("4.Exit")
    print("-"*65)
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        print("BACKUP SELECTED")
        backup_tool()
    elif choice == "2":
        print("SCAN SELECTED")
        scan_tool()
    elif choice == "3":
        print("CLEANUP SELECTED")
        cleanup_tool()
    elif choice == "4":
        print("EXIT.....")
        break
    else:
        print("Wrong choice, try again")
