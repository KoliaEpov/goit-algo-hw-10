import pulp


def main():
    model = pulp.LpProblem("Factory_products", pulp.LpMaximize)

    lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

    model += lemonade + fruit_juice, "Total_Products"
    model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
    model += lemonade <= 50, "Sugar_Constraint"
    model += lemonade <= 30, "Lemon_Juice_Constraint"
    model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

    model.solve()

    print("Status:", pulp.LpStatus[model.status])
    print("Lemonade =", pulp.value(lemonade))
    print("Fruit juice =", pulp.value(fruit_juice))
    print("Total products =", pulp.value(lemonade + fruit_juice))


if __name__ == "__main__":
    main()
