## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) 
    -   Results:
        - [404](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2Fasldkfjsadhlgk)
        - [500](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2Fprofile%2F610eaf9bd2861806adshk)
        - [Add tag](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2Fadd_tag%2Ftestuser)
        - [All words](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2Fall_words)
        - [Display by letter](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2Fdisplay_by_letter%2FB) The letter 'b' was used as many words existed for this letter at time of writing.
        - [Display by tag](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2Fdisplay_by_tag%2F611fd74aff3d2e6eb99c27f9) The 'Culchie' tag was used for the same reasons as above.
        - [Edit profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2Fedit_profile%2Ftestuser)
        - [Edit word](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fedit_word%2F611f9bcbc2e7d2c090a747ef)
        - [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyurt-index.herokuapp.com%2F)
        - [Log in](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Flog_in)
        - [New word](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fnew_word)
        - [Profile](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fprofile%2F610eaf9bd2861806a173811b)
        - [Register](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fregister)
        - [Search results](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fsearch)
        - [Word page](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fwords%2F611feae721fd807e62fe715b)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    -   Results:
        - [Stylesheet](https://yurt-index.herokuapp.com/static/images/readme/css-validation.png)
        - These results are in the form of a picture rather than the links above, as when the site is passed through the validator, it also validates the entire Materialize library, which as of Materialize 1.0.0, throws an error and fails validation. 
        - If needed, the CSS that I've written for the project can be validated via file upload, or direct input [here.](https://jigsaw.w3.org/css-validator/)
-   [JSHint Linter](https://jshint.com/)
    - Results:
        - [script.js](https://yurt-index.herokuapp.com/static/images/readme/js-script.png)
        - [sendEmail.js](https://yurt-index.herokuapp.com/static/images/readme/js-password.png)
-   [PEP8 online check](http://pep8online.com/)
    -   Results
        - [app.py](https://yurt-index.herokuapp.com/static/images/readme/pep8-check.png)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    - The Google dev tool Lighthouse was used to ensure that the project followed best practices.
    - Results
        - [Click here to see an image of the results](https://yurt-index.herokuapp.com/static/images/readme/lighthouse-results.png)
            - A brief aside; the reason the the SEO score is so low, is due to the way that Materialize handles tooltipping. It uses anchor tags that don't contain hrefs for whatever annoying reason, and so Lighthouse incorrectly interprets it as a non-crawlable link.  

### Testing User Stories from User Experience (UX) Section
-   #### First Time Visitor Goals
    1.  As a First Time Visitor, I want to easily understand the main purpose of the site and find definitions of words.
        - Upon reaching the Home Page the user is immediately displayed with a short paragraph describing the site's purpose
        - Also on the home page are some featured words, (the top four that have the highest rating) and their summaries, including links to the word pages themselves.
        - Another thing that user is greeted with is a large, striking search bar on the top of the page, in it's traditional locaiton under the navbar. 
        - The final point here is that there is also a metadescription that will inform any users of the site's purpose if they enter from Google, or if the site is linked in other applications. 
    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        - As mentioned above, a searchbar dominates the top of the page and many other relevant pages that it is appropriate for.
        - Users can see on the navbar at the top of the screen there is a 'categories' dropdown tab, which allows users to look at all words, find words by letter, or find words via their applicable tags.
        - Also on the bottom of every page, there is a 'return to home button' to stop the user getting "trapped" and having to the use the back buttons. It also ensures there is always a call-to-action on the page. On the home page itself, this button changes to a 'back to top' button
        -  Also, on the footer, there is a back to top button on the bottom right, saving the user from having to scroll back up to the top of the page using their scroll wheel or use the vertical scrollbar.
        - On many, many pages, short word cards, herein referred to as 'word summaries', have been employed. This includes on user profile pages if the user has ever created or edited a word, ensuring there is almost always a variety of words for the user to click on if interested.
        - While the 404 and 500 error pages of course have the 'return to home button' located on every page on the site, they have an additional link to the 'all words' page of the site, to lessen the dampening effect of being taken to an error page. 
    3. As a First Time Visitor, I want to easily be able to search or find a word that I'm interested in.
        - There is a search bar that dominates the screen on many pages.
        - If a user does not know exactly how to spell a word, they can find it by browsing through the 3 differing types of list pages: the first being a list of all the words on the page, the second being a list of each word on the site by it's initial letter, or if the user only knows the origin of the word or has a vague idea that does not include the first letter, they can find it through the website's tag system.
        - Every word that has been tagged, has it's tags displayed very visibly at the bottom of it's word page. These tags can themselves be clicked to be taken to a list of words that share this tag. 
    4. As a First Time Visitor, I want to learn extra information on words that I'm interested in, for instance how to spell or use a slang word.
        - While each word summary merely provides the primary definition and a link to the word page, the word page itself can contain a myriad of information about each word. 
        - Data systems are in place to provide information like multiple spellings, definitions and examples if there are any, along with the tag system which helps further categorize words. 
        - While the root spelling and definition are the bare minimum of the UX expectations, the site also provides space for alternative spellings and multiple uses in a clean and non-cluttered way.
        - Another feature in play is that when looking at the examples of a word on the word page, whenever the word appears in the example it will be underlined, so the user can more clearly see it in use in wordier examples.

-   #### Returning Visitor Goals
    1. As a Returning Visitor, I want to know what words are well-liked by the community and which have more dubious entries.
        - A rating system has been implemented into the date structure and design of the website, where registered users may like or dislike a word. (A quick aside, the rating system is tied to the sites delete protection, in that liked words cannot be deleted.)
        - Words that very well-liked by the website's community will become 'star words'. These words will gain a yellow star in the top right corner of both their page and word summary, which, when hovered over, will inform the user that this is a well-liked word by the community. This is now a very prominent feature in online dictionaries and encyclopedias.
        - Extremely well-liked words may appear on the 'home page' as part of the 'featured words' section. This is a fluid section of the site, and the top 4 words will always be the ones shown.
    2. As a Returning Visitor, I want to create an account so I can show my appreciation or discontent with entries on the site.
        - Following  the design choices of both [Urban Dictionary](https://www.urbandictionary.com/) and [Dictionary.com](https://www.dictionary.com/e/slang/), the user log in and registration option are located in a navbar dropdown button, represented by the traditional circular user icon.
        - There are other calls-to-action which call for new users to register an account. Firstly on the 'home page' in the introductory paragraph there is a call-to-action link to the user registration page. And perhaps most prominently, at the bottom of every word page, the user is provided with a link that to register or log in if they are not already. 
        - Once logged in, the like and dislike buttons on every word are clearly visible at the bottom of every word page.
        - Words that have liked/disliked erroneously, or any words that the user has changed their mind about, can be unliked. Click the the like/dislike button again if one has already clicked it, works exactly as expected, incrementing or decrementing the rating and removing the user from the word's like history and vice-versa. This format of liking objects is a mainstay of modern websites, not only used on contemporary dictionaries but also social media sites like Facebook, Youtube etc.
    3. As a Returning Visitor, I want to edit errors or add definitions/alternative spelling or examples to words I know.
        - As mentioned in the above section there is a registration call-to-action at the bottom of every word page, once logged in, a large edit button will appear in the bottom right of every word page. 
        - Here is one area I feel, where the Yurt Index outdoes various other slang dictionary contemporaries such as the inspirations ([Urban Dictionary](https://www.urbandictionary.com/) and [Dictionary.com](https://www.dictionary.com/e/slang/)) mentioned above.
        - The data and design structures are in place in such a way that a user can add a myriad of alternative spellings, definitions or examples to any word that they know. Great care has been taken to present these alternative options in a clean, non-cluttered way. While browsing other slang dictionaries, I found the [Urban Dictionary](https://www.urbandictionary.com/) format of alternative meanings and examples to be particularly dull from a UX standpoint. Alternative definitions are merely tacked on, to a numbered list, and alternative examples are tacked on to an unnumbered list. Without clear division, it is just a black wall of text on a white background, for example here with the word [MILF](https://www.urbandictionary.com/define.php?term=milf) (NSFW content warning!!)
        - The alternative spellings is a feature that one would think to be commonplace amonst contemporary slang dictionaries, surprisingly it is not. With both of the above examples necessitating a new entry for different spellings. 
        - On the Yurt Index the Alternative spellings section is clearly and cleanly marker, with a lower opacity common amongst normal language dictionaries, so as not to be too distracting. 
    4. As a Returning Visitor, I want to explore the profiles of other users who have created/edited entries on the site.
        - Similar to my contempoaries in slang dictionaries, a user profile is a feature of the website. Towards the bottom of each word page is a link to the profile page of the user who created each word.
        - There is also a link to the last user to edit the word, if applicable.
        - These profiles contain some basic information about the user, and two tabs at the bottom of this page that display the words that the user has created, and the words that the user has edited.

-   #### Frequent User Goals
    1. As a Frequent User, I want to create my own entries on the site for words that are not yet present.
        - Once a user has logged in, an option will appear in the navbar to add a word to the dictionary.
        - There is also a call-to-action on the home page, that takes the user to a new word page if they are logged in, or if not, it takes them to the the log in page. 
    2. As a Frequent User, I want customize my profile so other users can get an impression of my online persona.
        - Every user can edit information on their profile, Allowing them to change the generalized location that they've provided the site with, or add/edit a personal description about themselves.
        - Every word that a user creates or edits, will be added to the 'Words Created' or the 'Words Edited' tabs respectively. 
    3. As a Frequent User, I want to browse through various categories of entries on the site. 
        - There are several methods of categorization or ways to browse through words on the site. 
        - First and foremost is the 'all words' page which simply presents the user with a list of all words which they can sort by rating, or alphabetically.
        - Also if the user so chooses there is also a 'display by letter' page available. This page is linked both in the navbar and also in the top left of the 'all words' page.
        - There is also a tag system that has been implemented into the website. Admin user's can create various tags that further describe and contextualise words on the site. For example "Limerick", "Dublin" & "Townie" all describe the location of a word or if it comes from a rural or urban area.
        - Tags are displayed in a traditional and expectant manner at the bottom fo each word page. Clicking on any tag will take the user to a list of words that have been tagged with the selected tag.
        - There is also an option to view words by tag in the navbar. 
    4. As a Frequent User/Admin, I want to be able to create new tags for entries to be categorized by.
        - Admin users, who would be extremely familiar with the site will notice an 'add tag' optin in the navbar.
        - Adding tags is very simple, and admin users can add up to five tags at once if they so choose. 

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop (on various screen sizes), Laptop, iPad & other various types of tablets, iPhones 5, 6, 7 & X as well as other mobile phone types 
    including, but not limited to, Redmi, Huawei, Samsung and Sony.
-   [Included here is a link to the projects Responsinator home page](http://www.responsinator.com/?url=https%3A%2F%2Fyurt-index.herokuapp.com%2F)
-   [And here's another one on a word page](http://www.responsinator.com/?url=https%3A%2F%2Fyurt-index.herokuapp.com%2Fwords%2F611feae721fd807e62fe715b)
-   A large amount of testing was done to ensure that all aspects of the site were running correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.   

### Known Bugs

- **Resizing in Dev Tools Issue**
    - One of the issues that I came across in the development process was a very odd bug that i was only able to replicate in google dev tools
    - [Click here to see an image of the bug](https://yurt-index.herokuapp.com/static/images/readme/issues/odd-resizing-issue.png)
    - Sometimes, when you made the site smaller, on Google dev tools, the site would not fill the screen properly, instead only filling two thirds of the screen in width.
    - I could not replicate this issue outside of dev tools, and friends who tested the website who do not use dev tools did not report the issue.
    - One friend who is also learning to code and DID use Google dev tools said he could replicate it as well.
    - I put the site through the Unicorn Revealer add-on which highlights the size of objects on the page and found that there were in fact no objects pushing the website to the left.
    - [Here is an image of this process](https://yurt-index.herokuapp.com/static/images/readme/issues/odd-resizing-issue-unicorn.png)
    - I thought perhaps it was an issue I could replicate using the Firefox version of dev tools, but after trying exhaustively, I found that I could not.
    - While I use Google's dev tools frequently, I am admittedly unfamiliar with it's intricacies. A comprehensive understanding of dev tools interactions with website resizing feels far beyond the scope of this project, and as it does not inhibit normal UI I decided to merely include it here.

- **Firefox Search Button Displacement Issue**
    - I was disappointed to receive a visit from my old nemesis, Firefox compatibility issues in this project.
    - [Here's an image of the issue](https://yurt-index.herokuapp.com/static/images/readme/issues/search-button-issue.png)
    - This bug is only replicable in Firefox. I couldn't replicate in using Google Chrome, Safari, Opera, Microsoft Edge or the dreaded Internet Explorer.
    - So what happens, as shown in the image above, is that in Firefox, the search button for some reason snaps to below the search bar, rather than to the right of it, like in every single other browser.
    - Interestingly, the button seems to have a different look overall in Firefox, almost as if some style elements aren't being applied, or are for some reason being overridden. I tried tinkering around with the settings, but everything i did either did not fix the issue or created a myriad of other issues on other browsers.
    - Further efforts to fix this had to be cut short, due to time constraints.

### Issues Along The Way

- **Colour Contrast Problems**
    1. [Click here to see an image of the issue](https://yurt-index.herokuapp.com/static/images/readme/issues/colour-contrast-issue-1.png)
    2. An inordinate amount of time was spent fine tuning the colour contrasting of the website. Initially, it wasn't something I kept in mind. It was my first time using Materialize, and mistakenly assumed that many of the alternative colour options provided on their werbsite would contrast well with the default white that they provide on their navbar. 
    3. Unfortunately this was not the case, and when I began implementing the colour scheme for the website, the green white and gold/orange of the Irish flag, I soon realized that there were almost no colours I could use to properly contrast with the green that I had chosen. 
    4. It was unfortunately, a very middle of the road colour in terms of lightness, so colours that were very light or very dark did not contrast heavily enough, and many of the colours of the site were changed as a result.

- **Display by Letters Issues**
    1. [Click here to see an image of the issue](https://yurt-index.herokuapp.com/static/images/readme/issues/display-by-letters-1.png)
    2. As it was my firs time using the Flask framework there were some teething issues when it came to formatting and routing.
    3. After writing the html and python needed to view all of the words that began with a particular letter, I was greeted with the error above.
    4. What I didn't know, but was alerted to thanks to some help from tutor support, was that any variable you pass through the decorator must also be passed through the function and hence through the Jinja template anchor.
    5. [Click here to see an image of the solution](https://yurt-index.herokuapp.com/static/images/readme/issues/display-by-letters-2.png)

- **Edit Profile Page Not Loading**
    1. [Click here to see a before and after of the code for this problem](https://yurt-index.herokuapp.com/static/images/readme/issues/edit-profile-not-loading.png)
    2. Another thing I didn't understand about Flask, or perhaps I at one stage did but had forgotten, is that any code written after the `if __name__ == "__main__":` would not be rendered to the site. 

- **Prevent Duplication Problems**
    1. [Initially, I wrote some JavaScript that looked like this image which disabled the like buttons on click.](https://yurt-index.herokuapp.com/static/images/readme/issues/prevent-duplication-bug-1.png)
    2. [However, experienced JS users should be able to take one look at my html in this image and spot the problem.](https://yurt-index.herokuapp.com/static/images/readme/issues/prevent-duplication-bug-2.png). I'm trying to use the disabled property on an anchor tag, which it cannot be applied to. 
    3. [I thought that the solution had come to me here in this image.](https://yurt-index.herokuapp.com/static/images/readme/issues/prevent-duplication-bug-3.png) But all this ended up doing was not activating the action at all, changing the rating option into essentially a "back to top" button.
    4. Finally i realized that I could easily and seamlessly prevent user liking a word multiple times by simply checking if they were in the like user array before adding them.

### [Click here to return to the README section.](https://github.com/MichaelCWalsh7/Yurt-Index/blob/main/README.md)