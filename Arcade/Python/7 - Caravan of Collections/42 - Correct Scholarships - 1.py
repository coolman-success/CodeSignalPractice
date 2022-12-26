def solution(bestStudents, scholarships, allStudents):
    return all(b in scholarships for b in bestStudents) and all(s in allStudents for s in scholarships) and len(scholarships) < len(allStudents)
