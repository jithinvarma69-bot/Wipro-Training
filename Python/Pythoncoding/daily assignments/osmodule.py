import os

print("Current working directory:", os.getcwd())

new_dir = "new_directory"
os.mkdir(new_dir)

if os.path.exists(new_dir):
    print(f"'{new_dir}' directory created successfully.")

print("Files and directories in the current directory:", os.listdir())