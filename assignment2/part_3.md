## 1. Project Overview

I choose to use Wikipedia as my data source. I used Characterizing by Word Frequency, Computing Summary Statistics, and Natural Language Processing techniques to analyze and process the data.

## 2. Implementation

I used the word frequency and computing summary statistics to figure out the frequency of the title within the content of the Wikipedia page as well as figuring out the top 10 most occuring words in the content of the page. 

- Firstly, I cleaned the data as the data pulled from wikipedia contained punctuations, numbers and other unecessary strings that needed to be cleaned up. I also converted all letters into lowercase to better identify words re-occurance throughout the content of the page. 
- After the data was cleaned, I calculated the frequency of each words in the content and stored it as a dictionary (dictionary of each word and its frequency). Using the newly created dictionary of the words and frequency, I arranged the dictonary decending from the most frequent and printed the first 10 objects in the dictionary to display the top 10 most frequent words in the Wikipedia page of selection.

I also used Natural Language Processing techniques to validate the neutrality of Wikipedia contents. An informational website like Wikipedia should strive to have an neutral content for its users.

- Using the Natural Language Processing, I calcuated the Sentiment Analysis of the Wikipedia Content. From the analysis, I isolated the neutrality measurement. If the neutrality measurement value is greater or equals to 0.80, 80% neutral, the content is deemed to be neutral. This is a good way to find contents that are not neutral.

Lastly, I identified pairs of same words in two pages. 
- I referenced the words in one source to another to find pairs that are common on both pages.

## 3. Results

Through the Work Frequency Anaylsis, it was interesting to find how frequent the title of the Wikipedia Page is in the content of the page. Some pages didn't contain the title at all in the whole content and some titles were mentioned multiple times in the content. Another interesting think I've discovered through the analysis was the top frequent words in the each of the Wikipedia Pages. The most comon words throughout multiple pages were words like: the, of, and, to, and a. I expected those words to be frequent in any form of texts but its interesting to see validation of the hypothesis.

Intereting finding from validating the neutrality of the Wikipedia pages were that most pages were neutral except for pages assocaited with what the society indentifies as 'bad' or evil. For example, the Wikipedia page of 'Nazism' was found to be not neutral through my anaylsis. Nazism has a very strong negative connotation in the society and that aspect has played a significant roll on the content as all Wikipedia contents are written by the users as its an open source encyclopedia.

The common words found comparing contents of two different Wikipeida pages validate the hypothesis made for word frequency.

## 4. Reflection

The process is smooth and repeatable. Anyone other than me can use the program to indentify the word frequency, most frequent words, sentiment analysis results and whether the Wikipeida page is neutral or not. 

The project could have had a wider scope looking into validating the content of the Wikipedia pages. For the future, if I were to further expand on this project, I could analyze the professionality of the words choosen in the content of the pages, and to go deeper, audit the sources used in the Wikipedia pages.

This specific assignment is very helpful in implemeting to my finial group project. It has a lot if simmilarities with our final project. Our group will need to use live data (api) for the COVID cases to indentify the frequencies of cases in each region to deem the safety to travel there or not.