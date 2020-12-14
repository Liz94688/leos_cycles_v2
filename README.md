# Leo’s Cycles

Deployed site link [here](https://leos-cycles.herokuapp.com/)

##### Does your bike need a bit of TLC?
Leo’s Cycles offers its members the convenience of having a bike engineer travel to their home to complete a maintenance service on their bike, on a day of their choosing. 

Leo’s Cycles provides members with expert guidance on each service offered, as well as a clear breakdown of what they will be spending their money on before making a purchase. With experts on hand to answer any customer queries, in addition to a specialised ‘bespoke’ service available to all members, we are confident all of our customers’ biking needs can be met by using the site.

## Table of Contents
1. Why This Project
2. UX
* User Stories
* Wireframes
* Database Schema
3. Features
* Existing Features
* Features Left to Implement
4. Technologies Used
* Version Control
* Hosting
5. Testing
* Code Validation
* Automated Testing
* Manual Testing
6. Deployment
* Local Deployment
* Remote Deployment
7. Credits
* Content
* Acknowledgements

## Why This Project?
I created this app as part of the Full Stack Frameworks project of [_Code Institute’s_](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create an online bike maintenance service for customers of a local bike shop, allowing users who joined as members to easily access the expertise and maintenance services of the local business owners and their bike engineers.

Users can register to create an account, which then allows them access to the bike maintenance services offered by their local bike shop, as well as access to a specialised ‘bespoke’ service for bike enthusiasts who are looking for something a little more specific, before then going on to make a purchase.

Authenticated users can create reviews on a bike service they have already purchased and had experience of, these can then be viewed on the bike details page of each service. These same users can also view their order history on a User Profile page.

The front-end display and functionality uses HTML, CSS and JavaScript. The back-end functionality uses Python, Django, SQLite3 and PostgreSQL.

## UX
Leo’s Cycles is a place where bike owners of all kinds - weekend riders, commuters, professional competitors - are invited to join an ever-growing community of people in supporting their local bike business through a bike maintenance service.

Users can register, login and browse the current services available. Services can be paid for online, while users can view their order history via their profile page. Any user who has purchased a service is invited to leave a review which is then displayed for all other users who view the service details it references.

Leo’s Cycles is designed to give the user a clear and modern experience when searching for and purchasing a maintenance service for their bike, proving quick access to available services and  their specific details.

The navigation bar provides one-click links to the home, about, contact, login and registration pages, as well as a one-click link to the service page. Only registered and logged in users can see the specific details for each of the services available, as well as any reviews left by other members and the user profile link.

#### User Stories
Find a link to userstories[here](<a href=“https://github/Liz94688/leos_cycles_v2/tree/master/documents/user_stories.pdf”>).

#### Wireframes
I drew my wireframes by hand, copies of which can be found [here](<a href=“/Liz94688/leos_cycles_v2/blob/master/documents/wireframes”>). These show how I plan to make my website/app responsive.

#### Database Schema
Before building my project, I created an Entity Relationship Diagram (ERD) to outline the database schema for the various tables that I would use. The link for this file can be found [here](<a href=“/Liz94688/leos_cycles_v2/blob/master/documents/schema.jpg”>).


## Features
#### Existing Features

### Home Page
Serves as the initial landing page for all users

* **Navigation bar** - The navbar links vary depending on whether the user is logged in or not. ‘Leo’s Cycles’ is a link to the ‘Home’ page and is visible to all users at all times. If the user isn't logged in, the ‘Services’, ‘Contact’, ‘Login’ and 'Register' links are shown. When the user is logged in, the available links expand to include ’User Profile' and 'Logout' links. If the user is logged in as the ‘superuser’, the links expand again to include ‘Admin’ -  providing the ‘superuser’ with the ability to ‘Add Level’ and ‘Add Service’.

* **Basket** - Visible to all users, clicking this button will take the user to the basket.

* **'Our Story'** - This section provides the user with a short description of how the site came about, with a ‘click here’ link redirecting them to the ‘About’ page which provides more information on the business itself.

* **Benefits to Members** - Visible to all users. Provides three pieces of information on why becoming/being a member is so beneficial. The message introducing this section changes depending on whether the user has logged in or not, if a user has not registered or logged in, ‘Register’ and ‘Login' buttons are displayed and redirect users to the respective pages.

### About Page
* **'Where it all began'** - Visible to all users. Provides the user with a detailed description of how the site came about and the aim of the business towards its members and the local community.

* **'Where do I start?'** - The user is also given a short introduction to the site and how to go about navigating their way through it, starting with the direction that they register as a new user and start enjoying the benefits offered to members. 

* **Buttons** - These change depending on if the user is logged in or not. Users who have yet to register or login are shown buttons that redirect them to the ‘Register’ and ‘Login’ pages respectively. Users who have already logged in are encouraged to start browsing at the services available by being shown a ‘Services’ button which redirects them to the ‘Service’ page.

### Contact Us Page
* **Contact Form** - Visible to all users. A clean and easy-to-use contact form, including sections for email address and the users message. This has been designed to be as simple as possible, making the process of asking for further information a a pleasant experience for a user. Placeholders included in the form, as well as a button labelled ‘Submit’ guide the user on how to complete and send the form.

* **Contact Info** - Users on small screens are provided with the contact telephone number and residential address of the business, in case they wish to get in touch with the business in a way other than the Contact Form.

### Services Page
This page is visible to all users and displays all the current services available.

* **Services** - Displays a basic outline of the services available to users - including name and price.

* **Free Service Banner (included at the top of the screen)** - Reminder to users that services beyond the ‘Basic’ service will not include a service charge.

* **Register or Login button** - Visible only if users are not logged in. A statement informs the user they need to register or login to access any further information on each service and redirects the user to the ‘Registration’ and ‘Login’ pages respectively.

* **View Details button** - Visible only to users logged in, users click the button and the link redirects them to the selected ‘Service Details’ page.

* **Bespoke Service button** - Visible only if users are logged in. A section at the bottom of the page highlights a bespoke service option available to users and includes a button redirecting the user to the ‘Contact Us’ page to get more information on what can be provided.

* **Edit and Delete Links** - These are only visible if the superuser is logged in. The links are positioned below each individual service and, once, clicked, either redirect the superuser to the ‘Edit Service’ page or delete the chosen service. The delete link has been coloured in red to alert the superuser to the danger of clicking it.

### Service Details Page
Only visible to users who are logged in, displays further information about the selected service

* **Free Service Banner (included at the top of the screen)** - Visible to all users. Reminder to users that services beyond the ‘Basic’ service will not include a service charge.

* **Service Details** - Displays the service title, a detailed description of the level of service, including suggestions and helpful tips for users on who would use this level of service (i.e., if a user takes their bike out 2-3 a month for rides at the weekend, then Basic would be the right choice for them), as well as the price of the service.

* **Quantity Option** - Buttons ‘-’ and ‘+’ allow the user to increase or decrease the number of services they wish to purchase. This is intended for users who have more than one bike that needs a service (i.e., a family of four). A statement has been placed above this section to clarify why a user would need to increase the quantity of the service they have chosen.

* **Buttons** - Users are provided with the button ‘Keep Looking’, which redirects them back to the main ‘Services’ page. There is also an ‘Add To Basket’ button, which adds the chosen service (and number of services) to the users order. Users are informed of this action by a success message that appears in the top-right hand corner of the screen.

* **Edit and Delete Links** - These are only visible if the superuser is logged in. The links are positioned below the details of the chosen service and, once, clicked, either redirect the superuser to the ‘Edit Service’ page or delete the chosen service. The delete link has been coloured in red to alert the superuser to the danger of clicking it.

* **Reviews** - Users are able to see any reviews about the particular service that have been written by members who have used the service in the past. Each review includes the name of the service chosen, the content of the review left, the username of the author and the date the review was recorded.

### Basket Page
Only visible to users who are logged in. Shows the user a summary of the service(s) that were added to the basket. If there are no items in the basket, a message is displayed advising the user their basket is empty and providing a button to ‘Return To Services’

* **Service Details** - Displays the name and price of each chosen service.

* **Quantity** - Displays the quantity of each service chosen. Users can amend the quantity of the service by clicking the '-' or '+' buttons to increasing or decreasing the quantity in the basket and by clicking the ‘Update’ link underneath the quantity box. This link has been highlighted in a different colour in order to stand out to the user.

* **Sub Total** - Displays the sub-total of the basket. This comes in handy if the user has increased the quantity of services in the basket as, apposed to the ‘Price’ column, this column displays the accumulated figure of all the items in the basket.

* **Remove** - Allows the user to remove the chosen service from the basket via a link. The link is highlighted in red to make it very clear to the user what the link is there for. Once clicked, users are redirected back to the ‘Basket’ page and advised of the items removal through a success message that appears in the top right-hand corner of the screen . If there are no items left in the basket, a message appears in the main section of the basket, advising the user ‘Your basket is empty’ and providing a button directing the user to ’Return To Services’. This button redirects the user back to the ‘Services’ page.

* **Totals and Service Charge** - Displays the ‘Bag Total’, ‘Service Charge’ and ‘Grand Total’ for the user. If the user has decided to choose a service above the ‘Basic’, their ‘Service Charge’ figure shows as £0.00 to let them know they qualify for free service.

* **Return To Services Button** - Redirects the user back to the ‘Services’ page.

* **Secure Checkout Button** - Redirects the user to the ‘Checkout’ page.

### Checkout Page
Gives the user a summary of their order.

* **Order Summary** - Displays the item chosen (this is also a link back to the ‘Service Details’ page), the quantity, Subtotal for each item, Order Total, any service charge applied and the Grand Total.

* **Contact Details/Service Location/Payment Form** - this form collects the user’s contact information and the location details of the planned service. There is a select box at the end of this form with the default set to ‘True’; this saves the details provided by the user for future purchases and can be accessed in the user’s ‘User Profile’.

* **Service Date** - This allows the user to input a convenient date for engineers to visit them at their address and complete the service purchased. This date is included in the order summary, along with the order item and quantity chosen.

#### Stripe
Allows the user to pay securely using Stripe payment

* **Payment** - This allows the user to input their card details, connecting to Stripe once the ‘Complete Order’ button is clicked and processing the user’s card details. No card details are stored locally or on the server, they are only sent to Stripe and then discarded.

* **Loading Overlay** - while the payment is being processed, a blue overlay with a white, circular arrow is displayed to the user. This provides visual confirmation that an action is taking place.

### Order Confirmation Successful Page
After completing the payment, the user is redirected to an ‘Order Conformation’ page, where a ‘Thank You’ message is displayed and the user’s order confirmation and summary are held.

* **Order Confirmation** - User receives confirmation the order has been placed, as well as being given an order reference number and summary of their order that includes the Order Details, Service Location and Billing Information. 

* **Email** - User receives email confirmation their order has been placed.

* **Message** - As well as the ‘Thank You’ message and order confirmation message, the user is also shown a success message informing them that their order was successful and an email has been sent to their email address.

### Registration Page
Allows new users to sign-up for an account.

* **Register** - Users must provide a unique email address and username, both of which are checked against existing entries in the database. A password is required, which must be entered twice to check it has been input correctly.

* **Message** - On successfully registering the user will be redirected to a page informing them that a verification email has been sent to the email address provided and to follow the link provided to finalise the registration process. An alert message also notifies the user that their account has been created and an email sent to their email address.

### Log In Page
Allows existing users to log in to their account

* **Login Form** - Requires the user to input their username and password. There is button directing the user back to the ‘Home’ page, a ‘Sign In’ button that directs the user on to the ‘Home’ page and a password reset link if the user has forgotten or lost their password.

### User Profile Page
Only available to a logged in user.

* **Order History** - Users are able to view a summary of their previously purchased orders. Users can click on the truncated order number for each order and be redirected to the ‘Order Confirmation’ page for that specific order. An alert message appears in the top-right hand corner reminding them that this order is a past order. A button at the bottom of the summary redirects the user back to their ‘User Profile’ page.

* **Customer Address and Contact Information** - Users are able to add, view and edit their contact information and address using this form. If any edits are made, a message alert appears in the top right-hand side of the screen to inform them of the change.

* **Your Reviews** - User are encouraged to add a review on any services previously purchased by clicking on a link which redirects them to the ‘Add Review’ page. Once a review has been added, the user is redirected back to the ‘User Profile’ page and is able to view the review they have just written.

* **Recorded Bike** - Advises users they can add a bike to their profile, redirecting users to the ‘Add Bike’ page, where they can add, view and edit their bike. Once a bike has been added, the details show up in the user’s profile.

### Add Bike Page
Only available to a logged in user via the ‘User Profile’ page.

* **Add Bike Form** - Users are able to construct their bike using a series of drop-down options and text areas included on the form. Placeholders help the user navigate through the form and complete the required sections, allowing them to include specific details on their current bike, including Bike, Frame and Handlebar type, as well as sections on Wheel Size, Owner Description, Age and a checkbox asking the user to confirm if the bike is their current bike.

* **Buttons** - Buttons provide the user with the option to return to their ‘User Profile’ or to ‘Add Bike’.

### Bike Details Page
Only available to a logged in user. Users are redirected to this page from the ‘Add Bike’ page if the ‘Add Bike’ button has been clicked. The user is reminded that a bike has been successfully added by a success message placed in the top right-hand corner of the screen.

* **Edit Button** - Redirects the user to the ‘Edit Bike’ page, where they have the option to update any part of the bike model they wish to. 

* **Delete Button** - Allows users to delete the bike they have created. Once clicked, the user is redirected back to the ‘User Profile’ page and is alerted to the bike being deleted by an alert message placed in the top right-hand corner of the screen. The user then has the option to add a new bike, if they wish to do so. 

* **Recorded Bike** - The user can view the bike they have recently added from the ‘Add Bike’ page. This sections displays all the details recorded by the user - Bike, Frame and Handlebar type, as well as Wheel Size, Owner Description, Age and whether the bike is a current bike.

* **Return To Profile Button** - Provides the user with the ability to return to their ‘User Profile’ where they are then able to view the bike they have just created. The user is also provided with a message underneath their bike information, advising them that changes can be made to the bike by clicking the available link. This link redirects the user to the ‘Bike’ page where they have the option to view their current bike and make any changes.

### Bike Page
Only available to a logged in user. Users are provide with a synopsis of their current bike, including the Type and Age of the bike, as well as the Frame and Handlebar options.

* **Return to User Profile Button** - Users are redirected back to their ‘User Profile’.

* **View Details Button** - Users are redirected to the ‘Bike Details’ page where they have the options to edit or delete their bike or return to their ‘User Profile’.

### Edit Bike Page
Only available to a logged in user. Users are redirected to this page once the ‘Edit Bike’ button has been clicked.

* **Edit Bike Form** - Users are able to edit any area of their current bike using a series of drop-down options and text areas included similar to the ‘Add Bike’ form. Placeholders help the user navigate through the form and complete the required sections. An alert message appears in the top right-hand corner of the screen warning the user that they are editing their chosen bike.

* **Back Button** - Users can return to the ‘Bike’ Page if they change their mind and no longer want to edit their bike.

* **Edit Button** - Once any changes have been made, users can click this button and are redirected to the ‘Bike Details’ page where a success message advises them that their bike has been  successfully edited.

### Review Page
Only available to logged in user from the ‘User Profile’ page. Allows users to add a review on the level of service they have previously experienced.

**Review Form** - Users are able to input the level of service attached to their review, as well as some content in a message box. Placeholders navigate the user through the review process.

**Add  Review Button** - Allows user to add the review.

### Edit Level/Edit Service Pages
ONLY available to the superuser.

* **Alert Message** - Appears in the top right-hand corner of the screen as soon as the superuser arrives on the page, advising them on what service they are editing.

* **Service/Service Details Form** - Whether the superuser has chosen to edit the Level or the Service, the form appears in the same format. The sections included within each form include Level Type, Description and Price.

* **Buttons** - Buttons to ‘Cancel’ and ‘Update Service’ allow the superuser to decide what action to take.

#### Features Left to Implement
With more time and knowledge, I would have liked to implement the additional features to the app:

* **Add Bike To Order** - The intension in the future is to give users the ability to add multiple bikes to the ‘Stored Bike’ page as well as allowing them the ability to add a specific bike to an order at the checkout. 

* **Add Date and Time To Order** - I unfortunately ran out of time to include this in the app. The user is currently asked to input a date of their choosing for their purchased service and is advised by a statement that an engineer will be in touch to organise a specific time on that date. The intension would be to make this more user-friendly and include a calendar with options for time-slots for the user to pick on the front end and for the back end to make sure there were no date and time overlaps booked in by users.

* **Star Ratings** - I believe the current ‘Review’ page would benefit from a ratings option. While comments made by customers are informative I believe new users would also respond well to a ‘star-rating’ or percentage-based view of each service.

* **Messages** - Currently, users are advised of any success, alert and information actions by a message box appearing in the top right-hand screen that stays there until the user closes it themselves. A future feature would be to make sure enough time lapsed for the user to read the message and to then implement an automatic fade. 

## Technologies Used
* [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
The project uses **HTML** to create the basic elements and content of my app.
* [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
The project uses **CSS** to apply the custom styles to my app.
*  [**Bootstrap**](https://getbootstrap.com/)
The project uses the **Bootstrap** framework to add a responsive grid system, prebuilt components and Bootstrap styles, before adding my custom styles.
* [**jQuery**](https://jquery.com/)
The project uses **jQuery** as the primary JavaScript functionality. This is the standard jQuery built within Bootstrap components.
* [**Python**](https://www.python.org/)
The project uses **Python** as the back-end programming language for my app.
* [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
The project uses **Jinja** for templating in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
* [**Font Awesome**](https://fontawesome.com/)
The project uses **Font Awesome** for the visual icons used in my app.
* [**SQLite**](https://www.sqlite.org/index.html)
The project uses **SQLite** as the relational database to hold the backend information for the models used, when running locally.
* [**PostgreSQL**](https://www.postgresql.org/)
The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used, when deployed remotely.
* [**Google Fonts**](https://fonts.google.com/)
The project uses **Google Fonts** for the typography. The font styles used in the app were *Poppins and Sans-Serif*.
* [**Stripe API**](https://stripe.com/gb)
The project uses **Stripe** to make secure payments from the app.
* Gitpod
I've used **Gitpod** as the development environment to write the code for my app.

#### Version Control
* [**Git**](https://git-scm.com/)
I've used **Git** as a version control system to regularly add and commit changes made to my project in Gitpod, before pushing to GitHub.
* [**GitHub**](https://github.com/)
I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

#### Hosting
* [**Heroku**](https://www.heroku.com/)
I've used **Heroku** as the hosting platform to deploy my app.

## Testing

#### Code Validation
 * [**W3C HTML Validator Tool**](https://validator.w3.org/#validate_by_input) was used to validate HTML code.
 * [**W3C CSS Validator Tool**](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate CSS code.

#### Automated Testing
The [**Coverage**](https://pypi.org/project/coverage/) library was used for testing, to help keep track of how much code was covered by tests.

To generate a coverage report you need to install the package using `pip install coverage`
* Run `coverage run manage.py test`
* Then `coverage html` to generate the report
* The report can be viewed in a browser by opening the `index.html` file from inside the `htmlcov` folder.

#### Manual Testing
A seperate Manual Testing document can be found [here](<a href=“/Liz94688/leos_cycles_v2/blob/master/documents/manual_testing.pdf”>)

#### Problems and bugs
**Image Upload**

* When I deployed the project to **Heroku** none of the images I had chosen for the ‘Home’ page were loading. I ended up moving the images from the **Media** folder I had saved them in to a separate folder within the **Static** folder called **Images**. 

* I included `STATIC_ROOT = os.path.join(BASE_DIR, ‘staticfiles')` within `setting.py` and used the command `python3 manage.py collectstatic` to save all the images to the `STATIC_ROOT`.

* Once I had made these changes, the images displayed correctly in the deployed site through **Heroku**.

**Webhook Handler**

* I planned to include a date picker in the **Checkout** app, to allow the user to pick a preferred date for their service to be completed on. I unfortunately ran out of time for this and so included a Datefield in the **Checkout - Order** model, so the user could at least input their own date and have it recorded on their order. 

* This appeared to be a sufficient interim measure, however, during testing, I realised that an error was produced if the user didn’t input an exact format of the date (i.e. YYYY-mm-dd) and, as such, the form data collected in the **Order** model was recorded as invalided, causing issues with the webhook.

* As previously mentioned, at this point I had run out of time to fix this bug through form validation. As a preventative measure in the short term, I included a paragraph on the front-end of the form, warning the user to input the date in a certain way. 

## Deployment
I used **GitHub** for my version control and **Heroku** to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in **Heroku**, using the unique name of **'leos-cycles'**.

2. Went to the **Resources** tab in **Heroku** and searched for **Heroku Postgres** in the 'Add-Ons' section.

3. Selected the free **Hobby** level.

4. Returned to my local workspace and installed `dj_database_url` and `psycopg2-binary` before freezing both in the `requirements.txt`.

 5. Replaced the default database with a call to `dj_database_url.parse()`, entering the database URL from **Heroku**. 

6. Ran `python3 manage.py migrate` to connect the new **Heroku** database.

7. Used the `python3 manage.py createsuperuser` command to set up a new superuser in the PostgresSQL database.

8. Set up the `DATABASES` in `settings.py` with an if-statement so that when the app is running in Heroku, it connects to the **Postgres database**, otherwise, the app connects to **SQLite**.

9. Ran `pip3 install gunicorn` before freezing it in `requirements.txt` and created a **Procfile** to tell **Heroku** to create a web dyno.

10. Temporarily disabled `COLLECTSTATIC=1` to stop **Heroku** from collecting static files during deployment and added hostname of **Heroku** app to `ALLOWED_HOSTS` in `settings.py`, along with `localhost`.

11. Added and committed all these changes to **Github** and **Heroku** with commands `git push` and `git push heroku master` respectively.

12. Set up automatic deployment in **Heroku**. Went to the **Deploy** tab in **Heroku**, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.

13. Generated new `SECRET_KEY` and added to **Config Vars** in **Heroku**. Returned to `settings.py` and replaced `SECRET_KEY` settings with a call to get from the environment.

14. Set `DEBUG` to `True`, only when the variable called `DEVELOPMENT` can be found in the environment.

15. Went to the **S3** section of **AWS** and created a new S3 bucket. Enabled **Static Website Hosting**.

16. Within the **Permissions** tab of the bucket, the following CORS Configuration was included, to set up the required access between the **Heroku** app and the s3 bucket:
```
[
    {
		“AllowedHeaders”: [
			“Authorization”
		],
		“AllowedMethods”: [
			“GET”
		],
		“AllowedOrigins”: [
			“*”
		]
		“ExposedHeaders”: []
	}
]
```

17. Went to the **Bucket Policy** tab and selected the **Policy Generator** to create a security policy for the bucket. Set to **S3 Bucket Policy**, allowed all principles and chose the action **'get object'**. **Generated Policy** and copied into the **Bucket Policy** editor.

18. Went to the **Access Control List** tab and set the list objects permission for everyone under the **Public Access** section.

19. Went to the **IAM** section of **AWS** and created a ‘New Group’ named **'manage-leos-cycles'**.

20. Still in the **IAM** section of **AWS**, created a 'New Policy' called **'leos-cycles-policy'** and a 'New User' called **'leos-cycles-staticfiles-user'** and attached these to the newly created group.

21. Downloaded the **.csv** file holding the ‘New Users’ access key and secret access key.

22. Updated `settings.py` with an if-statement to check for a variable called `USE_AWS` and set this to **True** in **Config Vars** in **Heroku**. While still in `settings.py`, defined the `AWS_STORAGE_BUCKET_NAME` and `AWS_S3_REGION_NAME`, as well as the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, setting all to get their data from the environment. Updated **Config Vars** in **Heroku** with the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` - both generated in **IAMS** section of **AWS**.

23. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.

24. Updated the `settings.py` file with the relevant configuration for static and media file storage.

25. Created new ‘media’ folder in S3 section of AWS and uploaded the relevant media files attached to the site.

26. Added **STRIPE_PUBLIC_KEY** and **STRIPE_SECRET_KEY** to the **Config Vars** in **Heroku**.

27. Created new webhook endpoint in **Stripe** and added **STRIPE_WH_SECRET** to the **Config Vars** in **Heroku**

The app was successfully deployed to Heroku at this stage.

#### Repository Link
Click the link below to visit my project's GitHub repository:
[**Leo’s Cycles Repository**](https://github.com/Liz94688/leos_cycles_v2)

## Credits

#### Content
* My friend **Laura Fox** created all of the content, following discussions with me on the purpose of the site and what information needed to be displayed to users.

#### Media
* The carousel images on the **‘Home’** page were sourced from [Pexels](https://www.pexels.com/).

#### Acknowledgements
* I would like to thank my mentor **Guido Cecilio** for his feedback on my project's scope, design and functionality.
* Thanks to also to the **Tutors at Code Institute** for all their help and assistance throughout my project.

#### Disclaimer
This project is for educational purposes only.