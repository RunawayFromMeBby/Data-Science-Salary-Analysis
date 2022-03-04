Data Scientist Job Guide

Link to our presentation: https://docs.google.com/presentation/d/1z3JK7XNI6e-DHzWn-S0Kh8yuyXbcSnIgdJJ5LVjKLf8/edit?usp=sharing

The purpose of our project is to explore the wide range of salaries among entry-level data scientist roles and inform job seekers about the factors that could affect their salary.

By performing these analyses, we hope that new data scientists entering the field can be as educated as possible about their job prospects and land the best position based on what is important to them.

Our team consists of Alvaro Padilla, Jorge Angon, Lisa Hong, and Victor Tavares.

The questions that our team will answer are:

1. How does company size impact the salary of a data scientist?
2. Is there a correlation between job satisfaction  and salary?
3. How does job sector and location impact the salary of a data scientist?

We obtained our Data Scientist Salary dataset from Kaggle and cleaned the dataset by dropping all the columns that were not relevant to our analysis and dropping data that corresponded to non-entry-level positions.


Analysis #1: Company Size


For our first analysis, we looked at how company size affects average salary

We began by defining small, medium, and large companies in terms of number of employees. We define small companies as having 1-200 employees, medium companies as having 201-1000 employees,and large companies as having 1001-10000+ employees.

We created a new ‘Size Category’ column in our dataframe and created a boxplot to get a more detailed data distribution comparison between the company sizes. The boxplot revealed that the data for medium sized companies contained a lot of outliers. 

If we ignore the outliers and just look at the box and whiskers, the median average salaries for small/large company sizes are relatively the same, and medium sized companies have a slightly lower median average salary.

Overall, this analysis might encourage someone looking for the highest salary possible to focus more on small and large sized companies since there is less variance in their data compared to medium sized companies.

We filtered out the highest paying jobs with the highest average salary from each company size category and we printed enough jobs to cover 5 different companies since some companies have several jobs with the same titles.

The highest paying job in the small company category is a Data Scientist position in the company TechProjects.

The highest paying job in the medium company category is a Data Scientist -Sales position in the company Confluent. This is also the highest-paid job on our list overall.

The highest paying job in the large company category is a Data Engineer position in the company Audible.


Analysis #2: Job Satisfaction


For job satisfaction analysis, we listed the top five highest and lowest companies ranked by their job satisfaction.
4 of the top five highest-rated companies are located on the east coast and all 5 of them have a salary of over 100 thousand per year.
4 of the 5 lowest rating companies have a salary under 100k per year and the one that has a salary over 100 thousand per year is located on the west coast while the other companies are around the midwest and the east coast.
The bar charts show how the companies are ranked from 1 to 5, 5 being the highest and 1 being the lowest. We found that the lowest rated companies didn’t reach a rating higher than 2.5.


Analysis #3: Job Sector


We want to see what sectors these jobs are actually in. The bar chart shows the top 10 sectors in our data set. From this, we can see that about 24% of the jobs listed are in the IT sector, 17% are in business services and 11% are in healthcare. This makes up about 50% of all the job sectors we are looking at. 


Analysis #4: Job Location


Next, we want to explore if job location affects salary ranges. The box plot shows the average salary for data scientists jobs across the US. The US median is about 85K, but in our data there was 1 entry of 15.5K so that’s why one end of the box plot all the way to left but we kept that in because it met all of our criteria of being an entry level job.

We want to compare the US median to specific states. These are the top 5 states with the most data entries in our data set, which were CA, MA, VA, NY and TX. This could indicate that there are more job opportunities here but it could just be because there are more people in these states and that’s why we have more data on these states. States with fewer data entries may not be a good representation of the average salaries for that state. We can see that all states besides Texas have a median salary higher than the US median.

In addition to doing an analysis on the salaries for each state, we also did one on the salaries for the top 4 cities. Unfortunately, since our sample size is so limited, we did not go outside the top 4 cities.
Unsurprisingly, cities like New York and San Francisco are on the list. Additionally, so are Cambridge and Boston.
Based on these whisker plots, you can see that San Francisco pays entry-level Data Scientists by far the highest, followed by Boston, New York, and Cambridge.


Conclusion


To summarize our data, we see that:
1. Small and large companies pay more than medium sized company
2. There is a positive correlation between high average salary and high job rating
3. A lot of the top data science jobs are in California and San Francisco

Our team also noticed that when we looked at the top 10 paying jobs, they seemed to reflect much of the analyses we made.


Limitations


Some limitations to our data were:

1. Salary data is almost exclusively from Glassdoor
2. We had limited knowledge in running statistical analysis
3. We had limited amount of data for each state and city
4. The dataset was last updated 2 months ago
