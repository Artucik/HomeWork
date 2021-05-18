# задание 1
output_file = 'e84f9ad49c706008fba3b58e2a1e5b09.txt'

lines = []
with open(output_file, 'r') as o_f:
    for line in o_f:
        line = tuple(line.replace(line[line.find('HTTP'):],'').replace('-','').replace(line[line.find('['):line.rfind(']')+3],
                                                                                '').replace('   ', ' ').split())
        lines.append(line)
print(lines)
lst_id = [i[0] for i in lines]
print(lst_id)
for i in range(len(lst_id)):
    lst_id[i] = lst_id.count(lst_id[i])
print(lst_id)
# задание 2
