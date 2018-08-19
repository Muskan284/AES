sbox =  [  ['0x63', '0x7c', '0x77', '0x7b', '0xf2', '0x6b', '0x6f', '0xc5', '0x30', '0x01', '0x67', '0x2b', '0xfe', '0xd7', '0xab', '0x76'],
            ['0xca', '0x82', '0xc9', '0x7d', '0xfa', '0x59', '0x47', '0xf0', '0xad', '0xd4', '0xa2', '0xaf', '0x9c', '0xa4', '0x72', '0xc0'],
            ['0xb7', '0xfd', '0x93', '0x26', '0x36', '0x3f', '0xf7', '0xcc', '0x34', '0xa5', '0xe5', '0xf1', '0x71', '0xd8', '0x31', '0x15'],
            ['0x04', '0xc7', '0x23', '0xc3', '0x18', '0x96', '0x05', '0x9a', '0x07', '0x12', '0x80', '0xe2', '0xeb', '0x27', '0xb2', '0x75'],
            ['0x09', '0x83', '0x2c', '0x1a', '0x1b', '0x6e', '0x5a', '0xa0', '0x52', '0x3b', '0xd6', '0xb3', '0x29', '0xe3', '0x2f', '0x84'],
            ['0x53', '0xd1', '0x00', '0xed', '0x20', '0xfc', '0xb1', '0x5b', '0x6a', '0xcb', '0xbe', '0x39', '0x4a', '0x4c', '0x58', '0xcf'], 
            ['0xd0', '0xef', '0xaa', '0xfb', '0x43', '0x4d', '0x33', '0x85', '0x45', '0xf9', '0x02', '0x7f', '0x50', '0x3c', '0x9f', '0xa8'],
            ['0x51', '0xa3', '0x40', '0x8f', '0x92', '0x9d', '0x38', '0xf5', '0xbc', '0xb6', '0xda', '0x21', '0x10', '0xff', '0xf3', '0xd2'],
            ['0xcd', '0x0c', '0x13', '0xec', '0x5f', '0x97', '0x44', '0x17', '0xc4', '0xa7', '0x7e', '0x3d', '0x64', '0x5d', '0x19', '0x73'],
            ['0x60', '0x81', '0x4f', '0xdc', '0x22', '0x2a', '0x90', '0x88', '0x46', '0xee', '0xb8', '0x14', '0xde', '0x5e', '0x0b', '0xdb'],
            ['0xe0', '0x32', '0x3a', '0x0a', '0x49', '0x06', '0x24', '0x5c', '0xc2', '0xd3', '0xac', '0x62', '0x91', '0x95', '0xe4', '0x79'],
            ['0xe7', '0xc8', '0x37', '0x6d', '0x8d', '0xd5', '0x4e', '0xa9', '0x6c', '0x56', '0xf4', '0xea', '0x65', '0x7a', '0xae', '0x08'],
            ['0xba', '0x78', '0x25', '0x2e', '0x1c', '0xa6', '0xb4', '0xc6', '0xe8', '0xdd', '0x74', '0x1f', '0x4b', '0xbd', '0x8b', '0x8a'],
            ['0x70', '0x3e', '0xb5', '0x66', '0x48', '0x03', '0xf6', '0x0e', '0x61', '0x35', '0x57', '0xb9', '0x86', '0xc1', '0x1d', '0x9e'],
            ['0xe1', '0xf8', '0x98', '0x11', '0x69', '0xd9', '0x8e', '0x94', '0x9b', '0x1e', '0x87', '0xe9', '0xce', '0x55', '0x28', '0xdf'],
            ['0x8c', '0xa1', '0x89', '0x0d', '0xbf', '0xe6', '0x42', '0x68', '0x41', '0x99', '0x2d', '0x0f', '0xb0', '0x54', '0xbb', '0x16'],

         ]
Rcon=[['01','00','00','00'],
      ['02','00','00','00'],
      ['04','00','00','00'],
      ['08','00','00','00'],
      ['10','00','00','00'],
      ['20','00','00','00'],
      ['40','00','00','00'],
      ['80','00','00','00'],
      ['1b','00','00','00'],
      ['36','00','00','00']]

Q=[['02','03','01','01'],
   ['01','02','03','01'],
   ['01','01','02','03'],
   ['03','01','01','02']
  ]

def inhx(s):
    di={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    e=s[0]
    r=s[1]
    a=di[e]
    b=di[r]
    c=16*a+b
    return c

def hx(r):
    di={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
    a=r%16
    b=r-a
    c=b/16
    d=di[c]+di[a]
    return d

def  tohex(s):
     byt=[]
     for i in s:
         u=ord(i)
         v=hex(u)
         v=v[2:4]
         byt.append(v)
     return byt

def xor(a,b):
    u=len(a)
    for i in range(4):
        for j in range(4):
            m=inhx(a[i][j])
            n=inhx(b[i][j])
            e=m^n
            a[i][j]=hx(e)
    return a

def xor1(a,b):
    for i in range(4):
        m=inhx(a[i])
        n=inhx(b[i])
        c=m^n
        a[i]=hx(c)
    return a;
        
def shift(s):
        s[1][0], s[1][1], s[1][2], s[1][3] = s[1][1], s[1][2], s[1][3], s[1][0]
        s[2][0], s[2][1], s[2][2], s[2][3] = s[2][2], s[2][3], s[2][0], s[2][1]
        s[3][0], s[3][1], s[3][2], s[3][3] = s[3][3], s[3][0], s[3][1], s[3][2]
        #s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        #s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

def addroundkey(key,plain):
      return xor(plain,key)

def listtomatrix(k):
     m=[[k[0],k[4],k[8],k[12]],
        [k[1],k[5],k[9],k[13]],
        [k[2],k[6],k[10],k[14]],
        [k[3],k[7],k[11],k[15]]]
     return m;

def mix(u,v):
   di={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
   a=inhx(u)
   b=inhx(v)
   if a==1:
      return v
   elif a==2:
      c=di[v[0]]
      if b>=128:
         b=b-128
      b=b*2
      c=di[v[0]]
      if c>=8:
         b=b^inhx('1b')
      return hx(b)
   else:
      d=b
      if b>=128:
         b=b-128
      b=b*2
      c=di[v[0]]
      if c>=8:
         b=b^inhx('1b')
      b=b^d
      return hx(b)



def mixcol(a,b):
    c=[]
    for i in range(4):
        for j in range(4):
          s=0
          for k in range(4):
            d=mix(a[i][k],b[k][j])
            s=s^inhx(d)
          c.append(hx(s))
    c=listtomatrix(c)
    return  c

def eval(r):
   di={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
   m=r[0]
   n=r[1]
   a=di[m]
   b=di[n]
   c=sbox[a][b]
   d=c[2:4]
   return d;


def subbytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j]=eval(s[i][j])
    
def keygen(key,a):
    print(key)
    rot=[key[1][3],key[2][3],key[3][3],key[0][3]]
    for i in range(4):
        rot[i]=eval(rot[i])
    w=xor1(rot,Rcon[a])
    nkey=[]
    c1=[key[0][0],key[1][0],key[2][0],key[3][0]]
    c2=[key[0][1],key[1][1],key[2][1],key[3][1]]
    c3=[key[0][2],key[1][2],key[2][2],key[3][2]]
    c4=[key[0][3],key[1][3],key[2][3],key[3][3]]
    nc1=xor1(w,c1)
    nkey=nkey+nc1;
    nc2=xor1(nc1,c2)
    nkey=nkey+nc2;
    nc3=xor1(nc2,c3)
    nkey=nkey+nc3;
    nc4=xor1(nc3,c4)
    nkey=nkey+nc4;
    nkey=listtomatrix(nkey)
    return nkey

def transpose(d):
    for i in range(4):
        for j in range(i,4):
            temp=d[i][j]
            d[i][j]=d[j][i]
            d[j][i]=temp       
    return d;

def aes(k,p):
    c=tohex(k)
    print(c)
    d=tohex(p)
    print(d)
    e=listtomatrix(c)
    print(e)
    f=listtomatrix(d)
    print(f)
    g=xor(f,e)
    print(g)
    newkey=keygen(e,0)
    print(newkey)
    for i in range(9):
        keyl=newkey
        l=newkey
        print(i)
        subbytes(g)
        print(g)
        shift(g)
        print(g)
        g=mixcol(Q,g)
        print(g)
        keyl=transpose(keyl)
        print(keyl)
        g=addroundkey(keyl,g)
        print(g)
        print("key")
        l=transpose(l)
        newkey=keygen(l,i+1)
        print(newkey)

def main():
       key="Thats my Kung Fu"
       plain="Two One Nine Two"
       aes(key,plain)
       
if __name__=="__main__":
       main() 
   















    
