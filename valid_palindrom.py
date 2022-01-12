# string_1 = "a man, a plan, a canal: panama"
# string_1 = ''.join(e for e in string_1 if e.isalnum())
#
# string_1_reverted = string_1[::-1]
#
# print(string_1 == string_1_reverted)

def almost_palindrome(s):

    pointer_1 = 0
    pointer_2 = len(s) - 1
    string_2 = s

    while pointer_1 < pointer_2:
        if string_2[pointer_1] != string_2[pointer_2]:
            temp_string_1 = string_2.replace(string_2[pointer_1], '', 1)
            temp_string_2 = string_2.replace(string_2[pointer_2], '', 1)
            if temp_string_1 == temp_string_1[::-1] or temp_string_2 == temp_string_2[::-1]:
                return True
            else:
                return False

        pointer_1 += 1
        pointer_2 -= 1

    return True


string_1 = "abcba"
print(almost_palindrome(string_1))

