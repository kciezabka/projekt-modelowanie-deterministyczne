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
            mask = params["mask"][key]
            self.matrices[key][mask == 1] = 1


        self.bigmatrix = np.zeros((100, 100))
        for key in params["indexes"].keys():
            row_min = min([tup[0] for tup in params["indexes"][key]])
            row_max = max([tup[0] for tup in params["indexes"][key]])
            col_min = min([tup[1] for tup in params["indexes"][key]])
            col_max = max([tup[1] for tup in params["indexes"][key]])

            self.bigmatrix[row_min:row_max, col_min:col_max] = self.matrices[key]

        #for key in params["wall"].keys():
         #   w_row_min = min([tup[0] for tup in params["wall"][key]])
          #  w_row_max = max([tup[0] for tup in params["wall"][key]])
           # w_col_min = min([tup[1] for tup in params["wall"][key]])
            #w_col_max = max([tup[1] for tup in params["wall"][key]])
            #self.matrices[key][w_row_max - w_row_min, w_col_max - w_col_min] = 2

    def build(self):
        return self.matrices.values()

    def build2(self):
        return self.bigmatrix


if __name__ == '__main__':
    params = {"indexes": {"I": [(0, 0), (0, 50), (50, 0), (50, 50)],
                          "II": [(0, 50), (0, 100), (50,50), (50, 100)],
                          "III": [(50, 0), (50, 100), (70, 0), (70, 100)],
                          "IV": [(70, 0), (70,50), (100,0), (100,50)],
                          "V": [(70,50), (70,100), (100,50), (100, 100)]},
              "rozdzielczosc": {},
              "mask": {"I": 1, "II": 0, "III": 1, "IV": 1, "V": 1},
              #"wall":{"I":[(0,49), (0,50), (50,49), (50,50)]}
              }

    dom = Dom(params)
    print(dom.build2())
    plt.imshow(dom.build2())
    plt.show()
