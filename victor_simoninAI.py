# -*- coding: utf-8 -*-
"""
Created on Jan 2020

@author: victor.simonin
"""
def assignment1():
    question = "Is every human good grader ?"
    print(question, end = '\n')
    every = True
    human = True
    good_grader = True
    implication1 = [not every, not human, good_grader]
    implication2 = [every, human, not good_grader]
    solution = [every, human, good_grader]
    
    result = []
    
    for i in range(len(implication1)):
        result.append(implication1[i] and implication2[i])
    count = 0
    while(count < 3):
        if(result[count] != solution[count]):
            print("no", end = '\n')
            return False
        count+=1
    print("yes", end = '\n')
    return True 