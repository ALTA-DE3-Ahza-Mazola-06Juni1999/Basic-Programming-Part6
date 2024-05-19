def caesar(offset, input_str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    
    for i in input_str:
        if i.isalpha():
            is_upper = i.isupper()
            i = i.lower()
            shifted_index =(alphabet.index(i) + offset) % 26
            shifted_i = alphabet[shifted_index]
            result += shifted_i.upper()if is_upper else shifted_i
        else:
            result += char
    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl