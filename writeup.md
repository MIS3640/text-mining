##### **MIS3640**

##### **Jan Sirimongkolkasem, Amy Phenjati, Sammi Xu**

##### **March 17th, 2021**

##### **Assignment 2**

## Project Overview
Our goal is to look at the Star Wars movie series and explore the viewer reviews. By this, we can compare their sentiments with movie ratings to see if they align. We use data from IMDB data sources. We use natural language processing(NLTK) to work with the harvested human language data to perform sentiment analysis. We hope to examine the correlation between the reviews and the ratings. Furthermore, we would try to learn the overview trend of the people's opinions on the movie series. 

## Implementation
We implemented the following three steps to achieve our goal for this investigation.

*Step 1: Data Loading*

Firstly, we built a list containing the titles of all the Star Wars series movies. Then data is imported from the IMBD data using the imdbpie project. The data includes movie title, IMDB ID, total numbers of reviews, rating given by the user, specific reviews from each user, and their username. It is then stored in a list, with each item as a dictionary for a movie. We then store the data in a local file using pickles, allowing us access to the data without running the script every time. It also makes it faster to perform analysis later on. We decided to combine the data into a single, extracted file due to its convenience of access. If each movie information is stored in a separate local file, each step would have to be performed several times.

*Step 2: Data Cleaning*

Once everything is imported into a local file, we clean the data by removing punctuations and whitespace. We decided to perform this via strippables to prevent the situation in which the sentiment analyzer does not recognize a word token due to the punctuation attached. It would be easier not to clean the data and examine the extracted local file's data. An alternative would be to keep some of the punctuations and use vader_lexicon, which will also take account of punctuations in the sentiment analysis process (e.g. using exclamation marks together with a positive word would suggest a strong positive tone). However, not all of the punctuations are used to express sentiments. Most of them are more likely to be sentence separators and other symbols. Considering the probability of this scenario, we decided to remove all punctuations and focus on analyzing word choices.

*Step 3: Sentiment and Further Analysis*

Our sentiment analysis is done using the natural language toolkit or the "nltk" library. The output of functions implemented in this section is sentiment polarity scores for positivity, negativity, and neutrality. In addition, there is a compound score, which is a normalized sum of all lexicon ratings. 

For further analysis, we will be comparing the sentiment scores for each Star Wars movie to the numeric score on IMDB - focusing on two numerical variables: the compound score(-1,1) and the IMDB rating (0,10). Coordinates for each movie will be graphed to visualize if there is any correlation between the variables. In addition, the compound score will be plotted on a bar graph to see how they differ for each movie of the Star Wars sequel. 

## Results
After running the above four steps, we arrived at the following results. 
![](https://lh6.googleusercontent.com/CUEwJj_yQW4dRPaDJ9f24yyoR3RbsidMsfHpnq9Z10sLP-gEAiQl9AwEP-hURmnThc3yIrkakcLv1F25gYbHgPfJw4N3Okh_ySug7iPIlm0u1VY4TULwNNvw_uypcA1tK-FDtNSD)
###### Figure 1

Figure 1 is an example of the output of the sentiment analysis for each movie, classified by each reviwer.

![](https://lh5.googleusercontent.com/pfDdcexvyLqCmGEQl4nFCpZ5HJe9ay3wx5CRAl6mB38kCMYgZ0oN7F6lXHJf6CKNOh_IfcXT8ViS5bH52M-1veTYPa23zWV0X9iy4bU4YGYYMo5pZB7nFTyZx4gKQd7lbjSjN168) 
###### Graph 1
Graph 1 is a scatter plot showing the relationship between IMDB ratings and compound score. That is, each coordinate represents an individual review. Prior, we hypothesized that there would be a strong positive correlation between the two variables as we believed viewers who give good ratings would be inclined to write more positive reviews, generating a higher compound score. However, results suggest otherwise; based on the scatter plot created, there is little to no correlation between IMDB ratings and compound scores. From the graph, it is clear that reviewers are more likely to voice their opinions on the extreme ends of the spectrum, causing a gap in the middle.

![](https://lh6.googleusercontent.com/hzT9Lh3GNP52n-wexPkU0evQOOYsuPZ7aj9sIkUCFGRtifi4qvtzDK9GWU4jekVfyLBKtI2hoh2lr8rK-FeCjoTb6SD1KYl-gElbM1-HSkorWWomC3D_49PYu0-uhmokXw-E4ctS)
###### Graph 2
Graph 2 shows how users' sentiment towards Star Wars changes over time. The earliest movies (IV, V, and VI) released between 1975-1985 received more positive reviews, despite the less advancement of the use of special effects. After gaining some popularity in the market, Star Wars I, II, and III were released in the 2000s. On average, they received positive feedback from the audience, though it was relatively lower than the earlier ones. The last three movies were the results of a recent revival of the movie franchise. They have been widely criticized for their poorer quality. With the expectation built up from the previous movies, it would be reasonable that fans could be easily disappointed. Considering how much technology has evolved over the years, it is clear that special effects in the scenes are not a priority for the audience. 

## Reflection
From a process point of view, what went well was that the data loading process was easy to access and manage. The first stage of sentiment analysis was also not too difficult to perform. For the given timeframe, we believed that our project was appropriately scoped. By mapping out every step of the process and writing pseudocode before coding, we had a good plan for unit testing. With more time, we wish to dig deeper into further customizing the sentiment analysis. This is our first time coding as a group; thus, understanding that the key to completing the project is to collaborate is crucial. We wish we knew more about python visualization and the used library and its functions before starting the project. Initially, we thought pair programming through zoom call would work, but coding takes time, so doing it individually works better. Then, we combined the work for each step and discussed further actions. One prominent issue was that whenever there was a coding issue, the whole team was stuck, and we did not know what to do. To solve the problem, we asked Professor Li to help. Next time, we hope to collaborate more through pair programming and divide the task appropriately with the time constraints and skills.