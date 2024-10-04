import os

def list_directory_contents(path):
    try:
        if os.path.exists(path) and os.path.isdir(path):
            print(f"Contents of directory '{path}':")
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    print(f"[DIR]  {item}")
                else:
                    print(f"[FILE] {item}")
        else:
            print(f"Error: '{path}' is not a valid directory.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
