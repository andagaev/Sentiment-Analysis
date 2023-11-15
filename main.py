'''
Step 1: 
To start, define a function called strip_punctuation which takes one parameter,
a string which represents a word, and removes characters considered punctuation from everywhere in the word.
'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    new_s = ""
    for x in s:
        if x not in punctuation_chars:
            new_s += x
    return new_s

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
'''
Step 2:
Define a function called get_pos which takes one parameter, a string which represents one or more sentences,
and calculates how many words in the string are considered positive words.
'''
def get_pos(s):
    str_lst = strip_punctuation(s).lower().split(" ")
    count = 0

    for word in str_lst:
        if word in positive_words:
            count += 1
    return count

'''
Step 3:
Define a function called get_neg which takes one parameter, a string which represents one or more sentences,
and calculates how many words in the string are considered negative words.
'''

def get_neg(s):
    str_lst = strip_punctuation(s).lower().split(" ")
    count = 0

    for word in str_lst:
        if word in negative_words:
            count += 1
    return count
'''
Open the file project_twitter_data.csv whicn contains:
- text of a tweet
- number of retweets of that tweet
- number of replies to that tweet 
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
Create a csv file called resulting_data.csv, which contains:
- Number of Retweets
- Number of Replies
- Positive Score (which is how many happy words are in the tweet)
- Negative Score (which is how many angry words are in the tweet)
- Net Score (how positive or negative the text is overall) for each tweet.
'''
with open("project_twitter_data.csv", "r") as input_file, open("resulting_data.csv", "w") as output_file:
    header = input_file.readline()
    output_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    output_file.write("\n")

    for row in input_file:
        tweet = row.strip().split(",")
        retweets = int(tweet[1])
        replies = int(tweet[2])
        content = tweet[0]

        stripped_content = strip_punctuation(content)
        row_string = "{},{},{},{},{}".format(retweets, replies, get_pos(stripped_content), get_neg(stripped_content), get_pos(stripped_content) - get_neg(stripped_content))
        output_file.write(row_string)
        output_file.write("\n")