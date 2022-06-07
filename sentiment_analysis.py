'''
Program Name: sentiment_analysis.py
Due Date: November 17, 2021
Description: This program imports a tweets file and a keywords file. It then calculates the happiness scores,
keyword tweets and total tweets for each region. It then returns a tuple with the happiness scores, keyword
tweets and total tweets in order of Eastern, Central, Mountain and Pacific.

Created by: Fahmid Abdullah
Student Number: 251244838
'''

def regionCalculator(lat, long): #calculates which region a coordinate is in
    lat = float(lat.lstrip('[').rstrip(','))
    long = float(long.rstrip(']'))

    if not 24.660845 <= lat <= 49.189787 or not -125.242264 <= long <= -67.444574:
        return False #returns False if latitude or longtitude out of range

    if -87.518395 <= long <= -67.444574: #checks longtitude coordinate between p1 and p3
        return 'eastern'
    elif -101.998892 <= long < -87.518395: #checks longtitude coordinate between p3 and p5
        return 'central'
    elif -115.236428 <= long < -101.998892: #checks longtitude coordinate between p5 and p7
        return 'mountain'
    elif -125.242264 <= long < -115.236428: #checks longtitude coordinate between p7 and p9
        return 'pacific'

def tweetEditor(tweet):
    tweetList = []
    for i in tweet: #Iterate through the entire tweet
        if len(i) > 1 and i.count(i[0]) != len(i):
            i = i.lstrip(i[0]) if not i[0].isalnum() else i
            i = i.rstrip(i[-1]) if not i[-1].isalnum() else i
        tweetList.append(i.lower())
    return tweetList #Returns the list of tweets formatted

def happiness(tweet,sentimentDict): #Calculates and returns the total sentiment value for each tweet
    totalSentiment = 0
    for word in tweet:
        for key in sentimentDict.keys(): #If a word matches anything in the sentimentDict, it adds the sentiment value to totalSentiment
            if word == key:
                totalSentiment += sentimentDict[key]
    return totalSentiment

def compute_tweets(fileTweets, fileKeywords):
    eHappiness, eKeyword, eTweets = 0,0,0 #eastern
    cHappiness, cKeyword, cTweets = 0,0,0 #central
    mHappiness, mKeyword, mTweets = 0,0,0 #mountain
    pHappiness, pKeyword, pTweets = 0,0,0 #pacific

    finalList = []
    try: #Attempts to open the two provided files in the parameter
        kFile = open(fileKeywords, encoding='utf-8', errors='ignore')
        tFile = open(fileTweets, encoding='utf-8', errors='ignore')
    except: #If either file does not exist it returns an empty list
        return finalList

    keywordDict = {}

    for k in kFile: #Creates a dictionary of the keywords with the values
        key_value = k.rstrip('\n').split(',')
        keywordDict[key_value[0]] = int(key_value[1])

    for t in tFile:
        item = t.split() #Splits each line (t) and converts it to a list (item)

        tweet = []
        for i in range(5, len(item)): #creates a list of all the words in the tweet portion
            tweet.append(item[i])

        #Enters the first two values (item[0],item[1]) in each line (t) into regionCalculator
        if regionCalculator(item[0],item[1]) == 'eastern':
            eTweets += 1 #Total tweets in central
            eHappiness += happiness(tweetEditor(tweet), keywordDict)
            if happiness(tweetEditor(tweet), keywordDict) != 0:
                eKeyword += 1
        elif regionCalculator(item[0],item[1]) == 'central':
            cTweets += 1 #Total tweets in central
            cHappiness += happiness(tweetEditor(tweet), keywordDict)
            if happiness(tweetEditor(tweet), keywordDict) != 0:
                cKeyword += 1
        elif regionCalculator(item[0],item[1]) == 'mountain':
            mTweets += 1 #Total tweets in mountain
            mHappiness += happiness(tweetEditor(tweet), keywordDict)
            if happiness(tweetEditor(tweet), keywordDict) != 0:
                mKeyword += 1
        elif regionCalculator(item[0],item[1]) == 'pacific':
            pTweets += 1 #Total tweets in pacific
            pHappiness += happiness(tweetEditor(tweet), keywordDict)
            if happiness(tweetEditor(tweet), keywordDict) != 0:
                pKeyword += 1

    #The following deals with values dividing by 0
    if eKeyword != 0:
        eastern = (round((eHappiness/eKeyword), 3), eKeyword, eTweets)
    else:
        eastern = ('N/A', eKeyword, eTweets)
    if cKeyword != 0:
        central = (round((cHappiness/cKeyword), 3), cKeyword, cTweets)
    else:
        central = ('N/A', cKeyword, cTweets)
    if pKeyword != 0:
       pacific = (round((pHappiness/pKeyword), 3), pKeyword, pTweets)
    else:
        pacific = ('N/A', pKeyword, pTweets)
    if mKeyword != 0:
        mountain = (round((mHappiness/mKeyword), 3), mKeyword, mTweets)
    else:
        mountain = ('N/A', mKeyword, mTweets)

    #Creates a tuple of the happiness value, number of keywords, and the total tweets in each region
    finalList.append(eastern)
    finalList.append(central)
    finalList.append(mountain)
    finalList.append(pacific)
    return finalList

compute_tweets('tweets.txt', 'keywords.txt')
