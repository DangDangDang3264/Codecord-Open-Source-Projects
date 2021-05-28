# Codecord-Open-Source-Projects
More to come here in the future. This is just the Codecord repository, enjoy!

---Internal Python Style Guide---
A) Case Standards
    1) Variables should be written in one of two formats:
        a) all lowercase with underscores between words.
            ex: new_variable
        b) lowercase letters with numbers or capital letters for temporary or many similar variables. Variables written like this should be otherwise obvious in purpose.
            ex: variable1 or variableA or variableA1
    2) Functions should be written in 'camel case' with the first letter lowercase.
        ex: newFunction(args*, kwargs**)
    3) Classes should be written in 'camel case' with the first letter capitalized.
        ex: newClass

B) Classes
    1) Class variables should be defined in the '__init__' statement and not parentheses after the class declaration.

C) Docstrings
    1) Docstrings should be used with every function.
    2) The format of docstrings should follow the following format:
        def exampleFunction(arg1, arg2, kwarg1=None)
            '''Describe the purpose of the function here. The description should be relatively short.

            Arguments:
            arg1 -- (type) Describe the arguments here.
            arg2 -- (type) Take care to describe the variable used, especially if not immediately obvious.

            Keyword Arguments: 
            kwarg1 -- (type) Describe the keyword arguments here, if necessesary describe the default.

            Returns:
            result -- (type) The number list derived from the message.

            Notes:
            -Add notes in this section.
            -Ensure they are in a bulleted in this format.
            '''
            result = (arg1 + arg2) * kwarg1
            return result

D) Program Notes
    1) Programs should have a notes section starting on line 1.
    2) The format of the notes section should follow the following format:
        '''Program Name
        Version 1.0 pub.1/01/2001
        Written by [Author Handle]

        Notes:
        -Add any notes about the program here.
        '''