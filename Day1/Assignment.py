import math
class Siva:
    def prime(self,n):
        if n==2 or n==3:
            return True
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                return False
        return True
    def baby1(self,a,b): # Magic prime
        print("Magic Primes are")
        for i in range(a,b+1):
            if(self.prime(i)):
                rev = 0 
                k = i
                while(k>0):
                    rev = rev*10+(k%10)
                    k = k//10
                if(self.prime(rev)):
                    print(i,end=" ")
    
    def baby2(self,a,b): # Neon Number
        print("\nNeon Numbers are")
        for i in range(a,b+1):
            sq = i**2
            s = 0
            while(sq>0):
                s+=sq%10
                sq = sq//10
            if(s==i):
                print(i,end=" ")
obj = Siva()
obj.baby1(1,100)
obj.baby2(0,1000)
