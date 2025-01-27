import os

def main_menu():
    print("\nSelect an operation:")
    print("1. Check if a PDF can be read")
    print("2. Check if a specific text is in a file")
    print("3. Append text to a file")
    print("4. Overwrite file content with new text")
    print("5. Exit")
    return input("Enter your choice: ")

def check_pdf_readable(pdf_path):
    try:
        with open(pdf_path, "r") as book:
            print("PDF File Read Successfully")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_text_in_file(file_path, text_to_check):
    try:
        with open(file_path, "r") as book:
            content = book.read()
            if text_to_check in content:
                print(f"Text '{text_to_check}' is available in the file.")
            else:
                print(f"Text '{text_to_check}' is NOT in the file.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_text_to_file(file_path, text_to_append):
    try:
        with open(file_path, "a") as book:
            book.write(text_to_append)
            print(f"Text '{text_to_append}' appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def overwrite_file_content(file_path, new_content):
    try:
        with open(file_path, "w") as book:
            book.write(new_content)
            print("File content overwritten successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            pdf_path = input("Enter the full path of the PDF file: ")
            check_pdf_readable(pdf_path)
        elif choice == "2":
            file_path = input("Enter the full path of the text file: ")
            text_to_check = input("Enter the text to check in the file: ")
            check_text_in_file(file_path, text_to_check)
        elif choice == "3":
            file_path = input("Enter the full path of the text file: ")
            text_to_append = input("Enter the text to append: ")
            append_text_to_file(file_path, text_to_append)
        elif choice == "4":
            file_path = input("Enter the full path of the text file: ")
            new_content = input("Enter the new content to write: ")
            overwrite_file_content(file_path, new_content)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
