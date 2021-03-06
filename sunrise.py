__author__ = 'cepuuher'

# You need to do 'pip install selenium' at the terminal first
# Also need PhantomJS version >= 1.9
#   at the terminal do 'apt-get install phantomjs'

# v1 enter city
# v2 detect location and use lat long

# check last time info downloaded
## download it

#resource:  http://www.earthtools.org/webservices.htm#sun
# http://www.nrc-cnrc.gc.ca/eng/services/sunrise/advanced.html

import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def retrieve_web_sunrise_times(today, city):
    print "In retrieve_web_sunrise_times()..."
    #driver = webdriver.Firefox()
    driver = webdriver.PhantomJS()  # may need (executable_path='/usr/bin/phantomjs')
    driver.get("http://www.nrc-cnrc.gc.ca/eng/services/sunrise/")

    # TODO assert year or something
    elem_month = driver.find_element_by_name("month")

    # Hack hack hack!
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    elem_month.send_keys(months[today.month -1], Keys.ENTER)


    elem_day = driver.find_element_by_name("day")
    # TODO fix this for 1 digit days

    tomorrow_string =  str(today.day)[0] + str(int(str(today.day)[1]) +1)  #HACK HACK HACK!
    elem_day.clear()
    elem_day.send_keys(tomorrow_string)

    elem_city = driver.find_element_by_id("city")
    elem_city.send_keys(city, Keys.ENTER)

    elem_submit = driver.find_element_by_id("submit")
    elem_submit.click()

    table = driver.find_element_by_xpath("//div[@id='wb-main-in']")
    rcol = table.find_elements_by_xpath("//td[@class='align-right']")

    sunrise_time = str(rcol[2].text)
    print "The sun rises tomorrow, the " + tomorrow_string + "th at: " + sunrise_time
    driver.close()
    return sunrise_time  # stub... it certainly won't be a list returned

def calculate_bedtime(sleep_duration, sunrise_time):
    print 'In calculate_bedtime()...'
    bedtime = 1337

    [sunrise_hour, sunrise_minute] = sunrise_time.split(':')

    print "sunrise hour: " + sunrise_hour + ", sunrise minute: " + sunrise_minute

    return bedtime  # stub


def get_sunrise(today):
    print "In get_sunrise()..."
    return today  # worst stub ever

def main():
    print "Welcome to sunrise. We'll calculate your bedtime based on sunrise."

    # Prompt for user options
    sleep_duration = input("How many hours of sleep would you like? ")

#    city = raw_input("What city are you sleeping in? ")

    # Retrieve info
    today = datetime.date.today()  # can get year, month, day from this
    word_date = datetime.date.ctime(today)
    print "Today is " + word_date
    # TODO retrieve a bunch? then reretrieve only when stale, if not, just parse local data
    sunrise_time = retrieve_web_sunrise_times(today, 'Vancouver')  #TODO let user enter city


#    print "Today is " + str(today)
#    print "A.k.a. " + str(word_date)

    # Grab sunrise info from web, if necessary

    # Oh man I'm commenting too much...
    # I had get_sunrise here...

    # Calculate
    bedtime = calculate_bedtime(sleep_duration, sunrise_time)

    # Return bedtime to user
    print "Tonight's bedtime is " + str(bedtime)


if __name__ == main():
    try:
        main()
    except Exception as e:
        import pdb
        pdb.set_trace()
        print 'Entered debugger with Exception e.'
    finally:
        exit()
