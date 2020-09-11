'''
Created on 7 de abr de 2020

@author: tsjabrantes
'''
def student_grade(name, grade):
    return '"{} received {}% on the exam".'.format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))