import pandas as pd

pd.set_option('display.max_columns', None)
df_employees = pd.DataFrame({'First Name': ['Tom', 'Adam', 'Jane', 'Alice', 'Robert', 'Bob', 'John', 'Frank', 'Eva',
                                            'John', 'Lois'],
                   'Last Name': ['Brown', 'Green', 'Thompson', 'Smith', 'Newman', 'Parker', 'Williams', 'Taylor', 'Evans',
                                 'Lewis', 'White'],
                   'Type': ['Full-time Employee', 'Intern', 'Full-time Employee', 'Part-time Employee',
                            'Full-time Employee', 'Intern', 'Intern', 'Part-time Employee', 'Part-time Employee',
                            'Full-time Employee', 'Part-time Employee'],
                   'Department': ['Administration', 'Technical', 'Administration', 'Technical', 'Management',
                                  'Administration', 'Management', 'Administration', 'Management', 'Technical',
                                  'Management'],
                   'YearsOfExperience': [4, 3, 5, 7, 6, 1, 2, 2, 4, 5, 2],
                   'Salary': [15000, 6000, 9000, 10000, 20000, 3000, 4000, 6000, 12000, 8000, 5500]})

pivotTable = df_employees.pivot_table(
    index='Type',
    columns='Department',
    values='Salary',
    aggfunc={'Salary': ['sum', 'mean', 'count']}
)

print(pivotTable)