import re

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            r = re.search('id="P571".*>([0-9]+)', line) 
            if r:
                date = r.group(1)
                return date
            
def main(otherfile, info):
    with open(otherfile, 'w', encoding='utf-8') as t:
        table = 'Год основания:' + '\t' + info
        t.write(table)
        
        
if __name__ == "__main__":
    main('text.txt', readfile('hse.html'))

