import re

def t9_decode(t9nd_text):
	t9_dict = {
		2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
		6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
	}
	normalized = ""
	t9_words = re.findall(r'((\w)\2{0,4})|(\D)', t9nd_text)
	for t9_sequence, t9_num, word_delim in t9_words:
		if t9_sequence:
			normalized += t9_dict[int(t9_num)][len(t9_sequence)-1]
		if word_delim:
			normalized += word_delim
	return normalized
