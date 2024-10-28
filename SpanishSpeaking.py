import random
from playsound import playsound
from sys import exit

# Program by Katarzyna Zawistowska 2020

''' This program was created to help student study for spanish. 
   There are two sections of this code: 
		Practice Mode 
		and Assignment Mode.
    Practice mode will repeat all questions in a random order until 
    you turn off the program by pressing x.
    Assignment mode will ask all questions in a random order by topic once
    and tell you when you are done with a short congratulation message.'''


def main():  # main program. this will decide things at the beginning
    # variables
    media_questions = [  # all questions for media topic
        "./assets/audio/media/media1.mp3",
        "./assets/audio/media/media2.mp3",
        "./assets/audio/media/media3.mp3",
        "./assets/audio/media/media4.mp3",
        "./assets/audio/media/media5.mp3",
        "./assets/audio/media/media6.mp3",
        "./assets/audio/media/media7.mp3",
        "./assets/audio/media/media8.mp3",
        "./assets/audio/media/media9.mp3",
        "./assets/audio/media/media10.mp3",
        "./assets/audio/media/media11.mp3"
    ]
    family_questions = [  # all questions for family topic
        "./assets/audio/family/family1.mp3",
        "./assets/audio/family/family2.mp3",
        "./assets/audio/family/family3.mp3",
        "./assets/audio/family/family4.mp3",
        "./assets/audio/family/family5.mp3",
        "./assets/audio/family/family6.mp3",
        "./assets/audio/family/family7.mp3",
        "./assets/audio/family/family8.mp3",
        "./assets/audio/family/family9.mp3"
    ]
    job_studies_questions = [  # all questions for part time job and study topic
        "./assets/audio/job/job1.mp3",
        "./assets/audio/job/job2.mp3",
        "./assets/audio/job/job3.mp3",
        "./assets/audio/job/job4.mp3",
        "./assets/audio/job/job5.mp3",
        "./assets/audio/job/job6.mp3",
        "./assets/audio/job/job7.mp3",
        "./assets/audio/job/job8.mp3?",
        "./assets/audio/job/job9.mp3",
        "./assets/audio/job/job10.mp3",
        "./assets/audio/job/job11.mp3",
        "./assets/audio/job/job12.mp3"
    ]
    holidays_travel_questions = [  # all questions for holidays and travel topic
        "./assets/audio/holidays/holidays1.mp3",
        "./assets/audio/holidays/holidays2.mp3",
        "./assets/audio/holidays/holidays3.mp3",
        "./assets/audio/holidays/holidays4.mp3",
        "./assets/audio/holidays/holidays5.mp3",
        "./assets/audio/holidays/holidays6.mp3",
        "./assets/audio/holidays/holidays7.mp3",
        "./assets/audio/holidays/holidays8.mp3",
        "./assets/audio/holidays/holidays9.mp3",
        "./assets/audio/holidays/holidays10.mp3",
        "./assets/audio/holidays/holidays11.mp3",
        "./assets/audio/holidays/holidays12.mp3",
        "./assets/audio/holidays/holidays13.mp3",
        "./assets/audio/holidays/holidays14.mp3"
    ]
    lifestyles_questions = [  # all questions for lifestyle topic
        "./assets/audio/lifestyle/lifestyle1.mp3",
        "./assets/audio/lifestyle/lifestyle2.mp3",
        "./assets/audio/lifestyle/lifestyle3.mp3",
        "./assets/audio/lifestyle/lifestyle4.mp3",
        "./assets/audio/lifestyle/lifestyle5.mp3",
        "./assets/audio/lifestyle/lifestyle6.mp3",
        "./assets/audio/lifestyle/lifestyle7.mp3",
        "./assets/audio/lifestyle/lifestyle8.mp3",
        "./assets/audio/lifestyle/lifestyle9.mp3",
        "./assets/audio/lifestyle/lifestyle10.mp3",
        "./assets/audio/lifestyle/lifestyle11.mp3",
        "./assets/audio/lifestyle/lifestyle12.mp3",
        "./assets/audio/lifestyle/lifestyle13.mp3",
        "./assets/audio/lifestyle/lifestyle14.mp3",
        "./assets/audio/lifestyle/lifestyle15.mp3",
        "./assets/audio/lifestyle/lifestyle16.mp3",
        "./assets/audio/lifestyle/lifestyle17.mp3",
        "./assets/audio/lifestyle/lifestyle18.mp3",
        "./assets/audio/lifestyle/lifestyle19.mp3"
    ]
    citizenship_questions = [  # all questions for citizenship topic
        "./assets/audio/citizenship/citizenship1.mp3",
        "./assets/audio/citizenship/citizenship2.mp3",
        "./assets/audio/citizenship/citizenship3.mp3",
        "./assets/audio/citizenship/citizenship4.mp3",
        "./assets/audio/citizenship/citizenship5.mp3",
        "./assets/audio/citizenship/citizenship6.mp3",
        "./assets/audio/citizenship/citizenship7.mp3",
        "./assets/audio/citizenship/citizenship8.mp3"
    ]
    school_questions = [  # all questions for school topic
        "./assets/audio/school/school1.mp3",
        "./assets/audio/school/school2.mp3",
        "./assets/audio/school/school3.mp3",
        "./assets/audio/school/school4.mp3",
        "./assets/audio/school/school5.mp3",
        "./assets/audio/school/school6.mp3",
        "./assets/audio/school/school7.mp3",
        "./assets/audio/school/school8.mp3",
        "./assets/audio/school/school9.mp3",
        "./assets/audio/school/school10.mp3",
        "./assets/audio/school/school11.mp3",
        "./assets/audio/school/school12.mp3",
        "./assets/audio/school/school13.mp3",
        "./assets/audio/school/school14.mp3",
        "./assets/audio/school/school15.mp3",
        "./assets/audio/school/school16.mp3",
        "./assets/audio/school/school17.mp3",
        "./assets/audio/school/school18.mp3",
        "./assets/audio/school/school19.mp3",
        "./assets/audio/school/school20.mp3",
        "./assets/audio/school/school21.mp3",
        "./assets/audio/school/school22.mp3",
        "./assets/audio/school/school23.mp3",
        "./assets/audio/school/school24.mp3",
        "./assets/audio/school/school25.mp3"
    ]
    topic_list = [  # all topic lists will be inside of this list
        media_questions,
        family_questions,
        job_studies_questions,
        holidays_travel_questions,
        lifestyles_questions,
        citizenship_questions,
        school_questions
    ]

    # title and Introduction to this program.
    print("\t\t\t  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t\t    SPANISH SPEAKING ASSIGNMENT PROGRAM")
    print("\t\t\t  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles_questions, citizenship_questions, school_questions)


def practice_mode(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school):
    ''' Introduction to practice mode which will be displayed whenever this mode is
       turned on. It will make a quick guide on what you will need to do to successfully
       run this code and navigate around this mode. '''
    print("\n\n\n")
    print("\t\t\t\t   ~~~~~~~~~~~~~~~~~~~")
    print("\t\t\t\tWelcome to Practice Mode!")
    print("\t\t\t\t   ~~~~~~~~~~~~~~~~~~~")
    print("\n\nIn this mode you will be asked questions based on the topic you chose!")
    print("Try answering every question as best as you can.")
    print("Hit enter when you're ready for the next question!")
    print("If you want to exit practice mode first pick any of the topics,")
    print("then press 'X' and then the Enter key on your keyboard.\n\n")
    print(" Let's begin!")
    print(" ~~~~~~~~~~~~")
    # actual choices are starting to happen from here on wards

    print("\n\nPlease pick which topic you want to work on:")
    print("\t1. Media")
    print("\t2. Family and friends")
    print("\t3. Part time Jobs and studying")
    print("\t4. Holidays/travel")
    print("\t5. Lifestyle/ Healthy living")
    print("\t6. Citizenship")
    print("\t7. School")
    print("\t8. Both of your topics.")
    continue_ = False
    while not continue_:  # loop starts it will loop until continue is True
        try:
            answer = int(input("\n>>> "))  # this is the input this loop is validating
        except ValueError:
            print("Please enter a number.")  # if value error occurred this will be displayed
        else:  # if no value errors the following will be checked.
            if answer in [1, 2, 3, 4, 5, 6, 7, 8]:
                continue_ = True  # ends loop
            else:  # displays a message you picked the wrong numbers
                print("Hmm, seems like you entered a weird number. Please try again.")

    if answer in [1,2,3,4,5,6,7]:  # this allows the choices 1-7 if statements only be for title and topic (less code)
        if answer == 1:  # media questions
            print("\n\n~~~~~~~")
            print("MEDIA")
            print("~~~~~~~")
            topic = topic_list[0]

        elif answer == 2:  # family questions
            print("\n\n~~~~~~~~")
            print("FAMILY")
            print("~~~~~~~~")
            topic = topic_list[1]

        elif answer == 3:  # media questions
            print("\n\n~~~~~")
            print("JOBS")
            print("~~~~~")
            topic = topic_list[2]

        elif answer == 4:  # media questions
            print("\n\n~~~~~~~~")
            print("HOLIDAYS")
            print("~~~~~~~~")
            topic = topic_list[3]

        elif answer == 5:  # media questions
            print("\n\n~~~~~~~~~~")
            print("LIFESTYLE")
            print("~~~~~~~~~~")
            topic = topic_list[4]

        elif answer == 6:  # media questions
            print("\n\n~~~~~~~~~~~~")
            print("CITIZENSHIP")
            print("~~~~~~~~~~~~")
            topic = topic_list[5]

        elif answer == 7:  # media questions
            print("\n\n~~~~~~~~")
            print("SCHOOL")
            print("~~~~~~~~")
            topic = topic_list[6]

        answer = ""  # sets answer to an empty string
        while answer.upper() != "X":  # will generate random questions until input is 'x'
            rand_int = random.randint(0, len(topic) - 1)
            playsound(topic[rand_int])  # picks random question based on rand_int
            answer = input("\n>>> ")

    else:  # while this prevents an error from occurring if the lines 209-213 were after this bit
        if answer == 8:
            print("\n\n~~~~~~~")
            print("BOTH")
            print("~~~~~~~")

            print("\n\nPlease pick your two topics. Press enter after each one.")
            print("\t1. Media")
            print("\t2. Family")
            print("\t3. Job")
            print("\t4. Holidays")
            print("\t5. Lifestyle")
            print("\t6. Citizenship")
            print("\t7. School")
            continue_ = False
            choices = []
            while not continue_:  # loop starts it will loop until continue is True
                turn = 0
                while turn != 2:
                    try:
                        answer = int(input("\n>>> "))  # this is the input this loop is validating
                    except ValueError:
                        print("Please enter a number.")  # if value error occurred this will be displayed
                    else:  # if no value errors the following will be checked.
                        if answer in [1, 2, 3, 4, 5, 6, 7]:  # checks if its an appropriate answer
                            if answer in choices:  # if you already typed this number do
                                print("Hmm, seems like you've already picked this topic.")
                            else:  # otherwise continue with the loop
                                choices.append(answer)  # appends your answer to the list
                                turn += 1  # sets turn to turn + 1
                        else:  # displays a message you picked the wrong numbers
                            print("Hmm, seems like you entered a weird number. Please try again.")
                continue_ = True

            topics = []
            for index in range(2):
                topics.append(topic_list[choices[index]-1])
            # start loop here later
            answer = ""  # sets answer yo an empty string
            while answer.upper() != "X":  # starts a loop that will be broken when answer = X
                rand_int = random.randint(1, 2)
                if rand_int == 1:
                    topic = topics[0]
                    rand_int = random.randint(0, len(topic) - 1)
                    playsound(topic[rand_int])  # picks random question based on rand_int
                    answer = input("\n>>> ")
                if rand_int == 2:
                    topic = topics[1]
                    rand_int = random.randint(0, len(topic) - 1)
                    playsound(topic[rand_int])  # picks random question based on rand_int
                    answer = input("\n>>> ")

    decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)  # if x was pressed go to decision function


def assignment_mode(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school):
    print("\n\n\n")
    print("\t\t\t\t   ~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t\t\tWelcome to Assignment mode!")
    print("\t\t\t\t   ~~~~~~~~~~~~~~~~~~~~~")
    print("\n\nIn this mode you will be asked questions based on your 2 topics.")
    print("You will be assesed on one of the topics first and then on the second one.")
    print("The questions will be asked in a random order but only asked once.")
    print("Try keeping track of what questions you need to work on.")
    print("Hit enter when you're ready for the next question!")
    print("If you want to exit assignment mode first pick any of the topics,")
    print("then press 'X' and then the Enter key on your keyboard.\n\n")
    print(" Let's begin!")
    print(" ~~~~~~~~~~~~")

    print("\n\nPlease pick your two topics. Press enter after each one.")
    print("\t1. Media")
    print("\t2. Family and friends")
    print("\t3. Part time Jobs and studying")
    print("\t4. Holidays/travel")
    print("\t5. Lifestyle/ Healthy living")
    print("\t6. Citizenship")
    print("\t7. School")
    continue_ = False
    choices = []  # will make sure you don't pick the same topic twice'
    while not continue_:  # loop starts it will loop until continue is True
        turn = 0
        while turn != 2:
            try:
                answer = int(input("\n>>> "))  # this is the input this loop is validating
            except ValueError:
                print("Please enter a number.")  # if value error occurred this will be displayed
            else:  # if no value errors the following will be checked.
                if answer in [1, 2, 3, 4, 5, 6, 7]:  # checks if its an appropriate answer
                    if answer in choices:  # if you already typed this number do
                        print("Hmm, seems like you've already picked this topic.")
                    else:  # otherwise continue with the loop
                        choices.append(answer)  # appends your answer to the list
                        turn += 1  # sets turn to turn + 1
                else:  # displays a message you picked the wrong numbers
                    print("Hmm, seems like you entered a weird number. Please try again.")
        continue_ = True

    topics = []
    for index in range(2):  # loops twice and appends appropriate list
        topics.append(topic_list[choices[index] - 1])

    topic1 = topics[0]  # separates your two topics into two variables
    topic2 = topics[1]
    list1 = False
    list2 = False
    continue_ = False
    list_ = []
    while continue_ != True:  # starts main loop
        print("\n\n\n")
        rand_int = random.randint(1, 2)  # random num picks the first topic
        list_.append(rand_int)  # stores the random numbers
        if rand_int == 1 and list1 == False:
            list1 = True  # You will not be able to get topic 1 the second time
            answer = " "  # sets answer to an empty string
            num_list = []
            continue_1 = False
            while continue_1 != True:  # while the answer isn't X the loop will loop answer.upper() != "X" or
                if len(topic1) == len(num_list):  # if all questions were asked
                    # while continue_2 != True:
                    print("\n\nWell done! Topic complete")
                    answer = input("Press Enter to continue or X to exit\n>>> ")
                    if answer.upper() == "X":
                        decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)
                    continue_1 = True
                max = len(topic1) - 1  # the random number will be within the length of the list
                rand_int = random.randint(0, max)  # the number will be in the range of indices
                if rand_int not in num_list:  # if the random number wasn't already called it may proceed
                    num_list.append(rand_int)  # makes sure the question corresponding this index isn't called again
                    playsound(topic1[rand_int])  # picks random question based on rand_int
                    answer = input("\n>>> ")
                    if answer.upper() == "X":
                        decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)

        if rand_int == 2 and list2 == False:
            list2 = True
            num_list2 = []
            answer = " "
            continue_1 = False
            while continue_1 != True:
                if len(topic2) == len(num_list2):  # if all questions were asked
                    # while continue_3 != True:
                    print("\n\nWell done! Topic complete!")
                    answer = input("Press Enter to continue or X to exit\n>>> ")
                    if answer.upper() == "X":
                        decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)
                    continue_1 = True
                max = len(topic2) - 1  # the random number will be within the length of the list
                rand_int = random.randint(0, max)  # the number will be in the range of indices
                if rand_int not in num_list2:  # if the random number wasn't already called it may proceed'
                    num_list2.append(rand_int)  # makes sure the question corresponding this index isn't called again'
                    playsound(topic2[rand_int])  # picks random question based on rand_int
                    answer = input("\n>>> ")
                    if answer.upper() == "X":
                        decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)

        #if answer.upper() == "X":
            #decision(media_questions, family_questions, topic_list)
        if 1 in list_ and 2 in list_:
            print("\nWell done! Assignment Mode complete!")
            continue_ = True
    decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)


def decision(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school):
    print("\n\n\nWelcome to the 'SPANISH SPEAKING ASSIGNMENT PROGRAM'!")
    print("This program will help you study for your spanish speaking assignment.")
    print("Follow the instructions on the screen to proceed.")
    print("\nPlease wait for '>>>' to appear after the question was spoken.")
    print("Only then you can continue or exit the mode using 'X'.")
    print("\nIf you encounter any problems please read the README.txt file.")
    continue_ = False
    while not continue_:
        try:
            answer = int(input("\n\nPlease pick which mode you'd like to use:\n	1. Practice Mode\n	2. Assignment Mode\n	3. Exit\n\n>>> "))
        except ValueError:
            print("Hmm, seems like you haven't entered a correct value. Please try again")
        else:
            if answer not in [1, 2, 3]:
                print("Please enter 1, 2 or 3 only.")
            else:
                continue_ = True
    if answer == 1:
        practice_mode(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)
    elif answer == 2:
        assignment_mode(media_questions, family_questions, topic_list, job_studies_questions, holidays_travel_questions, lifestyles, citizenship, school)
    if answer == 3:
        print(" ")
        exit() # closes the program


main()  # calls for main function making it run.
input()
