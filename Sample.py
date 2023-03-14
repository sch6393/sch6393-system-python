import sys

def parameter(argv):
    i = 0
    while i < argv:
        i = i + 1
        print('%d 回' % i)
    
    print('End!')


print('Test Start!')
argv1 = int(sys.argv[1])
argv2 = int(sys.argv[2])

print('argv : %d' % (len(sys.argv) - 1))
for i in range(len(sys.argv)):
  print('sys.argv[%d] = %s' % (i, sys.argv[i]))

parameter(argv1)
parameter(argv2)
