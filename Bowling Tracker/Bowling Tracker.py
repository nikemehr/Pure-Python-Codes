class Bowling:
    def __init__(self, Scores):
        self.Scores = Scores

    def IsTurkey(self):
        # We try to find if there are three 7 in the list or not.
        Turkey_count = 0
        for i in range(len(self.Scores)):
            if self.Scores[i] == 10:
                Turkey_count += 1
                if Turkey_count == 3:
                    return True
                    break
                else:
                    continue
            else:
                Turkey_count = 0
        return False

    def FreeGame(self):
        # We check if there are three scores of 7 in the game
        return self.Scores.count(7) == 3

    def GetLowest(self):
        #in this bloc we find the lowest score in the list and its frame
        Lowest_frame = 0
        for i in range(len(self.Scores)):
            if self.Scores[i] < self.Scores[Lowest_frame]:
                Lowest_frame = i
            else:
                continue
        return Lowest_frame

    def GetMedian(self):
        # we find the median of the list
        n = len(self.Scores)
        sorted_scores = sorted(self.Scores)
        # median is different in even and odd numbers
        if n % 2 == 0:
            return (sorted_scores[n//2] + sorted_scores[(n//2)-1])/2
        else:
            return sorted_scores[n//2]


def main():
    Scores = [7, 9, 6, 10, 10, 10, 7, 5, 8, 7]
    MyBowling = Bowling(Scores)

    if MyBowling.IsTurkey():
        print("Congrats! You got a Turkey")
    else:
        print("No Turkey")

    if MyBowling.FreeGame():
        print("Free Game")
    else:
        print("No Free Game")

    index = MyBowling.GetLowest()
    print("Lowest Score:", Scores[index], "which occurred in frame", index + 1)
    print("The median score is:", MyBowling.GetMedian())


main()