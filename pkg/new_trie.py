import json
class Trie:
    def advanced_find_matches(self, document, variations):
        result_set = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i,len(document)):
                char = document[j]
                if char in variations:
                    char = variations.get(char)
                if char not in current_level:
                    break
                current_level = current_level.get(char)
                if self.end_symbol in current_level:
                    result_set.add(document[i:j+1])
            
        return result_set
        











    # 所以它求的是, tier树中的最长前缀
    def longest_common_prefix(self):
        prefix = ""
        current = self.root

        while True:
            children = list(current.keys())

            # 1️⃣ 如果当前节点是某个单词的结尾，必须停
            if self.end_symbol in children:
                break

            # 2️⃣ 只有一个孩子，才能继续
            if len(children) == 1:
                char = children[0]
                prefix += char
                current = current[char]
            else:
                break

        return prefix


    # 所以是从左往右, i不断缩小, 染过内部循环无法找到, 则跳出.开始另一个开头词

#     从左往右扫描
# i 依次向右移动（不是缩小）
# 对每一个 i：

# 从 Trie 的根节点开始

# 用 j = i → len(document)-1 向右尝试匹配

# 一旦某个字符不在 Trie 当前层

# break 内层循环

# 立刻换下一个起始位置 i+1
    def find_matches(self, document:str):
        result_set = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                if document[j] not in current_level:
                    break
                else:
                    current_level = current_level.get(document[j])
                if self.end_symbol in current_level:
                    result_set.add(document[i:j+1])
        return result_set    

    def search_level(self, current_level, current_prefix, words):
        # If this level marks the end of a word, record the prefix
        # 如果有当前终结的存在, current_prefix 添加
        if self.end_symbol in current_level:
            words.append(current_prefix)

        # Traverse children in alphabetical order
        for char in sorted(current_level.keys()):
            if char == self.end_symbol:
                continue
            # Extend prefix (do not modify in place)
            # 子树, 前缀也要加大, list
            self.search_level(
                current_level[char],
                current_prefix + char,
                words
            )

        return words
    # 以prefix 为前缀的词.
    def words_with_prefix(self, prefix):
        words = []
        current_level = self.root

        # Walk the trie according to the prefix
        for char in prefix:
            if char not in current_level:
                return []  # No words with this prefix
            current_level = current_level[char]

        # Collect all words starting from this level
        #第一个参数是prefix-based 的dic 
        return self.search_level(current_level, prefix, words)


    def add(self, word):
        current_level = 0
        current_dict = self.root
        for c in word:
            if c not in current_dict:
                current_dict.update([(c,{})])
            current_dict = current_dict.get(c)
        current_dict[self.end_symbol] = True

    def exists(self, word):
        current_dict = self.root
        for c in word:
            if c not in current_dict:
                return False
            current_dict = current_dict.get(c)
        return self.end_symbol in current_dict

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

run_cases = [
    (
        [
            "darnit",
            "nope",
            "bad",
        ],
        "This is a d@rn1t test with b@d words!",
        {
            "@": "a",
            "1": "i",
            "4": "a",
            "!": "i",
        },
        [
            "b@d",
            "d@rn1t",
        ],
    ),
    (
        [
            "darn",
            "shoot",
            "gosh",
        ],
        "h3ck this fudg!ng thing",
        {
            "@": "a",
            "3": "e",
        },
        [],
    ),
    (
        [
            "dang",
            "darn",
            "heck",
            "gosh",
        ],
        "d@ng it to h3ck",
        {
            "@": "a",
            "3": "e",
        },
        ["d@ng", "h3ck"],
    ),
]
submit_cases = run_cases + [
    (
        [
            "darn",
            "shoot",
            "fudging",
        ],
        "sh00t, I hate this fudg!ng assignment",
        {
            "@": "a",
            "3": "e",
            "0": "o",
            "!": "i",
        },
        ["sh00t", "fudg!ng"],
    ),
]


def test(words, document, variations, expected_matches):
    print("---------------------------------")
    print("Document:")
    print(document)
    print(f"Variations: {variations}")
    print(f"Expected matches: {sorted(expected_matches)}")
    try:
        trie = Trie()
        for word in words:
            trie.add(word)
        actual = sorted(trie.advanced_find_matches(document, variations))
        print(f"Actual matches: {actual}")
        if actual == sorted(expected_matches):
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()