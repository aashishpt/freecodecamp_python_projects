
from evaluate import evaluate

def arithmetic_arranger(problems:list,answers=False):
    
    if len(problems)>5:
        return "Error: Too many problems."
    # initiate empty variables needed
    first_str_list = []
    second_str_list = []
    sep_str_list = []
    ans_str_list = []


    exps = problems

    for exp in exps:
        
        # splits the string ['num1','operation','num2']
        exp_split = exp.split()

        # calculates the maximum length of number-string
        l = max(len(exp_split[0]),len(exp_split[2])) 
        
        ans = evaluate(exp)
        if "Error" in ans:
            return ans
            break

        # appends first number  
        # with right justification of l+2 as calculated above 
        first_str_list.append(exp_split[0].rjust(l+2))

        # appends second number with operation symbol and 4 blankspaces 
        # with right justification of l+2 calculated above 
        second_str_list.append((exp_split[1] + " " + exp_split[2].rjust(l)))

        # appends separator line
        sep_str_list.append("-"*(l+2))

        # appends final answer with rjust l+2
        ans_str_list.append(evaluate(exp).rjust(l+2))
    
    
        first =("    ".join(first_str_list))
        second = ("    ".join(second_str_list))
        sep = ("    ".join(sep_str_list))
        ans = ("    ".join(ans_str_list))
    
        res_without_solution = first + '\n' + second + '\n' + sep
        res_with_solution = first + '\n' + second + '\n' + sep + '\n' + ans
        
        if answers == True:
            arranged_problems = res_with_solution
        else:
            arranged_problems = res_without_solution
            

    return arranged_problems