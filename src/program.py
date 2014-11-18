from src.greedySearchEightQueens import greedySearchEightQueens
steps = greedySearchEightQueens([0,1,2,3,4,5,6,7]).execute()
for step in steps:
    print (step)
print("COST: %d" % len(steps))
