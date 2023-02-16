## Fan of Scran

## **About**

**Milestone 3 project - Back End Development - Code institute**

Fan of Scran is a website for lovers of dining out. Users can browse reviews and upload their own reviews of their restaurant experiences

---

## **UX**

User experience

### **User stories**

### **As a new user I want ...**



### **As a returning user I want ...**



### **As the business owner I want ...**



---

### **Strategy**

The following questions were asked when developing a strategy...

- Who is the target audience, and is it culturally appropriate?
    - The target audience is anyone age 8+ (or younger and able to read well) who has an interest in animals, and enjoys playing games.
- Is the technology appropriate for the user and the purpose of the website?
    - The strategy for the technology is simplicity, there is no need for any complex technology for the purpose of this website.
- How is the offering of this site different from competitors?
    - From carrying out a competitor review, most other sites either only provide route ideas and not the ability to book, or they allow you to book set routes and do not have the option to create custom routes to meet individual requests/needs.

Following on from this a list of opportunities were put together. Each opportunity was then rated on a scale of 1-5 in two dimensions.

1. Importance
    - How crucial is it this opportunity?
2. Viability/Feasibility
    - How realistic is implementing this opportunity?

From the above table, the focus for the strategy will be on the following:

- Increase booking requests through the form.
- Increase returning users
- Increase members of Routes of Europe Facebook group.

---

### **Scope**

The scope of this website is to provide...

- simple and straightforward navigation
- clear and concise content alongside large imagery
- information about the service the business offers
- links to social media, in particular the Routes of Europe Facebook group.
- inspirational route ideas
- testimonials from previous users/customers
- a form to allow users to get in touch to put in a booking request.

---

### **Structure**

The website is organised by a hierarchical tree structure. This is a standard structure used commonly, and it reduces complexity. This structure can sometimes provide problems in regards to the navigation bar when displayed on mobile devices, however including the burger toggle bar, solves this.

It is made up of 3 pages

- A home page - introducing the business, testimonials from customers and information about connecting with other travellers
- A routes page - three route options to inspire users for their trip
- A get in touch page - information about next steps if a user is interested in using the trip planning service, and a form for them to fill out to provide information about their ideal trip.

Components that are used across each page (and are consistent throughout)

- Navigation bar - conventional navigation elements displayed horizontally along the top of the page.
- Hero image - eye-catching image with a short caption of text overlayed on top, underneath the navigation bar of each page. There is enough content visible underneath each hero image, to entice the user to scroll down.
- Footer - copyright information, social media links with conventional logo icons, and an up arrow with a link to bring you back to the top of the page.

---

### **Skeleton**

- Each page has a statement hero image and a short heading, beneath this part of the further text on the page is visible to attract the user to keep reading, and scroll down the page
- I considered the responsive layout and how it would be viewed on tablet and mobile devices as well as on desktop.
- Padding and margins were used throughout to ensure that the content does not appear cluttered.
- Can I also just check, to create a custom 404 error page, do I just need to make a 404.html file and thats it? I have had a look on github but that just tells you how to make it from github rather than from gitpod which I want to do? I did it for my first project and it worked for that,

### **Wireframes**

The original wireframes differ slightly to the final layout of the website, this is because as I was developing the site naturally some changes occurred that seemed logical to improve UX.

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/wf1.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/wf1.png)

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/wf2.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/wf2.png)

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/wf3.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/wf3.png)

Changes made throughout development

- Initially I was considering having an extra page of "Top tips" however I decided this was not needed, but could be implemented in future updates.
- The text over each hero image was changed to a shorter, snappier tag-line and buttons were not added.
- An image was added to the who we are section.
- The testimonials do not have images, they were kept simple and clean by using cards.
- An image was added to the connect section.
- The layout of each route section was slightly altered to be more responsive on smaller devices.
- The get in touch page was stripped down of text, as it appeared too cluttered.

I did not produce wireframes for mobile and tablet, although I did have the vision in my head that horizontal items would stack vertically on top of each other.

---

### **Surface**

### **Colour**

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/palette.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/palette.png)

- #FFFFFF - the background colour for individual sections of the website and for some sections of text
- #F5F5F5 - the overall background colour
- #187795 - the form background colour
- #3A716D - the background of the testimonial cards and the background colour for buttons when hovered
- #0D0C1D - the text colour for most of the text throughout the website

I chose these colours as I wanted a clean, minimalistic look, but still with splashes of colour here and there. The reason I went for this was to keep the focus on the text and imagery.

### **Imagery**

It was hard to stick to a colour scheme within the imagery as the content of the images was incredibly varied. However I think as my main colour scheme of the website is quite minimal, the varying coloured images work quite well. Each image is clear and of good size, they are responsive for differing sizes of devices.

Click [here](https://github.com/bethanyalicehall/routes-of-europe-MS1/blob/main/media-sources.md) to see details of images and video used throughout the site

- Hero images
    - I chose bold and scenic images for each hero image. The Amalfi coast, Bruges, and Amsterdam. On each I included a black colour overlay to mute it slightly. I chose images from the same photographer, to keep within a theme.
- Carousel images
    - For each route option there are three images within the carousel. I tried to choose images that gave a taste of the countries included on the route, that may entice the user into booking a trip.
- Other imagery
    - I included two further images on the home page, each of these include people, the train featured in both appears similar to try and provide some continuity of theming.

### **Video**

I included a simple video of a view from a train window, on the get in touch page. The video does not add much in regards to content but rather provides aesthetic adding to the theme of travelling Europe by rail.

### **Typography and icons**

I used Google fonts for all of the fonts;

- Roboto - regular 400
    - This was the main text used throughout, applied to the body. This is a easy-read font that fits well into the theming of the website.
- Roboto 'Mono' - extralight 200
    - This was used for the testimonial cards, to differentiate them from the main body of text.
- Roboto-flex - thin 100
    - This was used for the location names and also for the form.
- Lobster, Special Elite, Skranji - regular 400
    - These were used for the Route titles, I chose each one to be different and to stand out to add something extra to the route cards.

For the logo, I added an icon to the text from Google fonts, this icon is called "Pin-drop". I added a grow animation to the logo when hovered, just to make it stand out more from the navigation links. A text-shadow was also added to make it stand out.

For the text overlaying the hero image, I included a grow animation when the page loads, to add some movement to the website, and make it more inviting.

Font awesome was used for all of the social media icons in the footer. Font awesome icons were also used as food icons within the route cards.

---

## **Features**

### **Responsiveness**

Bootstrap has been used throughout the website to allow for a responsive design, media queries were also used to aid this.

- The navigation bar collapses into a hamburger icon on smaller devices
- For the routes page when viewed on smaller devices, the carousel stacks on top of the text.

### **Accessibility**

- Alt attributes have been added to all images and the video
- Text size, font and colour were considered in a way to hopefully provide clear, easy reading.
- A grey background colour is behind the hero images so if the images were not to load, text would still be readable.
- Wave was used to carry out testing which looked at accessibility, see [Testing](https://github.com/bethanyalicehall/routes-of-europe-MS1/blob/main/README.md#testing) section.

### **Meta data**

Meta tags are included within the head element, including a description, the author and keywords.

### **Navigation bar**

The navigation bar is composed of navigation links in the top left, which take you to the appropriate pages, and a logo in the top right. Each of the navigation links go a darker colour when active, and also when hovered over. On smaller devices the navigation links compress down into a hamburger icon which can be clicked on and the navigation links drop down. The logo can be clicked to take you back to the home page. The navigation bar is does not have a sticky top, as I did not want the navigation bar to reduce space for other content on the page when scrolling.

### **404 error page**

A custom 404 error page was made, including a link to redirect back to the home page.

### **Carousels**

Within the routes page, each route has a carousel displaying 3 images of locations featured within that route. Arrows appear when hovering over them to allow the user to select which image they want to view at any given time, the images are on a slideshow setting if the user does not interact with the carousel.

### **Form**

The form is located on the get in touch page, it includes fields for the user to input their personal details and details about their ideal trip. A radio button is included to indicate if they want just transport or transport and accommodation booking. There is a check box to indicate if a user wants to subscribe to the newsletter. A submit button is located at the bottom of the form. The form has an action of "get" and once submitted the user is taken to a page to confirm their submission and an option to go back to the home page.

### **Footer**

The footer includes a copyright, an arrow to click to take you back to the top of the page, and social media links. The links change colour when hovered over, to indicate that they can be clicked on.

### **Future features to consider**

### **Map**

A map could be added to each route to show the exact location of each stop within the route

### **Form**

- Include a modal that appears once the form has been submitted, saying "Submission successful"
- Include the user to only be allowed to choose dates within the future, not the past.

### **Affiliate links**

Potential to have a separate page with backpacking essentials and affiliate links.

---

## **Technologies used**

### **Languages**

- [HTML5](https://en.wikipedia.org/wiki/HTML5) - a markup language used for presenting and structuring content.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - stylesheet language for adding style.

### **Programs and websites**

- [GitHub](https://github.com/) - to host the repository, and then deploy to GitHub pages.
- [GitPod](https://gitpod.io/) - to write the code and use GIT to commit and push to GitHub.
- [Balsamiq](https://balsamiq.com/) - used to produce the wireframes.
- [Coolors](https://coolors.co/) - used to create a colour palette for the website.
- [Techsini](https://techsini.com/multi-mockup/index.php) - used to create the multi device mockup.
- [W3C HTML Validation service](https://validator.w3.org/) - used to validate HTML
- [W3C Jigsaw CSS Validation service](https://jigsaw.w3.org/css-validator/) - used to validate CSS
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - for performance testing.
- [Wave](https://wave.webaim.org/) - for accessibility testing.
- [Chrome developer tools](https://developer.chrome.com/docs/devtools/) - for testing responsiveness throughout.

### **Frameworks and Libraries**

- [Bootstrap](https://getbootstrap.com/) - version 5.2 was used throughout the project. Bootstrap documentation was used for the navigation bar, the hero sections, testimonial cards, route cards, the carousels, the form, and the footer.
- [Google Fonts](https://fonts.google.com/) - Selected a variety of fonts and imported these into the code.
- [Font awesome](https://fontawesome.com/) - Used for icons throughout the site.
- [Image resizer](https://imageresizer.com/) - Used to resize all carousel images to be equal in size.
- [Tinypng](https://tinypng.com/) - Used to compress images to help with loading time

---

## **Testing**

Click [here](https://github.com/bethanyalicehall/routes-of-europe-MS1/blob/main/testing.md) to view all testing carried out.

---

## **Deployment**

### **Steps taken to deploy project to GitHub Pages**

1. Go to **My repositories**.
2. Select **bethanyalicehall/route-of-europe-MS1**.
3. At the top of the page click on **Settings**.
4. Scroll down and on the left hand side there is a **Pages** section.
5. Under **Source** click the drop down menu and select **Main**.
6. Click **Save**, the website will now be deployed (note it can take a minute or two to load).

### **Access to code**

1. Go to **My repositories**.
2. Select **bethanyalicehall/route-of-europe-MS1**.
3. At the top of the page click on **Code**, where **Zip files** can be downloaded locally.

---

## **Credits**

### **Media**

- [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/) - click [here](https://github.com/bethanyalicehall/routes-of-europe-MS1/blob/main/media-sources.md) to see details of images and video used throughout the site

### **Content**

- [Code institute boiler template](https://github.com/Code-Institute-Org/gitpod-full-template) was used.
- Code was taken from bootstrap documentation and altered slightly or written myself with inspiration and help from the following
    - [A designer who codes - Responsive background images with Bootstrap 5](https://www.youtube.com/watch?v=W87XNjvXiWw&t=18s)
    - [Traversy media - Bootstrap 5 video](https://www.youtube.com/watch?v=4sosXZsdy-s)
    - [W3 Schools](https://www.w3schools.com/)
    - [Code institute](https://codeinstitute.net/) projects, in particular the Love Running project.
    - [cntraveller](https://www.cntraveller.com/gallery/happiest-countries-in-the-world) - information about the happiest countries in the world
    - [The broke backpacker](https://www.thebrokebackpacker.com/backpacker-statistics/) - website used for statistics

### **Acknowledgements**

I would like to thank

- My mentor, Brian Macharia for guidance throughout the process.
- Pasquale Fasulo for running sessions to help me feel prepared for the project.
- The photographers who publish royalty free images on Pexels and Unsplash that allowed me to use high quality imagery throughout.
- All of the code institute team, for providing quality learning content to allow me to develop my skills to complete this project.

# testing

## **HTML validator**

I inputted my HTML into the W3C Markup Validation service.

### **Home page**

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/html-home.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/html-home.png)

- For error 1, I replaced the name attribute with an id attribute.
- For error 2, this was the only way I found in providing textual context to the background image as the image itself was within CSS. I removed this as the image is not providing any information to the user.
- For error 3 and 4 I changed the buttons to links.

### **Routes page**

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/html-routes.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/html-routes.png)

- For error 1, I replaced the name attribute with an id attribute.
- For error 2, this was the only way I found in providing textual context to the background image as the image itself was within CSS. I removed this as the image is not providing any information to the user.
- For error 3-6, I removed the id attributes as they were not needed, as there was already a class attribute.

### **Get in touch page**

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/html-touch.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/html-touch.png)

- For error 1, I replaced the name attribute with an id attribute.
- For error 2, this was the only way I found in providing textual context to the background image as the image itself was within CSS. I removed this as the image is not providing any information to the user.
- For error 3 and 4 I removed the br elements within the unordered list.

I corrected each error and re-checked the HTML through the validator, and it passed.

## **CSS validator**

I inputted code into the W3C validation service, initially this brought up two errors

- Text-shadow format was not correct, I decided the text shadow of the text over the hero image was not necessary so removed that.
- Font weight value was incorrect, I had used 200px instead of 200.
- Once these errors were corrected no further errors were found.

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/css-val.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/css-val.png)

## **Performance testing**

I utilised the [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) performance testing software.

- The results of the lighthouse testing can be seen below for each page.
- On the first round of testing, the performance was quite low due to image size and bootstrap stylesheets slowing down the first paint of the page.
- I reduced the size of the images and used [Tinypng](https://tinypng.com/) to compress the images. As you can see below, the doing this increased the performance significantly.
- The accessibility is good although not 100%, this will be looked into in more detail in the next section.
- The search engine optimisation is good but slightly low due to the link to bring the user back up to the top of the page being uncrawlable.

### **Home page**

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/home1.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/home1.png)

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/2home.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/2home.png)

### **Routes page**

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/routes1.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/routes1.png)

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/2routes.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/2routes.png)

### **Get in touch page**

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/touch1.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/touch1.png)

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/2touch.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/2touch.png)

## **Accessibility testing**

I utilised [Wave](https://wave.webaim.org/) which is a web accessibility evaluation tool.

- One error was detected, that an empty button was present. This was the collapsible hamburger navbar button, which was adapted from Bootstrap documentation. It works well so I decided to leave it as it is, however will consider that in future projects.
- The contrast ratio was good throughout and passed the tests for normal and large text, apart from the testimonial cards, so I made the background colour darker to increase readability, it then passed the tests.
- The social media links within the footer did not all have titles, this error was corrected.

## **Responsiveness**

- I utilised Chrome Developer tools to test responsiveness on different devices, the following devices were sucesfully tested through this.
    - iPhone SE
    - iPhone XR
    - iPhone 6/7/8
    - Samsung galaxy S8+
    - iPad Air
    - iPad Mini
    - Surface pro 7
    - Galaxy Fold
    - Nest Hub
- I manually tested the website on an iPhone 12 pro, an iPad 2 and a MacBook Air.

## **Manual testing**

### **Functional testing**

Each of the following tests were carried out on a Macbook Air and an iPhone 12 pro.

- A functional navigation bar is present
    - The navigation bar allows users to easily access links to the corresponding pages
- The footer contains a link which allows the user to go back to the top of the page
    - This is present on each page and works as expected
- The social media links open in a new tab
    - This works as expected
- Users can scroll through the carousel or they can watch the slideshow which is automatic
    - The carousels work as expected
- The video does not play automatically and there are controls available to the user
    - The video is paused until the user decides to play it.
- The form does not allow wrong input types to by inputted.
    - An alert will appear when attempting to submit if wrong input type has been used.
- A 404 error page will appear if an incorrect url is entered
    - This works as expected and has a link to go back to home page

### **Browser compatibility**

The following browsers were used to check compatibility with the website

- Chrome
- Safari
- Microsoft Edge

## **Testing User Stories**

### **As a new user I want ...**

- The purpose of the website to be clear.
    - The first section of text underneath the hero image explains what the company is all about

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-about.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-about.png)

- To easily navigate the website, to learn more about travelling around Europe.
    - Clear navigation bar that links to route page with information about where you can travel in Europe.

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-nav.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-nav.png)

- To find readily available information about the business and have clear contact options if I want to find out more.
    - There is a form to get in touch and social media links within the footer

### **As a returning user I want ...**

- Inspiring imagery and information to give me ideas for my next trip I will book through the website.
    - Hero images are eye catching and the route cards contain short but interesting sections of information alongside a carousel of images.

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-hero.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-hero.png)

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-route.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-route.png)

- A website that is easy to use and works well on mobile, tablet, and desktop.
    - The website has been fully tested and is responsive on all device sizes.

### **As the business owner I want ...**

- To increase awareness of the business.
    - Key words have been included within the meta tags to allow for search engine optimisation.
- To increase trip planning requests to allow the business to grow financially.
    - There is an extra link on the home page taking the user directly to the form, to encourage requests.

![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-letsgo.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-letsgo.png)

- To increase the businesses social media presence.
    - There is a dedicated section to the Routes of Europe Facebook group, as well social media links within the footer.
        
        ![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-connect.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-connect.png)
        
        ![https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-socials.png](https://github.com/bethanyalicehall/routes-of-europe-MS1/raw/main/readme-img/user-socials.png)
        

## **Identified bugs**

- Bug: On the routes page I noticed that when clicking left or right on the second or third carousel it was controlling the first and not the one that was being clicked.
    - How I fixed it: I realised that each carousel had the same id as I had copied and pasted without realising, once this was corrected the error was solved.
- Bug: The text on the get in touch page, explaining the next steps, when viewed on a mobile device was slightly off centre to the right.
    - How I fixed it: I changed the text from an unordered list with list items, to individual paragraphs, and this allowed the text to be aligned to the centre.
- Bug: When viewed on smaller screen sizes the carousel images appeared unequal in size.
    - How I fixed it: I used an image resizer to make sure images had the same dimensions.
- Unfixed bug - when first loading the page the pin drop icon that is part of the logo, it appears as text for a second before changing to the icon.