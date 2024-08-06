li = input().split()

if len(li)==6:
  result = int(li[0])
  nums = list(map(int,li[1:3])) # 12
  calc = li[3:5] # 34
  word = li[-1]  # 5
elif len(li)==5:
  result = int(li[0])
  nums = list(map(int,li[1:3])) # 12
  calc = list(li[3]) # 34
  word = li[-1]  # 5

for i in range(2):
  if calc[i]=="+":
    result+=nums[i]
  elif calc[i]=="-":
    result-=nums[i]
  elif calc[i]=="*":
    result*=nums[i]

result = str(result)+word

print(result)