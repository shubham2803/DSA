# https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/

def search_pattern(pattern, text):
    p_len = len(pattern)
    t_len = len(text)

    for i in range(t_len - p_len + 1):
        j = 0
        while j < p_len and text[i + j] == pattern[j]:
            j += 1

        if j == p_len:
            print(i)


# Example usage
if __name__ == "__main__":
    # Example 1
    text1 = "AABAACAADAABAABA"
    pattern1 = "AABA"
    print("Example 1:")
    search_pattern(pattern1, text1)

    # Example 2
    text2 = "agd"
    pattern2 = "g"
    print("\nExample 2:")
    search_pattern(pattern2, text2)
