from typing import List

# 然后你可以在你的代码中使用 List 作为类型提示
def my_function(numbers: List[int]) -> List[int]:
    return [x * 2 for x in numbers]

# 示例使用
result = my_function([1, 2, 3])
print(result)
