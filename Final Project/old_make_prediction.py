# -*- coding: utf-8 -*-
import csv

LINKS_COLUMN = 0
SPAMMY_WORDS_COLUMN = 1
LENGTH_COLUMN = 2
SYMBOLS_COLUMN = 3
CLASS_COLUMN = 4

def make_prediction(does_have_links, does_have_spammy_words, length_of_text, number_of_symbols):
    prediction = "SPAM."
    if does_have_spammy_words == False:
        if does_have_links == False:
            prediction = "HAM."
        else:
            prediction = "SPAM."
    else:
        # finish this code
        if length_of_text < 2.5:
            prediction = "HAM."
        else:
            if number_of_symbols < 10.5:
                if length_of_text < 3.5:
                    if does_have_links == False:
                        if number_of_symbols < 5.5:
                            prediction = "SPAM."
                        else:
                            prediction = "HAM."
                    else:
                        prediction = "SPAM."
                else:
                   prediction = "SPAM."
            else:
                prediction = "HAM."

    return prediction

def categorize_text_length(length_of_text):
    if length_of_text >= 158:
        length_category = 5
    elif length_of_text >= 131:
        length_category = 4
    elif length_of_text >= 100:
        length_category = 3
    elif length_of_text >= 47:
        length_category = 2
    else:
        length_category = 1
    return length_category

def main():

    does_have_links = input("Does the text have links (True or False): ")
    does_have_spammy_words = input("Does the text have spammy words (True or False): ")
    length_of_text = int(input("What's the length of the text (enter an integer): "))
    number_of_symbols = int(input("How many symbols are in the text (enter an integer): "))

    prediction = make_prediction(does_have_links, does_have_spammy_words, categorize_text_length(length_of_text), number_of_symbols)

    print("The text is", prediction)


main()
