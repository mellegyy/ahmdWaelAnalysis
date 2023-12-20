def align_sequences(x, y, scoring_matrix):
        n = len(x)
        m = len(y)
    
        # Initialize a matrix to store the scores
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        # Initialize the first row and column
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + scoring_matrix[x[i - 1]]['-']
    
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + scoring_matrix['-'][y[j - 1]]
    
        # Fill in the matrix using dynamic programming
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                match_score = dp[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]
                delete_score = dp[i - 1][j] + scoring_matrix[x[i - 1]]['-']
                insert_score = dp[i][j - 1] + scoring_matrix['-'][y[j - 1]]
                dp[i][j] = max(match_score, delete_score, insert_score)
    
        # Traceback to find the alignment and calculate the total score
        aligned_x = ""
        aligned_y = ""
        total_score = 0
        i, j = n, m
        while i > 0 and j > 0:
            current_score = dp[i][j]
            diagonal_score = dp[i - 1][j - 1]
            up_score = dp[i][j - 1]
            left_score = dp[i - 1][j]
    
            if current_score == diagonal_score + scoring_matrix[x[i - 1]][y[j - 1]]:
                aligned_x = x[i - 1] + aligned_x
                aligned_y = y[j - 1] + aligned_y
                total_score += scoring_matrix[x[i - 1]][y[j - 1]]
                i -= 1
                j -= 1
            elif current_score == up_score + scoring_matrix['-'][y[j - 1]]:
                aligned_x = '-' + aligned_x
                aligned_y = y[j - 1] + aligned_y
                total_score += scoring_matrix['-'][y[j - 1]]
                j -= 1
            elif current_score == left_score + scoring_matrix[x[i - 1]]['-']:
                aligned_x = x[i - 1] + aligned_x
                aligned_y = '-' + aligned_y
                total_score += scoring_matrix[x[i - 1]]['-']
                i -= 1
    
        # Add remaining characters if any
        while i > 0:
            aligned_x = x[i - 1] + aligned_x
            aligned_y = '-' + aligned_y
            total_score += scoring_matrix[x[i - 1]]['-']
            i -= 1
    
        while j > 0:
            aligned_x = '-' + aligned_x
            aligned_y = y[j - 1] + aligned_y
            total_score += scoring_matrix['-'][y[j - 1]]
            j -= 1
    
        return aligned_x, aligned_y, total_score
    
    # Test the code with the given sequences and scoring matrix
x = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
scoring_matrix = {
'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
'-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': float('-inf')}
}
    
result_x, result_y, total_score = align_sequences(x, y, scoring_matrix)
    
print("Aligned Sequence X:", result_x)
print("Aligned Sequence Y:", result_y)
print("Total Score:", total_score)
