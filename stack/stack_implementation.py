
# Ref : https://www.geeksforgeeks.org/stack-data-structure-introduction-program/
# Implementation of stack in python

def createStack():
	stack = []
	return stack

def isEmpty(stack):
	return len(stack) == 0

def push(stack, item):
	stack.append(item)

def pop(stack, item):
   if (isEmpty(stack)):
   	return str(-maxsize -1)
   return stack.pop()


def peek(stack): 
    if (isEmpty(stack)): 
        return str(-maxsize -1) # return minus infinite 
    return stack[len(stack) - 1] 


stack = createStack() 
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
