import os
from src.persistence.file_io import FileIO  # Import FileIO for DB interaction
from src.business.record import Record  # Assuming you still have the Record class
from src.presentation.menu import Menu

def main():
    """
    Main function to handle program execution.
    """
    print("Program by: Amir Kobaisse")

    # Initialize FileIO
    file_io = FileIO()  # Create the FileIO object

    # Load records from the database
    records = file_io.load_records_from_db(detailed=False)  # Adjust as needed (detailed=True/False)

    # Initialize and run the menu with file_io
    menu = Menu(file_io)  # Pass file_io since RecordManager is removed
    menu.show_menu()

if __name__ == "__main__":
    main()
