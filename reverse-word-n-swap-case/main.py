def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    word = sentence.split()
    reverse = word[::-1]
    swapcased = [i.swapcase() for i in reverse]
    result = ' '.join(swapcased)
    return result