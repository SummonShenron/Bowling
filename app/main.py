import random
import time
def greet(name: str) -> str:
    return f"Hello, {name}!"


def calculate_score(roll_scores: list):
    total_score = 0
    roll_index = 0
    for frame in range(10):
        if roll_index >= len(roll_scores):
            break
        if roll_index == len(roll_scores) - 1:
            total_score += roll_scores[roll_index]
            break
        # strike
        if roll_scores[roll_index] == 10:
            frame_score = 10
            if roll_index + 1 < len(roll_scores):
                frame_score += roll_scores[roll_index + 1]
            if roll_index + 2 < len(roll_scores):
                frame_score += roll_scores[roll_index + 2]
            total_score += frame_score
            roll_index += 1
        # spare
        elif roll_scores[roll_index] + roll_scores[roll_index + 1] == 10:
            frame_score = 10
            if roll_index + 2 < len(roll_scores):
                frame_score += roll_scores[roll_index + 2]
            total_score += frame_score
            roll_index += 2        
        else:
            total_score += roll_scores[roll_index] + roll_scores[roll_index + 1]
            roll_index += 2     
    return total_score

def bowling():
    roll_scores = []
    rolls = 0
    for frame in range(1, 10):
        print(f"frame {frame} / 10")
        roll = input("press enter to roll")
        roll = random.randint(0, 10)
        print(f"whoa you knocked down {roll} pin(s)! ")
        if roll == 10:
            print(f"wow, great roll, you hit a home run")
            roll_scores.append(roll)
            rolls + 1
            continue
        if roll < 10:
            roll_scores.append(roll)
            roll = input("press enter to roll your second turn")
            roll = random.randint(0, 10 - roll_scores[- 1])
            print(f"i cant believe you managed to knock down another {roll} pins!")
            roll_scores.append(roll)
        score = calculate_score(roll_scores)
        print(f"frame {frame} / 10 score: {score}")
    if frame in range(10): 
        tenth_roll_1 = input("press enter to roll your last round")
        tenth_roll_1 = random.randint(0, 10)
        if tenth_roll_1 == 10:
            roll_scores.append(tenth_roll_1)
            tenth_roll_bonus1 = input("press enter to roll your last round")
            tenth_roll_bonus1 = random.randint(0, 10)
            roll_scores.append(tenth_roll_bonus1)
            tenth_roll_bonus2 = input("press enter to roll your last round")
            tenth_roll_bonus2 = random.randint(0, 10)
            roll_scores.append(tenth_roll_bonus2)
        else:
            tenth_roll_2 = input("your final roll please:")
            tenth_roll_2 = random.randint(0, 10 - roll_scores[- 1])
            print(f"congrats you hit {tenth_roll_2} pins")
            roll_scores.append(tenth_roll_2)
            if tenth_roll_1 + tenth_roll_2 == 10:
                tenth_roll_3 = input("your final roll please:")
                tenth_roll_3 = random.randint(0, 10 - roll_scores[- 1])
                print(f"congrats you hit {tenth_roll_3} pins")
                roll_scores.append(tenth_roll_3)
    score = calculate_score(roll_scores)  
    print(f"you should be impressed, you got {score} points.")          
            
if __name__ == "__main__":
    print(greet("World"))
    bowling()
