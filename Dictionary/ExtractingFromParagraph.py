text="""
maximus at molestie egeximus, maximus at molestie eget, auctor ac turpis.
"""
def text_analyzer(text):
    solution={}
    for c in text:
        if c is not ' ':
            if c in solution:
                    solution[c]+=1
            else:
                solution[c]=1
    return solution
print(text_analyzer(text))

