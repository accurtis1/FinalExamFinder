B1 = "Wednesday, December 14th from 7:30-9:30 am"
C1 = "Thursday, December 15th from 7:30-9:30 am"
D1 = "Friday, December 16th from 7:30-9:30 am"
A2 = "Tuesday, December 13th from 9:45-11:45 am"
B2 = "Wednesday, December 14th from 9:45-11:45 am"
C2 = "Thursday, December 15th from 9:45-11:45 am"
D2 = "Friday, December 16th from 9:45-11:45 am"
A3 = "Tuesday, December 13th from 12:00-2:00 pm"
B3 = "Wednesday, December 14th from 12:00-2:00 pm"
C3 = "Thursday, December 15th from 12:00-2:00 pm"
D3 = "Friday, December 16th from 12:00-2:00 pm"
A4 = "Tuesday, December 13th from 2:15-4:15 pm"
B4 = "Wednesday, December 14th from 2:15-4:15 pm"
C4 = "Thursday, December 15th from 2:15-4:15 pm"
D4 = "Friday, December 16th from 2:15-4:15 pm"
A5 = "Tuesday, December 13th from 4:30-6:30 pm"
B5 = "Wednesday, December 14th from 4:30-6:30 pm"
C5 = "Thursday, December 15th from 4:30-6:30 pm"
A6 = "Tuesday, December 13th from 7:00-9:00 pm"
B6 = "Wednesday, December 14th from 7:00-9:00 pm"
C6 = "Thursday, December 15th from 7:00-9:00 pm"

print("Please enter your class information.")

course_name = []
course_credit = []
course_days = []
course_time = []
course_AMPM = []

def finalExam():
    run = True
    while run:
        name = input("\nWhat is the name of your class? (Or type q to quit) >>> ").upper()
        if name == "Q":
            run = False
        else:
            course_name.append(name)
            credit = input("How many credit hours is your class? >>> ")
            course_credit.append(credit)
            days = input("What days are your class? (i.e. MWF or TR [R = Thursday]) >>> ").upper()
            course_days.append(days)
            time = input("What time does your class start? (i.e. 1230 or 0800) >>> ")
            course_time.append(time)
            if time == "0800":
                amOrPm = input("Is this an AM class or a PM class? >>> ").upper()
                course_AMPM.append(amOrPm)
            continue
        for i in course_name:
            if i == "MATH 201" or i == "MATH201":
                date = (C5)
                if date == C5:
                    print("\nThe final exam for class {} will be a common final on {}.".format(name, date))
                    run = False
        if time == "0800":
            if amOrPm == "AM":
                if credit == "2":
                    if days == "TR":
                        date = (B1)
                    elif days == "MWF" or days == "MW" or days == "WF":
                        date = (C1)
                    else:
                        print("\nOops! There was a problem with the days you entered. Please check your course details.")
                        continue
                elif credit == "3":
                    if days == "TR":
                        date = (B1)
                    elif days == "MWF":
                        date = (C1)
                    else:
                        print("\nOops! There was a problem with the days you entered. Please check your course details.")
                        continue
                elif credit == "4":
                    date = (B1)
                elif credit == "5":
                    date = (C1)
                else:
                    print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                    continue
            elif amOrPm == "PM":
                if days == "TR":
                    date = (A6)
                elif days == "MW":
                    date = (B6)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            else:
                print("\nPlease enter AM or PM.")
                continue
        elif time == "0900":
            if credit == "2" or credit == "4":
                date = (D1)
            elif credit == "3":
                if days == "MWF":
                    date = (D1)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "0930":
            if credit == "2" or credit == "4":
                date = (D2)
            elif credit == "3":
                if days == "MWF":
                    date = (D2)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "1000":
            if credit == "2" or credit == "4" or credit == "5":
                date = (B2)
            elif credit == "3":
                if days == "MWF":
                    date = (B2)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "1100":
            if credit == "2":
                if days == "MWF" or days == "MW" or days == "WF":
                    date = (C2)
                elif days == "TR":
                    date = (A2)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "3":
                if days == "MWF":
                    date = (C2)
                elif days == "TR":
                    date = (A2)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "4":
                if days == "TR":
                    date = (A2)
                elif days == "MWF":
                    date = (C2)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "5":
                date = (C2)
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "1200":
            if credit == "2":
                date = (B3)
            elif credit == "3":
                if days == "MWF":
                    date = (B3)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "4" or credit == "5":
                date = (B3)
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "1230":
            if credit == "2" or credit == "4":
                date = (A3)
            elif credit == "3":
                if days == "TR":
                    date = (A3)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "0100":
            if credit == "2":
                if days == "TR":
                    date = (A3)
                elif days == "MWF" or days == "MW" or days == "WF":
                    date = (D3)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "3":
                if days == "MWF":
                    date = (D3)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "4":
                date = (D3)
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "0200":
            if credit == "2":
                if days == "TR":
                    date = (C3)
                elif days == "MWF" or days == "MW" or days == "WF":
                    date = (C4)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "3":
                if days == "TR":
                    date = (C3)
                elif days == "MWF":
                    date = (C4)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "4":
                date = (C3)
            elif credit == "5":
                date = (C4)
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "0300":
            if credit == "2" or credit == "4":
                date = (B4)
            elif credit == "3":
                if days == "MWF":
                    date = (B4)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "0330":
            if credit == "2" or credit == "3":
                if days == "TR":
                    date = (A4)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "4":
                date = (A4)
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "0400":
            if credit == "2" or credit == "4":
                date = (D4)
            elif credit == "3":
                if days == "MWF":
                    date = (D4)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            else:
                print("\nOops! There was a problem with the days you entered. Please check your course details.")
                continue
        elif time == "0500":
            if credit == "2":
                if days == "TR":
                    date = (A5)
                elif days == "MWF" or days == "MW" or days == "WF":
                    date = (B5)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "3":
                if days == "TR":
                    date = (A5)
                else:
                    print("\nOops! There was a problem with the days you entered. Please check your course details.")
                    continue
            elif credit == "4":
                date = (A5)
            elif credit == "5":
                date = (B5)
            else:
                print("\nOops! There was a problem with the credits you entered. Please check your course details.")
                continue
        elif time == "0630":
            date = ("Monday, December 12th at 6:30 pm")
            if days == "T" or days == "TR":
                date = (A6)
            elif days == "W":
                date = (B6)
            elif days == "R":
                date = (C6)
            elif days == "M" or days == "MW":
                print("\nThe final exam for class "+name+" is on "+date+".")
                if credit == "1":
                    print("\nYou will have to compensate for lost instructional time in "+name+" by meeting at 6:30-7:25 pm on Monday, December 12th.")
                    break
                elif credit == "2":
                    print("\nYou will have to compensate for lost instructional time in "+name+" by meeting at 6:30-8:25 pm on Monday, December 12th.")
                    break
                elif credit == "3":
                    print("\nYou will have to compensate for lost instructional time in "+name+" by meeting at 6:30-9:30 pm (including one 15 min. break) on Monday, December 12th.")
                    break
                elif credit == "4":
                    print("\nYou will have to compensate for lost instructional time in "+name+" by meeting at 06:30-10:15 pm (including one 10 min. break) on Monday, December 12th.")
                    break
                else:
                    print("\nThere was a problem with the credits you entered. Please check your course details.")
                    break
            else:
                print("\nOops! There was a problem with the days you entered. Please check your course details.")
                continue
        else:
            print("\nOops! Sorry, there was a problem with the time you entered. Please check your course details.")
            continue
        print("\nThe final exam for class "+name+" is on "+date+".")
        break

    print(course_name)
    print(course_credit)
    print(course_days)
    print(course_time)
    print(course_AMPM)
finalExam()
