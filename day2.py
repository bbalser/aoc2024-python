
def chunks(list, **kwargs):
    step = kwargs.get("step", 1)
    count = kwargs.get("count", 2)

    for i in range(0, len(list), step):
        entry = list[i:i+count]
        if len(entry) == count:
            yield entry

def is_safe(report):
    pairs = list(chunks(report))
    diffs = [abs(e[0] - e[1]) for e in pairs]

    all_descending = all(p[0] > p[1] for p in pairs)
    all_ascending = all(p[0] < p[1] for p in pairs)
    safe_levels = all(d >= 1 and d <= 3 for d in diffs)

    return (all_ascending or all_descending) and safe_levels

def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(0, len(report)):
        report_copy = report.copy()
        report_copy.pop(i)
        if is_safe(report_copy):
            return True
    
    return False

def main():
    reports = []
    with open("data/day2.txt") as inputfile:
        for line in inputfile:
            reports.append(list(map(int,line.split(" "))))
        
    safe_reports = list(filter(lambda b: b == True, map(is_safe_with_dampener, reports)))
    print("Safe reports = %d" % len(safe_reports))        

if __name__ == "__main__":
    main()

def test_chunks():
    l = [7,6,4,2,1]

    result = list(chunks(l))

    assert [[7,6],[6,4],[4,2],[2,1]] == result

import pytest

@pytest.mark.parametrize("input,expected", [
                         ([7,6,4,2,1], True),
                         ([1,2,7,8,9], False),
                         ([9,7,6,2,1], False),
                         ([1,3,2,4,5], False),
                         ([8,6,4,4,1], False),
                         ([1,3,6,7,9], True)
                     ])
def test_is_safe(input, expected):
    assert expected == is_safe(input)

@pytest.mark.parametrize("input,expected", [
                         ([7,6,4,2,1], True),
                         ([1,2,7,8,9], False),
                         ([9,7,6,2,1], False),
                         ([1,3,2,4,5], True),
                         ([8,6,4,4,1], True),
                         ([1,3,6,7,9], True)
                     ])
def test_is_safe_with_dampener(input, expected):
    assert expected == is_safe_with_dampener(input)
