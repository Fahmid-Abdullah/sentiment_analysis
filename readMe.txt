Program Structure:
-The program consists of two Python files: main.py and sentiment_analysis.py.
-The sentiment_analysis.py file contains the core functionality for analyzing sentiment in tweets using keywords.
-The main.py file serves as the main program and interacts with the user.

Input Files:
-The program requires two input files: tweets.txt and keywords.txt.
-tweets.txt contains the tweets with their details, including latitude, longitude, date, time, and text.
-keywords.txt contains sentiment keywords along with their happiness scores.

Program Execution:
-Execute the program by running main.py.

User Interaction:
-When you run main.py, it will prompt you to provide the filenames for the two required input files: tweets.txt and keywords.txt.

Processing:
-The program reads the input files and processes the data according to the specified instructions.

Sentiment Analysis:
-Sentiment analysis is performed by matching keywords from keywords.txt with the text of each tweet in tweets.txt.
-A "happiness score" is calculated for each tweet based on the keywords found in the text.
Timezone Analysis:

-The program also determines the timezone (Eastern, Central, Mountain, or Pacific) of each tweet based on its latitude and longitude.
-It computes the average "happiness score" for each timezone, considering only the tweets that contain sentiment keywords.

-Output:
The program provides the results, including the average happiness score and counts of keyword tweets and total tweets, for each of the four timezones.
The results are displayed in a readable format.