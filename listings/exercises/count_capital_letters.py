with open('very_big_text.txt') as f:

    # multiline solution
    # count = 0
    # text = f.read()
    # for character in text:
    #     if character.isupper():
    #         count += 1

    # one-liner
    count = sum(1 for line in f for character in line if character.isupper())

    print(count)
