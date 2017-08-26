# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from public import basic

class Search():

    def __init__(self, url):

        self.url = url
        self.driver = basic.chrome(headless=True)

    def open_page(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

    def find_data(self):
        tmp_num = self.driver.find_element_by_class_name("detail-realtime").text
        str_num = "".join(list(tmp_num)[:-1])
        return float(str_num)

    def real_time(self, count,interval):
        tmp_count = count
        self.open_page()
        start_data = self.find_data()
        print "Start number is: %.2f  Unit: 10K" % start_data
        last_data = start_data
        while tmp_count > 0:
            tmp_count -= 1
            time.sleep(interval)
            tmp_data = self.find_data()
            delta = tmp_data - last_data
            print "[%d]:"%(count - tmp_count) + " New: %.2f"%tmp_data + "    Delta: %.2f"%delta + "    Average: %.2f"%((tmp_data-start_data)/(count - tmp_count))
            last_data = tmp_data
        average = (last_data - start_data)/count

        return last_data, average

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    run_hours = 3600*1
    interval = 60*1
    count = int(run_hours/interval)
    url = "https://piaofang.maoyan.com/dashboard?movieId=344264"
    Movie_value = Search(url)
    latest_value, avg_value = Movie_value.real_time(count, interval)
    Movie_value.close()
    log = time.ctime() + "    Latest_value: %d"%latest_value + "    Averge_value(per min): %d\n%avg_value"
    with open("time.log", 'a') as f:
        f.write(log)





