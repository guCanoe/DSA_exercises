VOWELS = set(list("aeoui"))
def compare_letter(s):
    if len(s) == 1:
        return 1 if s[0] in VOWELS else -1
    else:
        return compare_letter(s[0]) + compare_letter(s[1:])

print compare_letter('gohangasalami')
