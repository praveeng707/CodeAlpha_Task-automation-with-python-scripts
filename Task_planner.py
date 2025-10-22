import os
import shutil
import re
import requests

#  Move all .jpg files from one folder to another
def move_jpg_files():
    source_folder = input("Enter the source folder name: ")
    destination_folder = input("Enter the destination folder name: ")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(f"✅ Moved {moved_count} .jpg file(s) successfully.\n")

#  Extract email addresses from a .txt file
def extract_emails():
    input_file = input("Enter the name of the .txt file to read from: ")
    output_file = input("Enter the name of the file to save emails to: ")

    with open(input_file, 'r') as file:
        content = file.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"✅ Extracted {len(emails)} email(s) to '{output_file}'.\n")

# Scrape the title of a fixed webpage
def scrape_webpage_title():
    url = input("Enter the full URL of the webpage: ")

    try:
        response = requests.get(url)
        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
        title = title_match.group(1) if title_match else 'No title found'

        with open('webpage_title.txt', 'w') as file:
            file.write(title)

        print(f"✅ Title saved to 'webpage_title.txt': {title}\n")
    except Exception as e:
        print("❌ Error fetching the webpage:", e)

# Main menu
def main():
    print("🔧 Python Task Automation Menu")
    print("1. Move all .jpg files")
    print("2. Extract email addresses from a .txt file")
    print("3. Scrape the title of a webpage")
    print("4. Exit")

    while True:
        choice = input("Choose a task (1-4): ")

        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            scrape_webpage_title()
        elif choice == '4':
            print("👋 Exiting the program. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 4.\n")

main()