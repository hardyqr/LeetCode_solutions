# April 14th, 2018 @M3

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def calc(word,i,j):
            if (word == "*"):
                return i*j
            if (word == "+"):
                return i+j
            else:
                return i-j

        def way(input):
            ans = []
            length = len(input)
            if ("+" not in input and "-" not in input and "*" not in input):
                return [int(input)]
            for i in range(length):
                word = input[i]
                if (word == "+" or word == "-" or word == "*"):
                    lhs = input[0:i]
                    rhs = input[i+1:length+1]
                    lhs_eval = way(lhs)
                    rhs_eval = way(rhs)
                    for i in lhs_eval:
                        for j in rhs_eval:
                            product = calc(word,i,j)
                            ans.append(product)
            return ans
        return way(input)
