google-python
=============
Python is a [dynamically typed](http://en.wikipedia.org/wiki/Type_system#Dynamic_typing) language, that offers a very
readable syntax and is often used as a scripting language. The code is interpreted at run-time which has the advantage
of flexibility but the disadvantage that syntactically incorrect code will only be flagged as an error when it is executed.


Style Guide
-----------
http://www.python.org/dev/peps/pep-0008/


Indentation
-----------
Whitespace indentation in Python code affects its meaning. A logical block of statements such as the ones that make up a
function should all have the same indentation, set in from the indentation of their parent. If one of the lines in a
group has a different indentation, it is flagged as a syntax error.


Underscores
-----------
The following conventions for leading/trailing underscores are used:
    
    single leading underscore	e.g. _foo		weak 'internal' indicator. These objects are not imported by 'import' statements
    single trailing underscore	e.g. class_		convention to avoid conflict with a Python keyword
    double leading underscore	e.g. __foo		invokes name mangling to prevent object being overridden by subclass e.g. _MyClass__foo
	double leading/trailing		e.g. __init__	Python reserved attributes. Never create new ones, only use as documented
    							
    

Modules
-------
A *module* is a Python file. A Python module can be run directly:

    python hello.py Bob

or it can be imported and used by some other module. When a Python file is run directly, the special variable
"\_\_name\_\_" is set to "\_\_main\_\_". Therefore, it's common to have the boilerplate:

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
* the first line of a function can be a "docstring" (documentation string) that describes what the function does (may
span multiple lines)
* variables defined in the function are local to that function


At run time, functions must be defined by the execution of a "def" before they are called. It is typical to define a
main() function towards the bottom of the file with the functions it calls above it.

    def main():
        print repeat('Yay', False)      ## YayYayYay
        print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!


Imports
-------
Modules may import other modules to access their features. With the statement "import sys" you can import the sys module
and access its definitions by their fully-qualified name, e.g. sys.exit().

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


Built-in Data Types
-------------------

    None           There is a single object with this value and it is accessed through the built-in name None.  It is
                   used to signify the absence of a value in many situations, e.g. it is returned from functions that
                   don’t explicitly return anything. Its truth value is false.

    NotImplemented There is a single object with this value and it is accessed through the built-in name NotImplemented.
                   Numeric methods and rich comparison methods may return this value if they do not implement the
                   operation for the operands provided. The interpreter will then try the reflected operation, or some
                   other fallback, depending on the operator. Its truth value is true.

    Ellipsis       There is a single object with this value and it is accessed through the built-in name Ellipsis. It is
                   used to indicate the presence of the ... syntax in a slice. Its truth value is true.

Numbers:

    Integral       Plain Integers - numbers in the range -2147483648 through 2147483647. The range may be larger on
                                    machines with a larger natural word size, but not smaller. When the result of an
                                    operation would fall outside this range, the result is normally returned as a long
                                    integer but in some cases, the exception OverflowError is raised instead.

                   Long Integers  - numbers with an unlimited range, subject to available (virtual) memory only.
                   Booleans       - 0 and 1 representing the truth values "False" and "True" respectively. When
                                    converted to a string, the strings "False" or "True" are returned.

    Real (float)   Machine-level double precision floating point numbers. The accepted range and handling of overflow
                   depends the underlying machine architecture (and C or Java implementation).

    Complex        Machine-level double precision floating point numbers. The real and imaginary parts of a complex
                   number z can be retrieved through the read-only attributes z.real and z.imag. The accepted range and
                   handling of overflow depends the underlying machine architecture (and C or Java implementation).

Set types:

These are unordered, finite sets of unique, immutable objects. As such, they cannot be indexed by any subscript.
However, they can be iterated over, and the built-in function len() returns the number of items in a set. Common uses
for sets are fast membership testing, removing duplicates from a sequence, and computing mathematical operations such as
intersection, union, difference, and symmetric difference.

Note that if two numbers compare equal (e.g. 1 and 1.0), only one of them can be contained in a set. There are currently
two intrinsic set types:

    Sets           A mutable set created by the built-in set() constructor and can be modified afterwards by several
                   methods, such as add().

    Frozen sets    An immutable set created by the built-in frozenset() constructor. As a frozenset is immutable and
                   hashable, it can be used again as an element of another set, or as a dictionary key.

Mappings:

These are finite sets of objects indexed by arbitrary index sets. The subscript notation a[k] selects the item indexed
by k from the mapping a. The built-in function len() returns the number of items in a mapping. There is currently a
single intrinsic mapping type:

    Dictionaries   Finite sets of mutable objects indexed by nearly arbitrary values. The only types of values not
                   acceptable as keys are values containing lists or dictionaries or other mutable types that are
                   compared by value rather than by object identity. This is because the efficient implementation of
                   dictionaries requires a key’s hash value to remain constant. If two numbers compare equal (e.g. 1 and
                   1.0) then they can be used interchangeably to index the same dictionary entry.

The extension modules *dbm*, *gdbm*, and *bsddb* provide additional examples of mapping types.

Sequence Types:

Sequence types are ordered sets indexed by from 0 to n-1 and are distinguished by their mutability.

Immutable sequences:

    Strings     Contain a sequence of characters, which are represented by strings of one item as there is no separate
                character type. Characters represent at least 8-bit bytes. The built-in functions chr() and ord()
                convert between characters and non-negative integers representing the byte values. Bytes with the values
                0-127 usually represent the corresponding ASCII values, but the interpretation of values is up to the
                program. The string data type is also used to represent arrays of bytes, e.g. to hold data read from a
                file.

    Unicode     Contains a sequence of Unicode objects of one item holding either a 16-bit or 32-bit value (the maximum
                value is given in sys.maxunicode, and depends on how Python is configured at compile time). Surrogate
                pairs may be present in the Unicode object, and will be reported as two separate items.

    Tuples      Contain a comma-separated lists of expressions surrounded by parenthethis. A tuple of one item is known
                as a 'singleton'. An empty tuple can be formed by an empty pair of parentheses.

Mutable sequences:

    Lists       Contain a sequence of comma-separated list of expressions surrounded by square brackets.

    Byte Arrays Contain a sequence of integers in the range 0 to 256 and are created by the built-in bytearray()
                constructor. They provide the same interface and functionality as immutable bytes objects except that
                they are mutable and hence unhashable.

Note - the extension module *array* provides an additional mutable sequence type.


Strings
-------
Strings are immutable and can be created by enclosing characters in either single, double or triple quotes. A string
literal can span multiple lines, but there must be a backslash \ at the end of each line to escape the newline unless
using tripe quotes.

Python has a built-in string *class* named "str" (do not use the older "string" *module*) which returns a printable
string representation of an object.

String Operators:

    +         concatenation                                  'abc' + 'def'                ## 'abcdef'
    *         repetition                                     'abc' * 2                    ## 'abcabc'
    [n]       slice                                          'abc'[1]                     ## 'b'
    [-n]      slice from end                                 'abc'[-1]                    ## 'c'
    [n:m]     range slice                                    'abc'[0:1]                   ## 'ab'
    in        membership                                     'a' in 'abc'                 ## True
    not in    not in membership                              'd' not in 'abc'             ## True
    for in    iteration                                      for x in 'abc': print x,     ## a b c
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
    center(width, fillchar)                                  'abc'.center(5)              ## ' abc '
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
    format(args, kwargs)           preferred over % formats  '{0}{1}'.format('a','b','c') ## 'ab'
                                                             '{}{}'.format('a','b','c')   ## 'ab'
    index(sub, start, end)         find + raises ValueError  'abcc'.index('c')            ## 2
                                                             'abcc'.index('c',3)          ## 3
                                                             'abcc'.index('d')            ## ValueError: substring not found
    isalnum()                      alphanumeric              'abc123'.isalnum()           ## True
    isalpha()                      alphabetic                'abc'.isalpha()              ## True
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


Lists
-----
Lists are mutable and consist of a comma delimited list of items surrounded by square brackets. The items can be of
different types.

List Operators:

    +                       concatenation                           [1,2,3] + [4,5,6]                  ## ['a', 'b', 'c', 'd', 'e', 'f']
    *                       repetition                              [1,2,3] * 2                        ## [1, 2, 3, 1, 2, 3]
    [n]                     slice                                   [1,2,3][0]                         ## 1
    [-n]                    slice from end                          [1,2,3][-1]                        ## 3
    [n:m]                   range slice                             [1,2,3][1:3]                       ## [2, 3]
    in                      membership                              2 in [1,2,3]                       ## True
    not in                  not in membership                       2 not in [1,2,3]                   ## False
    for in                  iteration                               for x in [1, 2, 3]: print x,       ## 1 2 3

List functions:

The following built-in functions can be used with lists:

    cmp(list1, list2)       compares elements of both lists         cmp([1,2,3], [4,5,6])              ## -1  list1 < list2
                                                                    cmp([4,5,6], [1,2,3])              ## 1   list1 > list2
                                                                    cmp([1,2,3], [1,2,3])              ## 0   list1 == list2
    len(list)               number of items in list                 len([1,2,3])                       ## 3
	max(list)               max value                               max([1,2,3])                       ## 3
	min(list)               min value in list                       min([1,2,3])                       ## 1
	list(seq)               converts a tuple to a list              list((1,2,3))                      ## [1, 2, 3]
    filter(function, seq)   apply a function to filter items        filter(lambda x: x==1, [1,2,3])    ## [1]       lambda is a shorthand function declaration
    map(function, seq)      apply a function to transform items     map(lambda x: x-1, [1,2,3])        ## [0, 1, 2]
    reduce(function, seq)   apply a function + return single value  reduce(lambda x,y: x+y, [1,2,3])   ## 6

List methods:

The list data type contains  the following methods:

    append(object)          equivalent to a[len(a):] = object       [1,2,3].append(4)                  ## [1, 2, 3, 4]
    count(object)           number of times object is in list       [1,2,1,3,1].count(1)               ## 3
    extend(iterable)        equivalent to a[len(a):] = iterable     [1,2].extend([3,4])                ## [1, 2, 3, 4]
    index(object)           return item position or throw error     [1, 2, 3].index(2)                 ## 1
                                                                    [1, 2, 3].index(4)                 ## ValueError
    insert(index, object)   insert item at given position           [2,3].insert(0, 1)                 ## [1, 2, 3]
                                                                    [1,2].insert(2,3)                  ## [1, 2, 3]
    pop(index)              remove item at position and return it   [1, 2, 3].pop()                    ## 3             list now contains [1, 2]
                                                                    [1, 2, 3].pop(0)                   ## 1             list now contains [2, 3]
    remove(object)          remove first match or throw error       [1,2,3].remove(2)                  ## [1, 3]
                                                                    [1,2,3].remove(4)                  ## ValueError
    reverse()               reverse the list, in place              [1,2,3].reverse()                  ## [3, 2, 1]
    sort(cmp, key, reverse) sort the list, in place.                [1,3,2].sort()                     ## [1, 2, 3]

List comprehensions:

List comprehensions provide a more concise way to create lists in situations where map() and filter() and/or nested
loops would currently be used. The format is \[expr for var in list\]

    >>> print [i for i in range(10)]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> print [i for i in range(20) if i%2 == 0]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

    >>> nums = [1,2,3,4]
    >>> fruit = ["Apples", "Peaches", "Pears", "Bananas"]

    >>> print [(i,f) for i in nums for f in fruit]
    [(1, 'Apples'), (1, 'Peaches'), (1, 'Pears'), (1, 'Bananas'),
     (2, 'Apples'), (2, 'Peaches'), (2, 'Pears'), (2, 'Bananas'),
     (3, 'Apples'), (3, 'Peaches'), (3, 'Pears'), (3, 'Bananas'),
     (4, 'Apples'), (4, 'Peaches'), (4, 'Pears'), (4, 'Bananas')]

    >>> print [(i,f) for i in nums for f in fruit if f[0] == "P"]
    [(1, 'Peaches'), (1, 'Pears'),
     (2, 'Peaches'), (2, 'Pears'),
     (3, 'Peaches'), (3, 'Pears'),
     (4, 'Peaches'), (4, 'Pears')]

    >>> print [(i,f) for i in nums for f in fruit if f[0] == "P" if i%2 == 1]
    [(1, 'Peaches'), (1, 'Pears'), (3, 'Peaches'), (3, 'Pears')]

    >>> print [i for i in zip(nums,fruit) if i[0]%2==0]
    [(2, 'Peaches'), (4, 'Bananas')]


Tuples
------
Tuples are immutable and consist of a sequence of elements, surrounded by brackets such as an (x, y) co-ordinate. They
are like lists, except they are immutable and do not change size (however, one of the contained elements could be
mutable). Tuples are a convenient way to pass around a small, logical, fixed size bundle of values. They are usually
input with surrounding parenthesis but can also be entered without as long as the tuple is not part of a larger
expression.

A function that needs to return multiple values can just return a tuple of the values. For example, if I wanted to have
a list of 3-d coordinates, the natural python representation would be a list of tuples, where each tuple is size 3
holding one (x, y, z) group. The "empty" tuple is just an empty pair of parenthesis. Accessing the elements in a tuple
is just like a list, len(), [ ], for, in,etc. all work the same.

Tuple creation:

    ()                     empty
    (50,)                  singleton
    50,                    singleton
    (1,2,3)                tuple containing 3 integers
    'a', 'b', 'c'          tuple containing 3 strings
    tuple(['a','b','c'])   list to tuple ('a', 'b', 'c')

Tuple operators:

    +                      concatenation                           (1,2,3) + (4,5,6)                  ## (1, 2, 3, 4, 5, 6)
    *                      repetition                              (1,2,3)*2                          ## (1, 2, 3, 1, 2, 3)
    [n]                    slice                                   (1,2,3)[0]                         ## 1
    [-n]                   slice from end                          (1,2,3)[-1]                        ## 3
    [n:m]                  range slice                             (1,2,3)[1:3]                       ## (2, 3)
    in                     membership                              2 in (1,2,3)                       ## True
    not in                 not in membership                       2 not in (1,2,3)                   ## False
    for in                 iteration                               for x in (1, 2, 3): print x,       ## 1 2 3

Tuple methods:

    count(object)          number of times object is in tuple      (1,2,1,3,1).count(1)               ## 3
    index(object)          return item position or throw error     (1, 2, 3).index(2)                 ## 1
                                                                   (1, 2, 3).index(4)                 ## ValueError

Built-in functions:

    cmp(tuple1, tuple2)    compares elements of both tuples        cmp((0, 2, 3), (1, 2, 3))          ## -1
                                                                   cmp((1, 2, 3), (1, 2, 3))          ## 0
                                                                   cmp((2, 2, 3), (1, 2, 3))          ## 1
	len(tuple)             the total length of the tuple           len((1,2,3))                       ## 3
	max(tuple)             return item with max value              max((1,2,3))                       ## 3
	min(tuple)             returns item with min value             min((1,2,3))                       ## 1
    tuple(seq)             convert a sequence to a tuple           tuple([1,2,3])                     ## (1, 2, 3)
    type(tuple)            'tuple'                                 type((1,2,3))                      ## <type 'tuple'>


Dictionaries
------------
A *dict* is an unordered set of *key/value* pairs, with the requirement that the keys are unique and immutable. Hence,
strings and integers can be used as keys as can tuples as long as they only contain immutable data, but lists cannot be
use as a dictionary key.

Dict creation:

    {}                                 {}                 ## empty
    dict()                             {}                 ## empty
    {'a': 1, 'b': 2}                   {'b': 2, 'a': 1}   ## can be in any order
    {"a": 1, "b": 2}                   {'b': 2, 'a': 1}
    dict(a=1, b=2)                     {'b': 2, 'a': 1}
    dict({'a': 1, 'b': 2})             {'b': 2, 'a': 1}
    dict(zip(('a', 'b'), (1, 2)))      {'b': 2, 'a': 1}
    dict([['a', 1], ['b', 2]])         {'b': 2, 'a': 1}
    d = {'a':1}; d['b']=2              {'b': 2, 'a': 1}
    dict([(x, x**2) for x in (1,2,3)]) {1: 1, 2: 4, 3: 9} ## using list comprehension

Dict operators:

    [n]                    retrieve value for key                  {'a':1, 'b':2}['a']                ## 1
    in                     membership                              'a' in {'a':1, 'b':2}              ## True
    not in                 not in membership                       'b' not in {'a':1, 'b':2}          ## False
                                                                   not 'b' in {'a':1, 'b':2}          ## False
    for in                 iteration                               for x in {'a':1, 'b':2}: print x,  ## a b
    del                    deletion                                del {'a':1, 'b':2}['b']            ## {'a':1}
                                                                   del mydict                         ## del dict object

Dict methods:

    clear()               remove all items                         {'a':1, 'b':1}.clear()             ## {}
    copy()                returns a shallow copy                   {'a':1, 'b':1}.copy()              ## {'a': 1, 'b': 1}
    fromkeys(seq, value)  new dict with keys from seq              {}.fromkeys({'a':1, 'b':2})        ## {'a': None, 'b': None}
                                                                   {}.fromkeys({'a':1, 'b':2},1)      ## {'a': 1, 'b': 1}
    get(key, default)     returns value or default for key         {'a':1, 'b':2}.get('a')            ## 1
                                                                   {'a':1, 'b':2}.get('c')            ## None
                                                                   {'a':1, 'b':2}.get('c',0)          ## 0
    has_key(key)          deprecated - use 'key in ' instead       'a' in {'a':1, 'b':2}              ## True
    items()               returns a copy of all (key, value) pairs {'a':1, 'b':2}.items()             ## [('a', 1), ('b', 2)]
    iteritems()           iterate over the (key, value) pairs      {'a':1, 'b':2}.iteritems()         ## itemiterator
    iterkeys()            iterate over the keys                    {'a':1, 'b':2}.iterkeys()          ## keyiterator
    itervalues()          iterate over the values                  {'a':1, 'b':2}.itervalues()        ## valueiterator
    keys()                returns a copy of all keys               {'a':1, 'b':2}.keys()              ## ['a', 'b']
    pop(key, default)     removes key/value and returns value      {'a':1, 'b':2}.pop('a')            ## 1               dict now contains {'b':2}
                                                                   {'a':1, 'b':2}.pop('c')            ## KeyError
                                                                   {'a':1, 'b':2}.pop('c',0)          ## 0
    popitem()             removes and return a (key, value) pair   {'c':1, 'a':1, 'b':2}.popitem()    ## ('a', 1)
                                                                   {}.popitem()                       ## KeyError
    setdefault(key, def)  return value else set and return default {'a':1, 'b':2}.setdefault('a')     ## 1
                                                                   {'a':1, 'b':2}.setdefault('c')     ## None
                                                                   {'a':1, 'b':2}.setdefault('c',0)   ## 0
    update(other)         update with dictionary/iterable          {'a':1, 'b':2}.update({'c':3})     ## {'a': 1, 'c': 3, 'b': 2}
                                                                   {'a':1, 'b':2}.update(c=3)         ## {'a': 1, 'c': 3, 'b': 2}
    values                returns a copy of all values             {'a':1, 'b':2}.values()            ## [1, 2]
    viewitems             returns a view of the items              {'a':1, 'b':2}.viewitems()         ## dict_items([('a', 1), ('b', 2)])
    viewkeys              returns a view of the keys               {'a':1, 'b':2}.viewkeys()          ## dict_keys(['a', 'b'])
    viewvalues            returns a view of the values             {'a':1, 'b':2}.viewvalues()        ## dict_values([1, 2])

Built-in functions:

    cmp(dict1, dict2)     compares elements of both dictionaries   cmp({'a':0, 'b':2}, {'a':1, 'b':2}) ## -1
                                                                   cmp({'a':1, 'b':2}, {'a':1, 'b':2}) ## 0
                                                                   cmp({'a':2, 'b':2}, {'a':1, 'b':2}) ## 1
    len(dict)             the number of items in the dictionary    len({'a':1, 'b':2})                 ## 2
    str(dict)             string representation of a dictionary    str({'a':1, 'b':2})                 ## "{'a': 1, 'b': 2}"
    type(variable)        'dict' for dictionary                    type({'a':1, 'b':2})                ## <type 'dict'>

Formatting:

The % operator can be used to substitute values from a dict into a string by name:

    map={'type':'cars', 'count':2}
    print "I can see %(count)d %(type)s" % map                     # I can see 2 cars



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


Files
-----

File objects can be created using the built-in *open()* function:

    f = open("hello.txt")
    try:
        for line in f:
            print line
    finally:
        f.close()

or in Python 2.6 and later:

    with open("hello.txt") as f:
        for line in f:
            print line


Attributes:

    closed    Read-only. Returns true if the file is closed. May not be available on all file-like objects.

    encoding  Read-only. Returns the encoding that this file uses. When Unicode strings are written to a file, they will
              be converted to byte strings using this encoding. In addition, when the file is connected to a terminal,
              the attribute gives the encoding that the terminal is likely to use (that information might be incorrect).
              May not be present on all file-like objects. It may also be None, in which case the file uses the system
              default encoding for converting Unicode strings.

    errors    The Unicode error handler used along with the encoding.

    mode      Read-only. The I/O mode for the file. If the file was created using the open() built-in function, this
              will be the value of the mode parameter. May not be available on all file-like objects.

    name      Read-only. If the file object was created using open(), the name of the file. Otherwise, some string that
              indicates the source of the file object, of the form <...>. May not be present on all file-like objects.

    newlines  Read-only. If Python was built with universal newlines enabled (the default) this read-only attribute
              exists, and for files opened in universal newline read mode it keeps track of the types of newlines
              encountered while reading the file. The values it can take are '\r', '\n', '\r\n', None (unknown, no
              newlines read yet) or a tuple containing all the newline types seen, to indicate that multiple newline
              conventions were encountered. For files not opened in universal newline read mode the value of this
              attribute will be None.

    softspace Boolean that indicates whether a space character needs to be printed before another value when using
              the print statement. Classes that are trying to simulate a file object should also have a writable
              softspace attribute, which should be initialized to zero. This will be automatic for most classes
              implemented in Python (care may be needed for objects that override attribute access); types
              implemented in C will have to provide a writable softspace attribute.

File object methods:

    close()             Close the file. Any operation which requires that the file be open will raise a ValueError after the
                        file has been closed. Calling close() more than once is allowed.

    flush()             Flush the internal buffer. This does not necessarily write the file’s data to disk. Use flush()
                        followed by os.fsync() to ensure this behavior.

    fileno()            Returns the integer “file descriptor” that is used by the underlying implementation to request I/O
                        operations from the operating system. This can be useful for other, lower level interfaces that use
                        file descriptors, such as the fcntl module or os.read().

    isatty()            Returns True if the file is connected to a tty(-like) device, else False.

    next()              A file object is its own iterator, for example iter(f) returns f (unless f is closed). When a file
                        is used as an iterator, typically in a for loop (for example, for line in f: print line), the next()
                        method is called repeatedly. This method returns the next input line, or raises StopIteration when
                        EOF is hit when the file is open for reading (behavior is undefined when the file is open for
                        writing). In order to make a for loop the most efficient way of looping over the lines of a file,
                        the next() method uses a hidden read-ahead buffer. As a consequence of using a read-ahead buffer,
                        combining next() with other file methods (like readline()) does not work right. However, using seek()
                        to reposition the file to an absolute position will flush the read-ahead buffer.

    read(size)          Read at most size bytes from the file (less if the read hits EOF before obtaining size bytes). If
                        the size argument is negative or omitted, read all data until EOF is reached. The bytes are returned
                        as a string object. An empty string is returned when EOF is encountered immediately. (For certain
                        files, like ttys, it makes sense to continue reading after an EOF is hit.) Note that when in
                        non-blocking mode, less data than was requested may be returned, even if no size parameter was given.

    readline(size)      Read one entire line from the file. A trailing newline character is kept in the string (but may
                        be absent when a file ends with an incomplete line). [6] If the size argument is present and
                        non-negative, it is a maximum byte count (including the trailing newline) and an incomplete line
                        may be returned. When size is not 0, an empty string is returned only when EOF is encountered
                        immediately.

    readlines(sizehint) Read until EOF using readline() and return a list containing the lines thus read. If the
                        optional sizehint argument is present, instead of reading up to EOF, whole lines totalling
                        approximately sizehint bytes (possibly after rounding up to an internal buffer size) are
                        read. Objects implementing a file-like interface may choose to ignore sizehint if it cannot
                        be implemented, or cannot be implemented efficiently.

    xreadlines()        Deprecated, use 'for line in file' instead.

    seek(offset,whence) Set the file’s current position. The whence argument is optional and defaults to os.SEEK_SET or
                        0 (absolute file positioning); other values are os.SEEK_CUR or 1 (seek relative to the current
                        position) and os.SEEK_END or 2 (seek relative to the file’s end). There is no return value. Not
                        all file objects are seekable.

    tell()              Return the file’s current position. Note that on Windows, tell() can return illegal values
                        (after an fgets()) when reading files with Unix-style line-endings. Use binary mode ('rb') to
                        circumvent this problem.

    truncate(size)      Truncate the file’s size. If the optional size argument is present, the file is truncated to
                        (at most) that size. The size defaults to the current position. The current file position is not
                        changed. Note that if a specified size exceeds the file’s current size, the result is
                        platform-dependent: possibilities include that the file may remain unchanged, increase to the
                        specified size as if zero-filled, or increase to the specified size with undefined new content.
                        Availability: Windows, many Unix variants.

    write(str)          Write a string to the file. There is no return value. Due to buffering, the string may not
                        actually show up in the file until the flush() or close() method is called.

    writelines(seq)     Write a sequence of strings to the file. The sequence can be any iterable object producing
                        strings, typically a list of strings. There is no return value. The name is intended to match
                        readlines(); writelines() does not add line separators.


Regular Expressions
-------------------
The "re" module provides Perl-like regular expression support:

The *match* and *search* functions attempt to match a regex pattern to a string with optional flags. They both return
*None* if there is no match or a [MatchObject] (http://docs.python.org/library/re.html#re.MatchObject) in the case of a
match. The *findall* function returns pattern matches as a list of strings and the *sub* function is used :

    re.match(pattern, string, flags=0)              # matches at the beginning of the string
    re.search(pattern, string, flags=0)             # matches anywhere in the string
    re.findall(patten, string, flags=0)             # returns all matches as a list of strings or tuples if using groups
    re.sub(pattern, repl, string, count=0, flags=0) # retuns a new string with all occurrences of the pattern with repl
                                                    # (unless count is supplied)

where:

    pattern	  the regular expression to be matched
    string	  the string to be searched to match the pattern
    flags	  an optional modifier to control various aspects of matching

multiple flags can be specified using bitwise OR (|):

    re.I	  case-insensitive matching.
    re.L	  interpret words according to the current locale. Affects the alphabetic group (\w and \W), as well as
              word boundary behavior (\b and \B).
    re.M	  makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line
              (not just the start of the string).
    re.S	  makes a period (dot) match any character, including a newline.
    re.U	  interpret letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B
    re.X	  permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped
              by a backslash), and treats unescaped # as a comment marker.


Regular-expression patterns:
<br/>
<br/>
All characters match themselves except for control characters, (+ ? . * ^ $ ( ) [ ] { } | \).<br/>
A control character can be eacaped by preceding it with a backslash. The following table lists the regular expression
syntax that is available in Python:

    ^           Matches beginning of line
    $	        Matches end of line
    .	        Matches any single character except newline. Using m option allows it to match newline as well
    [...]	    Matches any single character in brackets
    [^...]	    Matches any single character not in brackets
    a|b  	    Matches either a or b
    \w	        Matches word characters [a-zA-Z0-9_]
    \W	        Matches nonword characters
    \s	        Matches whitespace [\t\n\r\f]
    \S	        Matches non whitespace
    \d	        Matches digits [0-9]
    \D	        Matches nondigits
    \A	        Matches beginning of string
    \Z	        Matches end of string. If a newline exists, it matches just before newline
    \z	        Matches end of string
    \G	        Matches point where last match finished
    \b	        Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets
    \B	        Matches nonword boundaries
    \n, \t,     Matches newlines, carriage returns, tabs, etc.
    \1...\9	    Matches nth grouped subexpression
    \10	        Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of
                a character code
    *	        Matches 0 or more occurrences of the preceding expression
    +	        Matches 1 or more occurrence of the preceding expression
    ?	        Matches 0 or 1 occurrence of the preceding expression
    {n}	        Matches exactly n number of occurrences of preceding expression
    {n,}	    Matches n or more occurrences of preceding expression
    {n, m}      Matches at least n and at most m occurrences of preceding expression
    (re)	    Groups regular expressions and remembers matched text
    (?imx)	    Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that
                is affected
    (?-imx)	    Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that
                area is affected
    (?: re)	    Groups regular expressions without remembering matched text
    (?imx: re)	Temporarily toggles on i, m, or x options within parentheses
    (?-imx: re)	Temporarily toggles off i, m, or x options within parentheses
    (?#...)	    Comment
    (?= re)	    Specifies position using a pattern. Doesn't have a range
    (?! re)	    Specifies position using pattern negation. Doesn't have a range
    (?> re)	    Matches independent pattern without backtracking
    \           Escape following character so it is not treated as special


The basic rules of regular expression search for a pattern within a string are:<br/>
  * the search proceeds through the string from start to end, stopping at the first match found<br/>
  * all of the pattern must be matched, but not all of the string<br/>
  * if match = re.search(pat, str) is successful, match is not None and match.group() returns the matching text<br/>

Character Examples:

    re.search(r'Python', 'Python').group()                 ## 'python'        Match 'Python'
    re.search(r'[Pp]ython', 'python').group()              ## 'python'        Match 'Python' or 'python'
    re.search(r'[aeiou]', 'python').group()                ## 'o'             Match any vowel
    re.search(r'[0-9]', 'python2.7').group()               ## '2'             Match any digit
    re.search(r'[a-z]', 'Python2.7').group()               ## 'y'             Match any lower case ASCII char
    re.search(r'[A-Z]', 'Python2.7').group()               ## 'P'             Match any upper case ASCII char
    re.search(r'[a-zA-Z0-9]', 'Python2.7').group()         ## 'P'             Match any letter or digit
    re.search(r'[^A-Z]', 'Python2.7').group()              ## 'y'             Match anything other than an upper case char
    re.search(r'[^0-9]', '2.7Python').group()              ## '.'	          Match anything other than a digit

Special Character Examples:

    re.search(r'.', '\n\nPython').group()                  ## 'P'             Match any character except newline
    re.search(r'\d', 'python2.7').group()                  ## '2'             Match a digit [0-9]
    re.search(r'\D', 'python2.7').group()                  ## 'p'             Match a nondigit [^0-9]
    re.search(r'\s', 'python 2.7').group()                 ## ' '             Match a whitespace character [ \t\r\n\f]
    re.search(r'\S', 'python 2.7').group()                 ## 'p'             Match nonwhitespace: [^ \t\r\n\f]
    re.search(r'\w', 'Python2.7').group()                  ## 'P'             Match a single word character: [A-Za-z0-9_]
    re.search(r'\W', 'Python2.7').group()                  ## '.'             Match a nonword character: [^A-Za-z0-9_]

Repetition Examples:

    re.search(r'python2.7?', 'python2.').group()           ## 'python2.'      Match 'python2.' and 0 or 1 '7' chars
    re.search(r'python2.7?', 'python2.777').group()        ## 'python2.7'     Match 'python2.' and 0 or 1 '7' chars
    re.search(r'python2.7*', 'python2.777').group()        ## 'python2.777'   Match 'python2.' and 0 or more '7' chars
    re.search(r'python2.7+', 'python2.777').group()        ## 'python2.777'   Match 'python2.' and 1 or more '7' chars
    re.search(r'python2.7+', 'python2.')                   ## None            Match 'python2.' and 1 or more '7' chars
    re.search(r'[\w.-]+@[\w.]+', 'a-b.c@d.com').group()    ## 'a-b.c@d.com'   Simple email address match
    re.search(r'\d{3}', 'python2.789').group()             ## '789'           Match exactly 3 digits
    re.search(r'\d{1,}', 'python2.789').group()            ## '2'             Match 1 or more digits
    re.search(r'\d{1,3}', 'python2.789').group()           ## '2'             Match 1, 2 or 3 digits
    re.search(r'\d{1,3}', 'python2789').group()            ## '278'           Match 1, 2 or 3 digits

Greedy Repetition Examples:

    re.search(r'python2.*', 'python2.3232').group()        ## 'python2.3232'  Match all trailing '2' chars

Nongreedy Repetition Examples:

    re.search(r'python2.*?', 'python2.3232').group()       ## 'python2'       Stop at first trailing non '2' char

Grouping Examples:

    re.search(r'(python)(\d+.\d+)', 'python2.78').group()                               ## 'python2.789'
    re.search(r'(python)(\d+.\d+)', 'python2.78').group(1)                              ## 'python'
    re.search(r'(python)(\d+.\d+)', 'python2.78').group(2)                              ## '2.789'
    re.search(r'(?P<lang>python)(?P<version>\d+.\d+)', 'python2.78').group('lang')      ## 'python'
    re.search(r'(?P<lang>python)(?P<version>\d+.\d+)', 'python2.78').group('version')   ## '2.78'

Backreference Examples:

    re.search(r'(\w+)\s+\1', 'a the the b').group()        ## 'the the'       Find duplicate words
    re.search(r'(\w+)\s+\1', 'a the thh b').group()        ## None

Alternate Examples:

    re.search(r'python|ruby', 'python').group()            ## 'python'        Match "python" or "ruby"
    re.search(r'python(2.7|3.0)', 'python3.0').group()     ## 'python3.0'     Matches 'python2.7' or 'python3.0'
    re.search(r'python(!+|\?)', 'python!!!').group()       ## 'python!!!'     Matches one or more ! or one ?
    re.search(r'python(!+|\?)', 'python???').group()       ## 'python?'

Anchor Examples:

    re.search(r'^python', 'python').group()                ## 'python'        Match at start of string
    re.search(r'^python', '\npython')                      ## None            Does not match at start of line
    re.search(r'^python', '\npython', re.M).group()        ## 'python'        Match at start of line
    re.search(r'python$', 'is python').group()             ## 'python'        Match at end of string
    re.search(r'python$', 'python\nabc').group()           ## 'python'        Does not match at end of line
    re.search(r'python$', 'python\nabc', re.M).group()     ## 'python'        Match at end of line
    re.search(r'\Apython', 'python abc').group()           ## 'python'        Match at start of string
    re.search(r'python\Z', 'abc python').group()           ## 'python'        Match at end of string
    re.search(r'\bpython\b', ', python.').group()          ## 'python'        Match at a word boundary
    re.search(r'python\B', 'pythonista').group()           ## 'python'        Match at a non-word boundary
    re.search(r'python\B', 'python')                       ## None            Does not match for standalone word
    re.search(r'python(?=2)', 'python2').group()           ## 'python'        Match if followed by a '2'
    re.search(r'python(?!2)', 'python2')                   ## None            Match if not follwed by a '2'

Special parentheses syntax:

    re.search(r'python(?#comment)', 'python2').group()     ## 'python'        Coment is ignored
    re.search(r'(?i)python', 'PythoN2').group()            ## 'PythoN'        Case insensitive search (instead of re.I)


Built-in Functions
==================

open(name, mode, buffering)
---------------------------
