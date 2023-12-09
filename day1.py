import re

units= ["zero", "one", "two","three","four","five","six","seven","eight","nine"]
text_file=open("day1test.txt","r")
lines=text_file.readlines()
total=0

for line in lines:
    while any(unit in line for unit in units):
        for idx, word in enumerate(units):
            line=line.replace(word, str(idx), 1)
    nums=re.findall(r'\d', line)
    print(nums)
    if len(nums)==1:
        total+=10*int(nums[0])+int(nums[0])
    else:
        total+=10*int(nums[0])+int(nums[-1])
print(total)
