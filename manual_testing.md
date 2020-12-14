## Testing
### Manual Testing
Manual testing was conducted with each feature and on each user story, using different screen resolutions, devices and in different browsers to ensure the application is a good solution to user's needs.

**Navbar**
* clicked on all the links in the navbar, to check if they work properly and redirect the user to the correct destination
* checked these same links on different devices, due to the responsive design the navbar looks different on different devices
* make sure the navbar collapses on small screens and toggle button can be clicked by the user to find the menu
* scroll down each page to check the navbar is visible on larger screens, make sure the basket icon and amount are visible to the user on smaller screens 
* make sure the basket icon and amount are in proportion to the space allocated for the nav, no wrapping or squashed icons
* make sure links highlight when hovered over
* check to see if the user’s status is reflected in the navbar - Register, Login and Logout. If a user is not logged in, they are only able to see the Home, About, Contact and Service pages - limited viewing on the Services page. Check the user can see the full Services page, the Service Details page, Basket, Checkout, Userprofile, Add Review and Add Bike pages
* check only admin can see the Admin link to add and edit Levels and Services
check that when a service is added to the basket, the basket icon is highlighted in white and that total changes when further service is added or removed

**Footer**
* check the social media icons all lead to the corresponding pages and, as well as opening in new tabs
* check the link for ‘Leo’s Cycles’ redirects the user to the Home page
* check different devices to test if the footer is responsive - on small screens only social media icons show. On large screen the footer expands to include links to the About and Contact page, as well as providing further contact information on address and telephone for the local business

**Home**
* click all the buttons across the page
* check the image carousel by clicking on the chevrons
* verify the expected text and images are displayed

**About**
* verify the expected text is correctly displayed

**Contact**
* check user can input email and message and submit information on the form
* check form cannot be submitted without required information
* check page includes further contact details (i.e. address and telephone) on smaller screen - large screens record this information in the footer

**Services**
* check the expected data from the Services model is displayed correctly
* check the service delivery banner is displayed correctly
* check the buttons work - depending on if the user is logged in and if they are the admin. Admin also has access to ‘edit’ and ‘delete’ buttons - check these are displayed and redirect as per their purpose. Check users who are logged in can proceed to the ‘Service Details’ page and that users not logged in are directed to the ‘Registration’ and ‘Login’ pages
* check the logged in user is redirected to the ‘Contact’ page to enquire about the bespoke service available

**Service Details**
* verify the expected text and input boxes are displayed correctly
* check the service delivery banner is displayed correctly
* check the quantity input box is displaying the correct amount and that the button to increase and decrease are working
* check the user cannot decrease the quantity to below the number 1 - button stops working
* check the buttons increase in size when hovered over and redirect the user to their allocated destination - either to return back to ‘Services’ page or adding the item to the ‘Basket’
* check the data from the Review model is displaying properly - specific for that service
* check the basket icon is updated when ‘Add To Basket’ is clicked - highlighted in white and displaying the correct amount
* check the success message appears when item is added to basket

**Basket**
* check the service delivery banner is displayed correctly
* verify the data from the Service model is displaying properly
* verify the quantity input box is displaying the correct figure, as well as checking the increase and decrease buttons work properly and update when the ‘Update’ option is clicked
* check the subtotal, bag total, service charge and grand total are all displaying the correct amounts
* check the service charge is added to items under £80.00 and removed for items/totals over £80.00
* check the ‘Remove’ link and free service reminder are displaying as red, to alert the user
* check the ‘Remove’ links works properly
* check user is redirected to the correct page when ‘Return to Services’ or ‘Secure Checkout’ clicked

**Checkout**
* verify the service delivery banner is displayed correctly
* verify the items added to the basket by the user are displaying properly - including the chosen service, the quantity and the price
* check the sub totals, order totals, service charge and grand total all calculate correctly based on the items in the basket
* check the form fields are displayed correctly and include the required placeholders
* check the form verification works properly and the form cannot be submitted without all the fields being filled
* check the page displays properly on small and large screens - order summary should display above the contact details form on small screens and next to the contact details form on large screens
* check the ‘Adjust Basket’ button redirects the user back to their current basket
* check the order is successfully completed when user clicks the ‘Complete Order’ button
* check the overlay is displayed to the user while the order is being processed
check the user is automatically redirected to the ‘Checkout Success’ page once order processed
* check the ‘Checkout Success’ page displays the expected information to the user - including the order information, order details, customer address and service location and billing information
* check the user is shown a success message stating the order has been successfully processed

**User Profile**
* check the users address and contact information has been saved in the correct format, is user has already made and purchase and chosen this option
* check the form verification is correct and working on each field of the contact information form - remove details/leave field blank and try to update the form to * check if warning appears to user that field has to be completed
* check form updates correctly if completed fully by user with new information
* check service history is displayed correctly - including the order number, date of order, items and totals. 
* check order number can direct the user to the specific order summary displayed in the ‘Checkout Success’ page and that user can return back to the ‘User Profile’ when they want to 
* check the buttons for the ‘Leave A Review’ and ‘Add Your Bike’ work and direct the user on the appropriate pages 

**Add Review**
* check the appropriate fields are showing on the review form
* check the data pulled from the Services model is correct
* check an empty review cannot be added
* check the form validation is working correctly on each field
* verify the ‘Return to User Profile’ button redirects the user back to the correct page
* verify the ‘Add Review’ button successfully redirects the user back to their ‘User Profile’, where the users review should now be displayed and a success message should be informing the user of the newly added review in their profile

**Add Bike**
* check the appropriate fields are showing on the bike form
* check the data pulled from the Bike model is showing correctly
* check an empty form or an incomplete form cannot be added by the user
* verify the ‘Bike Frame Size Guide’ can be access and closed by the user
* verify the button to return to the user profile works
* verify the ‘Add Bike’ button re-directs the user to the ‘Bike Details’ page

**Bike Details**
* confirm the success message appears, letting the user know their bike has been successfully added
* check the page includes the expected information about the added bike
* verify the ‘Edit’ and ‘Delete’ button redirect the user to the appropriate pages - the ‘Delete’ button redirect the user back to the ‘User Profile’ page, where they are provided with an alert that their bike has been deleted

**Edit Bike**
* check alert message appears advising the user they are editing their bike
* check the appropriate fields are showing on the edit bike form
* check the fields are repopulated with the correct data already provided by the user
* check an empty form or an incomplete form cannot be edited by the user
* verify the ‘Bike Frame Size Guide’ can be access and closed by the user
* verify the ‘Back’ button returns the user to the ‘All Bikes’ page
* verify the ‘Edit Bike’ button re-directs the user back to the ‘Bike Details’ page

**All Bikes**
* check the page displays the correct information expected from the users saved bike
* check the button ‘Return To User Profile’ works correctly
* check the ‘View Details’ button redirects the user back to the ‘Bike Details’ page

## Authentication pages
These features are built-in components of Django allauth package, however, manual tests were also completed on these pages. With around 5-10 different accounts being created and tested from Registration through to ‘Checkout Success’.
Reset Password, Verification Email, Login, Create Account were all working as expected.

* try to register or login as a user with the incorrect information (i.e. incorrect email format, no password, incorrectly spelt password, using a username that already exists within the database)
* submit a valid ‘Registration’ form
* try to enter two alternate passwords in the registration form and try to enter an old password when re-setting a user’s password
* try to log into an account with the incorrect user information

## Compatibility and Responsiveness
This website had been being tested during the development across **multiple browsers** (Chrome, Edge, Safari, FireFox, Internet Explorer) and on **multiple devices**: mobile (iPhone 5, 6, 8, Samsung Galaxy), tablets (iPad, iPadPro) and laptops.

In addition to this, Google Chrome’s developer tools were constantly used to test the project:
* **Google Chrome's Developer Tools** to see how the site looks across all the different device screen sizes to ensure compatibility and responsiveness.

## Other Testing
The app was tested throughout the development process using the local debugger: `debug=True`. Each time an error occurred, the debugger displayed an error message, allowing me to find the location of the error and fix it.

I also asked my friends and family members to thoroughly test my website in different devices to give me a feedback about the design, functionality and their user experience.