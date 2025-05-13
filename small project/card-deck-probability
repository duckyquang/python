from math import comb

# ————————————————————————————————————————
#  Basic constants and helpers
# ————————————————————————————————————————
TOTAL_HANDS = comb(52, 7)           # 133 784 560
SUIT_WAYS   = {0: 1, 1: 4, 2: 6,    # C(4,k) for k = 0‥4
               3: 4, 4: 1}

# ————————————————————————————————————————
#  Complementary‑counting utilities
# ————————————————————————————————————————
def prob_at_least_pair() -> float:
    """
    P(hand has ≥ one pair) = 1 – P(all 7 cards are different ranks)
    """
    distinct = comb(13, 7) * (4 ** 7)          # choose 7 distinct ranks, one suit each
    return 1.0 - distinct / TOTAL_HANDS


def prob_at_least_triplet() -> float:
    """
    P(hand has ≥ one three‑of‑a‑kind) = 1 – P(no rank appears 3+ times)
    Dynamic‑programming counts the complement where each rank appears 0, 1 or 2 times.
    """
    # dp[r][c] = ways to pick c cards using the first r ranks with max 2 per rank
    dp = [[0] * 8 for _ in range(14)]
    dp[0][0] = 1
    for r in range(13):
        for c in range(8):
            if dp[r][c] == 0:
                continue
            for k in (0, 1, 2):               # pick k cards of this rank (k ≤ 2)
                if c + k <= 7:
                    dp[r + 1][c + k] += dp[r][c] * SUIT_WAYS[k]
    ways_no_triplet = dp[13][7]
    return 1.0 - ways_no_triplet / TOTAL_HANDS


def prob_full_house() -> float:
    """
    P(hand is a full house in 7‑card evaluation: at least one triple + at least one pair, no four‑of‑a‑kind).
    Closed‑form enumeration over the three possible rank‑multiplicity patterns.
    """
    ways = 0

    # Pattern 3‑2‑2 (one triple + two distinct pairs)
    ways += (
        comb(13, 1) *             # triple's rank
        comb(12, 2) *             # two pair ranks
        SUIT_WAYS[3] * SUIT_WAYS[2] * SUIT_WAYS[2]
    )

    # Pattern 3‑2‑1‑1 (one triple + one pair + two kickers)
    ways += (
        comb(13, 1) * comb(12, 1) * comb(11, 2) *
        SUIT_WAYS[3] * SUIT_WAYS[2] * SUIT_WAYS[1] ** 2
    )

    # Pattern 3‑3‑1 (two different triples + one kicker)
    ways += (
        comb(13, 2) * comb(11, 1) *
        SUIT_WAYS[3] ** 2 * SUIT_WAYS[1]
    )

    return ways / TOTAL_HANDS


# ————————————————————————————————————————
#  Quick demonstration
# ————————————————————————————————————————
if __name__ == "__main__":
    print(f"At least one pair:     {prob_at_least_pair():.6%}")
    print(f"At least one triple:   {prob_at_least_triplet():.6%}")
    print(f"Full house:            {prob_full_house():.6%}")
