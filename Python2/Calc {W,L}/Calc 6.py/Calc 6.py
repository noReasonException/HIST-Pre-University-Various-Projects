
#****************calc by stefanos stefanou
#************************** TEST 05
from math import *
print """
        CCCCCCCCCCCCC lllllll                                  66666666   
     CCC::::::::::::C l:::::l                                 6::::::6    
   CC:::::::::::::::C l:::::l                                6::::::6     
  C:::::CCCCCCCC::::C l:::::l                               6::::::6      
 C:::::C       CCCCCC  l::::l     cccccccccccccccc         6::::::6       
C:::::C                l::::l   cc:::::::::::::::c        6::::::6        
C:::::C                l::::l  c:::::::::::::::::c       6::::::6         
C:::::C                l::::l c:::::::cccccc:::::c      6::::::::66666    
C:::::C                l::::l c::::::c     ccccccc     6::::::::::::::66  
C:::::C                l::::l c:::::c                  6::::::66666:::::6 
C:::::C                l::::l c:::::c                  6:::::6     6:::::6
 C:::::C       CCCCCC  l::::l c::::::c     ccccccc     6:::::6     6:::::6
  C:::::CCCCCCCC::::C l::::::lc:::::::cccccc:::::c     6::::::66666::::::6
   CC:::::::::::::::C l::::::l c:::::::::::::::::c      66:::::::::::::66 
     CCC::::::::::::C l::::::l  cc:::::::::::::::c        66:::::::::66   
        CCCCCCCCCCCCC llllllll    cccccccccccccccc          666666666
|\__________________________________________________________________________/|
|������������ ���� ������������ Calc 6	                                     |
|                                    ��� ��� El_Sonador	                     |
|____________________________________________________________________________|
|��� �������� ������ �� 1
|��� �������� ������ �� 2
|��� �������������� ������ �� 3
|��� �������� ������ �� 4
|��� ������ ������ �� 5
|��� ���� ������ �� 6
"""
add = 1
rem = 2
mul = 3
div = 4
pon = 5
nun = 6 
while True:
    calc = input("� ������� ��� ����� � : ")
    if calc == nun:
        data1 = input("�������� ��� ������ ~ ")
        res = sqrt(data1)
        print "� ���� �����", res
    data1 = input("�������� ��� ����� ������ ~ ")
    data2 = input("�������� ��� ������� ������ ~ ")
    if calc == add:
        res = data1 + data2
        print "�� ���������� ��� ��������� �����", res
    if calc == rem:
        res = data1 - data2
        print "�� ���������� ��� ��������� �����", res
    if calc == mul:
        res = data1 * data2
        print "�� ���������� ��� ��������������� �����", res
    if calc == div:
     if data1 > data2:
       res = data1 / data2
       print "�� ���������� ��� ��������� �����", res
       rem = data1 % data2
       print "�� �������� ���������", rem
    if calc == div:
     if data1 == data2:
       res = data1 / data2
       print "�o ���������� ��� ��������� �����", res
       rem = data1 % data2
       print "�� �������� ���������", rem
    if calc == pon:
        res = data1 ** data2
        print "�� ���������� ��� ������� �����",res
    if calc < add:
        print "� ������� ",calc," ��� ���������"
    if calc > nun:
        print "� ������� ",calc," ��� ���������"

     


    
