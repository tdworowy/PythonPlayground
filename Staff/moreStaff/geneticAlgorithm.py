import random
import string


class Cities:
    def generateCityDistances(self, count, distanceRange):
        print("Generate Cities")
        keys = self.generateKeysCombinations(count)
        values = [random.randrange(distanceRange[0], distanceRange[1], 10) for _ in range(len(keys))]
        print("Values: ", values)
        distances = dict({(key, value) for key in keys for value in values})
        print("Before clan: ", distances)
        clean = self.cleanCityList(distances)
        print("After clan: ", clean)
        return self.cleanCityList(clean)

    def generateKeysCombinations(self, count):
        keys = []
        alphabet = list(string.ascii_uppercase);
        for i in range(count):
            try:
                city1 = "City" + alphabet[i]
                keys.extend([(city1, "City" + x) for x in alphabet[:count]])

            except (IndexError):
                index = 1
                alphabet2 = map((lambda x: str(index) + x), alphabet)
                alphabet.extend(alphabet2)
                index += 1
                continue
        print("Keys: ", keys)
        return keys

    def cleanCityList(self, dictionaries):
        keys = dictionaries.keys()
        newDictionaries = dictionaries
        for key in keys:
            # print(key)
            newDictionaries[key] = dictionaries[key[::-1]]
            if key[0] is key[1]: newDictionaries[key] = 0
        return newDictionaries


class TravelingSalesman():
    def __init__(self, distances, cityCount, initPopulationCount, iterations):
        self.distances = distances
        self.initPopulationCount = initPopulationCount
        self.iterations = iterations
        self.cityCount = cityCount

    def generateInitialPopulation(self):
        population = []
        allKeys = list(self.distances.keys())
        sample_size = random.randint(1, self.cityCount)
        for i in range(self.initPopulationCount):
            randomKeys = random.sample(allKeys, sample_size)
            population.append([(key, self.distances[key]) for key in randomKeys])

        return population

    def displayPopulation(self, population):
        print("Initial population size: ", len(population))
        print("Initial population: ", population)
        for vector in population:
            print("vector size: ", len(vector))
            print(vector)

    def resolve(self):
        initialPopulation = self.generateInitialPopulation()
        self.displayPopulation(initialPopulation)


def main():
    cities = Cities()
    distances = cities.generateCityDistances(20, (100, 1000))
    print(distances)
    ts = TravelingSalesman(distances, 20, 30, 100)
    ts.resolve()


if __name__ == '__main__':
    main()

#TODO
# 1. w vektorze odległości powinny być posortowane , kontynłować goenrowanie i sprawdzanie initial population aż będzie odpowidenia ich ilość
# 2. funkcja sprawdzajaca i krzyrzujaca
# 3. mutacje