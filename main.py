import re
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from write_to_csv import write_to_csv,remove_file
from ublox_request_functions import get_all_ublox_data

website_URL = 'https://clock.zone/asia/tel-aviv-yafo'

def parsing_timestamp(clock_element):
    year_month_day = datetime.now().strftime("%Y-%m-%d")
    clock_text = clock_element.text.replace('PM', '').replace(':', ':').replace('\n', '')
    clock_output = f"{year_month_day} {clock_text}"
    time_obj = datetime.strptime(clock_output, "%Y-%m-%d %H:%M:%S:%f")
    timestamp = time_obj.timestamp()
    return timestamp

def parsing_sync_precision(clock_stats_element):
    stats_text = clock_stats_element.text
    lines = stats_text.split('\n')
    sync_precision_line = next((line for line in lines if line.startswith("Sync precision")), None)
    if sync_precision_line:
        match = re.search(r"[-+]?\d*\.\d+|\d+", sync_precision_line)
        if match:
            sync_precision_value = match.group()
            return sync_precision_value
    return None

with webdriver.Chrome() as driver:
    try:
        remove_file('test.csv')
        driver.get(website_URL)

        clock_element = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'MyClockDisplay')))
        clock_stats_element = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'clock-stats')))

        while True:
            current_time = datetime.now()
            web_timestamp = parsing_timestamp(clock_element)
            ublox_timestamp,ublox_fix_quality,number_of_sat = get_all_ublox_data()
            sync_precision = parsing_sync_precision(clock_stats_element)
            write_to_csv("test.csv", current_time, ublox_timestamp, web_timestamp,sync_precision,ublox_fix_quality,number_of_sat)
            time.sleep(0.5)

    except KeyboardInterrupt:
        pass
