import re

def valid_expressions(input):
    matches = re.findall(r"mul\((\d+),(\d+)\)", input)    
    return [(int(a), int(b)) for a,b in matches]

class ExpressionParser:
    def __init__(self):
        self.enabled = True

    def parse(self, input):
        matches = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", input)    

        expressions = []
        for a,b,do,dont in matches:
            match (a,b,do,dont):
                case (_,_,"do",_):
                    self.enabled = True
                case (_,_,_,"don't"):
                    self.enabled = False
                case (x,y,_,_) if self.enabled:
                    expressions.append((int(x),int(y)))
        
        return expressions
        
def main():
    parser = ExpressionParser()
    expressions = []
    with open("data/day3.txt") as inputfile:
        for line in inputfile:
            expressions += parser.parse(line)

    answer = sum([a * b for a,b, in expressions])

    print("Answer is %d" % answer)

if __name__ == "__main__":
    main()

def test_valid_expressions():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    result = valid_expressions(input)

    assert [(2,4), (5,5), (11,8), (8,5)] == result
    
def test_better_valid_expressions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    parser = ExpressionParser()
    result = parser.parse(input)

    assert [(2,4), (8,5)] == result
    
