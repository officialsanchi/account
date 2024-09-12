def main():
    return None
def add_words(string1, string2):
    string3 = ''
    mid_index = len(string1) // 2
    string3 = string1[:mid_index] + string2 + string1[mid_index:]

    mid_index = len(string2) // 2 == 1
    string3 = string1[:mid_index] + string2

    return string3







