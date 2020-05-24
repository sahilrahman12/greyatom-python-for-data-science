import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset.


# The path for the dataset has been stored in a variable path
path = pd.read_csv("file.csv")

# Create dataframe bank by passing the path of the file
bank = pd.DataFrame(path)

# Create the variable 'categorical_var' and using 'df.select_dtypes(include = 'object')' check all categorical values.
categorical_var = bank.select_dtypes(include='object')

# print 'categorical_var'
# print(categorical_var)

# Create the variable 'numerical_var' and using 'df.select_dtypes(include = 'number')' check all categorical values.
numerical_var = bank.select_dtypes(include='number')

# print 'numerical_var'
# print(numerical_var)










# Step 2: Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them.


# From the dataframe bank, drop the column Loan_ID to create a new dataframe banks
banks = bank.drop("Loan_ID", axis=1)

# To see the null values, use "isnull().sum()" function and print it.
# print(banks.isnull().sum())

# Calculate mode for the dataframe banks and store in bank_mode
bank_mode = banks.mode()
# print(bank_mode)

# Fill missing(NaN) values of banks with bank_mode and store the cleaned dataframe back in banks.
banks = banks.fillna(bank_mode.iloc[0])

# Check if all the missing values (NaN) are filled.
# banks.shape should be (614 , 12) and banks.isnull().sum().values.sum() should be 0.
# print(banks.isnull().sum().values.sum())









# Step 3: Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person.


# Generate a pivot table with index as 'Gender', 'Married', 'Self_Employed' and values as 'LoanAmount', using mean aggregation
# Store the result in a variable called 'avg_loan_amount'
avg_loan_amount = pd.pivot_table(banks, index=["Gender","Married","Self_Employed"], values="LoanAmount", aggfunc=np.mean)
# print(avg_loan_amount)

# Print and check avg_loan_amount['LoanAmount'][1],2 should be 125.27.
# print(avg_loan_amount['LoanAmount'][1],2)









# Now let's check the percentage of loan approved based on a person's employment type.


# Create variable 'loan_approved_se' and store the count of results where Self_Employed == Yes and Loan_Status == Y.
loan_approved_se = len(banks[(banks["Self_Employed"]=='Yes') & (banks["Loan_Status"]=="Y")])
# print(loan_approved_se)

# Create variable 'loan_approved_nse' and store the count of results where Self_Employed == No and Loan_Status == Y.
loan_approved_nse = len(banks[(banks["Self_Employed"]=='No') & (banks["Loan_Status"]=="Y")])
# print(loan_approved_nse)

# Loan_Status count is given as 614.
Loan_Status_count = 614

# Calculate the percentage of loan approval for self-employed people and store result in variable 'percentage_se'.
percentage_se = (loan_approved_se*100)/Loan_Status_count
# print(percentage_se)

# Calculate the percentage of loan approval for people who are not self-employed and store the result in variable 'percentage_nse'.
percentage_nse = (loan_approved_nse*100)/Loan_Status_count
# print(percentage_nse)

# percentage_se, rounded off to two places, should be 9.12.
# percentage_nse, rounded off to two places, should be 59.61.










# Step 5: A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.


# Use "apply()" function to convert Loan_Amount_Term which is in months to a year and store the result in a variable 'loan_term'.
def month(fun):
    return fun/12
loan_term = banks['Loan_Amount_Term'].apply(func=month)


# Find the number of applicants having loan amount term greater than or equal to 25 years and store them in a variable called 'big_loan_term'.
big_loan_term = loan_term[loan_term>=25].count()

# big_loan_term should be 554.
# print(big_loan_term)










# Step 6: Now let's check the average income of an applicant and the average loan given to a person based on their income.


# Groupby the 'banks' dataframe by Loan_Status and store the result in a variable called 'loan_groupby'
loan_groupby = banks.groupby(banks['Loan_Status'])
# print(loan_groupby.groups)

# Subset 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History'] and store the subsetted dataframe back in 'loan_groupby'
loan_groupby = banks.groupby(banks['Loan_Status'])[['ApplicantIncome', 'Credit_History']]
# print(loan_groupby.groups)

# Then find the mean of 'loan_groupby' and store the result in a new variable 'mean_values'
mean_values = loan_groupby.mean()

# Print and check mean_values.iloc[1,0], 2 should be 5384.07 when rounded off to two palces.
# print(mean_values.iloc[1,0],2)









# Visualization for Company Stakeholders

# Step 1: Let's start with the simple task of visualizing the company's record with respect to loan approvals.


# Save the value counts of Loan_Status in a variable called loan_status using value_counts()
loan_status = banks["Loan_Status"].value_counts()
# print(loan_status)

# Plot a bar graph of loan_status
loan_status.plot.bar()
# plt.show()










# Step 2: Everyone needs money
# The company provides financial assistance across the different regions of the country. One interesting statistic that stakeholders want to see is the loan approval distribution across the regions.


# Group the 'data' dataframe by Property_Area and Loan_Status and store it in a variable called 'property_and_loan'
property_and_loan = banks.groupby(["Property_Area","Loan_Status"])


# Use the .size() method on 'property_and_loan' and then use .unstack() and save it back to 'property_and_loan'
property_and_loan = property_and_loan.size().unstack()


# Plot an unstacked bar plot of property_and_loan (It is similar to creating a stacked bar plot except change the parameter 'stacked' to False)
property_and_loan.plot.bar(stacked=False)


# Name the x-axis as Property Area
plt.xlabel('Property Area')


# Name the y-axis as Loan Status
plt.ylabel('Loan Status')


# Rotate the labels of x-axis by 45o
plt.xticks(rotation=45)
# plt.show()










# Step 3: Expensive Education
# Higher education has always been an expensive endeavour for people but it results in better career opportunities and stability in life. But does higher education result in a better guarantee in issuing loans?


# Group the 'data' dataframe by Education and Loan_Status and store it in a variable called 'education_and_loan'
education_and_loan = banks.groupby(["Education","Loan_Status"])


# Use the .size() method on 'education_and_loan' and then use .unstack() and save it back to 'education_and_loan'
education_and_loan = education_and_loan.size().unstack()


# Plot an stacked bar plot of education_and_loan
education_and_loan.plot.bar(stacked=True)


# Name the x-axis as Education Status
plt.xlabel("Education Status")


# Name the y-axis as Loan Status
plt.ylabel("Loan Status")


# Rotate the labels of x-axis by 45o
plt.xticks(rotation=45)










# Step 4: Smarter and Richer?
# After seeing the loan status distribution, let's check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values


# Create a dataframe called 'graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Graduate'"
graduate = banks[banks['Education']=='Graduate']


# Create a dataframe called 'not_graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Not Graduate'"
not_graduate = banks[banks['Education']=='Not Graduate']


# Plot a density plot LoanAmount of 'graduate' dataframe using "Series.plot()" and pass the parameter kind='density' and label='Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')


# Do the same for LoanAmount of 'not_graduate' dataframe but with label='Not Graduate'
not_graduate["LoanAmount"].plot(kind='density', label='Not Graduate')










# Step 5: Income vs Loan
# For any financial institution to be successful in its loan lending system, there has to be a correlation between the borrower's income and loan amount he is lent. Let's see how our company fares in that respect:


# Create three subplots with (nrows = 3 , ncols = 1) and store it in variable's fig ,(ax_1,ax_2,ax_3)
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3, ncols=1, figsize=(20,8))


# Since both are continuous variables, plot scatter plot between 'ApplicantIncome' and LoanAmount using ax_1. Set axis title as Applicant Income
ax_1.scatter(banks['ApplicantIncome'],banks["LoanAmount"])
ax_1.set(title='Applicant Income')


# Plot scatter plot between 'CoapplicantIncome' and LoanAmount using ax_2. Set axis title as Coapplicant Income
ax_2.scatter(banks['CoapplicantIncome'], banks['LoanAmount'])
ax_2.set(title='Coapplicant Income')


# Create a new column in the dataframe called 'TotalIncome' which is a sum of the values of columns ApplicantIncome and CoapplicantIncome
banks['TotalIncome'] = banks["ApplicantIncome"] + banks["CoapplicantIncome"]


# Plot scatter plot between 'TotalIncome' and LoanAmount using ax_3. Set axis title as Total Income
ax_3.scatter(banks['TotalIncome'],banks['LoanAmount'])
ax_3.set(title="Total Income")


# plt.show()
