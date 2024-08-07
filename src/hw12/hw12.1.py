import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        text = re.sub('<[^<]+?>', '', html)

        text_lines = text.split("\n")
        dest_file = open(result_file, 'w')

        for line in text_lines:
            purified_line = line.strip()
            if purified_line != "":
                dest_file.write(f'{purified_line}\n')


delete_html_tags('draft.html')
