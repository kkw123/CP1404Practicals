"""
CP1404/CP5632 Practical
Starter code for cumulative total income program

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""


def main():
    """Ask how many months and the income for each month"""
    incomes = []
    total_months = int(input("How many months? "))

    for month in range(1, total_months + 1):
        income = float(input("Enter income for month {}: ".format(str(month))))
        incomes.append(income)

    print_report(total_months, incomes)


def print_report(total_months, incomes):
    """Display income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
