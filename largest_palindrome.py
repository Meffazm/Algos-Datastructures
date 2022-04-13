from collections import deque


def palindrome_core(s, idx):
    if 1 <= idx <= len(s) - 2:
        if s[idx] == s[idx - 1] and s[idx] == s[idx + 1] or s[idx - 1] == s[idx + 1]:
            return deque(s[idx - 1:idx + 2]), 3
        elif s[idx] == s[idx - 1]:
            return deque(s[idx - 1:idx + 1]), 2
        elif s[idx] == s[idx + 1]:
            return deque(s[idx:idx + 2]), 2
        else:
            return deque(s[idx]), 1
    else:
        return deque(s[idx]), 1


def largest_palindrome(s):
    if len(s) == 1:
        return s
    elif len(s) == 0:
        return ''

    palindromes = deque()
    left_pointer = len(s) // 2 - 1
    right_pointer = len(s) // 2

    while left_pointer >= 0 and right_pointer <= len(s) - 1:
        l_qeue, l_len = palindrome_core(s, left_pointer)
        r_qeue, r_len = palindrome_core(s, right_pointer)

        if l_len != 1:
            for l, r in zip(range(left_pointer - l_len + 1, -1, -1), range(left_pointer + l_len - 1, len(s))):
                if s[l] == s[r]:
                    l_qeue.appendleft(s[l])
                    l_qeue.append(s[r])
                else:
                    break

        if r_len != 1:
            for l, r in zip(range(right_pointer - r_len + 1, -1, -1), range(right_pointer + r_len - 1, len(s))):
                if s[l] == s[r]:
                    r_qeue.appendleft(s[l])
                    r_qeue.append(s[r])
                else:
                    break

        palindromes.appendleft(l_qeue)
        palindromes.append(r_qeue)
        left_pointer -= 1
        right_pointer += 1

    max_len = max(map(len, palindromes))
    return ''.join(next(filter(lambda x: len(x) == max_len, palindromes)))
