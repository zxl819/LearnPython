#
# @lc app=leetcode.cn id=1472 lang=python3
#
# [1472] 设计浏览器历史记录
#

# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.idx = 0


    def visit(self, url: str) -> None:
        del self.stack[self.idx + 1 :]
        self.stack.append(url)
        self.idx += 1


    def back(self, steps: int) -> str:
        self.idx = max(self.idx - steps, 0)
        return self.stack[self.idx]



    def forward(self, steps: int) -> str:
        self.idx = min(self.idx + steps, len(self.stack) - 1)
        return self.stack[self.idx]





# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
