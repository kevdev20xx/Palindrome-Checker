

def is_palindrome(text:str):
    text_backwards = text[::-1]
    if text == text_backwards:
        return True
    else:
        return False
while True:
    text = input("Please type your text: ")

    if is_palindrome(text):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
