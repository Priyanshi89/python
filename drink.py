# n = int(input())
# k = int(input())
# l = int(input())
# c = int(input())
# d = int(input())
# p = int(input())
# nl = int(input())
# np = int(input())
n,k,l,c,d,p,nl,np = list(map(int, input().split()))
multiplication = (k*l)/nl
ans = c*d
aa = p/np
final_ans=int(min(multiplication,ans,aa)/n)
print(final_ans)

#n,k,l,c,d,p,nl,np = list(map(int, input().split()))
