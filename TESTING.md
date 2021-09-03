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
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    -   Results:
        - [Stylesheet](https://michaelcwalsh7.github.io/Milestone-Project-2/assets/images/readme-images/css-validation.png)
        - These results are in the form of a picture rather than the links above, as when the site is passed through the validator, it also validates the entire bootstrap library, which as of bootstrap 5, throws 17 errors and fails validation. 
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