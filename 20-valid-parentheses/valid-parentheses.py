class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                st.append(i)
            else:
                if not st:
                    return False
                elif i == ')':
                    if st[-1]=='(':
                        st.pop()
                    else:
                        return False
                elif i == '}':
                    if st[-1]=='{':
                        st.pop()
                    else:
                        return False
                elif i == ']':
                    if st[-1]=='[':
                        st.pop()
                    else:
                        return False
        return st == []
            