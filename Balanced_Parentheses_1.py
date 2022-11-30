class solution:
    def isval(self,s):
        st=[]
        char={"(":")","{":"}","[":"]"}
        for i in s:
            if i in char:
                st.append(i)
            elif len(st)==0 or char[st.pop()]!=i:
                return False
        return len(st)==0
print(solution().isval(input()))