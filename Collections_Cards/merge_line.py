import sys

if len(sys.argv) == 3:
        file1 = open(sys.argv[1],'r')
        file2 = open(sys.argv[2],'r')

while True:
        line1 = file1.readline().rstrip()
        line2 = file2.readline().rstrip()
        if line1 and line2:
                print line1 + ' ' + line2
        else:
                break;

file1.close()
file2.close()
sys.exit(0)
