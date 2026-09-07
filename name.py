def solution(name):
    return f"Hello, {name}. Welcome to Talent Nation."
print(solution("Ada"))
print(solution("Tunde"))

def solution(name):
    return f"Hello, {name}. Welcome to Talent Nation."
def solution(name, track):
    return f"{name} is starting the {track} track."
    print(solution("Ada", "Data science"))
def solution(name, cohort):
    return f"Name: {name}\nCohort: {cohort}\nStatus: Ready"
def solution(name, a, b, c):
    total = a + b + c 
    average = round(total / 3, 2)
    maximum = max(a, b, c)
    return f"Student: {name}\nSum: {total}\nAverage: {average}\nMaximum: {maximum}"           