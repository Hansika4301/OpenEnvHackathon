def grade(total_reward, max_reward):
    if max_reward == 0:
        return 0.01

    score = total_reward / max_reward

    # Strict range (0,1)
    if score <= 0:
        return 0.01
    elif score >= 1:
        return 0.99
    else:
        return score


def grade_easy(total_reward):
    return grade(total_reward, 3)


def grade_medium(total_reward):
    return grade(total_reward, 5)


def grade_hard(total_reward):
    return grade(total_reward, 7)