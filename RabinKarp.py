def are_equal(s1,s2):
    if len(s1)==len(s2):
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                continue
            else:
                return False
    else:
        return False
    return True

def polynomial_hashing(S,p,x):
    hash=0
    for i in range(len(S)-1,-1,-1):
        hash=(hash*x+ord(S[i]))%p
    return hash

def precompute_hashes(T,P_len,p,x):
    H=[0]*(len(T)-P_len+1)
    H[-1]=polynomial_hashing(T[len(T)-P_len:],p,x)
    y=1
    for i in range(P_len):
        y=(y*x)%p
    for i in range(len(H)-2,-1,-1):
        H[i]=(H[i+1]*x+ord(T[i])-ord(T[i+P_len])*y)%p
    return H

def rabinkarp_algorithm(T,P,p,x):
    H=precompute_hashes(T,len(P),p,x)
    P_hash=polynomial_hashing(P,p,x)
    matching_indices=[]
    for i in range(len(H)):
        if H[i]==P_hash and are_equal(T[i:i+len(P)],P):
            matching_indices.append(i)
    return matching_indices


rabinkarp_algorithm("Hi Hello. How are you? Hello. Hey there. Let's go","Hello",10000019,35)
rabinkarp_algorithm("Hi Hello. How are you? Hello. Hey there. Let's go","Let's",10000019,35)
