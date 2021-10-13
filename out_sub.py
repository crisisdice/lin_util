from pprint import pprint as print
#TODO learn vim snippets
def main():
    i = open('out.txt').read()
    l = [ line.split('(')[0] for line in i.split('\n') if line and 'src' in line ]
    #print(l)
    #s = '\n'.join(set(l))
    print(set(l))

if __name__ == '__main__':
    main()
