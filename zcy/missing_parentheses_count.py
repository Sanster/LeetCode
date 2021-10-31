def main(s: str) -> int:
    left_count = 0
    along_right_count = 0
    for c in s:
        if c == "(":
            left_count += 1
        else:
            if left_count > 0:
                # 匹配到了一组
                left_count -= 1
            else:
                # 孤立的右括号，不可能与其它左括号再匹配了
                along_right_count += 1
                left_count = 0

    return left_count + along_right_count


data = [
    ("()", 0),
    ("(", 1),
    (")", 1),
    ("()(", 1),
    (")(", 2),
    ("))(", 3),
    ("(()())", 0),
    ("((())", 1),
]
for s, gt in data:
    assert main(s) == gt
