###SECONDS WILL BE VERY TEMPERMENTAL DEPENDING ON THE COMPILER AND COMPUTER!!!###
"""if the number of seconds are weird or seem off in any way, fidget with the zeros that are dividing the miliseconds to get the seconds until it looks right.
   The default number crunch is at 1,000,000. If you set it to 10, 100, or 1000, you will get scientific notation automatically when using the original python 3.7 IDLE.
   Other higher numbers will work rather well. If it shows the ASCII art and the "Getting Started" line but the script doesn't show stats yet,
   this is because it doesn't show the number being guessed. It is built this way to minimize the amount of actions taking place. It works best with windows computers with no tabs open.
   If a windows computer is not open, the a linux computer will also work, just don't run it on machines that use windows XP or earlier and you're go for launch!"""


#Imports all the necessary modules
import random

#Defining "stale" variables that do not change

running = 1
count = 0
#RANDOM INTEGER NUMBERS
r1 = random.randint(0,1000)
miliseconds = 0

#Blacklist
#CHANGE HIGH TO THE SAME NUMBER AS THE MAX RANDOM INTEGER NUMBER
high = [1000]
low = [0]

min_value = low[0]
max_value = high[0]


#Wonderful ASCII artwork for aesthetics
print(":'######::'########::'##::::'##:'##::: ##::'######::'##::::'##::::'########:::'#######::'########:")
print("'##... ##: ##.... ##: ##:::: ##: ###:: ##:'##... ##: ##:::: ##:::: ##.... ##:'##.... ##:... ##..::")
print(" ##:::..:: ##:::: ##: ##:::: ##: ####: ##: ##:::..:: ##:::: ##:::: ##:::: ##: ##:::: ##:::: ##::::")
print(" ##::::::: ########:: ##:::: ##: ## ## ##: ##::::::: #########:::: ########:: ##:::: ##:::: ##::::")
print(" ##::::::: ##.. ##::: ##:::: ##: ##. ####: ##::::::: ##.... ##:::: ##.... ##: ##:::: ##:::: ##::::")
print(" ##::: ##: ##::. ##:: ##:::: ##: ##:. ###: ##::: ##: ##:::: ##:::: ##:::: ##: ##:::: ##:::: ##::::")
print(". ######:: ##:::. ##:. #######:: ##::. ##:. ######:: ##:::: ##:::: ########::. #######::::: ##::::")
print(":......:::..:::::..:::.......:::..::::..:::......:::..:::::..:::::........::::.......::::::..:::::")

#Shows that the script is running
print("\nGetting Started...\n")

#Must be the same number as the random integer range
#Constantly cycles through random numbers and changing varaiables

while running == 1:
    g1 = random.randint(min_value, max_value)
    number = g1
    miliseconds += 1
#THESE ARE THE ZEROS TO MESS WITH TO FIX WEIRD TIMING
    seconds = miliseconds/1000000

#Appends wrong numbers to a blacklist depending on the high or low value of the guess

    if g1 < r1:
        low[0] = (number)
        count += 1

    if g1 > r1:
        high[0] = (number)
        count += 1

#Prints out the statistics for the solved problem

    if g1 == r1:
        print("################FOUND NUMBER################")
        print("Number of guesses:   ", count)
        print("Elapsed Time:        ", seconds, "Sec.")
        print("Number is:           ", number)
        print("############################################")
        break

finish = input("Press Any Key to Finish...")
