import sys
import json
import traceback

from chomsky import chomsky


def main(archive):
    try: 
        file = open(archive)    
        try:
            data = json.load(file)
            variables = data['glc'][0]
            terminals = data['glc'][1]
            rules = data['glc'][2]
            starter = data['glc'][3]
            chomsky(variables, terminals, rules, starter)
        except Exception as e:
            traceback.print_exc()
            print("\nSomething went wrong")
            print( f"Error: {e}\n")
        finally:
            file.close()
    except:
        print("Something went wrong when opening the file")
        print("To run the script use: python [path to main.py] [path to json]")
        
    
if __name__ == "__main__":
    #print(f"size: {len(sys.argv)} & content: {sys.argv}")    
    main(sys.argv[1])