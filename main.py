import nltk #this is the natural language library
import os
import nltk.corpus
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.util import bigrams, ngrams, trigrams
from nltk.stem import PorterStemmer
from nltk import ne_chunk
import numpy 
import sqlite3
import random

#We import all the necessary libraries for the code to run

class User: #we create the user class to store the users information
    def __init__(self):#initiate class
        self.currentUser = None #stores information of the current user
    def initialise_male(self, name, weight, height, age): #this will initilise the male users, as they require different calories
        user = Male(name,weight,height,age) #assigns values to user
        self.currentUser= user  #currentUser is made equal to the user values
           
    def initialise_female(self, name, weight, height, age): #Same as before but for female users
        user = Female(name,weight,height,age)
        self.currentUser= user
    def calc_BMR_Male(weight,height,age):
        BMR = 66.47 + (13.75*weight) + (5.003 * height) + (6.755 + age)
    def calc_BMR_Female(weight,height,age):
        BMR = 66.47 + (13.75*weight) + (5.003 * height) + (6.755 + age)

    def get_calories(self):#This function will return the calories
        return self.currentUser.calories

class Male:
    def __init__(self,name,weight,height,age):#All the values for male user
        self.height = height
        self.name = name
        self.weight = weight
        self.age = age
        self.calories = 2500
   
class Female:
    def __init__(self,name,weight,height,age):#All the values for the female user
        self.height = height
        self.name = name
        self.weight = weight
        self.age = age
        self.calories = 2000
    
class GetOutOfLoop( Exception ): #We use this to exit nested loops
    pass

def set_User(user,name): #function will get values from user to put into class
    weight = input("How much do you weigh? ")
    height = input("How tall are you? ")
    age = input("Whats your age? ")
    
    genderValue = "false"
    while genderValue == "false":
        gender = input("Are you a boy or a girl ") #we use this to check if user is a boy or girl
        if gender == "boy":
            user.initialise_male(name, weight, height, age) #initialises class male
            calories=user.get_calories() #gets calories
            return (user,weight, height, age, calories) #returns values for user
            genderValue = "true"
        if gender == "girl":# Same as above we for the female class
            user.initialise_female(name, weight, height, age)
            calories=user.get_calories()
            return (user,weight, height, age, calories)
            genderValue = "true"
        if genderValue != "true":
            print("Please I need to know ")
def user_message(): #We use the natural language toolkit in order to properly break up sentances
    sent = str(input(" "))
    sent_tokenize = word_tokenize(sent) #seperates the words into tokens
    sent_tags= nltk.pos_tag(sent_tokenize) #assigns tags to each work, such as JJ for adjective NN for noun
    list_of_2 = list(nltk.bigrams(sent_tags)) #We create pairs of the words that are next to each other, e.g "how are you" becomes (how, are), (are, you)
    list_of_3 = list(nltk.trigrams(sent_tags))#Same as before except its in 3s instead of pairs
    randomLine() # pciks random line from file
    return(sent, sent_tags, list_of_3,list_of_2) #returns all the values


def randomLine(): #this will pick a random file from the 'text.txt' file and picks a random line to print
    lines = open('text.txt').read().splitlines()
    return random.choice(lines)

print("Hi! I am a Ploopy,what's your name? ")
def main(): #main function
    user = User() 
    adviceGiven = "false" #we use this to track if we already offered advice
    test = "true" 
    sent, sent_tags, list_of_3,list_of_2 = user_message() # gets new user inpput
    name = None
    while test == "true":       
        try:
            while name == None: #while we dont have a name, we check for a name
                for word in sent_tags: #loops through all the words
                    if word[0].lower() == "hello" or word[0].lower() == "hey" or word[0].lower() == "hi":#checks for a match
                        print("Hello there! How can I help?")
                        sent, sent_tags, list_of_3,list_of_2 = user_message()
                        break
                        

                for (one, two, three) in list_of_3:
                    if one[0].lower() == "my" and two[0].lower() == "name" and three[0].lower() == "is":#checks for the string "my name is"
                        for (word, tag) in sent_tags:
                            if tag == "JJ" or tag == "NNP": #Names most likely to be a Pronoun or adjective
                                    response =input("Are you really called " + word + "? ") #We check to see if we got the right word
                                    for words in response: #this will check the users response
                                        if words.lower() == "y" or words.lower() == "yes" or words.lower() == "yeah" or words.lower() == "yea" or words.lower() == "affirmative":
                                            name = word #if answer is user we set the user
                                            user, weight, height, age, calories = set_User(user,name)
                                            raise GetOutOfLoop #breaks loop
                                        elif words.lower() == "n" or words.lower() ==  "no" or words.lower() ==  "nah" or words.lower() ==  "negative":
                                            print("Damn, I guess i was wrong!")#this only occurs if answer is no
                                            raise GetOutOfLoop
                                            
                                        else:
                                            print("Oop i didnt quite catch that.")
                                            raise GetOutOfLoop#occurs if neither yes or no are given
                    

                for (one,two) in list_of_2:
                    if one[0].lower() == "i" and two[0].lower() == "'m":# Same as above code but checks for "I'm" instead
                        for (word, tag) in sent_tags:
                            if tag == "JJ":
                                response =input("Is " + word + " your real name? ")
                                for words in response:
                                    if words.lower() == "y" or words.lower() == "yes" or words.lower() == "yeah" or words.lower() == "yea" or words.lower() == "affirmative":
                                        name = word
                                        user,weight, height, age, calories = set_User(user,name)
                                        raise GetOutOfLoop
                                    elif words.lower() == "n" or words.lower() == "no" or words.lower() == "nah" or words.lower() == "negative":
                                        print("Damn, I guess i was wrong!")
                                        raise GetOutOfLoop
                                        
                                    else:
                                        print("Oops i didnt quite catch that.")
            
                

                for (word, tag) in sent_tags:
                    if tag == "NNP": #This code simmply checks if the word is a pronoun, and asks the user if thats their name
                        response =input("Is your name " + word + "? ")
                        for words in response:
                                    if words.lower() == "y" or words.lower() == "yes" or words.lower() == "yeah" or words.lower() == "yea" or words.lower() == "affirmative":
                                        name = word
                                        user,weight, height, age, calories = set_User(user,name)
                                        print(calories)
                                        raise GetOutOfLoop
                                    elif words.lower() == "n" or words.lower() == "no" or words.lower() == "nah" or words.lower() == "negative":
                                        print("Damn, I guess i was wrong!")
                                        raise GetOutOfLoop
                                    else:
                                        print("Oops i didnt quite catch that.")
                                        raise GetOutOfLoop
        except GetOutOfLoop:
            pass            

        if name != None and adviceGiven == "false": #once the name isnt empty we run these checks

            print("Do you want some health advice, " + name + "?") #aks the user if they want advice
            sent, sent_tags, list_of_3,list_of_2 = user_message()
            adviceGiven = "true" #Sets this to true so we dont ask again
            for words in sent:#simple check to see if we answer yes or no
                if words.lower() == "y" or words.lower() == "yes" or words.lower() == "yeah" or words.lower() == "yea" or words.lower() == "affirmative":
                    print("I can tell you about excerise and diet, just ask!")
                    sent, sent_tags, list_of_3,list_of_2 = user_message()
                    break
                elif words.lower() == "n" or words.lower() == "no" or words.lower() == "nah" or words.lower() == "negative":
                    print("No worries, just ask for some health advice if you need it!")
                    sent, sent_tags, list_of_3,list_of_2 = user_message()
                    break
                else:
                    print("Oops i didnt quite catch that.")
                    sent, sent_tags, list_of_3,list_of_2 = user_message()
                    raise GetOutOfLoop
        for (one,two,three) in list_of_3:
                if one[0].lower() == "how" and two[0].lower() == "much" and three[0].lower() == "exercise": #if the user asks "how much excercise" we give them an estimation based on age
                    age =int(age)
                    if age < 3: #these are based on the nhs age groups and recommended amount.
                        print("You're too young! Go relax")
                    elif age > 3 and age < 5:
                        print("You should be playing all day!")
                    elif age > 5 and age < 17:
                        print("You should do at least an hour of intense activity everyday!")
                    elif age > 18 and age < 64:
                        print("150 minutes of mild workouts, something like walking!")
                    elif age > 65:
                        print("150 minutes of mild workouts, something like walking! Try to include some balance training too!")
                    sent, sent_tags, list_of_3,list_of_2 = user_message()
        for (one,two) in list_of_2: #This relates to diets, checks for " lose weight" and "diet plan"
            if (one[0].lower() == "lose" and two[0].lower() == "weight") or (one[0].lower() == "diet" and two[0].lower() == "plan"):
                print("Well first off, how much do you work out on average? From 1-5, 1 being a little and 5 being a lot")
                sent, sent_tags, list_of_3,list_of_2 = user_message() #in order to calculate the correct amount of calories we need to figure out users activity level
                for words in sent:
                    if words == "1":
                        totalCal = 1.2*(10 * int(weight) + 6.25 * int(height) - 5*int(age) + 5) #this calculates the total calories, and tells the user
                        print("The ideal calorie intake per day for you is " + str(totalCal))
                    elif words == "2":
                        totalCal = 1.375*(10 * int(weight) + 6.25 * int(height) - 5*int(age) + 5)
                        print("The ideal calorie intake per day for you is " + str(totalCal))
                    elif words == "3":
                        totalCal = 1.55*(10 * int(weight) + 6.25 * int(height) - 5*int(age) + 5)
                        print("The ideal calorie intake per day for you is " + str(totalCal))
                    elif words == "4":
                        totalCal = 1.725*(10 * int(weight) + 6.25 * int(height) - 5*int(age) + 5)
                        print("The ideal calorie intake per day for you is " + str(totalCal))
                    elif words == "5":
                        totalCal = 1.9*(10 * int(weight) + 6.25 * int(height) - 5*int(age) + 5)
                        print("The ideal calorie intake per day for you is " + str(totalCal))
                    sent, sent_tags, list_of_3,list_of_2 = user_message()
        for words in sent:
            if words.lower() == "hello" or words.lower() == "hey" or words.lower() == "hi":
                print("Hello there! How can I help?")


        for words in sent: #breaks the loop if user wants to quit
                if words.lower() == "quit" or words.lower() == "goodbye" or words.lower() == "leave":
                    test = ""
                    print("Good Bye!")
                    break
            
        
      
        if name == None: #generates random facts, if name is known we use it
            print(randomLine())
            sent, sent_tags, list_of_3,list_of_2 = user_message()
        else:
            print("Hey " + name + ", heres a fun fact i know, " + randomLine())
            sent, sent_tags, list_of_3,list_of_2 = user_message()

#initiate the conversation
if __name__ == "__main__":
    main()

