import sys

def count_it():
    
    if len(sys.argv) == 1:
        print("none")
    else:
        
        print(f"parameters: {len(sys.argv) - 1}")
        
       
        for param in sys.argv[1:]:
            print(f"{param}: {len(param)}")

if __name__ == "__main__":
    count_it()
