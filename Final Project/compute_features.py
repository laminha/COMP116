# -*- coding: utf-8 -*-
import csv
import os

CLASS_LABEL_COLUMN = 0
TEXT_MESSAGE_COLUMN = 1

# determines if the text message contains a link:
def doesHaveLinks(text_message):
    if "www" in text_message or "http" in text_message or ".com" in text_message or "link" in text_message or ".online" in text_message:
        return True
    return False

# determines if the text message contains a word from spamwords.txt
def doesHaveSpammyWords(text_message):
    spammy_words = []
    file_object = open("spamwords.txt","r")
    entire_file = file_object.readlines()
    for element in entire_file:
        spammy_words.append(element.rstrip())
    # print(spammy_words)
    spammy_word_count = len(spammy_words)
    # print(spammy_word_count)
    for index in range(0,spammy_word_count):
        if spammy_words[index] in text_message.lower():
            return True
        else:
            index += 1
    return False

# determines length of text message including spaces
def lengthOfText(text_message):
    length_of_text = len(text_message)
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

# determines number of symbols from a list of symbols
def numberOfSymbols(text_message):
    number_of_symbols = 0
    symbols = ["!",".",",","?",":",";","÷","&"]
    for index in range(0,len(symbols)):
        if symbols[index] in text_message:
            number_of_symbols += text_message.count(symbols[index])
        index += 1
    # print("symbols: ",number_of_symbols)
    return number_of_symbols

def main():
    # remove the previous features file to make testing code easier
    os.remove('features.csv')
    # open the csv file in read mode
    with open('spam.csv', 'r', encoding="ISO-8859-1") as in_file:
        csv_reader = csv.reader(in_file, delimiter=',')

        # gets the headers row as a list
        header_row = next(csv_reader)
        # print(header_row)

        # add headers to features.csv
        with open('features.csv', 'a', newline='') as file:
            file_writer = csv.writer(file)
            file_writer.writerow (["Has Links", "Has Spammy Words", "Text Length", "Number of Symbols", "Class Label"])

        for row in csv_reader:
            does_have_links = doesHaveLinks(row[TEXT_MESSAGE_COLUMN])
            does_have_spammy_words = doesHaveSpammyWords(row[TEXT_MESSAGE_COLUMN])
            length_of_text = lengthOfText(row[TEXT_MESSAGE_COLUMN])
            number_of_symbols = numberOfSymbols(row[TEXT_MESSAGE_COLUMN])
            class_label = row[CLASS_LABEL_COLUMN]

            with open('features.csv', 'a', newline='') as file:
                # create writer object
                file_writer = csv.writer(file)
                # write a row takes a list

                file_writer.writerow ([does_have_links, does_have_spammy_words, length_of_text, number_of_symbols,class_label])
    print("Finished")


main()
