# CMPS 2200 Assignment 3
## Answers

**Name:**London Jones


Place all written answers from `assignment-03.md` here for easier grading.

1a) To convert a sum N into the fewest possible coins in Geometrica, employ this efficient greedy strategy:

    Begin by selecting the largest denomination not exceeding N, which is 2^k, where k is the greatest integer for which 2^k <= N.
    Use the maximum number of this denomination possible without surpassing N, calculated as N // 2^k coins of 2^k.
    Deduct the total value of these coins from N, yielding a new remaining amount N'.
    Continue this method with the subsequent lower denomination for N' until N equals 0.
    The outcome is a collection of coins that sum to N using the minimum number of coins.

1b) The coin system in Geometrica lends itself well to the greedy algorithm, validated through its inherent greedy choice and optimal substructure properties:

Greedy Choice Property: Selecting the maximum available denomination at each step ensures minimal coin usage. This is because using a smaller denomination would require more coins to equal the original amount.

Optimal Substructure: The problem of exchanging N using the largest coin 2^k can be decomposed into exchanging the remainder N - 2^k. The best method to exchange N includes the best method for N - 2^k, plus the coin 2^k. The subsequent subproblems are unaffected by the initial choice, allowing them to be solved optimally independently.

1c) Work (W) and Span (S):

    Work: The principal operations are divisions and modulo calculations to determine the highest denomination and the number of coins needed. For denominations as powers of 2, these operations amount to O(log N), as each step halves the problem size.
    Span: The sequential dependency of steps dictates the span as O(log N), since the algorithm progresses to the next step only after completing the previous one.

2a) Consider making change for N = 8 dollars with denominations {1, 3, 4, 6} in Fortuito.

    Greedy Algorithm: Choosing the largest denomination less than 8 leads to selecting a 6-dollar coin, then two 1-dollar coins for a total of 3 coins.
    Optimal Solution: Alternatively, using two 4-dollar coins results in just 2 coins, indicating a more efficient solution.

This illustrates the failure of the greedy approach to always yield the least number of coins in Fortuito.

2b) The optimal substructure in Fortuito's coin system can be stated thus:

    Property: The minimum coins needed for N using denominations D is derived from the minimum of the sums of coins required for N - d for each denomination d in D plus one extra coin of denomination d.
    Proof: Assume an optimal configuration for N. Removing a coin of denomination d should leave an optimal configuration for N - d. If a better configuration for N - d existed, replacing the configuration for N - d would yield a better overall solution, which contradicts the assumption. Thus, the problem exhibits the optimal substructure property.

2c) A dynamic programming approach using optimal substructure:

    Define dp[i] as the minimum number of coins needed for amount i.

    Start with dp[0] = 0, and set dp[i] for other amounts as a large number, indicating initially unknown minimums.

    For each amount i from 1 to N, and each denomination d, update dp[i] to dp[i] = min(dp[i], dp[i - d] + 1) if i >= d.

    The final dp[N] gives the fewest coins required for N.

    Work (W): This approach involves O(N * k) operations, iterating over amounts up to N and examining each denomination.

    Span (S): If dp[i] updates are parallelized, the span is O(N); if sequential, it increases to O(N * k).