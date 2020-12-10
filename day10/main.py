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
