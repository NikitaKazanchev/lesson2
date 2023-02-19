def main(st1, st2):
    
    if isinstance(st1, str) and isinstance(st2, str) and st1 == st2:
        return 1
    
    elif isinstance(st1, str) and isinstance(st2, str) and st1 != st2 and len(st1) > len(st2):
        return 2
    
    elif isinstance(st1, str) and isinstance(st2, str) and st1 != st2 and st2 == 'learn':
        return 3
    
    else:
        return 0

if __name__ == "__main__":
    your_input = main('12', 'learn')
    print(your_input)
