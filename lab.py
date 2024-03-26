def is_palindrome(s):

    def is_palindrome_recursive(s, start, end):

        if start >= end:
            return True

        if s[start] != s[end]:
            return False

        return is_palindrome_recursive(s, start + 1, end - 1)

    return is_palindrome_recursive(s, 0, len(s) - 1)


string = input("Введите строку: ")

if is_palindrome(string):
    print("Да, это палиндром.")
else:
    print("Нет, это не палиндром.")
