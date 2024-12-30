def total_distance(one,two):
    one.sort()
    two.sort()

    diffs = [(abs(a - b)) for a,b in zip(one,two)]    
    return sum(diffs)

def main():    
    one = []
    two = []
    with open("data/day1-1.txt") as inputfile:
        for line in inputfile:
            [a,b] = line.split("  ")
            one.append(int(a))
            two.append(int(b))

    total = total_distance(one,two)
    print("Answer is %d" % total)

if __name__ == "__main__":
    main()

def test_part1():
    one = [3,4,2,1,3,3]
    two = [4,3,5,3,9,3]

    result = total_distance(one,two)
    
    assert 11 == result
