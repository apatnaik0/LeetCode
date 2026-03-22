class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for char in s:
            if len(st)!=0:
                if char == '(' or char == '{' or char == '[':
                    st.append(char)
                else:
                    if char == ')' and st[-1]!='(':
                        return False
                    elif char == '}' and st[-1]!='{':
                        return False
                    elif char == ']' and st[-1]!='[':
                        return False
                    st.pop()

            else:
                st.append(char)
        return len(st)==0