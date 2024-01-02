def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]


    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

   
    index = lcs_table[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[index - 1] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


string1 = "AGGTAB"
string2 = "GXTXAYB"

result = longest_common_subsequence(string1, string2)
print("Longest Common Subsequence:", result)
