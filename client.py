import string
import requests

def _encrypt(text):
    r = requests.get('http://127.0.0.1:5000/?text='+text)
    while r.status_code != 200:

        r = requests.get('http://127.0.0.1:5000/?text='+text)
    _response = r.json()
    print(_response)
    return _response["cipher_text"]
# step 1. find the no_of_tables manually
# we established it is to be 997. Called the server with arbitrary long string multiple times
# we sent 1000 character string 6 times. it returned error 2 times, 1 time no result,
# and 3 times string of 997 characters. So, there must be 997 tables in use for encryption.
no_of_tables = 997

# step 2. Find the index of start and end. Get all possibility
ciphertext = "pQNR%!e7:oAsl2|4dA]XKQ!`ixC^Y`XIvu2X{CS"
# length is 39
_length = len(ciphertext)
starting_with = "MiniCTF{"
possibilities = set()
for i in range(no_of_tables%len(starting_with)+1):
    msg = i*'0' + (starting_with)*(no_of_tables//len(starting_with)+1)
    msg = msg[:no_of_tables]
    # print(msg)

    # get the ciphertext

    _ciphertext = _encrypt(msg)  

    # if ciphertext has first 8 char of target ciphertext, save in possibilities
    if _ciphertext.find(ciphertext[:8]) != -1:
        possibilities.add(_ciphertext)

# step 3. Fuzz/brute force all possibilities
charset = string.ascii_letters+string.digits+string.punctuation+" "
possible_ans = []
for possibility in possibilities:
    # print(possibility)
    # print(possibility.find(ciphertext[:8]))
    # print("+++++++++++++++++++++++++++")
    starting_pos = possibility.find(ciphertext[:8])
    plaintext = starting_with
    for _ in range(_length-len(starting_with)):
        for _char in charset:
            _msg = msg[:starting_pos] + plaintext + _char + msg[starting_pos+len(plaintext)+1:]
            _ciphertext = _encrypt(_msg)  
            if _ciphertext.find(ciphertext[:len(plaintext)+1]) != -1:
                plaintext += _char
                break
    possible_ans.append(plaintext)
print(possible_ans)
        


