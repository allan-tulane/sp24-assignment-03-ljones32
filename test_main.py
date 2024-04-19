from main import MED, fast_MED, fast_align_MED, test_cases, alignments

def test_MED():
    for S, T in test_cases:
        result = fast_MED(S, T)
        expected = MED(S, T)
        assert result == expected, f"Failed on {S}, {T}: Expected {expected}, got {result}"

def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        expected_S, expected_T = alignments[i]
        if (align_S != expected_S or align_T != expected_T):
            print(f"Testing alignment for {S} and {T}")
            print(f"Expected: ({expected_S}, {expected_T})")
            print(f"Got: ({align_S}, {align_T})")
        assert (align_S == expected_S and align_T == expected_T), f"Alignment failed for {S}, {T}"
