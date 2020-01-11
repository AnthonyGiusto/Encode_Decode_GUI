def encode(number, month):
    """Takes a user input value and encodes it with a predefined month index"""

    # creates known lists of indexes for encoding
    nullcode = {1: 'i', 2: 'c', 3: 'e', 4: 'd', 5: 'r', 6: 'a', 7: 'g',
                8: 'o', 9: 'n', 0: 's'}
    code_one = {1: 'n', 2: 'e', 3: 'a', 4: 'r', 5: 'd', 6: 'g', 7: 's',
                8: 'i', 9: 'o', 0: 'c'}
    code_two = {1: 'c', 2: 's', 3: 'g', 4: 'r', 5: 'd', 6: 'i', 7: 'o',
                8: 'a', 9: 'e', 0: 'n'}
    code_three = {1: 'a', 2: 'e', 3: 'r', 4: 'n', 5: 's', 6: 'i', 7: 'o',
                  8: 'g', 9: 'c', 0: 'd'}
    code_four = {1: 'd', 2: 'r', 3: 'a', 4: 's', 5: 'g', 6: 'o', 7: 'c',
                 8: 'i', 9: 'e', 0: 'n'}
    codelist = [nullcode, code_one, code_two, code_three, code_four]

    digitlist = []
    encodedstring = []
    codeindex = codelist[month].copy()
    for digit in number:
        digitlist.append(digit)
    for digit in digitlist:
        digit = int(digit)
        encodedstring.append(codeindex[digit])
    return encodedstring
