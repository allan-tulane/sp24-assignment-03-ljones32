from main import MED, fast_MED, fast_align_MED, test_pairs, correct_alignments

def test_MED():
    for source, target in test_pairs:
        result = fast_MED(source, target)
        expected = MED(source, target)
        assert result == expected, f"Failed on {source}, {target}: Expected {expected}, got {result}"

def test_align():
    for i in range(len(test_pairs)):
        source, target = test_pairs[i]
        aligned_source, aligned_target = fast_align_MED(source, target)
        expected_source, expected_target = correct_alignments[i]
        if (aligned_source != expected_source or aligned_target != expected_target):
            print(f"Testing alignment for {source} and {target}")
            print(f"Expected: ({expected_source}, {expected_target})")
            print(f"Got: ({aligned_source}, {aligned_target})")
        assert (aligned_source == expected_source and aligned_target == expected_target), f"Alignment failed for {source}, {target}"
