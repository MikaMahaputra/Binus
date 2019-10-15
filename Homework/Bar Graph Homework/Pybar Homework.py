import matplotlib.pyplot as p


with open("rickroll.txt") as f:
    for line in f:
        string= str(line)
        line_string= line.split()
        line_dict= {}
   
for word in line_string: 
    if word in line_dict:
        line_dict[word] = line_dict[word]+1
    else:
        line_dict[word] = 1
        
count_list = line_dict[word]+1

count_list = line_dict.values()
indentation = list(range(1, len(count_list)+1))
fig= p.figure(dpi= 100, figsize=(10,5))
p.title("Never Gonna Give You Up By Rick Astley", fontsize = 22, color ="purple")
p.xlabel ("Words",fontsize= 20,color = "green")
p.ylabel ("Frequency", fontsize= 20, color = "teal")
b1= p.bar(indentation, count_list, color = "magenta", edgecolor = "blue")
p.xticks(indentation, line_dict.keys())
p.show