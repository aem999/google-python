google-python
=============
Python is a [dynamically typed](http://en.wikipedia.org/wiki/Type_system#Dynamic_typing) language, that offers a very readable syntax and is often used as a scripting language.
The code is interpretted at run-time which has the advantage of flexibility but the disadvantage that syntactically
incorrect code will only be flagged as an error when it is executed. 


Style Guide
-----------
http://www.python.org/dev/peps/pep-0008/


Indentation
-----------
Whitespace indentation in Python code affects its meaning. A logical block of statements such as the ones that make up a
function should all have the same indentation, set in from the indentation of their parent. If one of the lines in a
group has a different indentation, it is flagged as a syntax error.


Modules
-------
A *module* is a Python file. A Python module can be run directly:  
    
    python hello.py Bob
    
or it can be imported and used by some other module. When a Python file is run directly, the special variable "\_\_name\_\_"
is set to "\_\_main\_\_". Therefore, it's common to have the boilerplate:

    if __name__ == '__main__':
        main()
    
to call a main() function when the module is run directly, but not when the module is imported by some other module.


Module Arguments
----------------
The list `sys.argv` contains the command line arguments with `sys.argv[0]` being the program itself, `sys.argv[1]` the
first program argument, and so on.

Functions
---------
Example:  

    def repeat(s, exclaim):
        """Returns the string s repeated 3 times.
        If exclaim is true, add exclamation marks.
        """

        result = s * 3
        if exclaim:
            result = result + '!!!'
        return result
        
* "def" defines the function with its parameters within parentheses
* function code must be indented at the same level
* the first line of a function can be a "docstring" (documentation string) that describes what the function does (may span multiple lines)
* variables defined in the function are local to that function


At run time, functions must be defined by the execution of a "def" before they are called. 
It is typical to define a main() function towards the bottom of the file with the functions it calls above it.

    def main():
        print repeat('Yay', False)      ## YayYayYay
        print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!


