import random

words = ["big" "red", "small", "baby", "yellow", "python", "jesoph" ]
def main():
    numbers = [16.2, 75.1, 52.3]
    word_list = []
    
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,3)
    print(numbers)

    append_random_words(word_list)
    print(word_list)
    append_random_words(word_list, 4)
    print(word_list)

def append_random_words(w_list,quantity=1):
    for _ in range(quantity):
        w_list.append(random.choice(words))


def append_random_numbers(numlist, quantity=1):
    for _ in range(quantity):
        
        num = random.uniform(0,100)
        num = round(num, 2)
        numlist.append(num)

if __name__ == "__main__":
    main()
    