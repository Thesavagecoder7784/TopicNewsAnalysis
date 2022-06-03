# Topic News Analysis
Analysis of news articles of a topic entered by a user by performing sentic computing

## Tools used:
- Python (Jupyter notebook)
- API: Newsapi
- Python packages - Newspaper & sentic
- GoogleNews for organizations

## About the project
Input: Enter a topic you are interested in and want to know th public opinion about (Eg.cryptocurrency)
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-27%20at%207.12.45%20PM.png)

1st Output:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.23.40%20PM.png)

Next adds all the details to a list:
- title
- date
- description 
- time 
- source
- text 
- keywords 
- summary
- links

Creates a dictionary of the following details:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.27.02%20PM.png)

Performs sentic computing on the articles and gets the following:
- lsentiment 
- sentence
- semantics 
- moodtags 
- sentics   

Example of one output:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.29.26%20PM.png)

Displays the mean polarity:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.30.44%20PM.png)

Graph of the number of times a word is associated with the topic:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.31.02%20PM.png)

Graph of the number of times a moodtag is assocaited with the topic:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.31.10%20PM.png)

Shows the mean plesantness, attention, sensitivity, aptitude:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.32.25%20PM.png)

Shows the number of of times of different sentics:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.32.37%20PM.png)

Shows the number of articles per sentiment:
![alt text](https://github.com/Thesavagecoder7784/images/blob/master/Screenshot%202022-05-28%20at%203.32.49%20PM.png)


