"""

Author: Amir kobaisse

Due Date: April 6, 2025

Professor: Stanley Pieda

Course: CST8002

Assessment: Practical Project 04

"""
# src/controller/sorter.py

def multi_column_sort(records, sort_columns, ascending_flags):
    """
    Sorts a list of Record objects based on multiple columns.

    Args:
        records (list): List of Record objects.
        sort_columns (list of str): List of attribute names to sort by 
            (e.g., ['region', 'crude_volumes_for_the_week']).
        ascending_flags (list of bool): List of booleans for each column 
            (True for ascending, False for descending).

    Returns:
        list: A new list of Record objects sorted as specified.
    """
    sorted_records = records[:]  # Create a shallow copy

    # Since Python's sort is stable, sort starting from the least significant key.
    for col, asc in reversed(list(zip(sort_columns, ascending_flags))):
        sorted_records = sorted(sorted_records, key=lambda record: getattr(record, col), reverse=(not asc))
    
    return sorted_records
