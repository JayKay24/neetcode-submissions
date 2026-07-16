class Solution:
    def generateParenthesis(
        self, 
        n: int, 
        open_rem: None | int = None, 
        closed_rem: None | int = None, 
        current=""
    ) -> List[str]:
        if open_rem is None:
            open_rem = n
        if closed_rem is None:
            closed_rem = n
        
        if open_rem == 0 and closed_rem == 0:
            return [current]
        
        result = []
        
        if open_rem > 0:
            result.extend(self.generateParenthesis(n, open_rem - 1, closed_rem, current + "("))
        if closed_rem > open_rem:
            result.extend(self.generateParenthesis(n, open_rem, closed_rem - 1, current + ")"))
        
        return result
        