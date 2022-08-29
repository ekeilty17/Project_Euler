from itertools import permutations, product
from collections import defaultdict

# This function assumes func is commutative and associative
def binary_function_on_list(L, func):
    total = L[0]
    for x in L[1:]:
        total = func(x, total)
    return total

# Note that this function could be made faster by not also calculating the actual expressions
# but I included this functionality because I thought it was cool
#
# TODO: There is still some redundancy due to * and + being associative
#       for example: 1 + (2 + 3) and (1 + 2) + 3 will both be calculated
def arithmetic_expression(digits, operations):
    # The set of targets we can achieve with this set of digits and operations
    targets = defaultdict(list)

    # iterate over all permutations of operations
    for op_perm_indices in product(range(len(operations)), repeat=len(digits)-1):
        op_perm = [operations[index] for index in op_perm_indices]

        # This may be useful in accounting for associativity, but not sure how to use it yet
        """
        # we group operations that are associative
        associative_groups = [ [op_perm[0]] ]
        for i, op in enumerate(op_perm[1:], 1):
            if op["associative"] and op == op_perm[i-1]:
                associative_groups[-1].append( op )
            else:
                associative_groups.append( [op] )

        # for debugging
        symbols = [[op["symbol"] for op in group] for group in associative_groups]
        print(symbols)
        print()
        """

        # for each permuation of operations, iterate over each permutation of digits
        # Note, this and the previous forloop are interchangeable
        for digits_perm in permutations(digits):
            
            # results is a list of all current results
            results = [digits_perm[0]]
            expressions = [str(digits_perm[0])]

            # we iterate through each operation
            for i in range(len(op_perm)):
                op = op_perm[i]

                # this is just an intermediate list
                updated_results = []
                updated_expressions = []
                for result, expression in zip(results, expressions):
                    
                    try:
                        # x ^ y
                        updated_results.append( op["func"](digits_perm[i+1], result) )
                        updated_expressions.append( f"{digits_perm[i+1]} {op['symbol']} " + (f"{expression}" if i == 0 else f"({expression})") )
                    except:
                        # This occurs if we get a divide by 0 error from the division operation
                        # in which case we don't care and skip it
                        pass

                    # if ^ not commutative
                    if not op["commutative"]:
                        try:
                            # we also need to do y ^ x
                            updated_results.append( op["func"](result, digits_perm[i+1]) )
                            updated_expressions.append( (f"{expression}" if i == 0 else f"({expression})") + f" {op['symbol']} {digits_perm[i+1]}" )
                        except:
                            # This occurs if we get a divide by 0 error from the division operation
                            # in which case we don't care and skip it
                            pass
                
                results = updated_results
                expressions = updated_expressions

            # then we add each integer result to targets
            for result, expression in zip(results, expressions):
                if int(result) == result and result > 0:
                    targets[int(result)].append( expression )
    
    # desired output
    sorted_targets = list(sorted(targets.keys()))
    
    """
    # printing stuff
    for result in sorted_targets:
        expressions = targets[result]
        print(result, '=')
        for expr in expressions:
            print('\t', expr)
    """

    return sorted_targets


def brute_force(operations, d):
    
    max_length = 28
    max_digits = [1, 2, 3, 4]

    digits = list(reversed(range(1, d+1)))
    i = 0
    while i < d:
        # This is all the logic to iterate through the digits
        if digits[i] >= 9:
            digits[i] = 0
            i += 1
            continue
        
        digits[i] += 1
        for k in range(i):
            digits[k] = digits[i] + (i-k)   # this ensures that we iterate in strict sorted order (no repeated digits)
        i = 0
        
        # its possible to have digits that are too large from the above, so we just have to check that case
        if any([digit > 9 for digit in digits]):
            continue
        
        # getting all targets for given permutation and the 1 to n consecutive length
        targets = arithmetic_expression(digits, operations=operations)
        length = get_consecutive_length(targets)
        #print(digits, length)
        
        # tracking maximum consecutive length
        if max_length < length:
            max_length = length
            max_digits = list(reversed(digits))

    #print(max_length)
    return max_digits

def get_consecutive_length(L):
    n = 0
    for i in range(len(L)):
        if i+1 == L[i]:
            n += 1
        else:
            break
    return n

def main(operations, d=4):
    max_digits = brute_force(operations, d)
    digit_str = "".join([str(x) for x in max_digits])
    print(f"The set of {d} digits for which the longest set of consecutive positive integers, 1 to n, can be obtained is:", digit_str)
    return digit_str

if __name__ == "__main__":
    def add(a, b):
        return a+b

    def sub(a, b):
        return a-b

    def mult(a, b):
        return a*b

    def div(a, b):
        return a/b
    
    operations = [
        {"name": "addition",        "func": add,    "symbol": "+",  "commutative": True,    "associative": True},
        {"name": "subtraction",     "func": sub,    "symbol": "-",  "commutative": False,   "associative": False},
        {"name": "multiplication",  "func": mult,   "symbol": "*",  "commutative": True,    "associative": True},
        {"name": "division",        "func": div,    "symbol": "/",  "commutative": False,   "associative": False}
    ]
    
    main(operations)