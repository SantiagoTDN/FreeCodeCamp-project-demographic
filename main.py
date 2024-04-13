# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()
# Read data from file
    df = pd.read_csv("/workspace/boilerplate-demographic-data-analyzer/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    rr=df.groupby("race")
    race_count = rr["race"].count()

    # What is the average age of men?
    qq=df["age"].loc[df["sex"] == "Male"].mean()
    average_age_men = round(qq,1)

    # What is the percentage of people who have a Bachelor's degree?
    bb=df["education"].count()
    
    hh=df.groupby("education")
    pp=hh["education"].count()["Bachelors"]
    percentage_bachelors = round(pp/bb*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.set_index("education").loc[["Bachelors", "Masters", "Doctorate"]]
    lower_education = df.set_index("education").drop(["Bachelors", "Masters", "Doctorate"])

    # percentage with salary >50K
    aa=higher_education["salary"].loc[higher_education["salary"] == ">50K"].count()
    c=df.groupby("education")["education"].count()
    cc=c[["Bachelors", "Masters", "Doctorate"]].sum()
    higher_education_rich = round(aa/cc*100, 1)

    dd=lower_education["salary"].loc[lower_education["salary"]==">50K"].count()
    cx=c.drop(["Bachelors", "Masters", "Doctorate"]).sum()
    lower_education_rich = round(dd/cx*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(df["hours-per-week"].min(),1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    ii=df["hours-per-week"].loc[df["hours-per-week"]==df["hours-per-week"].min()]
    num_min_workers = ii.count()
    jj=ii.loc[df["salary"]==">50K"].count()

    rich_percentage = round(jj/ii.count()*100,1)

    # What country has the highest percentage of people that earn >50K?
    k=df.groupby("native-country")["native-country"].count()
    l=df.loc[df["salary"]==">50K"]
    ll=l.groupby("native-country")["native-country"].count()
    lk=ll/k*100
    highest_earning_country = lk.idxmax()
    highest_earning_country_percentage = round(lk.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    m=l.loc[df["native-country"]=="India"]
    mm=m.groupby("occupation")["occupation"].count()
    top_IN_occupation = mm.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Run unit tests automatically
main(module='test_module', exit=False)