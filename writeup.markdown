# Assignment 2 Write up and Reflection
**Members: Brandon Hoang, Anna Zou, Rae Zhang**

## ***Project Overview***

    Our program downloads four books written by the same author, Jane Austen, from Project Gutenberg (http://www.gutenberg.org/) and stores and processes each one of the four books. Our program converts all four books into dictionaries with words as keys and frequencies of words as values. Our goal is to compare and contrast the four books and derive interesting insights about Jane Austen’s writing style from our analysis. Therefore, we analyzed her word choices, word frequencies, text sentiment, and similarities of the four texts by using tools like counter and natural language processing.

## ***Implementation***

    When designing the architecture of our program, we first decided on the five kinds of analysis we would like to conduct: top 20 common words, top 20 common words excluding stopwords, summary stats of unique words vs. total words, text sentiment, and test similarity. Then, we decided on what functions we would like to use and design for each one of the analyses (see below). From this quick overview we were able to see what kind of data structure the textbooks would need to be in, what kind of packages we would be importing, and what kind of methods we would be designing and writing. 

![implementation](python1.jpg)

    Our first step of implementing the project was to download the books with URL and stored the text files both as a string variable and processed as dictionaries since we know we would be utilizing both structures in future methods. We then imported analyze_book.py file from class assignment into our program to leverage some of the simple functions written in this file. Then, we started designing and writing each analysis one by one. For each analysis, the hardest part was debugging and testing to make sure the functions performed correctly and outputted accurately. These five analyses are built upon each other and some are called in order to perform another analysis. All of these relationships were carefully designed and planned out so that our program was as efficient as possible. Overall, our program is built upon three major components: downloading books, processing/storing books, five analyses.

    One design decision we had to make was to figure out the best way of presenting our output. We understood that the presentation of the final results is just as important as the data itself. Therefore, for both the first and third analysis, we decided to go one step further in order to present our output in a user-friendly fashion. For the first analysis, we utilized a for loop to print results for each book in a table so that it’s easy to compare and contrast. For the third analysis, we used the tabulate package to print the summary statistics in a nice table format with headers so it’s easier to comprehend and compare across results.  

## ***Results***

    From our analysis on the top 20 most common words, it is found that the lists returned are very similar. The lists contain mostly prepositions, transition words, and pronouns. This is not surprising since they are common in sentence structure across any book. To get a better sense of the similarity between each of Jane Austen’s books it is better to run an analysis that disregards these common prepositions, transition words, and pronouns. That’s where our Top 20 excluding stopwords comes in next. The result of the top 20 most common words are presented below. 

![results](python2.jpg)

    Then, the analysis of most common words of the four texts excluding the stop words allowed us to get a more accurate sense of word choice frequencies. Some of the interesting insights we found include: the word “said” was on the list for all four books which shows that Jane Austen’s books are all dialogue heavy, “could” “would” and “must” are frequently used across all four books which shows the author’s preference of word choice regarding sentence sentiment, character names are among the most frequent words regardless what topics or stories each book was on which shows the focus on characters and stories between them in all of Jane Austen’s novels. 

![results](python3.jpg)

    By computing a summary stats of the four books, we gained a better understanding of Jane’s word choices and writing style. The book Pride and Prejudice and Sense and Sensibility are very similar in total number of words and percentage of unique words that were used. On the other hand, the other two books Northanger Abbey and Mansfield Park are very different in terms of this measurement: Northanger Abbey is only around half of text length compared to Mansfield Park, but its percentage of unique words almost doubled. We think this may be due to the fact that longer texts allow higher possibility of repetition and less creativity in differentiating word choices, especially when similar scenarios came across in the story.

![results](python4.jpg)

    According to our natural language processing performance, the overall sentiment result of all four books are very similar. This sentiment analysis allows us to conclude that although the four books are in different lengths and written across 10+ years, Jane’s style and overall sentiment remains neutral across her compositions. This is interesting as we assumed her writings may lean slightly towards the negative mood more, or have drastically different styles across different books.

![results](python5.jpg)

    From the texts' similarity comparison, four texts’ Jaccard similarity score is quite low, but considering the fact that each book is compared against all four books combined, some numbers are surprisingly high. Across all four books, other than Northanger Abbey, the other three had similar scores which further proves that the books are indeed similar in terms of word choices, even though they are written in different years and of different stories. Since Northanger Abbey was Jane Austen’s first completed novel in full in 1803 while the other three were completed and published around 1811-1814, it makes sense that Northanger Abbey was less similar to the other three while the other three were more similar in word choices. 

![results](python6.jpg)

    Overall, we were able to take a closer look at Jane Austen’s four books and derive interesting insights about her writing style by using analytical and computational methods. 

## ***Reflection***

    Overall the project went well. We not only were able to implement many functions that we learned in class into this project but also explored new analysis such as the natural language processing technique as well as Jaccard similarity score comparison. Although creating and debugging the codes took us some time, it gave us a sense of accomplishment when we were finally able to run all of them. As long as we kept writing and debugging, we could improve little by little. 

    At the beginning of this project research, we eliminated the natural language processing method and were going to use the Markov analysis method. After careful planning and consideration of the fact these four texts are from the same author, we realized that NLP may suit our texts better and provide more insights. From this experience, we learned that it is always a good idea to research and consider all the possible approaches before making any assumptions. 

    There are also several things we can improve going forward. For example, although we embraced punctuations and digits in addition to the stopwords, we can eliminate more stopwords or symbols that may not be recognized by the program. This way our word selection and frequency analysis can be more comprehensive, thus providing more insights. Secondly, we can dissect the texts and analyze their sentiments by chapters or parts as opposed to comparing the whole book. By doing so will allow us to extract mood transitions and compare emotional flows (or changes)  throughout each story. Last but not least, for this project we divided and conquered the work among each team member and completed it individually. Although splitting the work may seem efficient and everything went smoothly, for better learning purposes we can try peer coding next time. By working together in WebEx, we will be able to learn from each other’s logic, as well as to improve on our codes collectively. 