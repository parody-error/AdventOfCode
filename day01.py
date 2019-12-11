

input_path = 'input.txt'


def fuel_mass(mass):
    return mass // 3 - 2


def total_fuel_for_mass(module_mass):
    total_mass = fuel_mass(module_mass)
    required_fuel_mass = fuel_mass(total_mass)
    while required_fuel_mass > 0:
        total_mass += required_fuel_mass
        required_fuel_mass = fuel_mass(required_fuel_mass)

    return total_mass


if __name__ == "__main__":
    totalFuel = 0

    with open(input_path, 'r') as input_file:
        for line in input_file:
            totalFuel += total_fuel_for_mass(int(line))

    print(f'Total fuel: {totalFuel}')
