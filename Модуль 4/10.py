# import sys
# for arg in sys.argv:
#     print(arg)

# python test.py -help user --flag # test.py -help user --flag
import sys
def parse_args():
    result = ""
    for arg in sys.argv[1:]:
        result += arg + ' '
            
        
    return result.strip()

# import sys
# def parse_args():
#     return ' '.join(sys.argv[1:])

