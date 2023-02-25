




output = open('diag_out.csv', 'w')

i = 1

with open('diagnosis1.csv', 'r') as file:
    for line in file:
        string_w = str(i) + ',' + line
        output.write(string_w)
        i +=1

output.close()