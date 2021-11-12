import sys

def problem3_1(filename):
    f=open(filename);
    c=0;
    for line in f:
        c=c+len(line)
        print(line, end="")
    print("\n\nThere are",c,"letters in the file.");
    f.close()

    
