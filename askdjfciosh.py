a, b = map(int, input().split())
result = (a*60 + 24*60 + b) - 45 
# result = (a*60 + b) - 45 + 24*60*int(bool(((a*60 + b) - 45)<0))
print(result//60%24,  result%60)