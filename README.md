I started with reading the assignment to get an understanding on what needs to be done. I looked over the other attached documents and made mental notes about how I could divide the problem into pieces and solve each piece. My plan came out to be: A) Turn txt files into list of strings that are words B) Iterate through the list of necromancer words and associate a counter with each unique word that is not found in the stop_words file C) print the words that had the largest number of occurrences.


Before writing code, I created a directory to hold my python file and the text files from I wanted to get the data from within the files into python so after doing that, I launched Vim and created my python and began making the code to take the text documents and get a list of words. I couldn't remember the syntax for this so I went to geeksforgeeks to see how it was done. I printed out the list to make sure it worked correctly and noticed some weird characters in the output, which I kept in mind for when I went to the next step in the program.


The next step in the program was to build a loop that would iterate through the words in the program and put them into a dictionary that stores a value which represents the number of times the number occurred. So I made a loop that removed weird characters and split words by spaces, then had the words checked against the list of stop words for matches, then put it in the dictionary.


After that I sorted the dictionary by values and printed the first 25 elements in the dictionary to get the answer. I checked to see if python had a built in way to sort dictionaries this way, and found on stack overflow that there was.


At the end, I created a github repository to keep track of my project and attached a readme.md to the repository.
