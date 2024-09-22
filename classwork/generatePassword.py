import random
import string

def generate_password(length=10):
    words = ["chidinma", "esther", "chiamaka", "obioma", "nwangwu"]
    numbers = string.digits
    special_chars = string.punctuation


    random_word = random.choice(words)
    random_number = random.choice(numbers)
    random_special_char = random.choice(special_chars)


    remaining_length = length - 2
    all_chars = words + list(numbers) + list(special_chars)
    random_chars = [random.choice(all_chars) for _ in range(remaining_length)]


    password = [random_word, random_number, random_special_char] + random_chars
    random.shuffle(password)


    return ''.join(password)

print(generate_password())

