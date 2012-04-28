google-python
=============
Python is a [dynamically typed](http://en.wikipedia.org/wiki/Type_system#Dynamic_typing) language, that offers a very readable syntax and is often used as a scripting language. The code is interpreted at run-time which has the advantage of flexibility but the disadvantage that syntactically incorrect code will only be flagged as an error when it is executed. 


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
    
or it can be imported and used by some other module. When a Python file is run directly, the special variable "\_\_name\_\_" is set to "\_\_main\_\_". Therefore, it's common to have the boilerplate:

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


At run time, functions must be defined by the execution of a "def" before they are called. It is typical to define a main() function towards the bottom of the file with the functions it calls above it.

    def main():
        print repeat('Yay', False)      ## YayYayYay
        print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!


Imports
-------
Modules may import other modules to access their features. With the statement "import sys" you can import the sys module and access its definitions by their fully-qualified name, e.g. sys.exit().

    import sys

    # Now can refer to sys.xxx facilities
    sys.exit(0)

There is another form of the import statement that makes features in another module available by their short names:

    from sys import exit
    
    # Now can call sys.exit using its short name
    exit(0)
    
However, this form is not recommended because it makes it more difficult to determine where a function or attribute came from.


Python Standard Library
-----------------------
There are many modules and packages which are bundled with a standard installation of the Python interpreter, so you don't have do anything extra to use them. These are collectively known as the "Python Standard Library." Commonly used modules/packages include:

    sys  -- access to exit(), argv, stdin, stdout, ...
    re   -- regular expressions
    os   -- operating system interface, file system

Documentation of all the Standard Library modules and packages can be found at http://docs.python.org/library.


help() and dir()
----------------
Inside the Python interpreter, the help() function pulls up documentation strings for various modules, functions, and
methods:

    help(len)         -- docs for the built in len function
    help(sys)         -- overview docs for the sys module (must do an "import sys" first)
    dir(sys)          -- dir() is like help() but just gives a quick list of the defined symbols
    help(sys.exit)    -- docs for the exit() function inside of sys
    help('xyz'.split) -- using an example of the sort of call you mean, here meaning the split() method on strings
    help(list)        -- docs for the built in "list" module
    help(list.append) -- docs for the append() function in the list module
    

Strings
-------
Strings are immutable and acan be created by enclosing characters in quotes (single, double or triple), either single quotes or double quotes.  These string literals are normally enclosed by single quotes but double quotes can also be used. A string literal can span multiple lines, but there must be a backslash \ at the end of each line to escape the newline. String literals inside triple quotes, """" or ''', can contain multiple lines of text.

Python has a built-in string class named "str" (do not use the older "string" module).

The full list of string methods can be found at http://docs.python.org/library/stdtypes.html#string-methods  
  
Examples:

    hello[0]                    ## 'h'
    'h' + 'i'                   ## 'hi'
    str(3.14)                   ## '3.14'
    r'this \n that'             ## 'this \n that'
    str.capitalize('abc')       ## 'Abc'
    'abc'.capitalize()          ## 'Abc'
    'abc'.center('abc',5)       ## ' abc '
    'abc'.center(5,'*')         ## '*abc*'
    'abc'.count('a')            ## 1
    'abc'.count('a',1,2)        ## 0
    'abc'.encode('base64')      ## 'YWJj\n'
    'YWJj\n'.decode('base64')   ## 'abc'
    
    
    