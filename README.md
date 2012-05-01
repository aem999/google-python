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


Dictionaries
------------
A *dict* is an unordered set of *key/value* pairs, with the requirement that the keys are unique and immutable. Hence,
strings and integers can be used as keys as can tuples as long as they only contain immutable data, but lists cannot be
use as a dictionary key.

Dict creation:

    {}                                 {}  ## empty
    dict()                             {}  ## empty
    {'one': 1, 'two': 2}               {'two': 2, 'one': 1}  ## can be in any order
    {"one": 1, "two": 2}               {'two': 2, 'one': 1}
    dict(one=1, two=2)                 {'two': 2, 'one': 1}
    dict({'one': 1, 'two': 2})         {'two': 2, 'one': 1}
    dict(zip(('one', 'two'), (1, 2)))  {'two': 2, 'one': 1}
    dict([['one', 1], ['two', 2]])     {'two': 2, 'one': 1}
    d = {'one':1}; d['two']=2          {'two': 2, 'one': 1}
    dict([(x, x**2) for x in (1,2,3)]) {1: 1, 2: 4, 3: 9}    ## using list comprehension

Dict operators:

    [n]                    retrieve value for key                  {'a':1, 'b':2}['a']                ## 1
    in                     membership                              'a' in {'a':1, 'b':2}              ## True
    not in                 not in membership                       'b' not in {'a':1, 'b':2}          ## False
                                                                   not 'b' in {'a':1, 'b':2}          ## False
    for in                 iteration                               for x in {'a':1, 'b':2}: print x,  ## a b
    del                    deletion                                del {'a':1, 'b':2}['b']            ## {'a':1}
                                                                   del mydict                         ## del dict object

Dict methods:

    clear()               remove all items                         {'a': 1, 'b': 1}.clear()           ## {}
    copy()                returns a shallow copy                   {'a': 1, 'b': 1}.copy()            ## {'a': 1, 'b': 1}
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

Formatting:

The % operator can be used to substitute values from a dict into a string by name:

    map={'type':'cars', 'count':2}
    print "I can see %(count)d %(type)s" % map                     # I can see 2 cars


Built-in Methods
----------------

to follow


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
