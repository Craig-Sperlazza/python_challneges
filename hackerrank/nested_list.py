# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    group_lst = []
    person_lst = []
    score_lst0 = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        score_lst0.append(score)
        person_lst.append(name)
        person_lst.append(score)
        group_lst.append(person_lst)
        person_lst = []
    print(group_lst)
    
    score_set = set(score_lst0)
    score_lst1 = list(score_set)
    score_lst1.sort()
    #print(score_lst)

    second_score = score_lst1[1]
    #print(second_score)

    second_score_names = []
    for person in group_lst:
        if person[1] == second_score:
            second_score_names.append(person[0])
    second_score_names.sort()
    for name in second_score_names:
        print(name)
