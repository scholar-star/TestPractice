n = [int(i) for i in input()]

half = len(n)//2

if(sum(n[:half]) == sum(n[half:])):
    print("LUCKY")
else:
    print("READY")