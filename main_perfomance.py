import time


def is_palindrome(input_string):
    clean_string = input_string.lower()
    left = 0
    right = len(clean_string) - 1

    while left < right:
        if clean_string[left] != clean_string[right]:
            return False
        left += 1
        right -= 1
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
