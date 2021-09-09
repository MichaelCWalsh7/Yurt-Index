<h1 align="center">Yurt Index</h1>

[View the live project here.](https://yurt-index.herokuapp.com/home_page)

A dictionary for Irish slang. It is designed to be responsible and accessible on a range of devices, making it easy to navigate for potential readers.

<h2 align="center"><img src="https://yurt-index.herokuapp.com/static/images/readme/readme-hero.png"></h2>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals
    
    1. As a First Time Visitor, I want to easily understand the main purpose of the site and find definitions of words.
    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
    3. As a First Time Visitor, I want to easily be able to search or find a word that I'm interested in.
    4. As a First Time Visitor, I want to learn extra information on words that I'm interested in, for instance how to spell or use a slang word.

    -   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to know what words are well-liked by the community and which have more dubious entries.
    2. As a Returning Visitor, I want to create an account so I can show my appreciation or discontent with entries on the site.
    3. As a Returning Visitor, I want to edit errors or add definitions/alternative spelling or examples to words I know. 
    4. As a Returning Visitor, I want to explore the profiles of other users who have created/edited entries on the site. 

    -   #### Frequent User Goals
    1. As a Frequent User, I want to create my own entries on the site for words that are not yet present.
    2. As a Frequent User, I want customize my profile so other users can get an impression of my online persona. 
    3. As a Frequent User, I want to browse through various categories of entries on the site. 
    4. As a Frequent User/Admin, I want to be able to create new tags for entries to be categorized by.

-   ### Design
    -   #### Colour Scheme
        - The colour scheme for the Yurt Index as a dictionary of Irish slang, is a fairly obvious choice of green, white & orange/gold. Matching the Irish tricolous flag.
        - The predominant green and white are also the colours of the Limerick flag, a city known for it's predominant use of slang that often enters the national zeitgeist.
        - However, the original colour scheme of the site was massively overhauled, midway through development. [Here is and image of the original colour scheme.](https://yurt-index.herokuapp.com/static/images/readme/readme-hero.png) This light green is much more inline with the original Irish and Limerick flag colours
        - As is evident from the above picture, the site now has a significantly darker colour theme, with the green chosen now closer to a darker forest green, rather than the flag-green of Ireland and Limerick.
        - This is mainly due to contrast. The light green shown in the above picture (#43a047) is extremely difficult to contrast with other classic text font colours.
        - The decision to go with a darker colour, rather than a lighter one, was inspired by contemporaries [Urban Dictionary](https://www.urbandictionary.com/) and [Dictionary.com](https://www.dictionary.com/e/slang/) (which surprisingly has a very comprehensive slang archive).
        - More on this in [the TESTING.md section](testing-section-link.com)
        - There is also a pale blue sometime visible on links on the site, this has no thematic relevance and is simply for pleasant, aesthetic contrast. 
    
    -   #### Typography
        - There are 3 main fonts in use on the site. 
        - The first being Eagle Lake, which has a back-up of serif. This is a highly stylized font, not used for long-form text, only for headings and even then only sparingly. This font has a celtic-style typography that is used to be somewhat reminiscent of [the legendary Book of Kells](https://yurt-index.herokuapp.com/static/images/readme/book-of-kells.png) and lean further into the Irish aesthetic of the site.
        - The second font in use is Hina Mincho, again with a back up of serif. This is a font that strikes a nice balance between modern and traditional, which compliments the Eagle Lake font well and is very appropriate for an online Irish slang database, it in and of itself being and blend of modern and traditional. 
        - Finally for variance and often for links, the third font is Merriweather, yet again with a back up of serif. the merriweather font stands out nicely from the other two, and thus is used for calls to action, sub-headings etc. It is a massive step-up from the default Materialize font that is overly generic for a site such as this one.

    -   #### Imagery
        - While imagery is quite important, the decision was made early on in the development process to move away from large visuals, for example a hero image. Multiple hero images were tested with the site, but none of them really looked or felt right. After a lengthy browse of popular competitors, namely [Urban Dictionary](https://www.urbandictionary.com/), [Online Slang Dictionary](http://onlineslangdictionary.com/) and [Dictionary.com](https://www.dictionary.com/e/slang/), I found that these sites had no hero image either, and very little in the way of imagery in general, it being often too distracting to the main content of the site. [Urban Dictionary](https://www.urbandictionary.com/), indisputably the most popular of the slang dictionaries goes so far as to have no home page at all, rather a word of the day that the user gets redirected to. While [Dictionary.com](https://www.dictionary.com/e/slang/) does have images in the slang archive of their site, these are almost exclusively to represent various word entries, a very cool feature, but far beyond the scope of a 1-man Milestone Project. (Though there is more on this in Future Features section located below.)

*   ### Wireframes

    - Home Page Desktop Wireframe - [View](https://yurt-index.herokuapp.com/static/images/readme/wireframes/home-desktop.png)

    - Home Page Mobile Wireframe - [View](https://yurt-index.herokuapp.com/static/images/readme/wireframes/home-mobile.png)

    - Word Page Desktop Wireframe - [View](https://yurt-index.herokuapp.com/static/images/readme/wireframes/word-page-desktop.png)

    - Word Page Mobile Wireframe - [View](https://yurt-index.herokuapp.com/static/images/readme/wireframes/word-page-mobile.png)

## Features

-   Responsive on all device sizes

-   Interactive elements

-   User account creation and management

## Planned Future Features

- Email verification
    - Although it is beyond the scope of this project, I discovered throughout the project that I am actually quite passionate about Irish slang, and would like to roll this website out to the general public. As far as I'm aware, there is no website that does this yet, so there's a definite gap. Email verification is a staple of modern websites with account creation and this feature will be implemented after I've finished the course and have more time. 
    - Unfortunately the implementation of this was pushed to future features due to time constraints. 

- Images
    - This is a two-fold plan. First I'd like to give the user the option to upload a picture or avatar to the site that they can use as a profile image.
    - Secondly, I'd like to include an option to upload an image associated with a word. 

- Pagination
    - This one really got the better of me for this proejct unfortunately. I spent a long time researching pagination using the tools and frameworks available, looking up tutorials online etc but almost everything that I found was related to sql. 
    - I desperately wanted to include it in the project, but I did not have the luxury of time, and so had to  relegate it to future features.

- Further Account Customization
    - While images have been mentioned above, other account features are planned for a later date as well, such as an option to curate what data is presented on each user's profile, user tags etc.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Materialize 1.0.0:](https://materializecss.com/)
    - Materialize was used to assist with the responsiveness, styling and for some icons of the website.
1. [MongoDB:](https://www.mongodb.com/)
    - MongoDb was used as the data storage and manipulation database for the project.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Eagle Lake', 'Hina Mincho' and 'Merriweather' fonts used on all throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for a small minority of icons on the website.
1. [jQuery:](https://jquery.com/)
    - jQuery is used to incorporate many of the Materialize elements throughout the site, but is also used in other areas of the site for general Ux and design improvements..
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Heroku:](https://id.heroku.com/login)
    - Heroku was used to deploy the live version of the site. 
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [Flask:](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask was the framework used to route and build the project.
1. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - The Jinja templating engine was used heavily throughout the project.
1. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
    - Werkzeug was the WGSI library used to hash and salt user passwords.
1. [Favicon](https://favicon.io/)
    - Favicon.io was used to generate the site's icon.

## Testing
- For the sake of brevity and concision, the documentation of all testing that has been conducted is located on a separate 
file. [Click anywhere on this sentence to be taken to the
TESTING.md file.](https://github.com/MichaelCWalsh7/Yurt-Index/blob/main/TESTING.md)

## Data Schema
- The data schema of the site (using MongoDB) employs the following 3 collections.

    1. Words
        - First and foremost there is the words collection. Obviously the bread-and-butter of any dictionary site is it's collection of words.
        - Of course each word has it's own unique ObjectId.
        - Each word item in the collection is assigned a myriad of data entries for site functionality.
        - Simple string entries are used for the word's name, it's base meaning and use, the date it was created and it's last edit date.
        - Each user has a string entry entitled 'password' which is a (salted) string containing the user's password.
        - Many booleans are employed, such as 'hasAltSpellings' and 'hasAltDefinitions'. These booleans dictate what will be displayed to the user when being taken to different word pages. There are many options on the site for alternative spellings/definitions/examples etc. and so a robust data system is required to manage them, which these booleans provided.
        - There are arrays used for a word's uses, alternate definitions and spellings. If none are provided on creation an empty array is present.
        - Every word has it's own unipque ObjectId obviously, however it also has an entry of the ObjectId of the user who created it. Rather than storing the user's name as a string, which may be liable to change, the ObjectId will mean that any edits to a user account will be reflected to anyone looking at the username on a word page. 
        - Every word has a 'rating' entry, which is an integer, this can be incremented or decremented by logged in users.
        - Every word has an 'edited' boolean, that by default is false but changes to true if a user edits a word. An aside on the bottom of every word page will then appear to indicate to the user what account was the last one to edit a word.
        - Every word has an array entitled 'editors' which stores the ObjectIds of all the users that have ever edited that word, so as to display a summary of the word on a user's profile.
        - Every word has a 'lastEditedBy' ObjectId of the last user to edit the word. This is stored as an ObjectId rather than a string of the user's username for the reasons mentioned above. (In the abscence of edits this is simply an empty string)
        - Every word has a 'lastEditedDate' entry that is simply a string of the date it was last edited on displayed on the word page. (In the abscence of edits this is simply an empty string)
        - Every word has two arrays connected to the 'rating' integer. These array entries are called 'liked' and 'disliked'. (If no rating action has been taken on a word these are merely empty arrays.)
        When a rating action such as liking or disliking a word has been taken by the user, that user's ObjectId gets added to, or removed from (as unliking and changing one's mind are also possible) the appropriate array. This system was implemented as an easy way to prevent any user from trying to 'double like' a word or manipulate the rating system in some way.
        - Every word has an 'isTagged' boolean that is true or false depending on the tagged status of a word. 
        - Every word has a 'tags' array. If untagged, this is merely an empty array. When a word has been tagged, the tag's ObjectId(s) is(are) added to the 'tags' array. While a tag is unlikely to change, this is still the most robust way to connect the two collections and ensures if a tag ever does change, it will change everywhere on the site. 

    2. Users
        - Users are an essential linchpin of any community-driven website, which is what this project eventually aims to be. 
        - Of course each user has it's own unique ObjectId.
        - Each user has a string entry entitled 'name', which is simply a string of their username.
        - Each user has a string entry entitled 'description', which begins empty, but can be edited in the edit_profile page.
        - Each user has a string entry entitled 'email', containing the email address the user provided upon registration. At the time of deployment, this is a somewhat redundant string, but when email verification is rolled out in the future it will become an essential aspect of the data structure. 
        - Each user has a string entry entitled 'dateOfBirth', At the time of deployment, this is also a somewhat redundant string, but when further account customization is rolled out in the future it will become an essential aspect of the data structure.
        - Each user has a string entry entitled 'dateJoined', which is displayed on each user's profile page.
        - Each user has two further string entries entitled 'city' & 'country'. These are displayed in tandem on every user's profile. 
        - Each user has a boolean entitled 'isAdmin', which, if true, will give the user extra permissions. i.e adding tags.
        - There are three final booleans that every user has: 'hasCity', 'hasCountry' and 'hasDescription'. These are used to decide what is shown to anyone viewing a user's profile.

    3. Tags
        - Tags are a great way to contextualise and categorize different words in a slang dictionary. 
        - Of course each tag has it's own unique ObjectId.
        - Each tag also has a 'name' entry, which is a string that contains the name of the tag.
        - Each tag also has the ObjectId of the user that created the tag.
        - And most importantly, each tag has a 'taggedWords' array, which contains the ObjectId of every word that has that tag. This allows the site to easily display all words that share a specific tag.

    - As shown above, great care was taken in the creation and maintenance of the of the data schema of the site. With every single collection being connected to others strictly by ObjectIds, and a robust and varied selection of data entries to each collection to ensure site functionality, but, also offer further developmental and analytical oppurtunites in the future. 

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MichaelCWalsh7/Yurt-Index)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. On the left-hand side of the 'Settings' page, second from bottom there is a tab titled 'Pages'.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site in the "GitHub Pages"
 section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make 
changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MichaelCWalsh7/Yurt-Index)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MichaelCWalsh7/Yurt-Index)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/MichaelCWalsh7/Yurt-Index
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/MichaelCWalsh7/Yurt-Index
> Cloning into `Yurt-Index-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here
](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)
 to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-  [Materialize](https://materializecss.com/): The Materialize framework definitely earns a credit in this README as more than just a basic framework. Their easy-to-use and style, responsive 'card' objects are a defining part of the project. It was also enjoyable to try a different framework to Bootstrap to compare the two.

-   [Luke Zhang](https://codepen.io/lukezhang/pen/JlImc): Big thanks Luke Zhang's great work on css tags, which was fundamental in my implementation of them in this project. It took some time just to style and recolur them so I can only imagine how many countless hours on the drawing board this CSS saved me.

-   [Ankit Chaudhary/Stack Overflow](https://stackoverflow.com/questions/28034638/hide-div-on-certain-pages-using-jquery): This answer from Ankit Chaudhary on a Stack Overflow question from quite some time ago was very helpful in the JS that was used to change the Return to Home button on the home page so it took the user back to the top.  

-   [Diego Leme](https://codepen.io/diegoleme/pen/surIK): I used this very tidy little piece of code as the basis of my own script, to ensure that both passwords and email fields has functional comparative confirmation.

-   [Red Eyed Coder Club](https://www.youtube.com/channel/UCh_LSaTv2GeZ3woJNTGihew): The error handler code that I used to route to the 404 page was partially inspired by [this Youtube tutorial video](https://www.youtube.com/watch?v=OczLouzgJSc).


### Content

-   All content was written by the developer.

### Media

-   All images and media for the site was created by the developer. 

### Inspirations 

-   Overall this Website had a couple of predominant inspirations 
    1. First of all, on a conceptual level, the two books of short stories published by RubberBandits member [Blindboy Boatclub](https://en.wikipedia.org/wiki/Blindboy_Boatclub).
    1. Secondly the [Urban Dictionary](https://www.urbandictionary.com/) and the [Dictionary.com](https://www.dictionary.com/e/slang/) slang archive were both used as inspirations, but also metrics on how modern, popular, slang dictionaries designed their sites.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

-   The Slack community for continued feedback.

-   Close friends along the way who helped test and give advice.