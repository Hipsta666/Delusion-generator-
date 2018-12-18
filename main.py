import random

def correct_transfer(string, length):
    """The function makes the text from the entered string, making a transfer to a new one after 60 characters."""
    lines = ""
    scorer = 1
    reduction = 0
    for num in range(len(string)):
        if num > length * scorer + reduction and string[num] == " ":
            lines += "\n"
            reduction = len(string[:num]) - length * scorer
            scorer += 1
        else:
            lines += string[num]
    print(lines)

def int_clear():
    '''Function open and clear file.'''
    with open("input.txt", 'r', encoding='utf-8') as file:
        a = "ЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛБЩДЮЗЖХЭЪЁ"
        b = "йфяцычувскамепинртгоьшлбщдюзжхэъё,.?!1234567890-\n "
        text = file.read()
        text_clean = ""
        for letter in text:
            if letter in a + b:
                text_clean += letter
        text = text_clean.replace("  ", " ").split()
        return(text)

def stop(text):
    '''Function find stop-words.'''
    list_stop_words = []
    for word in text:
        if word.endswith(".") or word.endswith("!") or word.endswith("?"):
            list_stop_words.append(word)
    return(list_stop_words)

def start(text,list_stop_words):
    '''Function find start-words.'''
    a = "ЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛБЩДЮЗЖХЭЪЁ"
    list_start_words = []
    for letters in text:
        if letters[0] in a and text[text.index(letters)-1] in list_stop_words:
            list_start_words.append(letters)
    return(list_start_words)

def sentences(text,list_stop_words,list_start_words):
    '''Function compose the sentences.'''
    new_list = []
    for item in text:
        if item not in new_list:
            new_list.append(item)
    d = {}
    fake = text
    for i in new_list:
        if i not in list_stop_words:
            new_list_1 = []
            for j in text:
                if j == i and j not in list_stop_words and text[text.index(j) + 1] not in new_list_1:
                    new_list_1.append(text[text.index(j) + 1])
                    h = text[text.index(j) + 1]
                    text = text[text.index(h):]
            text = fake
            d[i] = new_list_1

    last_text = ""
    for _ in list_start_words:
        random_start = random.choice(list_start_words)

        add_word = random.choice(d[random_start])
        sent = random_start
        for new in range(0, 19):
            add_word = random.choice(d[random_start])
            if new < 5 and add_word in list_stop_words:
                add_word = random.choice(d[random_start])
                if add_word in list_stop_words:
                    while add_word in list_stop_words:
                        add_word = random.choice(d[random.choice(list_start_words)])
            if new == 18 and add_word not in list_stop_words:
                add_word = random.choice(list_stop_words)
                sent += " " + add_word

            else:
                sent += " " + add_word
                random_start = add_word
            if add_word in list_stop_words:
                break
        last_text += sent + " "
    correct_transfer(last_text, 100)

def main():
    clear = int_clear()
    stop_1 = stop(clear)
    start_1 = start(clear,stop_1)
    sentences(clear,stop_1,start_1)
if __name__=='__main__':
    main()