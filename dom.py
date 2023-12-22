import numpy as np
import matplotlib.pyplot as plt

class Dom:
    def __init__(self, params):
        self.params = params
        matrices = {}
        self.matrices = matrices
        for key in params["indexes"].keys():
            row_min = min([tup[0] for tup in params["indexes"][key]])
            row_max = max([tup[0] for tup in params["indexes"][key]])
            col_min = min([tup[1] for tup in params["indexes"][key]])
            col_max = max([tup[1] for tup in params["indexes"][key]])
            self.matrices[key] = np.zeros((row_max - row_min, col_max - col_min))
            mask = params["mask"][key]
            self.matrices[key][mask == 1] = 1

    def build(self):
        return self.matrices.values()

    def build2(self):
        result = np.zeros((100, 100))
        result[0:35, 0:55] = self.matrices["I"]
        result[0:35, 55:100] = self.matrices["II"]
        result[35:65, 0:55] = self.matrices["III"]
        result[35:65, 55:100] = self.matrices["IV"]
        result[65:100, 0:55] = self.matrices["V"]
        result[65:100, 55:100] = self.matrices["VI"]
        return result


if __name__ == '__main__':

    params = {"indexes": {"I": [(0, 0), (0, 55), (35, 0), (35, 55)],
                          "II": [(0, 55), (0, 100), (35, 55), (35, 100)],
                          "III": [(35, 0), (35, 55), (65, 0), (65, 55)],
                          "IV": [(50, 55), (50, 100), (80, 55), (65, 100)],
                          "V": [(65, 0), (65, 55), (100, 0), (100, 55)],
                          "VI": [(65, 55), (65, 100), (100, 55), (100, 100)]},
              "rozdzielczosc": {},
              "mask": {"I": 1, "II": 0, "III": 1, "IV": 1, "V": 1, "VI": 1}}

    dom = Dom(params)
    print(dom.build2())
    plt.imshow(dom.build2())
    plt.show()
