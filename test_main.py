from main import MED, fast_MED, fast_align_MED, test_cases, alignments

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T), f"Failed on {S}, {T}"

def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        expected_S, expected_T = alignments[i]
        assert (align_S == expected_S and align_T == expected_T), f"Alignment failed for {S}, {T}"
