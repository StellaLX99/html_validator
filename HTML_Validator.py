#!/bin/python3


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
   
    listOfTags = []
    for i in range(len(html)-1): #indexting through every input
        str = "" #establish a string
        if html[i] == "<":#check to see if it a open tag
            str =str+html[i] #save it and add it to a temp string
            i =i+1 #keep going
            while html[i] != ">": #stop untill we find the closed ones
                str =str+ html[i]
                i =i+1 # keep going
            extractedtags = str + ">"#push that list with the closed tag
            listOfTags.append(extractedtags)
    return listOfTags

class Stack:
    def _init_(self):
        self.items=[]
    def isEmpty(self):
        return self.items ==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    s=[]
    validated=True
    newtags= _extract_tags(html)
    # this _extracted_tags function will give me a list of extracted tags
    for i in range(len(newtags)):
        if "/" not in newtags[i]:   #if not the closed tag, then add together
                s.append(newtags[i])
        else:
            if s==[]:#everything went through
                    validated=False
            else:
                top=s.pop() #start to count, get off the tags
                if top[1:]!=newtags[i][2:]:
                        return False
    if validated and s==[]:
        return True
    else:
        return False

 # index through input string
    #save the char ur looking at 
    # find the opening tag, and then add that to a temp string, and then keep looking for the next index, and if it hasn't met a closing tag yet, then also save those
    #characters into the temp string, stop until we find the closing tag, but also save the closing tag into the temp string
    # then push that list up, and that's the list that we've found that only have characters 
    #html_parsing, parse the string by using the symbols
