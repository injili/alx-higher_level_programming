# 0x12. JavaScript - Warm up
## Background Context
JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

1. Scripting (same as we did with Python)
2. Web front-end
For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

## Learning Objectives
- Why JavaScript programming is amazing.
- How to run a JavaScript script.
- How to create variables and constants.
- What are differences between var, const and let.
- What are all the data types available in JavaScript.
- How to use the if, if ... else statements.
- How to use comments.
- How to affect values to variables.
- How to use while and for loops.
- How to use break and continue statements.
- What is a function and how do you use functions.
- What does a function that does not use any return statement return.
- Scope of variables.
- What are the arithmetic operators and how to use them.
- How to manipulate dictionary.
- How to import a file.

### Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

### Install semi-standard
$ sudo npm install semistandard --global

[0. First constant, first print](0-javascript_is_amazing.js) - A script that prints "JavaScript is amazing".  
[1. 3 languages](1-multi_languages.js) - A script that prints 3 lines: “C is fun”, “Python is cool" and “JavaScript is amazing”.  
[2. Arguments](2-arguments.js) - A script that prints a message depending on the number of arguments passed: If no arguments are passed to the script, it prints “No argument”, If only one argument is passed to the script, it prints “Argument found” otherwise, the script prints “Arguments found”.  
[3. Value of my argument](3-value_argument.js) - A script that prints the first argument passed to it but if no arguments are passed to the script, it prints “No argument”.  
[4. Create a sentence](4-concat.js) - A script that prints two arguments passed to it, in the following format: “ is "by performing concatination.  
[5. An Integer](5-to_integer.js) - A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer but if the argument can’t be converted to an integer, print “Not a number”.  
[6. Loop to languages](6-multi_languages_loop.js) - A script that prints 3 lines: (like [1-multi_languages.js](1-multi_languages.js)) but by using an array of string and a loop.  
[7. I love C](7-multi_c.js) - A script that prints x times “C is fun” where x is the first argument of the script but if the first argument can’t be converted to an integer, print “Missing number of occurrences”.  
[8. Square](8-square.js) - A script that prints a square using the character 'x'. The first argument is the size of the square but if the first argument can’t be converted to an integer, print “Missing size”.  
[9. Add](9-add.js) - A script that prints the addition of 2 integers.  
[10. Factorial](10-factorial.js) - A script that computes and prints a factorial.  
[11. Second biggest!](11-second_biggest.js) - A script that searches the second biggest integer in the list of arguments.  
[12. Object](12-object.js) - A script to replace the value 12 with 89.  
[13. Add file](13-add.js) - A function that returns the addition of 2 integers.  
[14. Const or not const](100-let_me_const.js) - A file that modifies the value of myVar to 333.  
[15. Call me Moby](101-call_me_moby.js) - A function that executes x times a function.  
[16. Add me maybe](102-add_me_maybe.js) - A function that increments and calls a function.  
[17. Increment object](103-object_fct.js) - A  that increments the integer value.  

### Author
injili (nyarekigospel@gmail.com)
