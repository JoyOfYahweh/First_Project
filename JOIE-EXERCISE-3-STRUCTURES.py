grades = ['3.00','2.00','5.00','2.50','1.75'
          ,'1.75','5.00','1.25','1.00','5.00'
          ,'1.00','2.75','5.00','1.50','2.25']


from collections import Counter
grades_counts = Counter(grades)
top_one = grades_counts.most_common(1)
print "FAILED SUBJECTS THIS SEMESTER:) "
print(top_one)

