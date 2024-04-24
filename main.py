from collections import Counter
import math
import queue

# Define test cases and correct alignments for validation
test_pairs = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
correct_alignments = [('b--ook', 'bac--k'), ('kook-ab-ur-ra', 'kooky-bi-rd--'), ('-ele-phant', 'relev--ant'), ('AAAGAATTCA', 'AAA---T-CA')]

def simple_MED(source, target):
    """Calculate the Minimum Edit Distance using a simple recursive method."""
    if not source:
        return len(target)
    if not target:
        return len(source)
    if source[0] == target[0]:
        return simple_MED(source[1:], target[1:])
    else:
        return 1 + min(simple_MED(source, target[1:]), simple_MED(source[1:], target))

def memoized_MED(source, target, memo={}):
    """Calculate the Minimum Edit Distance using memoization to avoid redundant calculations."""
    if (source, target) in memo:
        return memo[(source, target)]
    if not source:
        return len(target)
    if not target:
        return len(source)
    if source[0] == target[0]:
        memo[(source, target)] = memoized_MED(source[1:], target[1:], memo)
    else:
        memo[(source, target)] = 1 + min(memoized_MED(source, target[1:], memo), memoized_MED(source[1:], target, memo))
    return memo[(source, target)]

def memoized_align_MED(source, target, memo={}):
    """Calculate the Minimum Edit Distance and return aligned sequences using memoization."""
    if (source, target) in memo:
        return memo[(source, target)]
    if not source:
        memo[(source, target)] = ("-" * len(target), target)
        return memo[(source, target)]
    if not target:
        memo[(source, target)] = (source, "-" * len(source))
        return memo[(source, target)]
    if source[0] == target[0]:
        aligned_src, aligned_tgt = memoized_align_MED(source[1:], target[1:], memo)
        memo[(source, target)] = (source[0] + aligned_src, target[0] + aligned_tgt)
    else:
        insert_src, insert_tgt = memoized_align_MED(source, target[1:], memo)
        delete_src, delete_tgt = memoized_align_MED(source[1:], target, memo)
        if 1 + len(insert_src) <= 1 + len(delete_src):
            memo[(source, target)] = ("-" + insert_src, target[0] + insert_tgt)
        else:
            memo[(source, target)] = (source[0] + delete_src, "-" + delete_tgt)
    return memo[(source, target)]