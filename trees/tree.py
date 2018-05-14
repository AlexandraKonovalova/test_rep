import os

def tree():
    dic = {'r': [], 'd': []}

    for root, dirs, files in os.walk('.'):
        for dr in dirs:
            if 'r' in dr:                    
                dic['r'].append(dr)
        for fl in files:
            if 'd' in fl:
                dic['d'].append(fl)
                if 'r' in root:
                    print(fl)
            
    return len(dic['r']), len(dic['d'])

def main():
    return tree()

if __name__ == "__main__":
    print(main())
