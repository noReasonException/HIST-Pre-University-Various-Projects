#****************calc by stefanos stefanou
#************************** TEST 03
calc = input("��� �� ���������� [1],�� ���������� [2],�� ����/���� [3],�� ��������� [4] � �� ������� �� ������??[5] ")
data1 = input("���� ��� ����� ������ ")
data2 = input("���� ��� ������� ������")
add = 1
rem = 2
mul = 3
div = 4
potn = 5
if calc == add:
    print data1 + data2
if calc == rem:
    print data1 - data2
if calc == mul:
    print data1 * data2
if calc == div:
 if data1 > data2:
    print data1 / data2
if data1 < data2:
    print "first input smaller than second input"
if calc == potn:
    print data1 ** data2


    
