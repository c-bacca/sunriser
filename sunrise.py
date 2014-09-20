__author__ = 'cepuuher'

# v1 enter city
# v1 detect location and use lat long

# check last time info downloaded
## download it

#resource:  http://www.earthtools.org/webservices.htm#sun
# http://www.nrc-cnrc.gc.ca/eng/services/sunrise/advanced.html

import datetime

def main ():
    print "Welcome to sunrise. We'll calculate your bedtime based on sunrise."

    # Prompt for user options
    sleep_time = input("How many hours of sleep would you like? ")
    city = raw_input("What city are you sleeping in? ")

    # Retrieve info
    today = datetime.date.today()
    word_date = datetime.date.ctime(today)
    # Calculate
    # Return bedtime


if __name__ == main:
    try:
        main()
    except Exception as e:
        import pdb
        pdb.set_trace()
        print 'Entered debugger with Exception e.'
    finally:
        exit()
