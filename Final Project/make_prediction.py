import csv

def doesHaveLinks(text_message):
    # do we have to split the sentence and use for loops here?
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
    return length_of_text

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

def make_prediction(does_have_links, does_have_spammy_words, length_of_text, number_of_symbols):
    prediction = "SPAM"
    if does_have_spammy_words == False:
        if does_have_links == False:
            prediction = "HAM"
        else:
            prediction = "SPAM"
    else:
        if length_of_text < 2.5:
            prediction = "HAM"
        else:
            if number_of_symbols < 10.5:
                if length_of_text < 3.5:
                    if does_have_links == False:
                        if number_of_symbols < 5.5:
                            prediction = "SPAM"
                        else:
                            prediction = "HAM"
                    else:
                        prediction = "SPAM"
                else:
                   prediction = "SPAM"
            else:
                prediction = "HAM"

    return prediction

def main():
    text_message = input("Enter Q to quit or enter the text message: ")
    while text_message != "Q" and text_message != "q":
        does_have_links = doesHaveLinks(text_message)
        does_have_spammy_words = doesHaveSpammyWords(text_message)
        length_of_text = lengthOfText(text_message)
        category_of_text = categorize_text_length(length_of_text)
        number_of_symbols = numberOfSymbols(text_message)
        prediction = make_prediction(does_have_links, does_have_spammy_words, category_of_text, number_of_symbols)
        print("The text is", prediction)
        print("Has Links: ", does_have_links)
        print("Has Spammy Words: ", does_have_spammy_words)
        print("Length of Text: ", length_of_text)
        print("Number of Symbols: ", number_of_symbols)
        text_message = input("Enter Q to quit or enter the text message: ")

main()

word = wordlist_10000
length: int=len(word)
