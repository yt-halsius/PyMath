#Math.py version 23.1.2.1
#Created to offer some stimulation that the Swedish School system could'nt offer.
#This is free and unencumbered software released into the public domain.
###########################################################################
################License: Unlicense ########################################
##Anyone is free to copy, modify, publish, use, compile, sell, or        ##
##distribute this software, either in source code form or as a compiled  ##
##binary, for any purpose, commercial or non-commercial, and by any      ##
##means.                                                                 ##
##                                                                       ##
##In jurisdictions that recognize copyright laws, the author or authors  ##
##of this software dedicate any and all copyright interest in the        ##
##software to the public domain. We make this dedication for the benefit ##
##of the public at large and to the detriment of our heirs and           ##
##successors. We intend this dedication to be an overt act of            ##
##relinquishment in perpetuity of all present and future rights to this  ##
##software under copyright law.                                          ##
##                                                                       ##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,        ##
##EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF     ##
##MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. ##
##IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR      ##
##OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,  ##
##ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR  ##
##OTHER DEALINGS IN THE SOFTWARE.                                        ##
##                                                                       ##
##For more information, please refer to <http://unlicense.org/>          ##
###########################################################################
###########################################################################
#Original creds to: https://gist.github.com/cwil323/9b1bfd25523f75d361879adfed550be2
#
#
import random
import sys
import os
import time
end_one = 1
end_two = 1
runonce = 0
result = None
    
def display_intro():
    title = "** Ett enkelt Matte-Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))
    print()


def display_menu():
    os.system('cls')
    display_intro()
    print ("*" * 12,"Välj räknesätt nedan", "*" * 12)
    menu_list = ["1. Addition", "2. Subtration", "3. Multiplikation", "4. Division (Heltal)", "5. Visa resultat", "6. Ändra gränser", "7. Avsluta"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])
    print(menu_list[5])
    print(menu_list[6])


def display_separator():
    print("-" * 24)


def get_user_input():
    try:
        user_input = int(input("Ange ditt val: "))
    except ValueError:
        user_input = None
    if user_input != None:
        if user_input > 7 or user_input <= 0 or user_input == " ":
            print("Felaktigt menyval, försök igen:")
            main()
        else:
            return user_input
    else:
        print("Felaktigt menyval, försök igen:")
        #Rerun menu creation on faulty menu option
        main()
    
def add_limits():
#Clarify that the varible names are global not local to function as is default for python
        global runonce
        global end_one
        global end_two
#In the case that user input is submitted empty we get value error, then we need to handle it
        try:
            end_one = int(input("Ange sluttal 1 (>3=):"))
        except ValueError:
            end_one = None
        if end_one != None and end_one >= 3:
            print ("Sluttal 1 OK")
            print ()
            try:
                end_two = int(input("Ange sluttal 2 (>=3 && <= sluttal 1):"))
            except ValueError:
                end_two = None
        if end_two != None and end_two >= 3 and end_two <= end_one:
            print ("Sluttal 2 OK")
            print ()
            print ("Spelet börjar strax")
            time.sleep(2)
            runonce = runonce +1
            main()
            return runonce, end_one, end_two   
        else:
            runonce = 0
            print ("Någonting har blivit fruktansvärt fel, vi får börja om ...")
            time.sleep(2)
            os.system('cls')
            main()


def get_user_solution(problem):
    global result
    print("Ange ditt svar")
    print(problem, end="")
    try:
        result = int(input(" = "))
#In the case that user input is submitted empty we get value error, then we need to handle it
    except ValueError:
        result = None
    if result != None:
        return result
    else:
        print ("Du måste ange ett svar, försök igen.")
#Resend the user to a new promt to enter solution again
        get_user_solution(problem)
        return result
##################################################################
#Not actually used or needed, problem solved with global variable#
#but it gets to stay just in case I need it at a later date. #####
def reset_solution(result,problem):                          #####
    if result == None:                                       #####
        result = 0                                           #####
        print ("Sent back to try input again")               #####
        get_user_solution(problem)                           #####
        return result                                        #####
    else:                                                    #####
        user_solution = get_user_solution(problem)           #####
        print ("Reset the solution value to ", user_solution)#####
######Needs to be evaluated and eventually removed!###############
##################################################################

def check_solution(user_solution, solution, count):
    global result
    if user_solution == solution:
        count = count + 1
        print("Rätt.")
        return count
    else:
        print("Fel.")
        return count

def menu_option(index, count):

    global end_one
    global end_two
    #number_one = random.randrange(1, 21)
    number_one = random.randrange(1, end_one)
    number_two = random.randrange(1, end_two)
    if index == 1:
        if number_one > number_two:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            number_one = random.randrange(number_two, end_one)
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count

    elif index == 2:
        if number_one > number_two:
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            number_one = random.randrange(number_two, end_one)
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        
    elif index == 3:
        if number_one > number_two:
            problem = str(number_one) + " * " + str(number_two)
            solution = number_one * number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            number_one = random.randrange(number_two, end_one)
            problem = str(number_one) + " * " + str(number_two)
            solution = number_one * number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
    elif index == 4:
        if number_one > number_two:
            problem = str(number_one) + " / " + str(number_two)
            solution = number_one // number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            number_one = random.randrange(number_two, end_one)
            problem = str(number_one) + " / " + str(number_two)
            solution = number_one // number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count        
#This is checked by a while loop in main!
#    elif index is 5:
#        print("option 5")
#        display_result(total, correct)
#        return total, correct
    elif index == 6:
        global runonce
        runonce = 0
        end_one = 0
        end_two = 0
        add_limits()
        return runonce, end_one, end_two
    else:
        print("Avslutar, välkommen åter.")
        time.sleep(2)
        sys.exit()

def display_result(total, correct):
    os.system('cls')
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("Du har besvarat", total, "frågor varav", correct, "rätt.")
    #print("Ditt resultat blev ", percentage, "%. Tack så mycket.", sep = "")
    print("Ditt resultat blev ", percentage, "%.", sep = "")
    print ("******************************************************")
    print ("")
    print ()
    time.sleep(2)
    main()

def main():
    global runonce
   # print ("First row of main", runonce)
    if runonce !=1:
        display_intro()
        add_limits()
    else:
        #print ("Else triggerd")
        #display_intro()
        display_menu()
        display_separator()
        option = get_user_input()
        total = 0
        correct = 0
        while option != 5:
            total = total + 1
            correct = menu_option(option, correct)
            option = get_user_input()

    
    display_separator()
    display_result(total, correct)

main()
