#!/usr/bin/python3

def multiple_returns(sentence):
    first = ""
    length = 0
    if not sentence:
        first = "None"
        length = 0
    else:
        length = len(sentence)
        first = "None" if length == 0 else sentence[0]
    return ((length, first))
    
