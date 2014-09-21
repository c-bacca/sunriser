__author__ = 'cepuuher'

# v1 enter city
# v1 detect location and use lat long

# check last time info downloaded
## download it

#resource:  http://www.earthtools.org/webservices.htm#sun
# http://www.nrc-cnrc.gc.ca/eng/services/sunrise/advanced.html

import datetime

def calculate_bedtime(sleep_duration, sunrise_time):
    print 'In calculate_bedtime()...'
    bedtime = 0

    return bedtime  # stub


def retrieve_web_sunrise_times(today, city):
    return []  # stub... it won't be a list returned

def get_sunrise(today):
    return today  # worst stub ever

def main():
    print "Welcome to sunrise. We'll calculate your bedtime based on sunrise."

    # Prompt for user options
    sleep_duration = input("How many hours of sleep would you like? ")

#    city = raw_input("What city are you sleeping in? ")

    # Retrieve info
    today = datetime.date.today()
    word_date = datetime.date.ctime(today)

#    print "Today is " + str(today)
#    print "A.k.a. " + str(word_date)

    # Grab sunrise info from web, if necessary

    # Oh man I'm commenting too much...
    sunrise_time = get_sunrise(today)

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
