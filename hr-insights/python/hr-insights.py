#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 23:20:11 2018

@author: mukuljain
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./HR_comma_sep.csv')

# Old and current Employess satisfaction_level group by salary

#df_leftEmployees = df[ df["left"] == 1 ]
#
#df_leftEmployeesBySalary = df_leftEmployees.groupby(["salary"], as_index = False)['satisfaction_level'].mean()
#
#df_currentEmployees = df[ df["left"] == 0 ]
#
#df_currentEmployeesBySalary = df_currentEmployees.groupby(["salary"], as_index = False)['satisfaction_level'].mean()


# Department wise satisfaction_level

fig, axs = plt.subplots(ncols=2, sharey=False, figsize=(15, 5))

fig.suptitle("Employee Satisfactory Level", color='red')

df_copy = df[ df['left'] == 1 ]
df_byDepartment = df_copy.groupby(["Department", "salary"], as_index=False)["satisfaction_level"].mean()
df_byDepartmentHighSalary = df_byDepartment[ df_byDepartment['salary'] == 'high']
df_byDepartmentMediumSalary = df_byDepartment[ df_byDepartment['salary'] == 'medium']
df_byDepartmentLowSalary = df_byDepartment[ df_byDepartment['salary'] == 'low']
#df_byDepartment = df_byDepartment.sort_values(["satisfaction_level"])
#df_byDepartment["depSalary"] = df_byDepartment["Department"] + df_byDepartment["salary"]

ax1 = axs[0]
ax1.set_title('Alumni Satisfactory Rate')
ax1.plot(df_byDepartmentHighSalary["Department"], df_byDepartmentHighSalary["satisfaction_level"], label='High')
ax1.plot(df_byDepartmentMediumSalary["Department"], df_byDepartmentMediumSalary["satisfaction_level"], label='Medium')
ax1.plot(df_byDepartmentLowSalary["Department"], df_byDepartmentLowSalary["satisfaction_level"], label='Low')
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')
ax1.legend()
ax1.set_xlabel("Departments")
ax1.set_ylabel("Satisfaction Level")


df_copy = df[ df['left'] == 0 ]
df_byDepartment = df_copy.groupby(["Department", "salary"], as_index=False)["satisfaction_level"].mean()
df_byDepartmentHighSalary = df_byDepartment[ df_byDepartment['salary'] == 'high']
df_byDepartmentMediumSalary = df_byDepartment[ df_byDepartment['salary'] == 'medium']
df_byDepartmentLowSalary = df_byDepartment[ df_byDepartment['salary'] == 'low']


ax1 = axs[1]
ax1.set_title('Current Employees Satisfactory Rate')
ax1.plot(df_byDepartmentHighSalary["Department"], df_byDepartmentHighSalary["satisfaction_level"], label='High')
ax1.plot(df_byDepartmentMediumSalary["Department"], df_byDepartmentMediumSalary["satisfaction_level"], label='Medium')
ax1.plot(df_byDepartmentLowSalary["Department"], df_byDepartmentLowSalary["satisfaction_level"], label='Low')
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')
ax1.legend()
ax1.set_xlabel("Departments")

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')
plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')
plt.show()
