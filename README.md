google-python
=============

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
