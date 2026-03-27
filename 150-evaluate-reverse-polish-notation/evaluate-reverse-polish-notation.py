class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token not in ['+','-','*','/']:
                st.append(int(token))
            else:
                o1 = int(st.pop())
                o2 = int(st.pop())

                if token == '+':
                    ans = o1 + o2
                elif token == '-':
                    ans = o2 - o1
                elif token == '*':
                    ans = o1 * o2
                else:
                    ans = int(o2/o1)
                st.append(ans)
            # print(st)
        return st[0]
