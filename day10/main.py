class JoltageAdapters(object):

    def __init__(self, init_values) -> None:
        self.values = sorted(init_values)
        self.device_max_joltage = max(init_values) + 3
        self.difference_1 = 1
        self.difference_3 = 1
        for i in self.values:
            if i + 1 in self.values:
                self.difference_1 += 1
            if (i + 1 not in self.values) and (i + 2 not in self.values) and i + 3 in self.values:
                self.difference_3 += 1

        self.result = self.difference_3 * self.difference_1
        self.groups = self.make_groups(self.values)
        self.combinations = self.compute_combinations(self.groups)

    @staticmethod
    def make_groups(values: list) -> list:
        array = []
        contiguous = [values[0]]
        for i in values[1:]:
            if i - 1 in contiguous:
                contiguous.append(i)
            else:
                array.append(contiguous)
                contiguous = [i]
        return array + [contiguous]

    @staticmethod
    def compute_combinations(groups: list) -> int:
        total = 1
        for i in groups:
            print(f'{i=},{len(i)=}')
            if len(i) == 1:
                print(f'multiplié par 1')
            if len(i) == 2:
                total *= 1
                print(f'multiplié par 1')
            if len(i) == 3:
                total *= 2
                print(f'multiplié par 2')
            if len(i) == 4:
                total *= 4
                print(f'multiplié par 4')
            if len(i) == 5:
                total *= 7
                print(f'multiplié par 10')
            if len(i) > 5:
                print(f'je dois calculer ça : {len(i)}')
                total *= 1
        return total
