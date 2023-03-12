def initialize():
    '''Initializes the global variables needed for the simulation'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    global resting_timer

    global last_finished
    global bored_with_stars

    global cur_star
    global cur_star_activity
    global num_stars
    global star_active

    global tired

    global start_time
    global start_time_list

    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None
    star_active = False
    num_stars = 0

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0
    resting_timer = 0

    tired = False

    start_time = 0
    start_time_list = []

    cur_time = 0

    last_finished = -1000



def star_can_be_taken(activity):
    '''Return True iff a star can be used to get more hedons for activity activity
     A star can only be taken if no time passed between the star’s being offered
     and the activity, and the user is not bored with stars, and the star was
     offered for activity activity.
    '''

    if start_time == cur_time:
        if not bored_with_stars:
            if star_active and cur_star == activity:
                return True
    return False


def perform_activity(activity, duration):
    '''Modify/update variables after performing functions

    '''
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    global resting_timer

    global last_finished
    global bored_with_stars

    global tired

    #if the user is not doing any specified activity
    if activity != "resting" and activity != "running" and activity != "textbooks":
        return

    cur_hedons += estimate_hedons_delta(activity, duration)
    cur_health += estimate_health_delta(activity, duration)

    if activity == "resting":
      resting_timer += duration
    else:
      resting_timer = 0

    if last_activity == activity: # If the same activity is continously performed
        last_activity_duration += duration
    else:
        last_activity_duration = duration
    last_activity = activity
    cur_time += duration

    if resting_timer >= 120 or resting_timer == cur_time:
        tired = False

    


def get_cur_hedons():
    '''Return the number of hedon the user has accumulated so far'''
    return cur_hedons

def get_cur_health():
    '''Return the number of health the user has accumulated so far'''
    return cur_health

def offer_star(activity):
    '''Cause the activity specified in the argument to gain
    3 additional hedons for the first 10 consecutive minutes

    Arguments:
    activity: assumed to be a string'''
    global bored_with_stars
    global cur_star
    global num_stars
    global star_active
    global start_time_list
    global start_time

    start_time_list.append(cur_time)
    start_time = cur_time

    if len(start_time_list) >= 3 and start_time_list[-1] - start_time_list[-3] < 120:
        bored_with_stars = True
    else:
        cur_star = activity
        star_active = True

def most_fun_activity_minute():
    global tired

    if tired == True and not star_active:
        return "resting"
    elif star_active:
        return cur_star
    else:
        return "running"

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    global tired
    if resting_timer >= 120 or last_activity == None or cur_time == resting_timer: # if the person isn't tired or they just started
        if activity == "running":
            return 10 # gains hedons for 10 mins
        elif activity == "textbooks":
            return 20 # gains hedons for 20 mins
        tired = False
    else:
        tired = True
        return 0 # doesn't gain any hedons

def get_effective_minutes_left_health(activity):
    '''Return the number of minutes during which the user will get the full
    amount of health for activity activity'''
    if last_activity != activity: # if effective minutes has been refreshed
        if activity == "running":
            return 180 # effective mins is 180
        else:
            return 0 # resting and textbooks don't have effective minutes
    elif last_activity == activity and activity == "running":
        # time diff between 180 and last running time
        # Can't be less than zero if last activity was longer than 180
        return max(0, 180 - last_activity_duration)
    else:
        return 0 # for resting and textbooks

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    global cur_star
    global star_active
    global tired
    global resting_timer

    gained_hedons = 0

    # Star bonus calculation
    if star_can_be_taken(activity) and activity != "resting":
            gained_hedons += min(duration * 3, 30)
            # if duration <= 10:
            #     gained_hedons += duration * 3
            # else:
            #     gained_hedons += 30

    if activity == "running":

        # gained_hedons = min(duration)
        # if the duration specified is more than the time left
        if duration > get_effective_minutes_left_hedons(activity):
            # the gained hedons after all time has been used up
            gained_hedons += (duration - get_effective_minutes_left_hedons(activity)) * -2
            # if there was some time left
            if get_effective_minutes_left_hedons(activity) > 0:
                gained_hedons += get_effective_minutes_left_hedons(activity) * 2
        else: # if the duration is less than time left
            gained_hedons += duration * 2

    elif activity == "textbooks":
        # if the duration specified is more than time left
        if duration > get_effective_minutes_left_hedons(activity):
            # gained hedons after all time has been used up
            gained_hedons += (duration - \
            get_effective_minutes_left_hedons(activity)) * -1
            if tired:
                gained_hedons += (duration - \
                get_effective_minutes_left_hedons(activity)) * -1
            # if there was some time left
            if get_effective_minutes_left_hedons(activity) > 0:
                gained_hedons += get_effective_minutes_left_hedons(activity)
        else: # if duration is less than time left
            gained_hedons += duration

    tired = True
    star_active = False
    cur_star = None
    return gained_hedons


def estimate_health_delta(activity, duration):
    ''' Return the amount of health the user would get for performing activity
    activity for duration minutes'''
    gained_health = 0

    if activity == "running":
        if duration > get_effective_minutes_left_health(activity):
            gained_health += duration - \
            get_effective_minutes_left_health(activity)
            if get_effective_minutes_left_health(activity) > 0:
                gained_health += get_effective_minutes_left_health(activity) * 3
        else:
            gained_health += duration * 3

    elif activity == "textbooks": # textbooks always increases hedons
        gained_health += duration * 2
    return gained_health


################################################################################

if __name__ == '__main__':
    
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10

    print("\n 2nd TESTS")	

    initialize()
    print(get_cur_health()) # 0
    print(get_cur_hedons()) # 0
    perform_activity("textbooks", 40)
    print(get_cur_health()) # 80 = 2 * 40
    print(get_cur_hedons()) # 0 = 20 - 20
    offer_star("textbooks")
    perform_activity("textbooks", 12)
    print(get_cur_health()) # 104 = 80 + 12 * 2
    print(get_cur_hedons()) # 6 = 0 + -2 * 12 + 10 * 3 

    print("\n OTHER CASES")

	# possible test cases (from FAQ):
    initialize()
    assert get_cur_health() == 0
    assert get_cur_hedons() == 0
    # starting an activity again right after finishing
    initialize()
    perform_activity("running", 180)
    perform_activity("resting", 1)
    perform_activity("running", 180)
    assert get_cur_health() == 1080

    # offer 3 stars within 1h59 and 2h
    # should give bored_with_stars == True and bored_with_stars == False
    initialize()
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    perform_activity("resting", 59)
    offer_star("running")
    assert bored_with_stars == True

    initialize()
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    assert bored_with_stars == False

    # taking a star for an activity, not using the full 10 mins, and starting again
    initialize()
    offer_star("running")
    perform_activity("running", 5)
    perform_activity("running", 5)
    assert get_cur_hedons() == 15
    
    # hedons gained if another star is offered after bored_with_stars == True
    initialize()
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    perform_activity("resting", 59)
    offer_star("running")
    perform_activity("textbooks", 1)
    assert get_cur_hedons() == 1

    # Edge Case Testing
    # Testing 180 minutes for both textbook and running
    initialize()
    perform_activity("running", 180)
    assert get_cur_health() == 540
    assert get_cur_hedons() == -320

    initialize()
    perform_activity("textbooks", 180)
    assert get_cur_health() == 360
    assert get_cur_hedons() == -140

    # Testing stars edge cases    
    # 5 minutes star
    initialize()
    offer_star("running")
    perform_activity("running", 5)
    assert get_cur_hedons() == 25
    
    # 10 minutes star
    initialize()
    offer_star("running")
    perform_activity("running", 10)
    assert get_cur_hedons() == 50

    # 20 minutes star
    initialize()
    offer_star("running")
    perform_activity("running", 20)
    assert get_cur_hedons() == 30

    # within 120 minutes stars
    # 121 minutes star 
    initialize()
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    perform_activity("resting", 59)
    offer_star("running")
    assert bored_with_stars == True
    assert get_cur_hedons() == 0
    assert get_cur_health() == 0
    assert tired == False
    perform_activity("running", 20)
    assert get_cur_health() == 60
    assert get_cur_hedons() == 0
    assert tired == True

    initialize()
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    assert bored_with_stars == False
    assert get_cur_hedons() == 0
    assert get_cur_health() == 0
    assert tired == False

    initialize()
    offer_star("running")
    perform_activity("resting", 60)
    offer_star("running")
    perform_activity("resting", 61)
    offer_star("running")
    assert bored_with_stars == False
    assert tired == False
    assert get_cur_hedons() == 0
    assert get_cur_health() == 0

    # Tired case
    initialize()
    perform_activity("running", 9)
    assert get_cur_health() == 27
    assert get_cur_hedons() == 18
    assert tired == True
    assert most_fun_activity_minute() == "resting"
    perform_activity("textbooks", 10)
    assert get_cur_health() == 47
    assert get_cur_hedons() == -2
    assert tired == True
    assert most_fun_activity_minute() == "resting"

    # Continous Running NonStop
    # FAQ
    initialize()
    perform_activity("running", 120)
    perform_activity("running", 30)
    perform_activity("running", 50)
    assert get_cur_health() == 560

    # Own
    initialize()
    perform_activity("running", 200)
    assert get_cur_health() == 560
    assert get_cur_hedons() == -360
    assert tired == True
    perform_activity("running", 200)
    assert get_cur_health() == 760
    assert get_cur_hedons() == -760
    assert most_fun_activity_minute() == "resting"


    # Using a star after tiredness
    initialize()
    perform_activity("running", 200)
    assert get_cur_health() == 560
    assert get_cur_hedons() == -360
    assert tired == True
    offer_star("running")
    perform_activity("running", 10)
    assert get_cur_health() == 570
    assert get_cur_hedons() == -350


    # perform_activity("running", 150)
    initialize()
    perform_activity("running", 150)
    assert get_cur_health() == 450 
    assert get_cur_hedons() == -260
    assert tired == True
    assert most_fun_activity_minute() == "resting"

    # Special Case
    initialize()
    perform_activity("running", 90)
    offer_star("running")
    perform_activity("running", 110)
    assert get_cur_health() == 560

    # Not doing anything
    initialize()
    perform_activity("something", 1000)
    assert get_cur_health() == 0
    assert get_cur_hedons() == 0
    assert tired == False
    assert star_active == False
    assert most_fun_activity_minute() == "running"
    perform_activity("RUNNING", 1000)
    assert get_cur_health() == 0
    assert get_cur_hedons() == 0
    assert tired == False
    assert star_active == False
    assert most_fun_activity_minute() == "running"

    # Time elapse after offered stars
    initialize()
    offer_star("running")
    assert star_can_be_taken("running") == True
    perform_activity("resting", 10)
    assert star_can_be_taken("running") == False

    # Tired tests
    initialize()
    perform_activity("running", 10)
    assert tired == True
    perform_activity("resting", 129)
    assert tired == False
    perform_activity("running", 20)
    perform_activity("running", 10)
    assert tired == True
    perform_activity("resting", 10)
    assert tired == True 
    perform_activity("resting", 100)
    assert tired == True 
    perform_activity("resting", 5)
    assert tired == True 
    perform_activity("resting", 4)
    assert tired == True
    perform_activity("resting", 1)
    assert tired == False

    # Interrupted resting
    perform_activity("running", 10)
    assert tired == True
    perform_activity("resting", 10)
    assert tired == True 
    perform_activity("resting", 100)
    assert tired == True 
    perform_activity("running", 1)
    perform_activity("resting", 5)
    assert tired == True 
    perform_activity("resting", 4)
    assert tired == True
    perform_activity("resting", 1)
    assert tired == True
