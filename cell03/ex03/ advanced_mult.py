import sys


if len(sys.argv) > 1:
    print("none")
else:
    
    i = 0
    while i <= 10:
        # Display the table header
        print(f"Table de {i}: ", end="")
        
        
        j = 0
        while j <= 10:
            print(i * j, end=" " if j < 10 else "\n") 
            j += 1
        
        i += 1
