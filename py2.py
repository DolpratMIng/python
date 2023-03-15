def cal(numLoop):
    
    num = 0;
    for x in range(numLoop):
        print("Current Number ", str(x), " Previous number ", str(num), " Sum: ", str(x+num))
        num = x;
        

        
print(cal(10));
  