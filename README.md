# environmental-quiz

#### For the capstone project of the **CS50 Web Programming with JavaScript and Python** I have created a multiple choice quiz. 

## Django backend

The quiz database is based on four clasess as you will see from the models.py file. First of all, it has a Question and an Answers class, with the question class as foreign key. In this way for each question I am be able to have multiple answers but only one correct, which I'm keeping track of with a Boolean field. The Question class also has a field in which I'm storing the explanation to the question. This is shown to the user after an answer is selected, regardless if it's correct or not. 

The database is completed by two additional models. One that keeps the score of the user and one that contains the URLs of the background images. Since the quiz is rendered in a single html page, I'm changing the background dynamically leveraging Django template language. 

## Views

In my views.py file I have four views:
* index
* questions
* score
* summary

### Index
In the index view I am generating a random number between 1 and 10000 with python's random function and then appending it to a list called scoreId, which is a global variable. I'm using this number to track the user and attribute him the correct score. This is a provisional solution as it's not designed for more than one quiz takers at the same time but it makes the quiz work properly. A more comprehensive solution would've been to use Django's session key but it would've been redundant for the sake of this project. 

### Questions
This is the main view as it is here that all the action takes place. It renders the questions.html template, a single page where all the quesitons are rendered. As you can see from urls.py, the function accepts an integer as argument, if it is between 1 and 10 (1 and 10 included) than it finds the correct question, aswer, background image and pass them as context to the questions.html template. Otherwise, a 404 error is thrown. This range (1-10) happens to match the number of questions that compose the quiz.

### Score
The score view keeps track of the user score throughout the quiz. It uses JavaScript fetch calls to update the users score after every correct answer with a PUT method.

### Summary
The summary view renders a standalone template where the user is displayed its quiz score. The template contains a background image, which is different for mobile and desktop, an h1 tag with the score and a p tag with a short sentence. The sentence changes accordingly to the user's score using Django's built in if tag.

## JavaScript
The quiz has one JavaScript file called questions.js. This is used only for the questions.html file, where the actual quiz takes place. All the events listners are happenning only after the DOM is loaded since they are place inside the event listener DOMContentLoaded. I have two functions, one for updating the score (as detailed above through a fetch call) and one for disabling the radio buttons, that I'm using for the multiple choices, after one is selected. 

The event listeners are:
* next button
* verify button
* multiple choice

The **next button** has an event listener associated to the click. When a click happens the the current question number is retrieved using the this.dataset attribute. After converting it into an integer and adding a one to this number, I'm then composing a new url using string concatenation. Using location.replace to pass the new URL, I'm rendering the next question and disallowing the user to go back in history.

The **verify button** appears only after the last question has been answered. When clicked, it takes the user to the summary.html template where his quiz score is displayed.

The **multiple choice** event listener is the most complex. First of all, I'm disabling the radio button by calling the disableRadio function one each of the buttons through a for loop. I'm then getting the value of the answer with event.target in order to know wheter the multiple choice that has been selected is correct or not. If the answer is correct I'm updating the score with a call to the score function and writing "Correct" in an empty h2 tag with innerHTML. Otherwise I'm only writing "Incorrect". In both instances the question's explanation is displayed by changing its display from hidden to block with querySelector. 

I'm also using the Window interface's matchMedia() method to check wheter the viewport is a mobile one. In that case, I'm not only dislaying the explanation but also changing the question's visbility to hidden as smaller viewports don't have enough real estate to display all this text on the screen. Hiding the question seemed the most reasonable choice for a better mobile experience.

## CSS
I have three seperate files for each of the html templates. A part from the standard styling of the various html elements, I'm using mediaqueries to make the website responsive.