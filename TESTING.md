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
        - [Searh results](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fsearch)
        - [Word page](https://validator.w3.org/nu/?doc=http%3A%2F%2Fyurt-index.herokuapp.com%2Fwords%2F611feae721fd807e62fe715b)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    -   Results:
        - [Stylesheet](https://yurt-index.herokuapp.com/static/images/readme/css-validation.png)
        - These results are in the form of a picture rather than the links above, as when the site is passed through the validator, it also validates the entire Materialize library, which as of Materialize 1.0.0, throws an error and fails validation. 
        - If needed, the CSS that I've written for the project can be validated via file upload, or direct input [here.](https://jigsaw.w3.org/css-validator/)
-   [JSHint Linter](https://jshint.com/)
    - Results:
        - [script.js](https://michaelcwalsh7.github.io/Milestone-Project-2/assets/images/readme-images/testing/linter-results.png)
            - Here the linter describes a warning, where something would be "better written in dot notation". However, this is erroneous, writing this in dot notation would have negative consequences on the functionality of the code.
        - [sendEmail.js](https://michaelcwalsh7.github.io/Milestone-Project-2/assets/images/readme-images/testing/emailjs-linter.png)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    - The Google dev tool Lighthouse was used to ensure that the project followed best practices.
    - Results
        - [Click here to see an image of the results](https://michaelcwalsh7.github.io/Milestone-Project-2/assets/images/readme-images/lighthouse-test.png)

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
        - There is a search bar that dominates the screen  on many pages.
        - If a user does not know exactly how to spell a word, they can find it by browsing through the 3 differing types of list pages: the first being a list of all the words on the page, the second being a list of each word on the site by it's initial letter, or if the user only knows the origin of the word or has a vague idea that does not include the first letter, they can find it through the website's tag system.
        - Every word that has been tagged, has it's tags displayed very visibly at the bottom of it's word page. These tags can themselves be clicked to be taken to a list of words that share this tag. 
    4. As a First Time Visitor, I want to learn extra information on words that I'm interested in, for instance how to spell or use a slang word.
        - While each word summary merely provides the primary definition and a link to the word page, the word page itself can contain a myriad of information about each word. 
        - Data systems are in place to provide information like multiple spellings, defnitions and examples if there are any, along with the tag system which helps further categorize words. 
        - While the root spelling and definition are the bare minunum of the UX expectations, the site also provides space for alternative spellings and multiple uses in a clean and non-cluttered way.

-   #### Returning Visitor Goals
    1. As a Returning Visitor, I want to know what words are well-liked by the community and which have more dubious entries.
        - A rating system has been implemented into the date structure and design of the website, where registered users may like or dislike a word. (A quick aside, the rating system is tied to the sites delete protection, in that liked words cannot be deleted.)
        - Words that very well-liked by the website's community will become 'star words'. These words will gain a yellow star in the top right corner of both their page and word summary, which, when overed hovered over, will inform the user that this is a well-liked word by the community. This is now a very prominent feature in online dictionaries and encyclopedias.
        - Extremely well-liked words may appear on the 'home page' as part of the 'featured words' section. This is a fluid section of the site, and the top 4 words will always be the ones shown.
    2. As a Returning Visitor, I want to create an account so I can show my appreciation or discontent with entries on the site.
        

    