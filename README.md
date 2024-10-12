# Luke Maycock Portraiture

![AmIResponsive image of Studio Booker]()

## Introduction

The project is to build an ecommerce website to sell hand drawn portrait service.

## Table of Contents

- [Luke Maycock Portraiture](#lukemaycockportraiture)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
      - [Epic 1 - User account creation process](#epic-1---user-account-creation-process)
      - [Epic 2 - Development of a the ecommerce platform](#epic-2---development-of-a-course-booking-system)
      - [Epic 3 - Enhancing website aesthetics](#epic-3---enhancing-website-aesthetics)
  - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
      - [Index page](#index-page)
      - [About page](#about-page)
      - [Booking page](#booking-page)
      - [My bookings page](#my-bookings-page)
      - [Success page](#success-page)
      - [Edit booking page](#edit-booking-page)
      - [Sign up page](#sign-up-page)
      - [Sign in page](#sign-in-page)
      - [Sign out page](#sign-out-page)
      - [404 page](#404-page)
    - [Entity Relationship Diagram - ERD](#entity-relationship-diagram---erd)
  - [Features](#features)
    - [Header](#header)
      - [Navigation bar](#navigation-bar)
      - [Navigation bar (as a logged in user)](#navigation-bar-as-a-logged-in-user)
      - [Navigation bar (as a staff member or superuser)](#navigation-bar-as-a-staff-member-or-superuser)
    - [Index page](#index-page-1)
      - [Hero image](#hero-image)
      - [Welcome text](#welcome-text)
      - [Member benefits](#member-benefits)
      - [Sign up button](#sign-up-button)
      - [Carousel](#carousel)
    - [About page](#about-page-1)
      - [Profile image](#profile-image)
      - [About text](#about-text)
      - [Testimonial form](#testimonial-form)
      - [Testimonial form response](#testimonial-form-response)
    - [Booking page](#booking-page-1)
      - [Studio presentation](#studio-presentation)
      - [Studio booking](#studio-booking)
      - [Booking pagination](#booking-pagination)
      - [Confirm booking modal](#confirm-booking-modal)
      - [Double booked modal](#double-booked-modal)
    - [Success page](#success-page-1)
      - [Confirmation text](#confirmation-text)
      - [Navigation buttons](#navigation-buttons)
    - [My bookings page](#my-bookings-page-1)
      - [No bookings - text](#no-bookings---text)
      - [No bookings - button](#no-bookings---button)
      - [Active bookings - text](#active-bookings---text)
      - [Active bookings - booked studios](#active-bookings---booked-studios)
      - [Active bookings pagination](#active-bookings-pagination)
      - [Confirm cancellation modal](#confirm-cancellation-modal)
    - [Edit booking page](#edit-booking-page-1)
      - [Available studios](#available-studios)
      - [Available studios pagination](#available-studios-pagination)
      - [Confirm studio change modal](#confirm-studio-change-modal)
    - [News page](#news-page)
    - [Sign up page](#sign-up-page-1)
    - [Sign in page](#sign-in-page-1)
    - [Sign out page](#sign-out-page-1)
    - [404 page](#404-page-1)
      - [404 page text](#404-page-text)
      - [404 page button](#404-page-button)
    - [Footer](#footer)
  - [Features to be Added](#features-to-be-added)
  - [Testing](#testing)
    - [Validation of Code](#validation-of-code)
      - [HTML](#html)
      - [CSS](#css)
      - [JavaScript](#javascript)
      - [Python](#python)
    - [Lighthouse](#lighthouse)
      - [Desktop](#desktop)
      - [Mobile](#mobile)
    - [Wave Webaim - accessibility testing](#wave-webaim---accessibility-testing)
      - [Index page](#index-page-2)
      - [About page](#about-page-2)
      - [Booking page](#booking-page-2)
    - [Contrast Grid](#contrast-grid)
    - [Automated Testing](#automated-testing)
      - [About](#about)
      - [Booking](#booking)
      - [News](#news)
    - [Manual Testing](#manual-testing)
      - [Navigation bar](#navigation-bar-1)
      - [Index page](#index-page-3)
      - [About page](#about-page-3)
      - [Booking page](#booking-page-3)
      - [Success page](#success-page-2)
      - [My bookings page](#my-bookings-page-2)
      - [Edit booking page](#edit-booking-page-2)
      - [News page](#news-page-1)
      - [Sign up page](#sign-up-page-2)
      - [Sign in page](#sign-in-page-2)
      - [Sign out page](#sign-out-page-2)
      - [404 page](#404-page-2)
      - [500 page](#500-page-2)
      - [Footer](#footer-1)
    - [Bugs](#bugs)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
    - [Fork repository in GitHub](#fork-repository-in-github)
    - [Clone repository in GitHub](#clone-repository-in-github)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Credits](#credits)
    - [Libraries used](#libraries-used)
    - [Used resources](#used-resources)
    - [Images](#images)
  - [Acknowledgements](#acknowledgements)

## User Experience

### User Goals

One of the user goals is to be able seamlessly purchase portraiture services online. The user should also have a smooth experience with full CRUD (Create, Read, Update and Delete) accessibility to their bookings. The goal is also to view already created projects and to inspire the user.

### Site Owner Goals

The site owner goal is to facilitate the frictionless purchase of portrait art services for the customer, with robust technologies in place to complete the processing of an order should something go wrong during the process.

### User Stories

For the project, four different Epics were created. To them, a total of 13 user stories were created. To view all user stories, they are viewable at the [Projects board](https://github.com/users/l3wk3m/projects/3). All user stories were assigned one of the following classes; Must have, Should have, Could have or Won't have. 

The following user stories were completed within the first release of Luke Maycock Portraiture.

#### Epic 1 - User account creation process

As a site owner, I would like to create a sign-up process that is intuitive and gets the user able to book studio spaces as soon as possible.

**User Story - Accessing the sign-up page**

As a site user I can easily find and access the sign-up page from the homepage so that I can create an account without confusion or unnecessary delays

- Acceptance Criteria 1  
Given the user is not signed up, the sign-up button will be easy to find.
- Acceptance Criteria 2  
Given a user is not signed up, clicking the sign-up button takes them to the sign up page.

**User Story - Filling in the sign-up form**

As a site user I can enter my personal details into a sign-up form so that I can register for a new account

- Acceptance Criteria 1  
Given the user doesn't have an account, when the user is filling out the sign up form the form includes fields for necessary information (e.g., email, password, confirmation of password)  
- Acceptance Criteria 2  
Given the user doesn't have an account, when the user is filling out the sign up form the form has input validation (e.g., email format)

#### Epic 2 - Customer purchasing experience

As a site owner I would like users of my website to be able to quickly see what it is they want and to buy it in as frictionless a manner as possible.

**User Story - Accessing the Products Page**

As a site user I want to be able to spot and navigate to the products page easily. I should be able to see where I need to go immediately with little investment.

**User Story - Add to Cart**

As a site user I want to be able to add an item to my cart as soon as I've decided to purchase the item.

**User Story - Confirmation Toast**

As a site user I will get an onscreen confirmation that an item has been added to my cart. This will give me confidence in the user experience I will have on the website.

- Acceptance Criteria 1  
Whenever the user adds or removes an item from their cart or checks out successfully, a toast pop-up should immediately appear, confirming the change  
- Acceptance Criteria 2  
Given a toast pop-up is displayed to the user when the user clicks the "Cancel" button the toast closes without making any modifications to the booking

**User Story - Edit Cart**

As a site user I will be able to edit my cart from the popup confirmation message or from the cart page. This will give me a sense of autonomy throughout the purchasing process.

**User Story - Checkout**

As a site user I will be able to checkout via the checkout page. Upon checking out I will get an order confirmation as well as a second confirmation via email. This will give me confidence that once I have paid for my purchase it has been registered by the site owner with an order number for me to be able to reference.

**User Story - View Orders**

As a user with an account I will be able to see my past orders once I have logged in to the website. This redoubles confidence that my order has been recieved and is being processed.


#### Epic 3 - Developing User Comments functionality

As a site owner I can have a user-friendly comments section so that visitors can easily send feedback about their previous purchases

**User Story - Accessing the comments form**

As a site user I can easily find and access the comments form from any page on the website so that I am as encouraged to leave feedback as is possible

- Acceptance Criteria 1  
Given the user is on a Product Details page for any product, they will have access to a comments section where they can leave reviews about past purchasing experiences they have had with the specified product.
- Acceptance Criteria 2
Given the user is on a Product Details page for any product, they will have access to viewing the comments that have been left for that product in the past.


**User Story - Receive confirmation after sending comment form**

As a site user I can receive immediate confirmation that my comment has been sent successfully when I submit the form so that I am assured my feedback has been received

- Acceptance Criteria 1  
I should see a confirmation message on the website indicating that my message has been sent successfully  

#### Epic 4 - Enhancing website aesthetics

As a website owner I would like to enhance the visual appeal and user experience of the website so that visitors are more engaged, find the website more trustworthy, and are encouraged to sign up using my service, due to its sleek presentation

**User Story - Implementing a responsive design**

As a site user I can easily navigate and view content so that I can use any device, whether it's a desktop, tablet, or smartphone

- Acceptance Criteria 1  
Given the user is visiting the site the website automatically adjusts its layout based on the screen size and orientation regardless of the device being used
- Acceptance Criteria 2  
Given the user is 
- Acceptance Criteria 3  
Given the user is  

**User Story - Using appealing fonts and color scheme**

As a site user I can visit the website with appealing fonts and a cohesive color scheme so that 

- Acceptance Criteria 1  
Given the user doesn't only use screen reader 
- Acceptance Criteria 2  
Given the user doesn't only use screen reader
- Acceptance Criteria 3  
Given the user doesn't only use screen reader


## Design

The design is aiming to be to be modern but easy to read. It should draw the attention to the websites core feature, the booking grid. 

### Color Scheme

The color scheme is set to  

### Typography

The typography was chosen to 

### Imagery

All the images are chosen to 

### Wireframes

#### Index page

![Wireframe of index page]()

#### About page

![Wireframe of about page]()

#### Booking page

![Wireframe of booking page]()

#### My bookings page

![Wireframe of my bookings page]()

#### Success page

![Wireframe of success page]()

#### Edit booking page

![Wireframe of edit booking page]()

#### Sign up page

![Wireframe of sign up page]()

#### Sign in page

![Wireframe of sign in page]()

#### Sign out page

![Wireframe of sign out page]()

#### 404 page

![Wireframe of 404 page]()

#### 500 page

![Wireframe of 500 page]()

### Entity Relationship Diagram - ERD

![ERD of Site Models](docs/images/Artists_ERD.webp)

The custom model added was a 'comments section' where users are able to leave feedback on items they have previously purchased.

## Features

### Header

#### Navigation bar

![Navigation bar as a not logged in user]()

.

#### Navigation bar (as a logged in user)

![Navigation bar as a logged in user]()

. 

#### Navigation bar (as a staff member or superuser)

![Navigation bar as a staff member or superuser]()

.

### Index page

#### Hero image

![Hero image at index page]()

.

#### Welcome text

![Welcome text at index page]()

.

#### Member benefits

![Benefits of becoming a member]()

. 

#### Sign up button

![Sign up button below member benefits]()

If the user is visiting the index page without being signed in, there is a sign up button below the member benefits. This is to make it easy for the user to sign up when they have read the fantastic benefits. 

#### Carousel

![Carousel of images]()

.

### About page

#### Profile image

![Profile image at the about page](d)

. 

#### About text

![A text about the owner and founder of ]()

.

#### Testimonial form

![The testimonial form at the about page]()

.

#### Testimonials Form

![The response after submitting the testimonials form]()

.

### Studios page

#### Studio Space Presentation

![The different studios are presented]()

The different are listed in a grid format and colour-coded using bootstrap's functionality.

#### Studio booking

![The booking section where the user can select which studio they are interested in]()

.

#### Booking pagination

![Pagination at booking page]()

.

#### Confirm booking modal

![Confirmation modal after a booking button in pressed]()

.

#### Double booked modal

![Modal to show that the user already has a booking at the chosen studio space]()

A double booking modal is triggered when the user tries to book a .

### Success page

#### Confirmation text

![Confirmation text after a successful booking]()

After a successful booking, a text that confirm the booking appears.

#### Navigation buttons

![Three navigation buttons; "View my bookings", "Home" and "Book another studio"]()

Under the confirmation text, three navigation buttons are visible; "View my bookings", "Home" and "Book another studio". On smaller devices, only "View my bookings" and "Book another studio" are visible. These buttons are there to make the user to stay at the website after a successful booking.

### My bookings page

#### No bookings - text

![The text on my booking page explains there is no bookings]()

When the user doesn't have any active bookings, a text informs the user about it. The text informs the user where they can find the booking page.

#### No bookings - button

![Button to direct the user to the booking page]()

.

#### Active bookings - text

![Text to notice the user that they have at least one active booking]()

When the user has at least one booking, 

#### Active bookings - booked studios

![The user bookings are presented]()

The user bookings are presented so that the booking that is next in time appears first. Each booked studio card has an Edit button and a Cancel button. When the Edit button is pressed, the user gets directed to the edit booking page. When the Cancel button is pressed, a confirmation modal is triggered. These two buttons allows the user to edit and delete the booked session if the user has to change their plans.

#### Active bookings pagination

![My bookings pagination]()

If the user has more than four active bookings, a pagination appears below the active bookings. This is to enhance the user experience, to make it easier for the user to see their active bookings.

#### Confirm cancellation modal

![Modal that the user gets to assure that they want to cancel their booking](doc/confirm-delete.webp)

When the user presses the Cancel button in their active bookings, a confirm cancellation modal is triggered. This is to make sure the user didn't press Cancel by mistake. The Confirm button in the modal is red to mark that if you press it, something that is irreversible will happen.

### Edit booking page

#### Available Studios

![All available studios presented as booking buttons]()

All available studios are presented in a  .

#### Available Studios Pagination

![Available Studios Pagination]()

If there are more than eight available studios to select from, pagination appears. This is to enhance the user experience, to avoid scrolling through a wall of available studios.

#### Confirm studio change modal

![Confirmation modal to ensure the user wants to change their studio booking]()

The confirmation modal ensures that the user wants to edit their booking to the selected .

### Sign up page

![Sign up page with fields for email, username, password and password again]()

The sign up page have fields where the user is required to fill out email, username, password and password again. This to make sure the user doesn't get a typo in the password and to ensure the user register a way to contact them.

### Sign in page

![Sign in page with fields for email and password]()

The sign in page allows the user who already has an account to sign in. This to make the user experience smoother where they don't have to fill out their email every time they want to make a booking. It is also an advantage that the user can see all their bookings.

### Sign out page

![Sign out page with a confirmation button]()

The sign out page allows the user to sign out to ensure no one else can edit the users booking. The sign out button ensures the user really wanted to sign out and didn't press on Sign out by mistake.

### 404 page

#### 404 page text

![Text provided when a 404 page is rendered]()

The text explains to the user in a fun way that the page they are looking for doesn't exist. It points the user in the direction of heading back to the homepage to give it a new try.

#### 404 page button

![Button which takes the user to the homepage]()

The button below the 404 text directs the user back to the homepage. This allows the user to give it a new shot to find the page they were looking for.

### 500 page

#### 500 page text

![Screenshot of the text at the 500 page]()

The text at the 500 page explains to the user that the server isn't working as intended. This is to make sure the user knows what is happening.

#### 500 page tips

![The tips of what to do when a 500 page is rendered]()

The tips suggests to the user what they can do; refresh the page or go back to the homepage. The suggestion about going back to the homepage is provided with a link to the homepage.

### Footer

![Footer with developers name and year to the left and links to the Testimoial form and connecting Facebook, Instagram and Pinterest accounts]()

.

## Features to be Added

Several features can be added in the future.

- 

## Testing

### Validation of Code

#### HTML

![Screenshot of HTML validation of index page]()

All the pages were tested at the [W3C Markup Validation Service](). The index page validation is presented above, all the other validations are linked below.

- [Home page](doc/)
- [Products page]()
- [Product Detail page]()
- [Cart page]()
- [Checkout page]()
- [Order Confirmation page]()
- [404 page]()
- [500 page]()

#### CSS

![Screenshot of CSS validation](doc/css-valid.webp)

The CSS code was tested at [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). It resulted in.

#### JavaScript

All JavaScript files were validated through [JSHint](https://jshint.com/). The validation rendered without errors. 


**_ page**

![JavaScript validation of _ page]()

#### Python

All Python files have been validated through [CI Python Linter](https://pep8ci.herokuapp.com/) to make sure the code meets the standards of PEP8. The validation resulted without errors.

**Cart - views.py**

![Python validation of views.py in cart]()

**Checkout - views.py**

![Python validation of views.py in checkout]()

**Home - views.py**

![Python validation of views.py in home]()

**Products - views.py**

![Python validation of views.py in products]()

**Profiles - views.py**

![Python validation of views.py in profiles]()

- [Python validation of models.py in checkout]()
- [Python validation of models.py in products]()

### Lighthouse

Tests in Lighthouse were performed for both desktop and mobile.

#### Desktop

![Lighthouse test for desktop]()

The test for desktop resulted in __ in both performance and accessibility. It also resulted in __ in both best practice and SEO.

#### Mobile

![Lighthouse test for mobile](doc/lighthouse-mobile.webp)

The test for mobile resulted in __.

### Wave Webaim - accessibility testing

The accessibility test at [Wave Webaim](https://wave.webaim.org/) resulted without errors and contrast errors on all pages.

#### Index page

![Wave webaim test of index page]()

#### About page

![Wave webaim test of about page]()

#### Booking page

![Wave webaim test of about page]()

### Contrast Grid

The [Contrast Grid](https://contrast-grid.eightshapes.com/) resulted in .

![Contrast Grid of the webpage]()

### Automated Testing

Automated testing is done for all different apps (cart, checkout, home, products and profiles). In total, __ tests were made - .

![Automated tests for all apps]()

#### Cart

![Automated tests for cart app]()

- [Test of forms.py]()
- [Test of views.py]()

#### Checkout

![Automated tests for checkout app]()

- [Test of models.py]()
- [Test of views.py]()
- [Test of signals.py]()

#### Home

![Automated tests for home app]()

- [Tests of admin.py]()
- [Tests of views.py]()

#### Products

![Automated tests for products app]()

- [Tests of admin.py]()
- [Tests of models.py]()
- [Tests of views.py]()

#### Profiles

![Automated tests for profiles app]()

- [Tests of admin.py]()
- [Tests of models.py]()
- [Tests of views.py]()

### Manual Testing

Every page at the website has been manually tested. It is done in Google Chrome DevTools and on different devices. The devices used were one mobile phone, one laptop and one external screen:

- Fairphone 4 5G (1080 x 2400)
- Macbook Pro 2020 (1366 x 768)

#### Navigation bar

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Home link | When clicked, directs the user to the home page | Click at "Home" | Got directed to the home page | __ |
| Products link | When clicked, gives user a dropdown to select various different categories of products | Click at "Products" | Got shown dropdown menu of categories of product | __ |

#### Index page


#### Products page


#### Comments section

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |

#### Sign up page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| All fields required | An error message appears when the user tries to sign up but leaves one field empty | Leave one field empty one by one and try to Sign Up | An error message appeared when a field was left empty | __ |
| Redirected | When the "Sign Up" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign up, fill out all required fields, press "Sign Up" button | The user got redirected to Booking page | __ |

#### Sign in page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| All fields required | An error message appears when the user tries to sign in but leaves one field empty | Leave one field empty one by one and try to Sign In | An error message appeared when a field was left empty | __ |
| Sign In button | When the "Sign In" button is pressed, the user gets signed in | Click at "Sign In" button | The user gets signed in | __ |
| Redirected | When the "Sign In" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign in, press "Sign In" button | The user got redirected to Home page | __ |

#### Sign out page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Sign Out button | When the "Sign Out" button is pressed, the user gets signed out | Click at "Sign Out" button | The user gets signed out | __ |
| Redirected | When the "Sign Out" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign out, press "Sign Out" button | The user got redirected to Home page | __ |

#### 404 page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Return to stability button | When "Return to stability" button is pressed, the user gets directed to the home page | Click at "Return to stability" button | The user got directed to the home page | __ |

#### Footer

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The footer changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The footer was responsive and changed depending on screen size | ___ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Link to testimonial form | When the pencil icon is clicked, the user gets directed to the testimonial form | Click at the icon | The user got directed to the testimonial form | __ |
| Link to Facebook | When the Facebook icon is clicked, the user gets directed to Facebook which opens in a new tab | Click at the Facebook icon | The user got directed to Facebook which opens in a new tab | __ |
| Link to Instagram | When the Instagram icon is clicked, the user gets directed to Instagram which opens in a new tab | Click at the Instagram icon | The user got directed to Instagram which opens in a new tab | __ |
| Link to Pinterest | When the Pinterest icon is clicked, the user gets directed to Pinterest which opens in a new tab | Click at the Pinterest icon | The user got directed to Pinterest which opens in a new tab | __ |

### Bugs

During the testing several bugs have been discovered. No bugs were left unfixed.

When  

## Technologies Used

The repository is created from [Code Institutes Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template) through [GitHub](https://github.com/). The Project board is created at [GitHub](https://github.com/). The code is written in [Gitpod](https://www.gitpod.io/) and deployed at [Heroku](https://www.heroku.com/). The wireframes are created in [Balsamiq](https://balsamiq.com/).

The code languages used in this project are HTML, CSS, JavaScript and Python. The main frameworks used are Django and Bootstrap.

## Deployment

### Fork repository in GitHub

- Open the chosen repository in GitHub 
- Click on the "Fork" button
- A copy of the repository is now located in your own account

### Clone repository in GitHub

- Open the chosen repository in GitHub 
- Click on "Code" button
- Copy the URL
- Open your command line interface
- Navigate to the directory you want to clone the repository to
- Use 'git clone', followed by the earlier copied URL
- Move into the newly created directory
- Install the dependencies using 'pip install -r requirements.txt'
- Run the application with 'python manage.py runserver'

### Deployment to Heroku

- Open Heroku and log in
- Click on "New" and choose the option "Create new app"
- Choose an app name and which region (Europe or United States) you are located in
- Press "Create app"
- When the app is created, choose the Settings tab
- Under "Config Vars", press "Reveal Config Vars"
- In keys, write DATABASE_URL
- In value, insert the url to the database
- Press "Add"
- Under "Buildpacks", press "Add buildpack"
- Choose "Python", press "Add buildpack"
- Change tab to the Deploy tab
- Choose deploy method - GitHub
- Search for the correct repository name at your connected GitHub account
- Press "Connect"
- Under "Manual deploy", choose which branch to deploy and press "Deploy Branch"

Link to deployed website: <https://_____.herokuapp.com/>

## Credits

### Libraries used

| Library | Functionality |
| ------------------- | --------------------------------- |
| django-allauth | Used for authentication, registration and account management |
| django-summernote | Integrated editor in djangos admin panel |
| gunicorn | Used to run Python web applications |
| oauthlib | Used to implement OAuth functionality |
| sendgrid | For interacting with the SendGrid email service |
| urllib3 | Used to make HTTP requests |
| whitenoise | Simplifies static file serving for Python web apps |

### Used resources

| Page | Used for |
| --------------| ----------------- |
| [Djecrety](https://djecrety.ir/) | Generate a secret key |
| [Frida Wikell](https://github.com/FridaWikell/frisa-booking) | For the ReadMe format |
| [Font Awesome](https://fontawesome.com/) | All icons at the website |
| [W3Schools](https://www.w3schools.com/howto/howto_js_read_more.asp) | Base for read more/read less buttons |
| [django](https://docs.djangoproject.com/) | Knowledge about django |
| [Emojipedia](https://emojipedia.org/) | Select emojis |
https://learndjango.com/tutorials/django-testing-tutorial
| [Learn Django](https://learndjango.com/tutorials/django-testing-tutorial) | Learn Django's page on testing |

### Images

| Page | Used for |
| ------------- | --------------- |
| [Vecteezy](https://www.vecteezy.com/photo/_) | Background image at 500 page, from [_](https://www.vecteezy.com/members/_) |
| [BeFunky](https://www.befunky.com/) | Edit and resize images |
| [Pixelied](https://pixelied.com/convert) | Convert images to webp |
| [TinyPNG](https://tinypng.com/) | Compress images |

All other photos are taken by the website creator, [Luke Maycock](https://github.com/l3wk3m).

## Acknowledgements

A big thanks to my mentor Ronan McLeland for feedback and direction throughout!

[Back to top](#studiobooker)