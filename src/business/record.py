import uuid

class Record:
    """


    Attributes:
        week_end (str): The week ending date.
        week_end_last_year (str): The week ending date for last year.
        region (str): The region.
        crude_volumes_for_the_week (float): The crude volumes for the week.
        percent_of_capacity (float): The percentage of capacity.
        four_week_avg (float): The 4-week average.
        four_week_avg_last_year (float): The 4-week average for last year.
        ytd_avg (float): The year-to-date average.
        ytd_avg_last_year (float): The year-to-date average for last year.
        unit (str): The unit of measurement.
    """

    def __init__(self, week_end, week_end_last_year, region, crude_volumes_for_the_week,
                 percent_of_capacity, four_week_avg, four_week_avg_last_year,
                 ytd_avg, ytd_avg_last_year, unit):
       

        self.week_end = str(week_end)
        self.week_end_last_year = str(week_end_last_year)
        self.region = str(region)
        self.crude_volumes_for_the_week = float(crude_volumes_for_the_week)
        self.percent_of_capacity = float(percent_of_capacity)
        self.four_week_avg = float(four_week_avg)
        self.four_week_avg_last_year = float(four_week_avg_last_year)
        self.ytd_avg = float(ytd_avg)
        self.ytd_avg_last_year = float(ytd_avg_last_year)
        self.unit = str(unit)

    def display(self):
        """
        Prints the record details in a formatted way.
        """
        print(self.__str__())

    def __str__(self):
        """
        Returns a formatted string representation of the record.
        """
        return (f"Week End: {self.week_end} | Region: {self.region} | "
                f"Crude Volumes: {self.crude_volumes_for_the_week} {self.unit} | "
                f"Percent Capacity: {self.percent_of_capacity}% | "
                f"4-Week Avg: {self.four_week_avg} | YTD Avg: {self.ytd_avg}")