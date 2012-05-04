#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """

    html = read_html(filename)
    year = extract_year(html, filename)
    ranks = extract_ranks(html, filename)

    names=[]
    for rank, boys_name, girls_name in ranks:
        names.append('%s %s' % (boys_name, rank))
        names.append('%s %s' % (girls_name, rank))

    return [year] + sorted(names)

def read_html(filename):
    with open(filename, 'r') as f:
        html = f.read()
    return html

def extract_ranks(html, filename):
    """Searches the html for a table containing cells rank, male name, female name
    and returns a list of tuples containg (rank, male name, female name)"""

    match = re.search(r'<table.*?Rank.*?male.*?female.*?</tr>(.*?</table>)', html, re.S|re.I)
    if match is None:
        sys.stderr.write('Unable to find the table containing the names in %s, exiting' % filename)
        sys.exit(1)

    names_html = match.group(1)
    return re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', names_html)

def extract_year(html, filename):
    """Searches the specified html for the String 'Popularity in nnnn' and returns nnnn"""

    match = re.search(r'Popularity\sin\s(?P<year>\d\d\d\d)', html)
    if match is None:
        sys.stderr.write('Unable to find the year in %s, exiting' % filename)
        sys.exit(1)

    return match.group('year')

def write_summary(names, filename):
    """Write name and rank list to a file"""
    with open(filename, 'w') as f:
        f.write('\n'.join(names))
    print 'Summary written to %s' % filename

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for arg in args:
        if summary:
            write_summary(extract_names(arg), arg + '.summary')
        else:
            print extract_names(arg)

if __name__ == '__main__':
    main()
