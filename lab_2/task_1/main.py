import functions

if(__name__ == "__main__"):
    with open("/Users/chuchmek/Desktop/учёба 4 сем/иги/labs/lab_2/task_1/file") as file:
      text = file.read()

    print(text)

    print(f'Amount of sentences: {functions.amount_of_sentences(text)}')
    print(f"Amount of non-declarative sentences: {functions.amount_of_non_declarative_sentences(text)}")
    print(f"Average amount of characters in sentences: {functions.average_amount_of_characters_in_sentence(text)}")
    print(f"Average amount of characters in word: {functions.average_amount_of_characters_in_word(text)}")
    print("Top-K N-grams:")

    k = input("Entered K:")
    while not k.isdigit():
        k = input("Error! Entered K:")

    n = input("Entered N:")
    while not k.isdigit():
        n = input("Error! Entered N:")

    print(functions.top_grams(text, k, n))