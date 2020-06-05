def is_pangram(sentence):
    import string
    for c in string.ascii_lowercase:
        if c not in sentence.lower():
            return False
    return True
