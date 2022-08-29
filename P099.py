import numpy as np

def main(base_exp):
    # log(b^e) = e * log(b)
    # and since log() is monotonic, it doesn't change the order of the results
    log_result = [exp * np.log(base) for base, exp in base_exp]
    max_index = np.argmax(log_result) + 1
    
    print(f"The line with the largest numerical value is:", max_index)
    return max_index

if __name__ == "__main__":
    with open("p099_base_exp.txt",'r') as f:
        lines = f.readlines()
    
    base_exp = [line.strip().split(',') for line in lines]
    base_exp = [tuple([int(x) for x in pair]) for pair in base_exp]
    main(base_exp)