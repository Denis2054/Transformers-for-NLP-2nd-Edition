#BLEU : Bilingual Evaluation Understudy Score
#Copyright 2020, MIT License BLEU Examples
#REF PAPER: Kishore Papineni, et al.,2002,“BLEU: a Method for Automatic Evaluation of Machine Translation“. 
#                                                https://www.aclweb.org/anthology/P02-1040.pdf
#NLTK : Natural Language Toolkit
#NLTK sentence_bleu doc: http://www.nltk.org/api/nltk.translate.html#nltk.translate.bleu_score.sentence_bleu
#NLTK smoothing doc: https://www.nltk.org/api/nltk.translate.html
#NLTK REF PAPER for smoothing():Chen et al.,http://acl2014.org/acl2014/W14-33/pdf/W14-3346.pdf
#REF DOC  : https://machinelearningmastery.com/calculate-bleu-score-for-text-python/

from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction

#Example 1
reference = [['the', 'cat', 'likes', 'milk'], ['cat', 'likes' 'milk']]
candidate = ['the', 'cat', 'likes', 'milk']
score = sentence_bleu(reference, candidate)
print('Example 1', score)

#Example 2
reference = [['the', 'cat', 'likes', 'milk']]
candidate = ['the', 'cat', 'likes', 'milk']
score = sentence_bleu(reference, candidate)
print('Example 2', score)

#Example 3
reference = [['the', 'cat', 'likes', 'milk']]
candidate = ['the', 'cat', 'enjoys','milk']
score = sentence_bleu(reference, candidate)
print('Example 3', score)


#Example 4
reference = [['je','vous','invite', 'a', 'vous', 'lever','pour', 'cette', 'minute', 'de', 'silence']]
candidate = ['levez','vous','svp','pour', 'cette', 'minute', 'de', 'silence']
score = sentence_bleu(reference, candidate)
print("without soothing score", score)

chencherry = SmoothingFunction()
r1=list('je vous invite a vous lever pour cette minute de silence')
candidate=list('levez vous svp pour cette minute de silence')
        
#sentence_bleu([reference1, reference2, reference3], hypothesis2,smoothing_function=chencherry.method1)
print("with smoothing score",sentence_bleu([r1], candidate,smoothing_function=chencherry.method1))


