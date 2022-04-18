# Sentimental-Analysis-Twitter-API
This project aims to provide a Sentimental Analysis of any keyword through Tweets using twitter API to judge the prefrence of the public.

## Program
This uses various python libraries including tweepy,textblob,tweet-preprocessor.

The tweets containing the keyword are filtered out put into a list,which is then cleaned,analyzed,and given a sentimental polarity score between -1 to 1.
Later we calculate the mean sentiment for the keyword on twitter and we can get an average sentimental score for the keyword on twitter.

This can have its application for a Brand wanting to know its position on social media platforms like twitter,or access the likelablity between two Keywords through public opinions.(Like if people prefer Russia over Ukraine or vice versa)

I use these scores to compare two keyword on the basis of there average sentimental scores.
The accuracy of the program increases when we have a larger data set (More Tweets = Better Result).

Kindly refer for the Output here: https://user-images.githubusercontent.com/100189617/163753003-0f2bf4a7-7cec-4892-810e-e4dc4d012b29.png
