# /usr/bin/env python

def splitString():
    """split string by seperator
        1. split(): string object, but in simply condition
        2. re.split(): 
    """
    line = 'asdf fjdk; afedm, fjek,asdf, foo'
    import re
    print(re.split(r'[;,\s]\s*', line))




if __name__ == '__main__':
    splitString()
