def stable_matching(n: int, men_preferences: list, women_preferences) -> list:
    unmarried_men = list(range(n))
    man_spouse = [None] * n
    woman_spouse = [None] * n
    next_man_choice = [0] * n

    while unmarried_men:
        he = unmarried_men[0]
        his_preferences = men_preferences[he]

        she = his_preferences[next_man_choice[he]]
        her_preferences = women_preferences[she]
        current_husband = woman_spouse[she]

        if current_husband is None:
            next_man_choice[he] = next_man_choice[he] + 1
            man_spouse[he], woman_spouse[she] = she, he
            unmarried_men.remove(he)

        else:
            next_man_choice[he] = next_man_choice[he] + 1

            if her_preferences.index(current_husband) > her_preferences.index(he):
                man_spouse[he], woman_spouse[she] = she, he
                man_spouse[current_husband] = None
                unmarried_men.remove(he)
                unmarried_men.append(current_husband)

    return man_spouse


if __name__ == "__main__":
    assert stable_matching(1, [[0]], [[0]]) == [0]
    assert stable_matching(2, [[0, 1], [1, 0]], [[0, 1], [1, 0]])
