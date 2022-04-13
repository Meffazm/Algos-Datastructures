# Given a list of courses and a list of prerequisites for each course
# (in a form of a dict) output the list of courses sorted in such
# a way that each course appears in this list only after all it's prerequisites.
# If it is not possible, output -1.


def dfs(v, course_order, visited, prerequisites_list):
    visited[v] = True
    for u in prerequisites_list[v]:
        if not visited[u]:
            dfs(u, course_order, visited, prerequisites_list)
    course_order.append(v)


def sortCourses(course_list, prerequisites_dict):
    if len(prerequisites_dict) == 0:
        return course_list

    course_order = []
    prerequisites_list = [[] for i in range(len(course_list))]
    n = len(prerequisites_list)
    visited = [False for i in range(n)]
    for key, values in prerequisites_dict.items():
        for value in values:
            prerequisites_list[value].append(key)
    print(prerequisites_list)
    for v in range(n):
        if not visited[v]:
            dfs(v, course_order, visited, prerequisites_list)
    if len(course_order) == 0:
        return -1
    return course_order[::-1]


course_list = [0, 1, 2, 3]
prerequisites_dict = {0: [1], 1: [2], 2: [0]}

print(sortCourses(course_list, prerequisites_dict))
