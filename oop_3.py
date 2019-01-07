##############################################################################
# The program do not nothing special, only shows oop
##############################################################################


class Box:
    def __init__(self, coin):
        self.coin = coin

    def total_sum(self):
        return sum(self.coin)

    def __lt__(self, other_box):
        sum1 = self.total_sum()
        sum2 = other_box.total_sum()
        return sum1 < sum2

    def __gt__(self, other_box):
        sum1 = self.total_sum()
        sum2 = other_box.total_sum()
        return sum1 > sum2

    def __eq__(self, other_box):
        sum1 = self.total_sum()
        sum2 = other_box.total_sum()
        return sum1 == sum2


b1 = Box([1, 1, 2, 2, 0.5])
b2 = Box([1, 1, 2, 2, 0.5, 0.2, 0.05])
