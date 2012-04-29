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

    +         concatenation                                  'abc' + 'def'                ## 'abcdef'
    *         repetition                                     'abc' * 2                    ## 'abcabc'
    [n]       slice                                          'abc'[1]                     ## 'b'
    [-n]      slice from end                                 'abc'[-1]                    ## 'c'
    [n:m]     range slice                                    'abc'[0:1]                   ## 'ab'
    in        membership                                     'a' in 'abc'                 ## True
    not in    not in membership                              'd' not in 'abc'             ## True
    r         raw string (esc chars are not interpreted)     r'abc\n'                     ## 'abc\n'


String Formatting Operator % (modulo)

    %         no conversion displays %                       'abc %'                      ## 'abc %'
    %c        character (accepts integer or character)       'abc %c' % 100               ## 'abc d'
    %d        signed decimal integer                         'abc %d' % -3                ## 'abc -3'
    %e        exponential notation (with lowercase 'e')      'abc %e' % -3                ## 'abc -3.000000e+00'
    %E        exponential notation (with uppercase 'E')      'abc %E' % -3                ## 'abc -3.000000E+00'
    %f        floating point real number                     'abc %f' % 1.23              ## 'abc 1.230000'
    %g        the shorter of %f and %e                       'abc %g' % 1.23              ## 'abc 1.23'
    %G        the shorter of %f and %E                       'abc %G' % 1.23              ## 'abc 1.23'
    %i        signed decimal integer                         'abc %i' % -3                ## 'abc -3'
    %o        octal integer                                  'abc %o' % 123               ## 'abc 173'
    %r        string conversion (using repr())               'abc %r' % 123               ## 'abc 123'
    %s        string conversion (using str())                'abc %s' % 'def'             ## 'abc def'
    %x        hexadecimal integer (lowercase letters)        'abc %x' % 123               ## 'abc 7b'
    %X        hexadecimal integer (lowercase letters)        'abc %X' % 123               ## 'abc 7B'
    %#        use alternate form                             'abc %#x' % 123              ## 'abc 0x7b'
    %n        pad from left with spaces                      'abc %3d' % 3                ## 'abc   3'
    %0        pad from left with zeros                       'abc %03d' % 3               ## 'abc 003'
    %-        left align                                     'abc %-5d' % 123             ## 'abc 123  '
    %+        display +/- sign                               'abc %+5d' % 123             ## 'abc  +123'
    %<SP>     display a space before a positive number       'abc % d' % 123              ## 'abc  123'
    %(var)    mapping variable (dictionary arguments)        'abc %(x)s' % {'x': 'def'}   ## 'abc def'
    %m.n      m is the minimum total width                   'abc %3.1f' % 12.345         ## 'abc 12.3'
              n no. of digits to display after decimal point

String methods:

    capitalize()                                             str.capitalize('abc')        ## 'Abc'
                                                             'abc'.capitalize()           ## 'Abc'
    center(width, fillchar)                                  'abc'.center('abc',5)        ## ' abc '
                                                             'abc'.center(5,'*')          ## '*abc*'
    count(sub, start, end)                                   'abc'.count('a')             ## 1
                                                             'abc'.count('a',1,2)         ## 0
    decode(encoding, errors)       see <encodings> below     'YWJj\n'.decode('base64')    ## 'abc'
    encode(encoding, errors)                                 'abc'.encode('base64')       ## 'YWJj\n'
    endswith(suffix, start, end)   suffix can be a tuple     'abc'.endswith('bc')         ## True
                                                             'abc'.endswith(('c','bc'))   ## True
                                                             'abc'.endswith('b',1,2)      ## True
    expandtabs(tabsize)            replace tabs with spaces  '\t'.expandtabs(1)           ## ' '
    find(sub, start, end)          returns first match pos   'abcc'.find('c')             ## 2
                                                             'abcc'.find('c',3)           ## 3
                                                             'abcc'.find('d')             ## -1
    format(args, kwargs)           preferred over % formats  '{0}{1}'.format('a','b')     ## 'abc'
                                                             '{}{}'.format('a','b')       ## 'abc'
    index(sub, start, end)         find + raises ValueError  'abcc'.index('c')            ## 2
                                                             'abcc'.index('c',3)          ## 3
                                                             'abcc'.index('d')            ## ValueError: substring not found
    isalnum()                      alphanumeric              'abc123'.isalnum()           ## True
    isalpha()                      alpahbetic                'abc'.isalpha()              ## True
    isdigit()                      numeric                   '123'.isdigit()              ## True
    islower()                      lower case                'abc'.islower()              ## True
    isspace()                      space(s)                  '  '.isspace()               ## True
    istitle()                      title case                'Abc'.istitle()              ## True
    isupper()                      upper case                'ABC'.isupper()              ## True
    join(iterable)                 string is separator       ','.join(['abc','def'])      ## 'abc,def'
    ljust(width, fillchar)         left justify              'abc'.ljust(5)               ## 'abc  '
                                                             'abc'.ljust(5,'*')           ## 'abc**'
    lower()                        lower case                'ABC'.lower()                ## 'abc'
    lstrip(chars)                  left strip in any order   'abcde'.lstrip('cba')        ## 'de'
    partition(sep)                 head, 1st sep, tail       'abbc'.partition('b')        ## ('a', 'b', 'bc')
                                                             'abbc'.partition('d')        ## ('abbc', '', '')
    replace(old, new, count)       replace old with new      'abdd'.replace('d','c')      ## 'abcc'
                                                             'abdd'.replace('d','c',1)    ## 'abcd'
    rfind(sub, start, end)         reverse find              'abcc'.rfind('c')            ## 3
                                                             'abcc'.rfind('c',0,3)        ## 2
                                                             'abcc'.rfind('d')            ## -1
    rindex(sub, start, end)        rfind + raises ValueError 'abcc'.rindex('c')           ## 3
                                                             'abcc'.rindex('c',0,3)       ## 2
                                                             'abcc'.rindex('d')           ## ValueError: substring not found
    rjust(width, fillchar)         right justify             'abc'.rjust(5)               ## '  abc'
                                                             'abc'.rjust(5,'*')           ## '**abc'
    rpartition(sep)                head, last sep, tail      'abbc'.rpartition('b')       ## ('ab', 'b', 'c')
                                                             'abbc'.rpartition('d')       ## ('', '', 'abbc')
    rsplit(sep, maxsplit)          reverse split             'a b c'.rsplit()             ## ['a', 'b', 'c']
                                                             'a b c'.rsplit(None, 1)      ## ['a b', 'c']
                                                             'a  b c'.rsplit()            ## ['a', 'b', 'c']
                                                             'abc'.rsplit('b')            ## ['a', 'c']
                                                             'abbc'.rsplit('b')           ## ['a', '', 'c']
                                                             'abbbc'.rsplit('b')          ## ['a', '', '', 'c']
                                                             'abbbc'.rsplit('b',1)        ## ['abb', 'c']
                                                             'abbc'.rsplit('bb')          ## ['a', 'c']
    rstrip(chars)                  right strip in any order  'abcde'.rstrip('dec')        ## 'ab'
    split(sep, maxsplit)           split on sep delimiter    'a b c'.split()              ## ['a', 'b', 'c']
                                                             'a b c'.split(None, 1)       ## ['a', 'b c']
                                                             'a  b c'.split()             ## ['a', 'b', 'c']
                                                             'abc'.split('b')             ## ['a', 'c']
                                                             'abbc'.split('b')            ## ['a', '', 'c']
                                                             'abbbc'.split('b')           ## ['a', '', '', 'c']
                                                             'abbbc'.split('b',1)         ## ['a', 'bbc']
                                                             'abbc'.split('bb')           ## ['a', 'c']
    splitlines(keepends)           split on line endings     'a\nbc'.splitlines()         ## ['a', 'bc']
                                                             'a\nbc'.splitlines(True)     ## ['a\n', 'bc']
    startswith(prefix, start, end) prefix can be a tuple     'abc'.startswith('ab')       ## True
                                                             'abc'.startswith(('a','ab')) ## True
                                                             'abc'.startswith('b',1,2)    ## True
    strip(chars)                   lead + trail in any order ' abc '.strip()              ## 'abc'
                                                             ' abc '.strip(None)          ## 'abc'
                                                             'abcde'.strip('edba')        ## 'c'
    swapcase()                     convert upper and lower   'aBc'.swapcase()             ## 'AbC'
    title()                        convert words             'abc'.title()                ## 'Abc'
                                                             'ab cd'.title()              ## 'Ab Cd'
                                                             'they\'re'.title()           ## "They'Re"
    translate(table, deletechars) map chars using 256-char   import string
                                  translation table          table = string.maketrans('abc','def')
                                                             'abc'.translate(table)       ## 'def'
                                                             'abc'.translate(table, 'a')  ## 'ef'
                                                             'abc'.translate(None)        ## 'abc'
                                                             'abc'.translate(None, 'a')   ## 'bc'
    upper()                       upper case                 'abc'.upper()                ## 'ABC'
    zfill(width)                  left zero fill             'abc'.zfill(5)               ## '00abc'

Unicode string methods:

    isnumeric()                   unicode strings only       u'123'.isnumeric()           ## True
    isdecimal()                   unicode strings only       u'123'.isdecimal()           ## True

Further info:

<code>String methods:&nbsp;&nbsp;&nbsp;&nbsp;</code> <http://docs.python.org/library/stdtypes.html#string-methods><br/>
<code>String encodings:&nbsp;&nbsp;</code> <http://docs.python.org/library/codecs.html#standard-encodings>

if statement
------------

    if expression:
       statement(s)
    elif expression:
       statement(s)
    else
       statement(s)

    if expression: statement

* uses indentation and spaces for grouping instead of {}
* : ends the expression
* no switch or case statements

