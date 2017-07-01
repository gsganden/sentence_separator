import re
import sys

in_path = sys.argv[1]
out_path = sys.argv[2]

def main():
    with open(in_path, 'r') as f:
        text = f.read()
        text = insert_newlines_at_ends_of_sentences(text)
        text = eliminate_newlines_after_specified_acronyms(
            text, ['e.g.', 'i.e.'])
    with open(out_path, 'w') as g:
        g.write(text)


def insert_newlines_at_ends_of_sentences(text):
    # [.?!] is used as an indicator of the end of a sentence. It is
    # preceded by [^.A-Z] and followed by [^.0-9] to avoid capturing
    # ellipses, decimal numbers, and initials. \'* is used to ensure
    # that the the ends of quotations are captured. \s* captures
    # whitespace between sentences, which will be replaced with a
    # newline character. [^\n] is used to ensure that the sentence is
    # not already followed by a newline character, e.g. at the end of a
    # paragraph.
    return re.sub(r'([^.A-Z][.?!][^.\w]\'*)(\s*)([^\n])', r'\1\n\3', text)


def eliminate_newlines_after_specified_acronyms(text, acronyms):
    for acronym in acronyms:
        text = text.replace(acronym + '\n', acronym)
    return text


if __name__ == '__main__':
    main()
