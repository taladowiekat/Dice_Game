with open("project2(Madlib generator)/story.txt", "r") as f:
    story = f.read()

# initialize list to store words or phrases that will be extracted from the story
# words = []
words = set() # to store the unique words

# to keep track of words inside the < > if we found the start of a phrase we hve found the end 
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        '''i+1 is used because slicing in Python excludes the end index, 
        so adding 1 includes the > character in the extracted substring'''
        word = story[start_of_word:i+1]
        # words.append(word)
        words.add(word)
        start_of_word = -1

# then we want to ask the user to give us values for each of the words -> 
# the way to do this , by using dictionary
# make a loop through the all keywords on the set 

answers = {}

for word in words:
    #prompt the user to enter a replacement for each word/phrase enclosed in < >.
    answer = input("Enter a word for " + word + ": ")
    #store the user's input in the answers dictionary, using the word as the key.
    answers[word] = answer

# Replace the placeholders in the story with the user's input
for word in words:
    # Replace each word/phrase in the story with the user's provided answer
    story = story.replace(word, answers[word])

# At this point, the 'story' variable contains the updated text with all replacements.
print(story)
