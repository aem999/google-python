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
Strings are immutable and can be created by enclosing characters in either single, double or triple quotes. A string literal can span multiple lines, but there must be a backslash \ at the end of each line to escape the newline unless using tripe quotes.

Python has a built-in string class named "str" (do not use the older "string" module) which returns a printable string representation of an object.  

String Operators:

    'abc' + 'def'               ## 'abcdef'    concatenation
    'abc' * 2                   ## 'abcabc'    repetition
    'abc'[1]                    ## 'b'         slice
    'abc'[-1]                   ## 'c'         slice from end
    'abc'[0:1]                  ## 'ab'        range slice
    'a' in 'abc'                ## True        membership
    'd' not in 'abc'            ## 1           not in membership
    r'abc\n'                    ## 'abc\n'     raw string (escape characters are not interpreted)


String Formatting Operator % (modulo)

    'abc %'                     ## 'abc %'              %  no conversion displays %
    'abc %c' % 100              ## 'abc d'              %c character (accepts integer or character)
    'abc %d' % -3               ## 'abc -3'             %d signed decimal integer
    'abc %e' % -3               ## 'abc -3.000000e+00'  %e exponential notation (with lowercase 'e')
    'abc %E' % -3               ## 'abc -3.000000E+00'  %E exponential notation (with uppercase 'E')
    'abc %f' % 1.23             ## 'abc 1.230000'       %f floating point real number
    'abc %g' % 1.23             ## 'abc 1.23'           %g the shorter of %f and %e
    'abc %G' % 1.23             ## 'abc 1.23'           %G the shorter of %f and %E
    'abc %i' % -3               ## 'abc -3'             %i signed decimal integer
    'abc %o' % 123              ## 'abc 173'            %o octal integer
    'abc %r' % 123              ## 'abc 123'            %r string conversion (using repr())
    'abc %s' % 'def'            ## 'abc def'            %s string conversion (using str())
    'abc %x' % 123              ## 'abc 7b'             %x hexadecimal integer (lowercase letters)
    'abc %X' % 123              ## 'abc 7B'             %X hexadecimal integer (lowercase letters)
    'abc %#x' % 123             ## 'abc 0x7b'           %# use alternate form
    'abc %3d' % 3               ## 'abc   3'            %n pad from left with spaces 
    'abc %03d' % 3              ## 'abc 003'            %0 pad from left with zeros
    'abc %-5d' % 123            ## 'abc 123  '          %- left align
    'abc %+5d' % 123            ## 'abc  +123'          %+ display +/- sign
    'abc % d' % 123             ## 'abc  123'           %<SP> display a space before a positive number
    'abc %(x)s' % {'x': 'def'}  ## 'abc def'            %(var) mapping variable (dictionary arguments)
    'abc %3.1f' % 12.345        ## 'abc 12.3'           %m.n m is the minimum total width
                                                             n is the no. of digits to display after the decimal point

String methods:

    str.capitalize('abc')       ## 'Abc'                capitalize()
    'abc'.capitalize()          ## 'Abc'
    'abc'.center('abc',5)       ## ' abc '              center(width, fillchar)
    'abc'.center(5,'*')         ## '*abc*'
    'abc'.count('a')            ## 1                    count(sub, start, end)
    'abc'.count('a',1,2)        ## 0
    'YWJj\n'.decode('base64')   ## 'abc'                decode(encoding, errors)
    'abc'.encode('base64')      ## 'YWJj\n'             encode(encoding, errors)
    'abc'.endswith('bc')        ## True                 endswith(suffix, start, end)
    'abc'.endswith('b',1,2)     ## True
    '\t'.expandtabs(1)          ## ' '                  expandtabs(tabsize)
    'abcc'.find('c')            ## 2                    find(sub, start, end)
    'abcc'.find('c',3)          ## 3
    'abcd'.find('e')            ## -1
    '{0}{1}'.format('a', 'b')   ## 'abc'                format(args, kwargs)
    '{}{}'.format('a', 'b')     ## 'abc'
    'abcc'.index('c')           ## 2                    index(sub, start, end)                   
    'abcc'.index('c',3)         ## 3
    'abc123'.isalnum()          ## True                 isalnum()
    'abc-123'.isalnum()         ## False
    'abc'.isalpha()             ## True                 isalpha()
    '123'.isdigit()             ## True                 isdigit()
    'abc'.islower()             ## True                 islower()
    '  '.isspace()              ## True                 isspace()
    'Abc'.istitle()             ## True                 istitle()
    'ABC'.isupper()             ## True                 isupper()
    ','.join(['abc','def'])     ## 'abc,def'            join(iterable)

Further detail for the string methods can be found at http://docs.python.org/library/stdtypes.html#string-methods    
    