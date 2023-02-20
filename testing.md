# Testing

## HTML validator
I inputted my HTML into the W3C Markup Validation service. I put each page through this. A few errors did appear on each page, mostly due to Jinja templating. An example is shown below

![Screenshot of HTML validation results](static/img/README/html.png)

## CSS validator
I inputted code into the W3C validation service and no errors were found

![Screenshot of CSS validation results stating that no errors were found](static/img/README/css.png)

## JS validator

I used [JSHint](https://jshint.com/).
This gave some information of the following metrics, warnings and undefined variables. The undefined variable is the $ sign, this was due to the use of JQuery. The warnings do not directly impact the functioning of the site or cause a console error.

![Screenshot of metrics from JSHint](static/img/README/jshint.png)

## PEP8 Compliant 
I ensured that my Python code was PEP8 compliant, I corrected any linting errors within the IDE. I referred to [this site](https://peps.python.org/pep-0008/) to check some rules regarding indentation.

Below are some screenshots of linting errors, mainly due to indentation errors.

![Screenshot of linting errors within the IDE](static/img/README/linting1.png)
![Screenshot of linting errors within the IDE](static/img/README/linting2.png)
![Screenshot of linting errors within the IDE](static/img/README/linting3.png)

## Performance testing
I utilised the [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) performance testing software.
- The results of the lighthouse testing can be seen below. 

### Home page
![Screenshot of Lighthouse testing for home page](static/img/README/lighthouse1.png)

### Profile page
![Screenshot of Lighthouse testing for profile page](static/img/README/lighthouse2.png)

### Add a review page
![Screenshot of Lighthouse testing for add review page](static/img/README/lighthouse3.png)


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

- I tested the website on an iPhone 12 pro, an iPad 2 and a MacBook Air.

## Manual testing

### Functional testing

#### Testing elements on each page 

| Page | Element and expected action | Pass or Fail | 
| ----------- | ----------- | ----------- |
| All pages | There is a navigation bar displaying the logo "Fan of Scran" and navigation links, which all take you to the relevant page | Pass |
| All Pages | When viewing on smaller screens the navigation bar is displayed as a sidenav with a burger menu | Pass |
| All Pages | When hovering over a link the pointer changes | Pass |
| All Pages | There is a footer with social media links that all open in a new tab | Pass |
| All Pages | The website is responsive on desktop, tablet and mobile | Pass |
| Home page (Logged out) | url linked in README.md displays Fan of Scran homepage, and the Burger Favicon is visbile | Pass |
| Home page (Logged out) | There is a main title and further information about purpose of site | Pass |
| Home page (Logged out) | The register link takes you to the registration page | Pass |
| Home page (Logged out + logged in)| The review accordian opens when clicked on and displays the review correctly | Pass |
| Home page (Logged out + logged in)| The latest reviews displays the three most recent reviews in order | Pass |
| Home page (Logged in) | The add a review link takes you to the new review page | Pass |
| Home page (Logged in) | The browse reviews link takes you to the reviews page | Pass |
| Home page (Logged in) | The log out link, takes the user to the home page and displays a flash message to confirm the user has logged out. | Pass |
| Home page (Logged in) | The edit button on each review takes the user to the edit review page. A user is only allowed to edit their own reviews  | Pass |
| Home page (Logged in) | The delete button on each review opens a modal asking if the user is sure that they want to delete that review, and then if the user selects delete again, the review is succesfully deleted and a flash message confirms this to the user. A user is only allowed to delete their own reviews, apart from Admin who can delete any reviews.  | Pass |
| Login page | The login page works succesfully and only allows registered users to login | Pass |
| Login page | The password is hidden | Pass |
| Login page | The login button takes the user to their profile page, and displays a flash message to welcome them | Pass |
| Register page | The validation works for username and password length | Pass |
| Register page | The password is hidden  | Pass |
| Register page | The register button takes the user to their profile page, and displays a flash message to say their registration was successful | Pass |
| Profile page | The title of the page is the current users username  | Pass |
| Profile page | Only reviews made by the current user are displayed, in order of when they were made (most recent first)  | Pass |
| Profile page | The review accordian opens when clicked on and displays the review correctly | Pass |
| Profile page | The edit button on each review takes the user to the edit review page  | Pass |
| Profile page | The delete button on each review opens a modal asking if the user is sure that they want to delete that review, and then if the user selects delete again, the review is succesfully deleted and a flash message confirms this to the user  | Pass |
| Review page | The add a review link takes you to the new review page | Pass |
| Review page | The review accordian opens when clicked on and displays the review correctly | Pass |
| Review page | All reviews are displayed, in order of when they were made (most recent first) | Pass |
| Review page | The search function allows users to search for a review using either the restaurant name, location or rating | Pass |
| Review page | The search function button displays all relevant reviews from the users search | Pass |
| Review page | The clear search button returns the user back to all reviews | Pass |
| Review page | If there are no reviews that match the users search, there will be a message to the user explaining this | Pass |
| Review page | The edit button on each review takes the user to the edit review page. A user is only allowed to edit their own reviews   | Pass |
| Review page | The delete button on each review opens a modal asking if the user is sure that they want to delete that review, and then if the user selects delete again, the review is succesfully deleted and a flash message confirms this to the user. A user is only allowed to delete their own reviews, apart from Admin who can delete any reviews. | Pass |
| Cuisine page | Each cuisine card displayed has a relevant corresponding image and also the cuisine in the native language | Pass |
| Cuisine page | Each cuisine card when clicked on displays the relevant cuisine page | Pass |
| Specific cuisine page | The title of the page reflects the relevant cuisine | Pass |
| Specific cuisine page | If there are no reviews of that cuisine, a message will be displayed explaining this | Pass |
| Specific cuisine page | All reviews of that cuisine are displayed, in order of when they were made (most recent first)| Pass |
| Specific cuisine page | The review accordian opens when clicked on and displays the review correctly | Pass |
| Specific cuisine page | The edit button on each review takes the user to the edit review page. A user is only allowed to edit their own reviews | Pass |
| Specific cuisine page | The delete button on each review opens a modal asking if the user is sure that they want to delete that review, and then if the user selects delete again, the review is succesfully deleted and a flash message confirms this to the user. A user is only allowed to delete their own reviews, apart from Admin who can delete any reviews. | Pass |
| Add a review page | The page displays a form for the user to add a review | Pass |
| Add a review page | Each text input works and validates successfully | Pass |
| Add a review page | Each dropdown select works and validates successfully | Pass |
| Add a review page | The submit review button successfully submits the form and displays a flash message to the user to confirm this. | Pass |
| Edit review page | The page displays a form for the user to edit a review, and contains the relevant pre-filled fields within the form | Pass |
| Edit review page | Each text input works and validates successfully | Pass |
| Edit review page | Each dropdown select works and validates successfully | Pass |
| Edit review page | The edit review button successfully submits the form and displays a flash message to the user to confirm that the form has been updated | Pass |


### Browser compatibility
The following browsers were used to check compatibility with the website
- Chrome
- Safari
- Microsoft Edge

## Testing User Stories

### As a new user I want ...
- To understand what the sites purpose is immediatley.
    - The imagery, the site name and the heading all indicate the website is about food/restaurants. On Further reading it is clear the site is a restaurant review site. 

![Screenshot of home page](static/img/README/user-homepage.png)

- To be able to navigate to and use the registration page easily.
    - From the initial home page there are three opportunities for a user to sign up and access the registration page

![Screenshot of opportunity to sign up](static/img/README/user-signup1.png)
![Screenshot of opportunity to sign up](static/img/README/user-signup2.png)
![Screenshot of opportunity to sign up](static/img/README/user-signup3.png)

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