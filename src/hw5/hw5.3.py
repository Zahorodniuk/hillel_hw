import string

mean = input('Enter your word:')

mean = mean.title()
mean = mean.replace(' ', '')
mean = mean.translate(str.maketrans('', '', string.punctuation))

hashtag = ('#' + mean)[:140]
print(hashtag)
