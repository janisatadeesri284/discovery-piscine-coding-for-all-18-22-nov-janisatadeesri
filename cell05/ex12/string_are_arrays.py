import sys

def string_are_arrays():
    
    if len(sys.argv) != 2:
        print("none")
        return
    
    
    input_string = sys.argv[1]
    
    
    found_z = False
    
   
    for char in input_string:
        if char == 'z':
            print("z", end="")
            found_z = True
    
    
    if not found_z:
        print("none")

if __name__ == "__main__":
    string_are_arrays()
