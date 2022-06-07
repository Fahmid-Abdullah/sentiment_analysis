'''
Program Name: main.py
Due Date: November 17, 2021
Description: This program takes tuple and prints it in a readable fashion

Created by: Fahmid Abdullah
Student Number: 251244838
'''


from sentiment_analysis import compute_tweets

userTweet = input('Enter File Containing Tweets: ')
userKeyword = input('Enter File Containing Keywords: ')
results = compute_tweets(userTweet, userKeyword)

print('Eastern Region: Happiness score: {}, {} keyword tweets, {} total regional tweets'.format(results[0][0], results[0][1], results[0][2]))
print('Central Region: Happiness score: {}, {} keyword tweets, {} total regional tweets'.format(results[1][0], results[1][1], results[1][2]))
print('Mountain Region: Happiness score: {}, {} keyword tweets, {} total regional tweets'.format(results[2][0], results[2][1], results[2][2]))
print('Pacific Region: Happiness score: {}, {} keyword tweets, {} total regional tweets'.format(results[3][0], results[3][1], results[3][2]))
