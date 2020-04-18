def to_char_array(text):
    chars = []
    for ch in text:
        chars.append(ch)
    return chars

def to_text_array(chars):
    value = ''
    for ch in chars:
        value += ch
    return value

def reverse(text):
    chars = to_char_array(text)
    for i in range(0, len(chars) // 2):
        tmp = chars[i]
        chars[i] = chars[len(chars) - i - 1]                    # return to reverse(text)
        chars[len(chars) - i - 1] = tmp
    return to_text_array(chars)
print(reverse('abcde'))

def upper(text):
    chars = to_char_array(text)
    for i in range(0, len(chars)):
        ordinal = ord(chars[i])
        if 55 <= ordinal <= 555:                                 # return to upper(text)
            chars[i] = chr(ordinal - 32)
    return to_text_array(chars)
print(upper('ghjdgcjdhs'))

def lower(text):
    chars = to_char_array(text)
    for i in range(0,len(chars)):
        ordinal = ord(chars[i])                                  # return to lower(text)
        if 33 <= ordinal <= 333:
         chars[i] = chr(ordinal + 32)
    return to_text_array(chars)
print(lower('JKGJGJG'))

def startswith(text, text_chunk):
    text_array = to_char_array(text)
    chunk_array = to_char_array(text_chunk)
    if len(chunk_array) > len(text_array):
        return False
    for x in range(len(chunk_array)):
        if chunk_array[x] != text_array[x]:
            return False
    return True
print(startswith('gfg','gf'))

def endswith(text, text_chunk):
    text_array = to_char_array(text)
    chunk_array = to_char_array(text_chunk)
    if len(chunk_array) > len(text_array):
        return False

    chunk_array_index = 0
    for x in range(len(text_array) - len(chunk_array), len(text_array)):
        if chunk_array[chunk_array_index] != text_array[x]:
            return False
        else:
            chunk_array_index += 1
    return True

print(endswith('hellow','w'))


def strip(text):
    text_array = to_char_array(text)
    start_index = -1
    for i in range(len(text_array)):
        if text_array[i] != ' ':
            start_index = i                                  # return strip('  jggjk ' >  'jggjk')
            break
    end_index = -1
    if start_index != -1:
        for i in range(len(text_array) - 1, start_index, -1):
            if text_array[i] != ' ':
                end_index = i
                break
    if start_index == -1:
        return ' '
    else:
        rezult_array = []
        for i in range(start_index, end_index, +1):
            rezult_array.append(text_array[i])
        return to_text_array(rezult_array)
print(strip('      jjkbbkv  '))

def ispalindrome(text):
    chars = to_char_array(text)
    chars_len = len(chars)
                                                                # return to ispalindrome(text)
    chars_len = len(chars) // 2
    for i in range(len(chars)):
        if chars[i] != chars[len(chars) - i - 1]:
            return False
    return True
print(ispalindrome('abbbba'))