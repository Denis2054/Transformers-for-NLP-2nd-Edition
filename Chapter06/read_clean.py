#Pre-Processing datasets for Machine Translation
#Copyright 2020, Denis Rothman, MIT License
#Denis Rothman modified the code for educational purposes.
#Reference:
#Jason Brownlee PhD, ‘How to Prepare a French-to-English Dataset for Machine Translation
# https://machinelearningmastery.com/prepare-french-english-dataset-machine-translation/


from pickle import load
from pickle import dump
from collections import Counter
 
# load a clean dataset
def load_clean_sentences(filename):
	return load(open(filename, 'rb'))
 
# save a list of clean sentences to file
def save_clean_sentences(sentences, filename):
	dump(sentences, open(filename, 'wb'))
	print('Saved: %s' % filename)
 
# create a frequency table for all words
def to_vocab(lines):
	vocab = Counter()
	for line in lines:
		tokens = line.split()
		vocab.update(tokens)
	return vocab
 
# remove all words with a frequency below a threshold
def trim_vocab(vocab, min_occurance):
	tokens = [k for k,c in vocab.items() if c >= min_occurance]
	return set(tokens)
 
# mark all OOV with "unk" for all lines
def update_dataset(lines, vocab):
	new_lines = list()
	for line in lines:
		new_tokens = list()
		for token in line.split():
			if token in vocab:
				new_tokens.append(token)
			else:
				new_tokens.append('unk')
		new_line = ' '.join(new_tokens)
		new_lines.append(new_line)
	return new_lines
 
# load English dataset
filename = 'English.pkl'
lines = load_clean_sentences(filename)
# calculate vocabulary
vocab = to_vocab(lines)
print('English Vocabulary: %d' % len(vocab))
# reduce vocabulary
vocab = trim_vocab(vocab, 5)
print('New English Vocabulary: %d' % len(vocab))
# mark out of vocabulary words
lines = update_dataset(lines, vocab)
# save updated dataset
filename = 'english_vocab.pkl'
save_clean_sentences(lines, filename)
# spot check
for i in range(20):
	print("line",i,":",lines[i])
 
# load French dataset
filename = 'French.pkl'
lines = load_clean_sentences(filename)
# calculate vocabulary
vocab = to_vocab(lines)
print('French Vocabulary: %d' % len(vocab))
# reduce vocabulary
vocab = trim_vocab(vocab, 5)
print('New French Vocabulary: %d' % len(vocab))
# mark out of vocabulary words
lines = update_dataset(lines, vocab)
# save updated dataset
filename = 'french_vocab.pkl'
save_clean_sentences(lines, filename)
# spot check
for i in range(20):
	print("line",i,":",lines[i])
