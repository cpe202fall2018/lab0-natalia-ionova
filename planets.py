def weight_on_planets():
    earth_weight = int(input("What do you weigh on earth? "))
    mars_weight = earth_weight * 0.38
    jupiter_weight = earth_weight * 2.34
    print('')
    print("On Mars you would weigh " + str(mars_weight) + " pounds.")
    print("On Jupiter you would weigh " + str(jupiter_weight) + " pounds.")


if __name__ == '__main__':
    weight_on_planets()