import time
from datetime import datetime
from dateutil import parser
from write_to_csv import write_to_csv
import random
import re
# Get the current year, month, and day
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ublox_request import get_data_from_UBLOX,get_sat_number_from_UBLOX


year_month_day = datetime.now().strftime("%Y-%m-%d")

def parsing_clock_element(clock_element) :
    clock_text = clock_element.text
    clock_text = clock_text.replace('PM', '').replace(':', ':').replace('\n', '')  
    clock_output = f"{year_month_day} {clock_text}"
    time_obj = datetime.strptime(clock_output, "%Y-%m-%d %H:%M:%S:%f")
    timestamp = time_obj.timestamp()
    return timestamp

def scrape_clock_stats(clock_stats_element):
    stats_text = clock_stats_element.text
    stats_data = stats_text.split('\n')
    return stats_data

def parse_stats_data(stats_data):
    date_match = re.search(r'[A-Za-z]+\s\d{1,2},\s\d{4}', stats_data)
    if date_match:
        date_str = date_match.group()
        date_obj = datetime.strptime(date_str, "%B %d, %Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
    return (formatted_date)


with webdriver.Chrome() as driver:
    try:
        driver.get('https://clock.zone/asia/tel-aviv-yafo')

        clock_element = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.ID, 'MyClockDisplay'))
        )

        clock_stats_element = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'clock-stats'))
        )

        while True:
            current_time = datetime.now()
            web_timestamp=parsing_clock_element(clock_element)
            date_from_stats = parse_stats_data(clock_stats_element.text)
            ublox_data = get_data_from_UBLOX()
            # clock_stats = scrape_clock_stats(clock_stats_element)
            # stats_output = parse_stats_data(clock_stats)
            # print(clock_stats_element.text)
            print(ublox_data)
            write_to_csv("test.csv" ,current_time,ublox_data , web_timestamp)
            # Wait for 0.5 second
            time.sleep(0.5)

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl+C) gracefully
        pass
