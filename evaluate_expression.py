class EvalExpression:
  def evaluate(self, s: str) -> int:
    self.s = s
    self.expr = []
    self.stack = []
    self.pf = ''
    self.op = ('-','+','*','/')

    self.expr = self.conversion()

    for i in self.expr:
      if (len(self.stack) > 1) and (self.stack[-1] == self.stack[0]):
          self.pf += self.stack[-1] + ' '
          self.stack.pop()
      if i not in self.op:
        self.pf += i + ' '
      elif i in self.op:
        if len(self.stack) == 0:
          self.stack.append(i)
        elif (i == self.op[0]) and (self.stack[-1] == '-'):
          self.stack.append(i)
        elif (i == self.op[0]) and (self.stack[-1] == '+'):
          self.pf += self.stack[-1] + ' '
          self.stack.pop()
          self.stack.append(i)
        elif (self.stack[-1] in self.op[2:]) and (i in self.op[:2]):
          self.pf += self.stack[-1] + ' '
          self.stack.pop()
          self.stack.append(i)
        elif (self.stack[-1] in self.op[:2]) and (i in self.op[:2]):
          self.stack.append(i)
        elif (self.stack[-1] == self.op[-1]) and (i == '*'):
          self.pf += self.stack[-1] + ' '
          self.stack.pop()
          self.stack.append(i)
        else:
          self.stack.append(i) 
    
    if len(self.stack) == 2:
      self.stack[0], self.stack[1] = self.stack[1], self.stack[0]

    self.pf += ' '.join(self.stack)

    self.pf = self.pf.split(' ')

    result = 0
    for j,i in enumerate(self.pf):
        if i == '/':
          total = int(self.pf[j-2]) // int(self.pf[j-1])
          result += total
          self.pf.pop(j)
          self.pf.pop(j-1)
          self.pf[j-2] = total
        elif i == '*':
          total = int(self.pf[j-2]) * int(self.pf[j-1])
          result += total
          self.pf.pop(j)
          self.pf.pop(j-1)
          self.pf[j-2] = total        
        elif i == '+':
          total = int(self.pf[j-2]) + int(self.pf[j-1])
          result += total
          self.pf.pop(j)
          self.pf.pop(j-1)
          self.pf[j-2] = total
        elif i == '-':
          total = int(self.pf[j-2]) - int(self.pf[j-1])
          result += total
          self.pf.pop(j)
          self.pf.pop(j-1)
          self.pf[j-2] = total
    
    for i in self.pf:
      if i == '/':
        result = int(self.pf[1]) // int(self.pf[0])
      elif i == '+':
        result = int(self.pf[1]) + int(self.pf[0])
      elif i == '-':
        result = int(self.pf[0]) - int(self.pf[1])
      elif i == '*':
        result = int(self.pf[1]) * int(self.pf[0])
                                
    return result
      
  def conversion(self):
    y = self.s.replace(' ', '')
    num = ''
  
    for i in y:
        if i.isdigit():
            num += i
        else:
            self.expr.append(num)
            self.expr.append(i)
            num = ''
    if len(num) > 0:
        self.expr.append(num)

    return self.expr

x = EvalExpression()
assert x.evaluate('3+2*2') == 7
assert x.evaluate(" 3/2 ") == 1
assert x.evaluate(' 3+5 / 2 ') == 5
assert x.evaluate(" 23 + 4 / 2 ") == 25
assert x.evaluate(" 1000 - 400 / 2") == 800