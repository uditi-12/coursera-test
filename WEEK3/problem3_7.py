import csv

def problem3_7(filename,name):
    f=open(filename);
    reader=csv.reader(f);
    for keys in reader:
        if(keys[0]==name):
            print(keys[1]);

    f.close();




