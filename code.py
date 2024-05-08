class Bolopuntaje:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if self.strike(roll_index):
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
                if frame == 9:
                    if len(self.rolls) > roll_index + 1:
                        total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                    break
            elif self.spare(roll_index):
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
                if frame == 9:
                    if len(self.rolls) > roll_index:
                        total_score += self.rolls[roll_index]
                    break
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2

        return total_score

    def frame_score(self, roll_index):
        if roll_index < len(self.rolls) - 1:
            return self.rolls[roll_index] + self.rolls[roll_index + 1]
        else:
            return 0

    def strike_bonus(self, roll_index):
        if len(self.rolls) > roll_index + 2:
            return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
        else:
            return 0

    def spare_bonus(self, roll_index):
        if len(self.rolls) > roll_index + 2:
            return self.rolls[roll_index + 2]
        else:
            return 0


