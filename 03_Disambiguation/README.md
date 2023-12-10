Comparison of the two taggers:
1. Both taggers have perfect scores in Tokens, Sentences, Words categories, indicating they are equally effective at tokenizing the input and identifying sentence and word boundaries.
2. The UDPipe tagger has a slightly higher accuracy (95.89%) compared to the perceptron tagger (94.66%). This suggests that UDPipe may be slightly better at identifying universal part-of-speech tags.
3. For the Feats category, the UDPipe model shows a slightly higher accuracy (96.28%) than the perceptron tagger which had a perfect score. This indicates that UDPipe might be better at capturing the morphological characteristics of Spanish.
4. Both taggers achieved perfect scores for UAS (Unlabeled Attachment Score) and LAS (Labeled Attachment Score), suggesting that they are equally effective at syntactic parsing when it comes to identifying the correct head of each word and the correct dependency label.
5. Overall, the UDPipe tagger seems to perform slightly better on UPOS and morphological features, while the perceptron tagger has an edge in lemmatization. 
