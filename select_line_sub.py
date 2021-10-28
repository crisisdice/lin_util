import sys

def main():
    input_stream = sys.stdin.read()
    print(input_stream.split('\n')[int(sys.argv[1])])

if __name__=='__main__':
    main()
