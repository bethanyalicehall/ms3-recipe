# Testing

## HTML validator
I inputted my HTML into the W3C Markup Validation service. I put each page through this. A few errors did appear on each page, mostly due to Jinja templating. An example is shown below

![Screenshot of HTML validation results](static/img/README/html.png)

## CSS validator
I inputted code into the W3C validation service and no errors were found

![Screenshot of CSS validation results stating that no errors were found](static/img/README/css.png)

## JS validator

I used [JS Lint](https://www.jslint.com) to review my JavaScript code.
- The first error which appeared quite a bit through my code was the use of single quotes instead of double quotes, so I changed those.
- I had missed off a few semi-colons at the end of and within functions - i corrected these.
Some warnings which I did not act upon in this instance, as they did not directly impact the functioning of the website or cause any console errors. However I will make a note of these for my learning going forward
- A few errors came up that certain lines were longer than 80 characters
- Advice to use function rather than => when there are longer functions

I also put my code through [JSHint](https://jshint.com/).
This gave some information of the following metrics.

![Screenshot of metrics from JSHint](readme-img/metrics.png)

This brought up some warnings however again as they did not directly impact the functioning of the site or cause a console error, I will take forward these points in my learning.

![Warning 1](readme-img/warning1.png)
![Warning 2](readme-img/warning2.png)
![Warning 3](readme-img/warning3.png)
![Warning 4](readme-img/warning4.png)



## Performance testing
I utilised the [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) performance testing software.
- The results of the lighthouse testing can be seen below for each page. 

### Home page
![Screenshot of Lighthouse testing for home page](readme-img/index-1.png)

### Level 1 page
![Screenshot of Lighthouse testing for routes page](readme-img/level1-1.png)

### Level 2 page
![Screenshot of Lighthouse testing for routes page](readme-img/level2-1.png)

### Fun Facts page
![Screenshot of Lighthouse testing for get in touch page](readme-img/facts-1.png)

## Accessibility testing
I utilised [Wave](https://wave.webaim.org/) which is a web accessibility evaluation tool.

- One error was dected, there was a paragraph, that the tool detected as looking like a heading so I changed that to an h2 element, from a paragraph element.
- Some contrast errors were picked up on the buttons on the level 1 and 2 pages, I changed the text from an ivory colour to a dark green colour.
- Some contrast errors were also acknowledged in the facts page, however they did still pass teh large text test and the text was large so it was ok.

## Responsiveness
- I utilised Chrome Developer tools to test responsiveness on different devices, the following devices were sucesfully tested through this.
    - iPhone SE
    - iPhone XR
    - iPhone 6/7/8
    - Samsung galaxy S8+
    - iPad Mini
    - Surface pro 7
    - Galaxy Fold
    - Nest Hub

- I manually tested the website on an iPhone 12 pro, an iPad 2 and a MacBook Air.


## Manual testing

### Functional testing

#### Testing elements on each page 

| Page | Element and expected action | Pass or Fail | 
| ----------- | ----------- | ----------- |
| All pages | There is a multi-toned green background | Pass |
| All Pages | When hovering over a link the pointer changes and there is a colour change to indicate interactivity | Pass |
| Home page | url linked in README.md displays Creature Corner homepage, and the frog Favicon is visbile | Pass |
| Home page | There is a main title and a subtitle, giving more information about purpose of site | Pass |
| Home page | The Play link takes you to level 1 of the memory game | Pass |
| Home page | The Rules link opens up a modal explaining the rules| Pass |
| Home page | Within the modal there are clear rules and a link to level 1 to start playing and a button to exit the modal | Pass |
| Home page | The Animal facts link takes you to the facts page| Pass |
| Level 1 and Level 2 | The game board fits centrally within the screen| Pass |
| Level 1 and Level 2| The button to start the game, starts the timer for the game | Pass |
| Level 1 and Level 2| The link back to the home page takes you to the home page| Pass |
| Level 1 and Level 2| The timer and the moves counter work correctly| Pass |
| Level 1 and Level 2| Each card starts face down| Pass |
| Level 1 and Level 2| Each card turns over when clicked on adn you can only turn 2 cards over at the same time| Pass |
| Level 1 and Level 2| If two cards do not match they will go facedown | Pass |
| Level 1 and Level 2| If two cards do match they will stay face up | Pass |
| Level 1 and Level 2| Once all of the cards are face up the game ends and a winning message appears | Pass |
| Level 1 and Level 2| Within the winning text, information is provided on the users game stats including how many moves they have made and the time they took | Pass |
| Level 1 and Level 2| Within the winning text there is a link to play again on level 1 and this takes you to the game area again | Pass |
| Level 1 and Level 2| Within the winning text there is a link to play level 2 and this takes you to the level 2 page | Pass |
| Facts page | The main website name, a title and a subtitle are presented at the top of the page, providing some more information about what this page is about | Pass |
| Facts page | There is a link back to the home page which works | Pass |
| Facts page | There are 12 colourful square images of animals | Pass |
| Facts page | When you click on any animal the card flips and the name of the animal and a fact is displayed about the correct animal | Pass |
| Facts page | When you click on the fact the card will again flip and the animal will be displayed | Pass |



### Browser compatibility
The following browsers were used to check compatibility with the website
- Chrome
- Safari
- Microsoft Edge

## Testing User Stories

### As a new user I want ...
- A fun, colourful, quick game
    - Obviously 'fun' is subjective however friends and family who have tested it have enjoyed it, and I have had fun playing it myself! THe game is colourful, with a green and blue theme throughout and bright coloured cartoon emojis.

![Screenshot of game board](readme-img/full-game-board.png)

- To learn how to play quickly, with straightforward, clear rules
    - Easily accessible rules from the home page, that are concise and logical.

![Screenshot of rules](readme-img/rules.png)

- To learn interesting facts about a wide range of animals.
    - There are 12 different animals on the facts page from all over the world and from different habitats. Each fact is fun and a bit unusual which makes that animal quite unique.

![Screenshot of facts](readme-img/user-facts.png)


### As a returning user I want ...
- The game to change each time so that there is a new order of cards each time.
    - The game has lots of possibilities, there are 18 pairs of animal emojis which can be featured in the game, and within JavaScript Math.random was used to allow a different selection from the array of emojis to be used each time, so that the pairs locations and animals change each game.

![Screenshot of game](readme-img/game-one.png)
![Screenshot of game](readme-img/game-two.png)

- To be able to see my stats while playing the game, so I can challenge myself each time
    - The game stats are available during the game and also once you have finished they will be displayed.

![Screenshot of game](readme-img/stats.png)


### As the website owner I want ...
- To create a game that both children and adults can enjoy
    - Friends and family aged 12-55 tried out the game and had fun.

- To increase visits to the website, and gain returning users.
    - As this is just a concept and not a properly published game site, this cannot be measured. However friends and family said they will be playing again and showing their friends too.


### Feedback from friends and family
I shared this project with a few family members and friends, some feedback I receieved -
"I think the game is great, simple but still fun"
"One thing you could add would be something to alert the user that their cards match - such as a colour change to the cards that have matched"
"I think the colours and the font tie in well to the overall theme"

## Identified bugs
- Bug: When the screen size became smaller on certain devices, the emojis were positioned wrong on the cards and splilled over the edge of them.
    - How I fixed it: I altered the line height of the emoji and put this style into a media query for those specific screen sizes.
- Bug: On smaller devices the winning text message was all mis-aligned. 
    - How I ficed it: I removed the padding on the buttons for screen sizes below 800px
- Bug: Initially I had a 6x6 grid for level 2, however this was spilling off the screen and I did not want to make the user have to scroll to see the full game board
    - How I fixed it: I had initally implemented a rule in my code to only allow even numbers of columns however I removed this and created a 5x grid which fit much better on the screen.