def main(st1, st2):
    
    if type(st1) == str and type(st2) == str and st1 == st2:
        return 1
    
    elif type(st1) == str and type(st2) == str and st1 != st2 and len(st1) > len(st2):
        return 2
    
    elif type(st1) == str and type(st2) == str and st1 != st2 and st2 == 'learn':
        return 3
    
    else:
        return 0

a = main('12', 'learn')
print(a)
