def get_ranking():
    for stu_a in range(1,4):
        for stu_b in range(1,4):
            for stu_c in range(1,4):
                for stu_d in range(1,4):
                    if (
                            ((stu_a==1 and stu_b==3) is False and (stu_a==1 or stu_b==3) is True) and \
                            ((stu_c==1 and stu_d==4) is False and (stu_c==1 or stu_d==4) is True) and \
                            ((stu_d==2 and stu_a==3) is False and (stu_d==2 or stu_a==3) is True) and \
                            (stu_a!=stu_b and stu_a!=stu_c and stu_a!=stu_d and stu_b!=stu_c and stu_b!=stu_d and \
                            stu_c!=stu_d)
                            ): return [stu_a, stu_b, stu_c, stu_d]

if __name__ == '__main__':
    ranking_result = get_ranking()
    print(ranking_result)
