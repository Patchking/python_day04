
from random import sample

def turrets_generator(count):
    def shoot(self):
        print("Shooting")

    def search(self):
        print("Searching")

    def talk(self):
        print("Talking")

    def generate_numbers(n, total):
        dividers = sorted(sample(range(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

    def create_turret_class():
        randnums = generate_numbers(5, 100)
        return type(
            "Turret",
            (),
            {
                "neuroticism": randnums[0],
                "openness": randnums[1],
                "conscientiousness": randnums[2],
                "extraversion": randnums[3],
                "agreeableness": randnums[4],
                "shoot": shoot,
                "search": search,
                "talk": talk
            }
        )

    for i in range(count):
        yield create_turret_class()()

# Example usage
def main():
    turret_generator = turrets_generator(10)
    turret_instance = next(turret_generator)
    print(f"Personality Traits: "
          f"Neuroticism={turret_instance.neuroticism}, "
          f"Openness={turret_instance.openness}, "
          f"Conscientiousness={turret_instance.conscientiousness}, "
          f"Extraversion={turret_instance.extraversion}, "
          f"Agreeableness={turret_instance.agreeableness}")
    turret_instance.shoot()
    turret_instance.search()
    turret_instance.talk()


if __name__ == "__main__":
    main()