from ..business.record import Record  # Ensure to import Record class
from ..persistence.file_io import FileIO  # Ensure to import FileIO
from src.controller.sorter import multi_column_sort  # Import the sorting function

"""

Author: Amir kobaisse

Due Date: April 6, 2025

Professor: Stanley Pieda

Course: CST8002

Assessment: Practical Project 04

"""

class Menu:
    def __init__(self, file_io):
        self.file_io = file_io  # Instance of FileIO to handle file operations

    def show_menu(self):
        """
        Displays the menu options to the user and processes input.
        """
        while True:
            print("\n--- Crude Run Weekly Data Menu ---")
            print("1. Display All Records")
            print("2. Search for a Record by Week End")
            print("3. Add a New Record")
            print("4. Update an Existing Record")
            print("5. Save Records to Database")
            print("6. Sort Records")  # New option for sorting
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                self.display_all_records()
            elif choice == "2":
                self.search_record_by_week_end()
            elif choice == "3":
                self.add_record()
            elif choice == "4":
                self.update_record()
            elif choice == "5":
                self.save_data()
            elif choice == "6":
                self.sort_records()  # Call the new sort method
            elif choice == "7":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_all_records(self):
        """
        Displays all records from the database.
        """
        print("\nDisplaying Records:")
        records = self.file_io.load_records_from_db(detailed=False)  # Get records from DB
        if not records:
            print("No records available.")
        else:
            for i, record in enumerate(records, start=1):
                record.display()
                if i % 10 == 0:
                    print("\nProgram by Amir Kobaisse\n")

    def search_record_by_week_end(self):
        """
        Searches for a record by its week_end from the database.
        """
        week_end = input("Enter Week End to search: ")
        records = self.file_io.load_records_from_db(detailed=False)  # Get records from DB
        record = next((r for r in records if r.week_end == week_end), None)
        if record:
            record.display()
        else:
            print(f"Record with Week End {week_end} not found.")

    def add_record(self):
        """
        Adds a new record to the database.
        """
        print("\nEnter new record details:")
        week_end = input("Week End: ")
        week_end_last_year = input("Week End Last Year: ")
        region = input("Region: ")
        crude_volumes_for_the_week = float(input("Crude Volumes For The Week: "))
        percent_of_capacity = float(input("Percent Of Capacity: "))
        four_week_avg = float(input("4 Week Average: "))
        four_week_avg_last_year = float(input("4 Week Average Last Year: "))
        ytd_avg = float(input("YTD Average: "))
        ytd_avg_last_year = float(input("YTD Average Last Year: "))
        unit = input("Unit: ")

        # Create a new record
        new_record = Record(week_end, week_end_last_year, region, crude_volumes_for_the_week,
                            percent_of_capacity, four_week_avg, four_week_avg_last_year, 
                            ytd_avg, ytd_avg_last_year, unit)
        
        # Save to database
        self.file_io.save_record_to_db(new_record)
        print("\nRecord added successfully!")

    def update_record(self):
        """
        Updates a record in the database by its week_end.
        """
        week_end = input("Enter the Week End of the record to update: ")
        records = self.file_io.load_records_from_db(detailed=False)  # Get records from DB
        record = next((r for r in records if r.week_end == week_end), None)
        
        if record:
            print("Updating record... Enter new details below.")
            record.week_end = input(f"New Week End (Current: {record.week_end}): ") or record.week_end
            record.week_end_last_year = input(f"New Week End Last Year (Current: {record.week_end_last_year}): ") or record.week_end_last_year
            record.region = input(f"New Region (Current: {record.region}): ") or record.region
            record.crude_volumes_for_the_week = float(input(f"New Crude Volumes For The Week (Current: {record.crude_volumes_for_the_week}): ") or record.crude_volumes_for_the_week)
            record.percent_of_capacity = float(input(f"New Percent of Capacity (Current: {record.percent_of_capacity}): ") or record.percent_of_capacity)
            record.four_week_avg = float(input(f"New 4 Week Average (Current: {record.four_week_avg}): ") or record.four_week_avg)
            record.four_week_avg_last_year = float(input(f"New 4 Week Average Last Year (Current: {record.four_week_avg_last_year}): ") or record.four_week_avg_last_year)
            record.ytd_avg = float(input(f"New YTD Average (Current: {record.ytd_avg}): ") or record.ytd_avg)
            record.ytd_avg_last_year = float(input(f"New YTD Average Last Year (Current: {record.ytd_avg_last_year}): ") or record.ytd_avg_last_year)
            record.unit = input(f"New Unit (Current: {record.unit}): ") or record.unit
            
            # Update the record in the database
            self.file_io.update_record_in_db(record.week_end, record)
            print("Record updated successfully!")
        else:
            print("Record not found.")

    def save_data(self):
        """
        Saves all records to the database.
        """
        records = self.file_io.load_records_from_db(detailed=False)  # Get records from DB
        for record in records:
            self.file_io.save_record_to_db(record)
        print("Data saved to the database successfully!")

    # Method for the sorting functionality
    def sort_records(self):
        """
        Prompts the user to choose sorting options and displays sorted records.
        """
        # Load records from the database
        records = self.file_io.load_records_from_db(detailed=False)
        if not records:
            print("No records available to sort.")
            return

        # Get available columns from the first record (assumes all records have the same attributes)
        available_columns = list(vars(records[0]).keys())
        print("\nAvailable columns to sort by:")
        for idx, col in enumerate(available_columns, start=1):
            print(f"{idx}. {col}")

        # Prompt the user to enter column numbers (comma-separated)
        user_input = input("Enter the column numbers (comma-separated) to sort by (in order of priority): ")
        try:
            selected_indexes = [int(x.strip()) for x in user_input.split(',') if x.strip().isdigit()]
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return

        sort_columns = []
        ascending_flags = []
        for idx in selected_indexes:
            if idx < 1 or idx > len(available_columns):
                print(f"Invalid column number: {idx}")
                continue
            col_name = available_columns[idx - 1]
            sort_columns.append(col_name)
            order_input = input(f"Sort by '{col_name}' ascending (A) or descending (D)? [A/D]: ").strip().lower()
            ascending_flags.append(order_input == 'a')

        if not sort_columns:
            print("No valid sorting options selected.")
            return

        # Sort the records using the multi_column_sort function from the controller
        sorted_records = multi_column_sort(records, sort_columns, ascending_flags)

        # Display a preview of the sorted records (first 10)
        print("\n--- Sorted Records Preview ---")
        for i, record in enumerate(sorted_records[:10], start=1):
            print(f"Record {i}: {record}")
