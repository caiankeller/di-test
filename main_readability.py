import time


def is_palindrome(input_string):
    clean_string = input_string.lower()
    length = len(clean_string)
    for i in range(length // 2):
        if clean_string[i] != clean_string[length - i - 1]:
            return False
    return True


def get_user_input(prompt):
    user_input = input(prompt)
    return user_input


word = get_user_input("Enter a word or phrase: ")

start_time = time.time()

result = is_palindrome(word)
print(result)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")
