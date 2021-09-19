import random
def rohanMultiplication(number) :
    for x in range(1,10+1):
        table = [number*x for x in range(1,10+1)]
    random_index = random.randint(1,9)
    table1 = table[:]
    table1[random_index] = random.randint(table1[random_index]-1,table1[random_index]+1)
    while table1==table:
        random_index1 = random.randint(1, 9)
        table1[random_index1] = random.randint(table1[random_index1] - 1, table1[random_index1] + 1)
    return table1

def  isCorrect(table,number):
    print(table)
    corret_table = [number*x for x in range(1,10+1)]
    for n in range(10+1) :
        if corret_table[n]!=table[n]:
            return f"{table[n]} in index {n} is wrong. The correct number should be {corret_table[n]}.\nThe correct " \
                   f"tale is  {corret_table}"

if __name__ == '__main__':
    which_table_to_print = int(input("Enter the of number of table you want to print.\n"))
    table = rohanMultiplication(which_table_to_print)
    print(isCorrect(table,which_table_to_print))
