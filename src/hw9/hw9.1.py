def popular_words(text, words):
    res = {}
    for word in text.split():
        word = word.lower()
        if word in words:
            res[word] = res.get(word, 0) + 1
    else:
        for w in words:
            if w not in res:
                res[w] = 0
    return res



assert_phrase = 'When I was One I had just begun When I was Two I was nearly new '
required_word_list = ['i', 'was', 'three', 'near']
expected_result = { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }

assert popular_words(assert_phrase, required_word_list) == expected_result, 'Test1'
print('OK')