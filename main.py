from collections import Counter
import math
import queue

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if S == "":
        return len(T)
    if T == "":
        return len(S)
    if S[0] == T[0]:
        return MED(S[1:], T[1:])
    else:
        return 1 + min(MED(S[1:], T), MED(S, T[1:]))

def fast_MED(S, T, cache=None):
    if cache is None:
        cache = {}
    if (S, T) in cache:
        return cache[(S, T)]
    if S == "":
        return len(T)
    if T == "":
        return len(S)
    if S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], cache)
    else:
        result = 1 + min(fast_MED(S[1:], T, cache), fast_MED(S, T[1:], cache))
    cache[(S, T)] = result
    return result

def fast_align_MED(S, T, cache=None):
    if cache is None:
        cache = {}
    if (S, T) in cache:
        return cache[(S, T)]
    if S == "":
        return ("-" * len(T), T)
    if T == "":
        return (S, "-" * len(S))
    if S[0] == T[0]:
        edited_S, edited_T = fast_align_MED(S[1:], T[1:], cache)
        result = (S[0] + edited_S, T[0] + edited_T)
    else:
        insert_S, insert_T = fast_align_MED(S, T[1:], cache)
        delete_S, delete_T = fast_align_MED(S[1:], T, cache)
        if (1 + len(insert_S)) <= (1 + len(delete_S)):
            result = ("-" + insert_S, T[0] + insert_T)
        else:
            result = (S[0] + delete_S, "-" + delete_T)
    cache[(S, T)] = result
    return result
