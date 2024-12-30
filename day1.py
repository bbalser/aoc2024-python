def total_distance(one,two):
    one.sort()
    two.sort()

    diffs = [(abs(a - b)) for a,b in zip(one,two)]    
    return sum(diffs)

def similarity_score(one, two):
    counts = dict()
    for n in two:
        counts[n] = counts.get(n, 0) + 1

    return sum(map(lambda n: n * counts.get(n, 0), one))

def main():    
    one = []
    two = []
    with open("data/day1-1.txt") as inputfile:
        for line in inputfile:
            [a,b] = line.split("  ")
            one.append(int(a))
            two.append(int(b))

    total = similarity_score(one,two)
    print("Answer is %d" % total)

if __name__ == "__main__":
    main()

def test_part1():
    one = [3,4,2,1,3,3]
    two = [4,3,5,3,9,3]

    result = total_distance(one,two)
    
    assert 11 == result

def test_part2():
    one = [3,4,2,1,3,3]
    two = [4,3,5,3,9,3]

    result = similarity_score(one,two)
    
    assert 31 == result
    
