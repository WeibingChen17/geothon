import math
def getACirleFromThreePoint(x1, y1, x2, y2, x3, y3):
    A = x1*(y2-y3)-y1*(x2-x3)+x2*y3-x3*y2
    if A < 1e-6:
        return None, None, None
    B = (x1*x1+y1*y1)*(y3-y2)+(x2*x2+y2*y2)*(y1-y3)+(x3*x3+y3*y3)*(y2-y1)
    C = (x1*x1+y1*y1)*(x2-x3)+(x2*x2+y2*y2)*(x3-x1)+(x3*x3+y3*y3)*(x1-x2)
    D = (x1*x1+y1*y1)*(x3*y2-x2*y3)+(x2*x2+y2*y2)*(x1*y3-x3*y1)+(x3*x3+y3*y3)*(x2*y1-x1*y2)
    x = -B/2/A
    y = -C/2/A
    r = math.sqrt(B*B+C*C-4*A*D)/2/A
    return x, y, r

print(getACirleFromThreePoint(-1, 0, 1, 0, 0, 1))
print(getACirleFromThreePoint(0, 0, 1, 0, 0, 1))
print(getACirleFromThreePoint(0, 1, 1, 0, 1+math.sqrt(2)/2, 1+math.sqrt(2)/2))
