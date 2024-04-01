def create_file():
    try:
        # Attempt to open the file in write mode
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("Hello, this is our file's first line\n")
            file.write("Here goes line 2\n")
            file.write("Finally, Line 3!\n")
        print("File created successfully!")
    except PermissionError:
        # Handle permission denied error
        print("Permission denied to create file.")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
    finally:
        # Cleanup or finalization code
        print("File creation process completed.\n")


def read_and_display_file():
    try:
        # Attempt to open the file in read mode
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            # Read and display each line of the file
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        # Handle file not found error
        print("File not found.")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
    finally:
        # Cleanup or finalization code
        print("File reading and display process completed.\n")


def append_to_file():
    try:
        # Attempt to open the file in append mode
        with open("my_file.txt", "a") as file:
            # Append three lines of text to the file
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("Content appended to file successfully!")
    except PermissionError:
        # Handle permission denied error
        print("Permission denied to append to file.")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
    finally:
        # Cleanup or finalization code
        print("File appending process completed.\n")


if __name__ == "__main__":
    # Call functions to perform file operations
    create_file()
    read_and_display_file()
    append_to_file()
