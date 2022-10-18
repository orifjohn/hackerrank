import string


def pangrams(s):
    s = s.lower()
    
    alphabet = list(string.ascii_lowercase)
    for i in s:
        if i in alphabet:
            alphabet.remove(i)
            
    if not alphabet:
        print("pangram")
    else:
        print("not pangram")
    
    

if __name__ == "__main__":
    s = input()
    pangrams(s)
    
