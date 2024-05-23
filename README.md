# Rock Paper Scissors
---

## Overview <a name="overview"></a>

This is an implementation of the classic Rock Paper Scissors game in Python. The aim of the game is to beat the computer by choosing a gesture that defeats its choice based on the following rules: Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock. The game prompts the player to enter their choice and then randomly generates the computer's choice. It then compares both choices to determine the winner and displays the result. The player can play multiple rounds within one game and keep record of their scores as well as see their success rate of winning the game.

UPDATE [live site](https://justynath.github.io/landmarks-quiz/)

UPDATE ![Am I Responsive](./assets/readme-resources/am-i-responsive.png)

## Table of Contents
1. [**Overview**](#overview) 
2. [**Planning**](#planning)
    - [**Aim**](#aim)
    - [**Targeted Audience**](#targeted-audience)
3. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Flowchart**](#flowchart)
        - [**Design Choices**](#design-choices)
4. [**Features**](#features)
    - [**Welcome Screen**](#welcome-screen)
5. [**Future Features**](#future-features)
6. [**Technologies**](#technologies)
7. [**Testing**](#testing)
    - [**Manual Features testing**](#features-testing) 
    - [**Bugs Resolved**](#bugs)
    - [**Python Validator Testing**](#validator-testing)
8.  [**Deployment**](#deployment)
9.  [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Anknowledgements**](#anknowledgements)

---

## Planning <a name="planning"></a>

### Aim <a name="aim"></a>
The aim of creating the Rock Paper Scissors game in Python for a user is to offer a simple, engaging, and interactive way to enjoy a classic game through a digital medium. It provides users with a quick and fun break, allowing them to play against the computer and test their luck and strategy. Additionally, the game serves as a practical demonstration of basic programming capabilities, potentially inspiring users to explore and learn more about coding and software development. By delivering an easy-to-use and entertaining application, it aims to enhance the user's experience with technology and gaming.

### Targeted Audience <a name="targeted-audience"></a>
The targeted audience for the Rock Paper Scissors game includes casual gamers looking for quick entertainment. It is great for individuals interested in classic games and those who enjoy small, interactive applications that can be played in short bursts. The game appeals to a broad range of ages and skill levels, making it accessible and enjoyable for anyone with a few minutes to spare.

---

## UX <a name="ux"></a>

### User Stories <a name="user-stories"></a>
- As a user, I want to easily understand how to start and play the game.
- As a user, I want the option to play multiple rounds within one game.
- As a user, I want to input my choice of rock, paper, or scissors.
- As a user, I want the game to randomly generate the computer's choice.
- As a user, I want to see the result of each round, including both my choice and the computer's choice.
- As a user, I want to know if I won, lost, or if the game was a draw.
- As a user, I want to be able to exit the game easily when I am done playing.
- As a user, I want to know what my overall success rate is while playing the game.
- As a user, I want clear instructions and feedback throughout the game to enhance my playing experience.

### Design <a name="design"></a>
UPDATE

#### Flowchart <a name="flowchart"></a>

#### Design Choices <a name="design-choices"></a>

---

## Features <a name="features"></a>
UPDATE

### Welcome Screen <a name="welcome-screen"></a>
On the welcome screen the user is asked to enter their name 
UPDATE ![welcome page](./assets/readme-resources/welcome-page.png)

## Future Features <a name="future-features"></a>
UPDATE
While the current version of the project is fully functional, I have some exciting features planned for future updates. Here are a few ideas that I didn't have time to implement in this release:

- Login system for keeping accurate scores record

---

## Technologies <a name="technologies"></a>
1. Python: The program was written entirely in Python.
2. Github: Used to store the project's code after being pushed from Git.
3. Gitpod: The terminal was used to commit my code and push it to Github.
4. Git: Was used for version control through the vscode terminal.
5. Heroku: Used to deploy, manage, and scale my application.

---

## Testing <a name="testing"></a>
UPDATE

### Manual Features Testing <a name="features-testing"></a>

|  Feature |  Action | Effect |
|---|---|---|
|Start Quiz button|Click|Displays the first question|
|Next button|Click|Displays the next question|
|Try Again button|Click|Starts the quiz and displays the first question|
|Github link in the footer|Click|Opens the github repository in new tab|
|Linkedin link in the footer|Click|Opens the Linkedin profile in new tab|

### Bugs Resolved <a name="bugs"></a>

**Introduction**
This section provides a summary of bugs that have been identified, reported, and subsequently resolved.

**Bug Tracking**
Below is a summary of resolved bugs:

| Bug ID | Bug Description | Status |
|--------|-----------------|--------|
| #001   | After adding welcome page, the 'Start Quiz' button not working correctly | Resolved |
| #002   | The background on feedback page is not changing colour | Resolved |
| #003   | The background colour not reseting for first question | Resolved |

**Bug Details**
Here are the details of the resolved bugs:

**Bug #001**
- **Description**:  After I added the welcome page the 'Start Quiz' button was not working correctly (Jumping to question two, then repeating that question in a loop)
- **Resolution**: I removed the original event listener and added a new one to correctly respond to the 'Start Quiz' button
- **Impact**: Including a welcoming page gives more information about the quiz and allows the user to make decision about taking the quiz

**Bug #002**
- **Description**:  The background of the feedback page was not changing despite assigning a variable and getting element by class name
- **Resolution**: The element by class name is returned as an array, hence I needed to use indexing to return the first element
- **Impact**: When the colour of the background changes based on the score it give instant feedback to the user

**Bug #003**
- **Description**:  After taking the quiz for the second time the background of the first question was not reseting
- **Resolution**: I included if/else method in the startQuiz function to reset the background
- **Impact**: The user is reassured that the quiz has restarted and the previous score has been reset

### Python Validator Testing <a name="validator-testing"></a>

I validated my files using Code Institute's Python Linter

UPDATE ![python validator](./assets/readme-resources/validator-html.png)

---

## Deployment <a name="deployment"></a>

UPDATE

UPDATE The live link can be found here - [live site](https://justynath.github.io/landmarks-quiz/)

---

## Credits  <a name="credits"></a>
UPDATE

### Content <a name="content"></a>
- The fonts were imported from [Google Fonts](https://fonts.google.com/)
- The icons used were taken from [Font Awesome](https://fontawesome.com/)
- The colour scheme was inspired by this [article](https://muffingroup.com/blog/calm-color-palette/)
- I used this video tutiorial to set the structure of my quiz [JavaScript Quiz Tutorial](https://www.youtube.com/watch?v=PBcqGxrr9g8)
- I used chatGTP to reaserch information about the landmarks. The text content was written by me and enhanced by ChatGTP
- I used this article and my mentor's support for creating the shuffle function [article](https://medium.com/@omar.rashid2/fisher-yates-shuffle-a2aa15578d2f)


### Media <a name="media"></a>
- I used images from this website [images](https://www.jetpunk.com/quizzes/landmarks-quiz-1)

### Anknowledgements <a name="anknowledgements"></a>
- Medale Oluwafemi, my mentor at Code Institute for his guidance and invaluable support with this project
- Tutor support at Code Institute for assisting me with solving problems and fixing bugs and errors