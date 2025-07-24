import os

directory_path = "D:\\"

try:
    content = os.listdir(directory_path)
    for item in content:
        print(item)
except Exception as e:
    print(f"Error: {e}")