from Tkinter import *
import sys
import tkMessageBox
A = """                       
               AAA               
              A:::A              
             A:::::A             
            A:::::::A            
           A:::::::::A           
          A:::::A:::::A          
         A:::::A A:::::A         
        A:::::A   A:::::A        
       A:::::A     A:::::A       
      A:::::AAAAAAAAA:::::A      
     A:::::::::::::::::::::A     
    A:::::AAAAAAAAAAAAA:::::A    
   A:::::A             A:::::A   
  A:::::A               A:::::A  
 A:::::A                 A:::::A 
AAAAAAA                   AAAAAAA
"""
B = """
BBBBBBBBBBBBBBBBB   
B::::::::::::::::B  
B::::::BBBBBB:::::B 
BB:::::B     B:::::B
  B::::B     B:::::B
  B::::B     B:::::B
  B::::BBBBBB:::::B 
  B:::::::::::::BB  
  B::::BBBBBB:::::B 
  B::::B     B:::::B
  B::::B     B:::::B
  B::::B     B:::::B
BB:::::BBBBBB::::::B
B:::::::::::::::::B 
B::::::::::::::::B  
BBBBBBBBBBBBBBBBB
"""
C = """
        CCCCCCCCCCCCC
     CCC::::::::::::C
   CC:::::::::::::::C
  C:::::CCCCCCCC::::C
 C:::::C       CCCCCC
C:::::C              
C:::::C              
C:::::C              
C:::::C              
C:::::C              
C:::::C              
 C:::::C       CCCCCC
  C:::::CCCCCCCC::::C
   CC:::::::::::::::C
     CCC::::::::::::C
        CCCCCCCCCCCCC
"""
D = """
DDDDDDDDDDDDD        
D::::::::::::DDD     
D:::::::::::::::DD   
DDD:::::DDDDD:::::D  
  D:::::D    D:::::D 
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D    D:::::D 
DDD:::::DDDDD:::::D  
D:::::::::::::::DD   
D::::::::::::DDD     
DDDDDDDDDDDDD
"""
E = """
EEEEEEEEEEEEEEEEEEEEEE
E::::::::::::::::::::E
E::::::::::::::::::::E
EE::::::EEEEEEEEE::::E
  E:::::E       EEEEEE
  E:::::E             
  E::::::EEEEEEEEEE   
  E:::::::::::::::E   
  E:::::::::::::::E   
  E::::::EEEEEEEEEE   
  E:::::E             
  E:::::E       EEEEEE
EE::::::EEEEEEEE:::::E
E::::::::::::::::::::E
E::::::::::::::::::::E
EEEEEEEEEEEEEEEEEEEEEE
"""
F = """
FFFFFFFFFFFFFFFFFFFFFF
F::::::::::::::::::::F
F::::::::::::::::::::F
FF::::::FFFFFFFFF::::F
  F:::::F       FFFFFF
  F:::::F             
  F::::::FFFFFFFFFF   
  F:::::::::::::::F   
  F:::::::::::::::F   
  F::::::FFFFFFFFFF   
  F:::::F             
  F:::::F             
FF:::::::FF           
F::::::::FF           
F::::::::FF           
FFFFFFFFFFF
"""
G = """
        GGGGGGGGGGGGG
     GGG::::::::::::G
   GG:::::::::::::::G
  G:::::GGGGGGGG::::G
 G:::::G       GGGGGG
G:::::G              
G:::::G              
G:::::G    GGGGGGGGGG
G:::::G    G::::::::G
G:::::G    GGGGG::::G
G:::::G        G::::G
 G:::::G       G::::G
  G:::::GGGGGGGG::::G
   GG:::::::::::::::G
     GGG::::::GGG:::G
        GGGGGG   GGGG
"""
H = """
HHHHHHHHH     HHHHHHHHH
H:::::::H     H:::::::H
H:::::::H     H:::::::H
HH::::::H     H::::::HH
  H:::::H     H:::::H  
  H:::::H     H:::::H  
  H::::::HHHHH::::::H  
  H:::::::::::::::::H  
  H:::::::::::::::::H  
  H::::::HHHHH::::::H  
  H:::::H     H:::::H  
  H:::::H     H:::::H  
HH::::::H     H::::::HH
H:::::::H     H:::::::H
H:::::::H     H:::::::H
HHHHHHHHH     HHHHHHHHH
"""
I = """
IIIIIIIIII
I::::::::I
I::::::::I
II::::::II
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
II::::::II
I::::::::I
I::::::::I
IIIIIIIIII
"""
J = """
          JJJJJJJJJJJ
          J:::::::::J
          J:::::::::J
          JJ:::::::JJ
            J:::::J  
            J:::::J  
            J:::::J  
            J:::::j  
            J:::::J  
JJJJJJJ     J:::::J  
J:::::J     J:::::J  
J::::::J   J::::::J  
J:::::::JJJ:::::::J  
 JJ:::::::::::::JJ   
   JJ:::::::::JJ     
     JJJJJJJJJ       
"""
K = """
KKKKKKKKK    KKKKKKK
K:::::::K    K:::::K
K:::::::K    K:::::K
K:::::::K   K::::::K
KK::::::K  K:::::KKK
  K:::::K K:::::K   
  K::::::K:::::K    
  K:::::::::::K     
  K:::::::::::K     
  K::::::K:::::K    
  K:::::K K:::::K   
KK::::::K  K:::::KKK
K:::::::K   K::::::K
K:::::::K    K:::::K
K:::::::K    K:::::K
KKKKKKKKK    KKKKKKK
"""
L = """
LLLLLLLLLLL             
L:::::::::L             
L:::::::::L             
LL:::::::LL             
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L         LLLLLL
LL:::::::LLLLLLLLL:::::L
L::::::::::::::::::::::L
L::::::::::::::::::::::L
LLLLLLLLLLLLLLLLLLLLLLLL
"""
M = """
MMMMMMMM               MMMMMMMM
M:::::::M             M:::::::M
M::::::::M           M::::::::M
M:::::::::M         M:::::::::M
M::::::::::M       M::::::::::M
M:::::::::::M     M:::::::::::M
M:::::::M::::M   M::::M:::::::M
M::::::M M::::M M::::M M::::::M
M::::::M  M::::M::::M  M::::::M
M::::::M   M:::::::M   M::::::M
M::::::M    M:::::M    M::::::M
M::::::M     MMMMM     M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
MMMMMMMM               MMMMMMMM
"""
N = """
NNNNNNNN        NNNNNNNN
N:::::::N       N::::::N
N::::::::N      N::::::N
N:::::::::N     N::::::N
N::::::::::N    N::::::N
N:::::::::::N   N::::::N
N:::::::N::::N  N::::::N
N::::::N N::::N N::::::N
N::::::N  N::::N:::::::N
N::::::N   N:::::::::::N
N::::::N    N::::::::::N
N::::::N     N:::::::::N
N::::::N      N::::::::N
N::::::N       N:::::::N
N::::::N        N::::::N
NNNNNNNN         NNNNNNN
"""
O = """
     OOOOOOOOO     
   OO:::::::::OO   
 OO:::::::::::::OO 
O:::::::OOO:::::::O
O::::::O   O::::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O::::::O   O::::::O
O:::::::OOO:::::::O
 OO:::::::::::::OO 
   OO:::::::::OO   
     OOOOOOOOO
"""
P = """
PPPPPPPPPPPPPPPPP   
P::::::::::::::::P  
P::::::PPPPPP:::::P 
PP:::::P     P:::::P
  P::::P     P:::::P
  P::::P     P:::::P
  P::::PPPPPP:::::P 
  P:::::::::::::PP  
  P::::PPPPPPPPP    
  P::::P            
  P::::P            
  P::::P            
PP::::::PP          
P::::::::P          
P::::::::P          
PPPPPPPPPP
"""
Q = """
     QQQQQQQQQ      
   QQ:::::::::QQ    
 QQ:::::::::::::QQ  
Q:::::::QQQ:::::::Q 
Q::::::O   Q::::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O  QQQQ:::::Q 
Q::::::O Q::::::::Q 
Q:::::::QQ::::::::Q 
 QQ::::::::::::::Q  
   QQ:::::::::::Q   
     QQQQQQQQ::::QQ 
             Q:::::Q
              QQQQQQ
"""
R = """
RRRRRRRRRRRRRRRRR   
R::::::::::::::::R  
R::::::RRRRRR:::::R 
RR:::::R     R:::::R
  R::::R     R:::::R
  R::::R     R:::::R
  R::::RRRRRR:::::R 
  R:::::::::::::RR  
  R::::RRRRRR:::::R 
  R::::R     R:::::R
  R::::R     R:::::R
  R::::R     R:::::R
RR:::::R     R:::::R
R::::::R     R:::::R
R::::::R     R:::::R
RRRRRRRR     RRRRRRR
"""
S = """
   SSSSSSSSSSSSSSS 
 SS:::::::::::::::S
S:::::SSSSSS::::::S
S:::::S     SSSSSSS
S:::::S            
S:::::S            
 S::::SSSS         
  SS::::::SSSSS    
    SSS::::::::SS  
       SSSSSS::::S 
            S:::::S
            S:::::S
SSSSSSS     S:::::S
S::::::SSSSSS:::::S
S:::::::::::::::SS 
 SSSSSSSSSSSSSSS
"""
T ="""
TTTTTTTTTTTTTTTTTTTTTTT
T:::::::::::::::::::::T
T:::::::::::::::::::::T
T:::::TT:::::::TT:::::T
TTTTTT  T:::::T  TTTTTT
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
      TT:::::::TT      
      T:::::::::T      
      T:::::::::T      
      TTTTTTTTTTT
"""
U = """
UUUUUUUU     UUUUUUUU
U::::::U     U::::::U
U::::::U     U::::::U
UU:::::U     U:::::UU
 U:::::U     U:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U::::::U   U::::::U 
 U:::::::UUU:::::::U 
  UU:::::::::::::UU  
    UU:::::::::UU    
      UUUUUUUUU
"""
V = """
VVVVVVVV           VVVVVVVV
V::::::V           V::::::V
V::::::V           V::::::V
V::::::V           V::::::V
 V:::::V           V:::::V 
  V:::::V         V:::::V  
   V:::::V       V:::::V   
    V:::::V     V:::::V    
     V:::::V   V:::::V     
      V:::::V V:::::V      
       V:::::V:::::V       
        V:::::::::V        
         V:::::::V         
          V:::::V          
           V:::V           
            VVV
"""
W = """
WWWWWWWW                           WWWWWWWW
W::::::W                           W::::::W
W::::::W                           W::::::W
W::::::W                           W::::::W
 W:::::W           WWWWW           W:::::W 
  W:::::W         W:::::W         W:::::W  
   W:::::W       W:::::::W       W:::::W   
    W:::::W     W:::::::::W     W:::::W    
     W:::::W   W:::::W:::::W   W:::::W     
      W:::::W W:::::W W:::::W W:::::W      
       W:::::W:::::W   W:::::W:::::W       
        W:::::::::W     W:::::::::W        
         W:::::::W       W:::::::W         
          W:::::W         W:::::W          
           W:::W           W:::W           
            WWW             WWW
"""
X = """
XXXXXXX       XXXXXXX
X:::::X       X:::::X
X:::::X       X:::::X
X::::::X     X::::::X
XXX:::::X   X:::::XXX
   X:::::X X:::::X   
    X:::::X:::::X    
     X:::::::::X     
     X:::::::::X     
    X:::::X:::::X    
   X:::::X X:::::X   
XXX:::::X   X:::::XXX
X::::::X     X::::::X
X:::::X       X:::::X
X:::::X       X:::::X
XXXXXXX       XXXXXXX
"""
Y = """
YYYYYYY       YYYYYYY
Y:::::Y       Y:::::Y
Y:::::Y       Y:::::Y
Y::::::Y     Y::::::Y
YYY:::::Y   Y:::::YYY
   Y:::::Y Y:::::Y   
    Y:::::Y:::::Y    
     Y:::::::::Y     
      Y:::::::Y      
       Y:::::Y       
       Y:::::Y       
       Y:::::Y       
       Y:::::Y       
    YYYY:::::YYYY    
    Y:::::::::::Y    
    YYYYYYYYYYYYY
"""
Z = """
ZZZZZZZZZZZZZZZZZZZ
Z:::::::::::::::::Z
Z:::::::::::::::::Z
Z:::ZZZZZZZZ:::::Z 
ZZZZZ     Z:::::Z  
        Z:::::Z    
       Z:::::Z     
      Z:::::Z      
     Z:::::Z       
    Z:::::Z        
   Z:::::Z         
ZZZ:::::Z     ZZZZZ
Z::::::ZZZZZZZZ:::Z
Z:::::::::::::::::Z
Z:::::::::::::::::Z
ZZZZZZZZZZZZZZZZZZZ
"""
a = """
  aaaaaaaaaaaaa   
  a::::::::::::a  
  aaaaaaaaa:::::a 
           a::::a 
    aaaaaaa:::::a 
  aa::::::::::::a 
 a::::aaaa::::::a 
a::::a    a:::::a 
a::::a    a:::::a 
a:::::aaaa::::::a 
 a::::::::::aa:::a
  aaaaaaaaaa  aaaa
"""
b = """
bbbbbbbb            
b::::::b            
b::::::b            
b::::::b            
 b:::::b            
 b:::::bbbbbbbbb    
 b::::::::::::::bb  
 b::::::::::::::::b 
 b:::::bbbbb:::::::b
 b:::::b    b::::::b
 b:::::b     b:::::b
 b:::::b     b:::::b
 b:::::b     b:::::b
 b:::::bbbbbb::::::b
 b::::::::::::::::b 
 b:::::::::::::::b  
 bbbbbbbbbbbbbbbb
"""
c = """
    cccccccccccccccc
  cc:::::::::::::::c
 c:::::::::::::::::c
c:::::::cccccc:::::c
c::::::c     ccccccc
c:::::c             
c:::::c             
c::::::c     ccccccc
c:::::::cccccc:::::c
 c:::::::::::::::::c
  cc:::::::::::::::c
    cccccccccccccccc
"""
d = """
            dddddddd
            d::::::d
            d::::::d
            d::::::d
            d:::::d 
    ddddddddd:::::d 
  dd::::::::::::::d 
 d::::::::::::::::d 
d:::::::ddddd:::::d 
d::::::d    d:::::d 
d:::::d     d:::::d 
d:::::d     d:::::d 
d:::::d     d:::::d 
d::::::ddddd::::::dd
 d:::::::::::::::::d
  d:::::::::ddd::::d
   ddddddddd   ddddd
"""
e = """
    eeeeeeeeeeee    
  ee::::::::::::ee  
 e::::::eeeee:::::ee
e::::::e     e:::::e
e:::::::eeeee::::::e
e:::::::::::::::::e 
e::::::eeeeeeeeeee  
e:::::::e           
e::::::::e          
 e::::::::eeeeeeee  
  ee:::::::::::::e  
    eeeeeeeeeeeeee
"""
f = """
   ffffffffffffffff  
  f::::::::::::::::f 
 f::::::::::::::::::f
 f::::::fffffff:::::f
 f:::::f       ffffff
 f:::::f             
f:::::::ffffff       
f::::::::::::f       
f::::::::::::f       
f:::::::ffffff       
 f:::::f             
 f:::::f             
f:::::::f            
f:::::::f            
f:::::::f            
fffffffff
"""
g = """
   ggggggggg   ggggg
  g:::::::::ggg::::g
 g:::::::::::::::::g
g::::::ggggg::::::gg
g:::::g     g:::::g 
g:::::g     g:::::g 
g:::::g     g:::::g 
g::::::g    g:::::g 
g:::::::ggggg:::::g 
 g::::::::::::::::g 
  gg::::::::::::::g 
    gggggggg::::::g 
            g:::::g 
gggggg      g:::::g 
g:::::gg   gg:::::g 
 g::::::ggg:::::::g 
  gg:::::::::::::g  
    ggg::::::ggg    
       gggggg
"""
h = """
hhhhhhh             
h:::::h             
h:::::h             
h:::::h             
 h::::h hhhhh       
 h::::hh:::::hhh    
 h::::::::::::::hh  
 h:::::::hhh::::::h 
 h::::::h   h::::::h
 h:::::h     h:::::h
 h:::::h     h:::::h
 h:::::h     h:::::h
 h:::::h     h:::::h
 h:::::h     h:::::h
 h:::::h     h:::::h
 hhhhhhh     hhhhhhh
"""
i = """
  iiii  
 i::::i 
  iiii  
        
iiiiiii 
i:::::i 
 i::::i 
 i::::i 
 i::::i 
 i::::i 
 i::::i 
 i::::i 
i::::::i
i::::::i
i::::::i
iiiiiiii
"""
j = """
            jjjj 
           j::::j
            jjjj 
                 
          jjjjjjj
          j:::::j
           j::::j
           j::::j
           j::::j
           j::::j
           j::::j
           j::::j
           j::::j
           j::::j
           j::::j
           j::::j
           j::::j
 jjjj      j::::j
j::::jj   j:::::j
j::::::jjj::::::j
 jj::::::::::::j 
   jjj::::::jjj  
      jjjjjj
"""
k = """
kkkkkkkk           
k::::::k           
k::::::k           
k::::::k           
 k:::::k    kkkkkkk
 k:::::k   k:::::k 
 k:::::k  k:::::k  
 k:::::k k:::::k   
 k::::::k:::::k    
 k:::::::::::k     
 k:::::::::::k     
 k::::::k:::::k    
k::::::k k:::::k   
k::::::k  k:::::k  
k::::::k   k:::::k 
kkkkkkkk    kkkkkkk
"""
l = """
lllllll 
l:::::l 
l:::::l 
l:::::l 
 l::::l 
 l::::l 
 l::::l 
 l::::l 
 l::::l 
 l::::l 
 l::::l 
 l::::l 
l::::::l
l::::::l
l::::::l
llllllll
"""
m = """
   mmmmmmm    mmmmmmm   
 mm:::::::m  m:::::::mm 
m::::::::::mm::::::::::m
m::::::::::::::::::::::m
m:::::mmm::::::mmm:::::m
m::::m   m::::m   m::::m
m::::m   m::::m   m::::m
m::::m   m::::m   m::::m
m::::m   m::::m   m::::m
m::::m   m::::m   m::::m
m::::m   m::::m   m::::m
mmmmmm   mmmmmm   mmmmmm
"""
n = """
nnnn  nnnnnnnn    
n:::nn::::::::nn  
n::::::::::::::nn 
nn:::::::::::::::n
  n:::::nnnn:::::n
  n::::n    n::::n
  n::::n    n::::n
  n::::n    n::::n
  n::::n    n::::n
  n::::n    n::::n
  n::::n    n::::n
  nnnnnn    nnnnnn
  """
o = """
   ooooooooooo   
 oo:::::::::::oo 
o:::::::::::::::o
o:::::ooooo:::::o
o::::o     o::::o
o::::o     o::::o
o::::o     o::::o
o::::o     o::::o
o:::::ooooo:::::o
o:::::::::::::::o
 oo:::::::::::oo 
   ooooooooooo
"""
p = """
ppppp   ppppppppp   
p::::ppp:::::::::p  
p:::::::::::::::::p 
pp::::::ppppp::::::p
 p:::::p     p:::::p
 p:::::p     p:::::p
 p:::::p     p:::::p
 p:::::p    p::::::p
 p:::::ppppp:::::::p
 p::::::::::::::::p 
 p::::::::::::::pp  
 p::::::pppppppp    
 p:::::p            
 p:::::p            
p:::::::p           
p:::::::p           
p:::::::p           
ppppppppp
"""
q = """
   qqqqqqqqq   qqqqq
  q:::::::::qqq::::q
 q:::::::::::::::::q
q::::::qqqqq::::::qq
q:::::q     q:::::q 
q:::::q     q:::::q 
q:::::q     q:::::q 
q::::::q    q:::::q 
q:::::::qqqqq:::::q 
 q::::::::::::::::q 
  qq::::::::::::::q 
    qqqqqqqq::::::q 
            q:::::q 
            q:::::q 
           q:::::::q
           q:::::::q
           q:::::::q
           qqqqqqqqq
"""
r = """
rrrrr   rrrrrrrrr   
r::::rrr:::::::::r  
r:::::::::::::::::r 
rr::::::rrrrr::::::r
 r:::::r     r:::::r
 r:::::r     rrrrrrr
 r:::::r            
 r:::::r            
 r:::::r            
 r:::::r            
 r:::::r            
 rrrrrrr
"""
s = """
    ssssssssss   
  ss::::::::::s  
ss:::::::::::::s 
s::::::ssss:::::s
 s:::::s  ssssss 
   s::::::s      
      s::::::s   
ssssss   s:::::s 
s:::::ssss::::::s
s::::::::::::::s 
 s:::::::::::ss  
  sssssssssss
"""
t = """
      ttt:::t          
      ttt:::t          
      t:::::t          
      t:::::t          
ttttttt:::::ttttttt    
t:::::::::::::::::t    
t:::::::::::::::::t    
tttttt:::::::tttttt    
      t:::::t          
      t:::::t          
      t:::::t          
      t:::::t    tttttt
      t::::::tttt:::::t
      tt::::::::::::::t
        tt:::::::::::tt
          ttttttttttt
"""
u = """
uuuuuu    uuuuuu  
u::::u    u::::u  
u::::u    u::::u  
u::::u    u::::u  
u::::u    u::::u  
u::::u    u::::u  
u::::u    u::::u  
u:::::uuuu:::::u  
u:::::::::::::::uu
 u:::::::::::::::u
  uu::::::::uu:::u
    uuuuuuuu  uuuu
"""
v = """
vvvvvvv           vvvvvvv
 v:::::v         v:::::v 
  v:::::v       v:::::v  
   v:::::v     v:::::v   
    v:::::v   v:::::v    
     v:::::v v:::::v     
      v:::::v:::::v      
       v:::::::::v       
        v:::::::v        
         v:::::v         
          v:::v          
           vvv
"""
w = """
wwwwwww           wwwww           wwwwwww
 w:::::w         w:::::w         w:::::w 
  w:::::w       w:::::::w       w:::::w  
   w:::::w     w:::::::::w     w:::::w   
    w:::::w   w:::::w:::::w   w:::::w    
     w:::::w w:::::w w:::::w w:::::w     
      w:::::w:::::w   w:::::w:::::w      
       w:::::::::w     w:::::::::w       
        w:::::::w       w:::::::w        
         w:::::w         w:::::w         
          w:::w           w:::w          
           www             www
"""
x = """
xxxxxxx      xxxxxxx
 x:::::x    x:::::x 
  x:::::x  x:::::x  
   x:::::xx:::::x   
    x::::::::::x    
     x::::::::x     
     x::::::::x     
    x::::::::::x    
   x:::::xx:::::x   
  x:::::x  x:::::x  
 x:::::x    x:::::x 
xxxxxxx      xxxxxxx
"""
y = """
yyyyyyy           yyyyyyy
 y:::::y         y:::::y 
  y:::::y       y:::::y  
   y:::::y     y:::::y   
    y:::::y   y:::::y    
     y:::::y y:::::y     
      y:::::y:::::y      
       y:::::::::y       
        y:::::::y        
         y:::::y         
        y:::::y          
       y:::::y           
      y:::::y            
     y:::::y             
    y:::::y              
   y:::::y               
  yyyyyyy
"""
z = """
zzzzzzzzzzzzzzzzz
z:::::::::::::::z
z::::::::::::::z 
zzzzzzzz::::::z  
      z::::::z   
     z::::::z    
    z::::::z     
   z::::::z      
  z::::::zzzzzzzz
 z::::::::::::::z
z:::::::::::::::z
zzzzzzzzzzzzzzzzz
"""
#Big Letters-------------------------------------------------------------
def PrintCharaters():
    Ch = EN.get().strip()
    if Ch == "A":
        text.insert(INSERT, A)
    if Ch == "B":
        text.insert(INSERT, B)
    if Ch == "C":
        text.insert(INSERT, C)
    if Ch == "D":
        text.insert(INSERT, D)
    if Ch == "E":
        text.insert(INSERT, E)
    if Ch == "F":
        text.insert(INSERT, F)
    if Ch == "G":
        text.insert(INSERT, G)
    if Ch == "H":
        text.insert(INSERT, H)
    if Ch == "I":
        text.insert(INSERT, I)
    if Ch == "J":
        text.insert(INSERT, J)
    if Ch == "K":
        text.insert(INSERT, K)
    if Ch == "L":
        text.insert(INSERT, L)
    if Ch == "M":
        text.insert(INSERT, M)
    if Ch == "N":
        text.insert(INSERT, N)
    if Ch == "O":
        text.insert(INSERT, O)
    if Ch == "P":
        text.insert(INSERT, P)
    if Ch == "Q":
        text.insert(INSERT, Q)
    if Ch == "R":
        text.insert(INSERT, R)
    if Ch == "S":
        text.insert(INSERT, S)
    if Ch == "T":
        text.insert(INSERT, T)
    if Ch == "U":
        text.insert(INSERT, U)
    if Ch == "V":
        text.insert(INSERT, V)
    if Ch == "W":
        text.insert(INSERT, W)
    if Ch == "X":
        text.insert(INSERT, X)
    if Ch == "Y":
        text.insert(INSERT, Y)
    if Ch == "Z":
        text.insert(INSERT, Z)
#Small Letters-------------------------------------------------------------
    if Ch == "a":
        text.insert(INSERT, a)
    if Ch == "b":
        text.insert(INSERT, b)
    if Ch == "c":
        text.insert(INSERT, c)
    if Ch == "d":
        text.insert(INSERT, d)
    if Ch == "e":
        text.insert(INSERT, e)
    if Ch == "f":
        text.insert(INSERT, f)
    if Ch == "g":
        text.insert(INSERT, g)
    if Ch == "h":
        text.insert(INSERT, h)
    if Ch == "i":
        text.insert(INSERT, i)
    if Ch == "j":
        text.insert(INSERT, j)
    if Ch == "k":
        text.insert(INSERT, k)
    if Ch == "l":
        text.insert(INSERT, l)
    if Ch == "m":
        text.insert(INSERT, m)
    if Ch == "n":
        text.insert(INSERT, n)
    if Ch == "o":
        text.insert(INSERT, o)
    if Ch == "p":
        text.insert(INSERT, p)
    if Ch == "q":
        text.insert(INSERT, q)
    if Ch == "r":
        text.insert(INSERT, r)
    if Ch == "s":
        text.insert(INSERT, s)
    if Ch == "t":
        text.insert(INSERT, t)
    if Ch == "u":
        text.insert(INSERT, u)
    if Ch == "v":
        text.insert(INSERT, v)
    if Ch == "w":
        text.insert(INSERT, w)
    if Ch == "x":
        text.insert(INSERT, x)
    if Ch == "y":
        text.insert(INSERT, y)
    if Ch == "z":
        text.insert(INSERT, z)
    else:
        pass
def Save_in_txt_file():
    File = open("Ascii Art file.txt","wb")
    File.write(text.get(CURRENT, INSERT));
    File.close()
def Load_Settings():
    Optionsfile=open('Settings.AAGCF')
    lines=Optionsfile.readlines()
    Backround =  lines[0]
    
    if Backround == "Bgoptr":
        background = "red"
        root.configure(bg=background)
    if Backround == "Bgoptbl":
        background = "blue"
        root.configure(bg=background)
    if Backround == "Bgoptgr":
        background = "Green"
        root.configure(bg=background)
def Default_Settings():
    background = "red"
    root.configure(bg=background)
def Exit():
    sys.exit()
    
def About():
    tkMessageBox.showinfo("About","""
Ascii Art Generator By El Sonador version 1.0 {under develepoment}
""")
def Help():
    tkMessageBox.showinfo("Help","""
Ascii Art Generator is a simple programm you can generate beautiful charaters
for messages chat or for your Text User Interface Programm
Easy to use
Warning  one one charater in textbox.....
Thanks for using Ascii Art Generator
""")
root = Tk()
root.title("Ascii Art Generator GUI v1")
root["padx"] = 40
root["pady"] = 20
background = "red"
root.configure(bg=background)
text = Text(root,font="Consolas")
text.pack()
button = Button(root, text="Generate Charaters", command=PrintCharaters)
button.pack(side = RIGHT)
EN = Entry(root, bd =5)
EN.pack(side = RIGHT)
LAB = Label(root, text="Charaters TextBox >")
LAB.pack( side = RIGHT)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Choices", menu=filemenu)
filemenu.add_command(label="Print Charaters", command=PrintCharaters)
filemenu.add_command(label="Save in text file", command=Save_in_txt_file)
filemenu.add_command(label="Exit",command=Exit)
#----------------------------------------------------------------------------
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=editmenu)
editmenu.add_command(label="Load Settings", command=Load_Settings)
editmenu.add_command(label="Default_Settings", command=Default_Settings)
#=----------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_command(label="About...", command=About)
#--------------------------------------------------------------------  
root.config(menu=menubar)
root.mainloop()
