class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if not st:
                    return False
                top = st.pop()
                if (i==')' and top=='(') or (i=='}' and top=='{') or (i==']' and top=='['):
                    continue
                else:
                    return False
        if not st:
            return True
        return False
        