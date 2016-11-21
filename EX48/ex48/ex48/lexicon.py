lexicon = {
'north': 'direction',
'south': 'direction',
'east': 'direction',
'west': 'direction',
'go': 'verb',
'kill': 'verb',
'eat': 'verb',
'the': 'stop',
'in': 'stop',
'of': 'stop',
'bear': 'noun',
'princess': 'noun'
    }

def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        try:
            result.append((lexicon[word.lower()], word))
        except KeyError:
            if convert_number(word) != None:
                result.append(('number', int(word)))
            else:
                result.append(('error', word))

    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
