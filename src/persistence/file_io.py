from .database_handler import DatabaseHandler
from ..business.record import Record  # Import the Record class directly

"""

Author: Amir kobaisse

Due Date: April 6, 2025

Professor: Stanley Pieda

Course: CST8002

Assessment: Practical Project 04

"""

class FileIO:
    """
    Handles database input and output operations, including reading from and writing to the MySQL database.
    """

    @staticmethod
    def load_records_from_db(detailed=False):
        """
        Loads records from the database.
        
        Args:
            detailed (bool): Flag indicating whether to load detailed records or not.
        
        Returns:
            list: A list of Record objects.
        """
        records = []
        db_handler = DatabaseHandler()
        db_handler.connect()

        # Query to fetch records
        query = "SELECT * FROM crude_runs_weekly"
        result = db_handler.fetch_results(query)

        # Create the records using the Record class
        for row in result:
            record = Record(
                week_end=row[1],  # week_end
                week_end_last_year=row[2],  # week_end_last_year
                region=row[3],  # region
                crude_volumes_for_the_week=row[4],  # crude_volumes_for_the_week
                percent_of_capacity=row[5],  # percent_of_capacity
                four_week_avg=row[6],  # four_week_avg
                four_week_avg_last_year=row[7],  # four_week_avg_last_year
                ytd_avg=row[8],  # ytd_avg
                ytd_avg_last_year=row[9],  # ytd_avg_last_year
                unit=row[10]  # unit
            )
            records.append(record)

        db_handler.close()
        return records

    @staticmethod
    def save_record_to_db(record):
        """
        Saves a single Record object to the database.
        
        Args:
            record (Record): The record object to save to the database.
        """
        db_handler = DatabaseHandler()
        db_handler.connect()

        insert_query = """
        INSERT INTO crude_runs_weekly 
        (week_end, week_end_last_year, region, crude_volumes_for_the_week, percent_of_capacity, 
        four_week_avg, four_week_avg_last_year, ytd_avg, ytd_avg_last_year, unit)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        record_data = (
            record.week_end, record.week_end_last_year, record.region,
            record.crude_volumes_for_the_week, record.percent_of_capacity,
            record.four_week_avg, record.four_week_avg_last_year,
            record.ytd_avg, record.ytd_avg_last_year, record.unit
        )
        db_handler.execute_query(insert_query, record_data)
        db_handler.close()

    @staticmethod
    def update_record_in_db(record_id, record):
        """
        Updates an existing record in the database by its ID.
        
        Args:
            record_id (int): The ID of the record to update.
            record (Record): The record object with updated data.
        """
        db_handler = DatabaseHandler()
        db_handler.connect()

        update_query = """
        UPDATE crude_runs_weekly 
        SET week_end=%s, week_end_last_year=%s, region=%s, crude_volumes_for_the_week=%s,
            percent_of_capacity=%s, four_week_avg=%s, four_week_avg_last_year=%s,
            ytd_avg=%s, ytd_avg_last_year=%s, unit=%s
        WHERE id=%s
        """
        updated_record = (
            record.week_end, record.week_end_last_year, record.region,
            record.crude_volumes_for_the_week, record.percent_of_capacity,
            record.four_week_avg, record.four_week_avg_last_year,
            record.ytd_avg, record.ytd_avg_last_year, record.unit,
            record_id
        )
        db_handler.execute_query(update_query, updated_record)
        db_handler.close()
