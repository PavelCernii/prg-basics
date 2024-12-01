import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.put(char)
        elif char in ')}]':
           if stack.empty() or stack.get() != brackets[char]:
              return False
           
    return stack.empty()

if brackets_ok(expression1):
   print('All is good')
else:
   print('wrong')

if brackets_ok(expression2):
   print('All is good')
else:
   print('wrong')

if brackets_ok(expression3):
   print('All is good')
else:
   print('wrong')