def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        sentence = list(sentence)
        sentence.append(None)
        sentence = ''.join(sentence)
        answer = (length, sentence)
        return answer
    else:
        sentence = list(sentence)
        store = sentence[:1]
        sentence.clear()
        sentence = store
        sentence = ''.join(sentence)
        answer = (length, sentence)
        return answer
