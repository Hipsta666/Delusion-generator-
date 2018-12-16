
with open("input.txt", "r") as file:
    a = "ЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛБЩДЮЗЖХЭЪЁ1234567890"
    b = "йфяцычувскамепинртгоьшлбщдюзжхэъё,.?!\n "
    text = file.read()
    text_list = []
    text_clean = ""
    for letter in text:
        if letter in a + b:
            text_clean += letter
    text = text_clean.replace("  ", " ").split()
    list_start_words = []
    list_stop_words = []

    for word in text:
        if word.endswith(".") or word.endswith("!") or word.endswith("?"):
            list_stop_words.append(word)

    for letters in text:
        if letters[0] in a and ".!?" in text[text.index(letters)-1]:
            list_start_words.append(letters)

new_list = []
for item in text:
    if item not in new_list:
        new_list.append(item)

fake = text
vocab_list = []
for i in new_list:
    if i not in list_stop_words:
        new_list_1 = []
        for j in text:
            if j == i and j not in list_stop_words and j not in new_list_1:
                new_list_1.append(text[text.index(j) + 1])
                h = text[text.index(j) + 1]
                text = text[text.index(h):]
        text = fake
        d = {i: new_list_1}
        vocab_list.append(d)
print(vocab_list)



