def tokenRecognizer(word: str):
    word = word.lower()
    try:
        if isSubjek(word): return 'S'
        elif isPredikat(word): return 'P'
        elif isObjek(word): return 'O'
        elif isKeterangan(word): return 'K'
        else: raise Exception("TokenUnrecognizedError")
    except Exception as e: 
        print(f"ERROR: {e}")
        print(f"Word \"{word}\" tidak masuk ke kategori token manapun\n")
        return '?'

def isSubjek(word: str) -> bool:
    # Subjek = {aku, andi, budi, dia, dian}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'a': currState = 1
                elif letter == 'b': currState = 4
                elif letter == 'd': currState = 7
                elif letter == ' ': currState = 0
                else: currState = -1
            case 1:
                if letter == 'k': currState = 2
                elif letter == 'n': currState = 5
                else: currState = -1
            case 2: currState = 3 if letter == 'u' else -1
            case 3: currState = 3 if letter == ' ' else -1 # FINAL STATE
            case 4: currState = 5 if letter == 'u' else -1
            case 5: currState = 6 if letter == 'd' else -1
            case 6: currState = 3 if letter == 'i' else -1
            case 7: currState = 8 if letter == 'i' else -1
            case 8: currState = 9 if letter == 'a' else -1
            case 9: currState = 3 if letter == 'n' or letter == ' ' else -1 # FINAL STATE
    return currState == 3 or currState == 9

def isPredikat(word: str) -> bool:
    # Predikat = {membaca, membawa, membeli, menulis, menukar}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'm': currState = 1
                elif letter == ' ': currState = 0
                else: currState = -1
            case 1: currState = 2 if letter == 'e' else -1
            case 2:
                if letter == 'm': currState = 3
                elif letter == 'n': currState = 10
                else: currState = -1
            case 3: currState = 4 if letter == 'b' else -1
            case 4:
                if letter == 'a': currState = 5
                elif letter == 'e': currState = 8
                else: currState = -1
            case 5: currState = 6 if letter == 'c' or letter == 'w' else -1
            case 6: currState = 7 if letter == 'a' else -1
            case 7: currState = 7 if letter == ' ' else -1 # FINAL STATE
            case 8: currState = 9 if letter == 'l' else -1
            case 9: currState = 7 if letter == 'i' else -1
            case 10: currState = 11 if letter == 'u' else -1
            case 11:
                if letter == 'l': currState = 12
                elif letter == 'k': currState = 14
                else: currState = -1
            case 12: currState = 13 if letter == 'i' else -1
            case 13: currState = 7 if letter == 's' else -1
            case 14: currState = 15 if letter == 'a' else -1
            case 15: currState = 7 if letter == 'r' else -1
    return currState == 7

def isObjek(word: str) -> bool:
    # Objek = {buku, kamus, komik, koran, novel}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'b': currState = 1
                elif letter == 'k': currState = 5
                elif letter == 'n': currState = 14
                elif letter == ' ': currState = 0
                else: currState = -1
            case 1: currState = 2 if letter == 'u' else -1
            case 2: currState = 3 if letter == 'k' else -1
            case 3: currState = 4 if letter == 'u' else -1
            case 4: currState = 4 if letter == ' ' else -1 # FINAL STATE
            case 5:
                if letter == 'a': currState = 6
                elif letter == 'o': currState = 9
                else: currState = -1
            case 6: currState = 7 if letter == 'm' else -1
            case 7: currState = 8 if letter == 'u' else -1
            case 8: currState = 4 if letter == 's' else -1
            case 9:
                if letter == 'm': currState = 10
                elif letter == 'r': currState = 12
                else: currState = -1
            case 10: currState = 11 if letter == 'i' else -1
            case 11: currState = 4 if letter == 'k' else -1
            case 12: currState = 13 if letter == 'a' else -1
            case 13: currState = 4 if letter == 'n' else -1
            case 14: currState = 15 if letter == 'o' else -1
            case 15: currState = 16 if letter == 'v' else -1
            case 16: currState = 17 if letter == 'e' else -1
            case 17: currState = 4 if letter == 'l' else -1
    return currState == 4

def isKeterangan(word: str) -> bool:
    # Ket = {di_sana, di_sini, di_kelas, di_taman, di_toko}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'd': currState = 1
                elif letter == ' ': currState = 0
                else: currState = -1
            case 1: currState = 2 if letter == 'i' else -1
            case 2: currState = 3 if letter == '_' else -1
            case 3:
                if letter == 's': currState = 4
                elif letter == 'k': currState = 10
                elif letter == 't': currState = 14
                else: currState = -1
            case 4:
                if letter == 'a': currState = 5
                elif letter == 'i': currState = 8
                else: currState = -1
            case 5: currState = 6 if letter == 'n' else -1
            case 6: currState = 7 if letter == 'a' else -1
            case 7: currState = 7 if letter == ' ' else -1 # FINAL STATE
            case 8: currState = 9 if letter == 'n' else -1
            case 9: currState = 7 if letter == 'i' else -1
            case 10: currState = 11 if letter == 'e' else -1
            case 11: currState = 12 if letter == 'l' else -1
            case 12: currState = 13 if letter == 'a' else -1
            case 13: currState = 7 if letter == 's' else -1
            case 14:
                if letter == 'a': currState = 15
                elif letter == 'o': currState = 18
                else: currState = -1
            case 15: currState = 16 if letter == 'm' else -1
            case 16: currState = 17 if letter == 'a' else -1
            case 17: currState = 7 if letter == 'n' else -1
            case 18: currState = 19 if letter == 'k' else -1
            case 19: currState = 7 if letter == 'o' else -1
    return currState == 7

def parser(sentence):
    ERR = Exception('ParsingError')
    words = sentence.split()
    words.append('')
    res = []
    stack = []
    state = 0
    print("Stack:")
    print(stack)
    stack.append('#')
    state = 1
    print(stack)
    stack.append('X')
    state = 2
    i = 0
    try:
        while stack[-1] != '#':
            print(stack)
            word = words[i]
            if word != '': token = tokenRecognizer(word)
            match stack[-1]:
                case 'X':
                    if token == 'S':
                        stack.pop()
                        stack.append('Y')
                        stack.append('P')
                        stack.append('S')
                    else: raise ERR
                case 'Y':
                    if word == '': stack.pop()
                    else:
                        if token == 'O':
                            stack.pop()
                            stack.append('Z')
                            stack.append('O')
                        elif token == 'K':
                            stack.pop()
                            stack.append('Z')
                        else: raise ERR
                case 'Z':
                    if word == '': stack.pop()
                    elif token == 'K':
                        stack.pop()
                        stack.append('K')
                    else: raise ERR
                case 'S':
                    if token == 'S':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case 'P':
                    if token == 'P':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case 'O':
                    if token == 'O':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case 'K':
                    if token == 'K':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case _:
                    if token != '?':
                        stack.pop()
                        i += 1
                    else: raise ERR
        print(stack)
        stack.pop()
        print(stack)

        print("Struktur: ", end='')
        for i in res[:-1]:
            print(f"{i} - ", end='')
        print(res[-1], "\n")

        return True 
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kalimat \"{sentence}\" tidak memiliki struktur yang sesuai\n")
        return False

if __name__ == '__main__':  
    sentence = input("Kalimat: ")
    print()
    print(f"String: {sentence}\nStatus: Diterima ✔️\n") if parser(sentence) else print(f"String: {sentence}\nStatus: Ditolak ❌\n")