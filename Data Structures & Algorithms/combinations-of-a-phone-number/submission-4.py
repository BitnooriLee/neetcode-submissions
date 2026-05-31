class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.l = len(digits)
        output = []
        path = []
        def bt(i):
            if i == self.l:
                output.append("".join(path[:]))
                return

            for ch in self.dic[digits[i]]:
                path.append(ch)
                bt(i+1)
                path.pop()

        bt(0)

        return output
        