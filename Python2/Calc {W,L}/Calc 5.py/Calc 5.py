#****************calc by stefanos stefanou
#************************** TEST 05
from math import *
print "********************************"
print "�������� [1]                  *"
print "�������� [2]                  *"
print "��������������� [3]           *"
print "�������� [4]                  *"
print "������ [5]                    *"
print "���� (��� ������ �������) [6] *"
print "********************************"
calc = input("������� ~ ")
data1 = input("�������� ��� ����� ������ ~ ")
data2 = input("�������� ��� ������� ������ ~ ")
add = 1
rem = 2
mul = 3
div = 4
pon = 5
nun = 6
if calc == add:
    print "�� ���������� ��� ��������� �����", data1 + data2
if calc == rem:
    print "�� ���������� ��� ��������� �����", data1 - data2
if calc == mul:
    print "�� ���������� ��� ��������������� �����", data1 * data2
if calc == div:
 if data1 > data2:
   print "�� ���������� ��� ��������� �����", data1 / data2
   print "�� �������� ���������", data1 % data2
if calc == div:
 if data1 == data2:
   print "�� ���������� ��� ��������� �����", data1 / data2
   print "�� ���������� ���������", data1 % data2
if calc == pon:
    print "�� ���������� ��� ������� �����", data1 ** data2
if calc == nun:
    print "� ���� �����", sqrt(data1)
if calc < add:
    print "� ������",calc,"��� ���������"
if calc > nun:
    print "� ������",calc,"��� ���������"

     


    
