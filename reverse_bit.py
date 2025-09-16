keyboard = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}
def letterCombinations(digits: str):
    res = []
    if not digits:
        return res

    def bt(permutation, digits, pointer=0):
        if pointer >= len(digits):
            res.append(permutation)
            return
        print(permutation, digits, pointer, digits[pointer])
        for letter in keyboard[digits[pointer]]:
            bt(permutation+letter, digits, pointer + 1)
        
    bt("", digits)
    return res

print(letterCombinations("23"))

