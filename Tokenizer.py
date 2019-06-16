import nltk
f=open('fil.txt','r')
text=f.read()
f.close()
print text
stokens = nltk.sent_tokenize(text)
print "Sentence tokenized"
print stokens
tokens = nltk.word_tokenize(text)
print "Word tokenized"
print tokens
tagged = nltk.pos_tag(tokens)
print tagged
nt=['NN','NNP','NNS','NNPS']
d={}
for word,tag in tagged:
	if tag in nt:
		if word not in d:
			d[word]=1
		else:
			d[word]+=1
d=sorted(d,key=d.get,reverse=True)
print ("Five most frequently occuring nouns are")
print d[0:5]	
