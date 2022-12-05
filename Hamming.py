def distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("string do not match")

    i = 0
    counter = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            counter += 1
        i += 1
    return counter
