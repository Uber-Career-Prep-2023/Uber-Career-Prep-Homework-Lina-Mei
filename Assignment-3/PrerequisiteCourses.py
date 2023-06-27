"""
Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, 
return a valid order for them to take their courses assuming they only take one course for their major at once.
Time Complexity: O(n*logk) where n represents the number of required courses and k represents the number of relationships between courses
Space Complexity: O(n) where n represents the number of required courses because stacks take up no additional space but we need a set that stores
all the required and visited courses
Data Structure: Stack, set
Algorithm: topological sort
Time Taken: 27 minutes

"""
def dfs(visited, course, prereq, stack):
    visited.add(course)
    if course in prereq:
        for preq in prereq[course]:
            if preq not in visited:
                dfs(visited, preq, prereq, stack)
    stack.append(course)
        
    return

def takeCourses(required, prereq):
    # use stack, only push when all the prereqs have been met
    # visited set to keep track of what nodes we have traversed
    visited = set()
    
    stack = []
    for course in required:
        if course not in visited:
            dfs(visited, course, prereq, stack)
    return stack

def main():
    required = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    prereq =  { "Data Structures": ["Intro to Programming"], 
     "Advanced Algorithms": ["Data Structures"], 
     "Operating Systems": ["Advanced Algorithms"], 
     "Databases": ["Advanced Algorithms"] }
    print(takeCourses(required, prereq)) #["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"] 
    
    req2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    prereq2 = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
    print(takeCourses(req2, prereq2))
    # ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    return

main()
