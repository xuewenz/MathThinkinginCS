def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for i in dice1:
        for j in dice2:
            if j>i:
                dice2_wins+=1
            if i>j:
                dice1_wins+=1
    # write your code here

    return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    # write your code here
    # use your implementation of count_wins method if necessary

    for idx in range(len(dices)):
        win = 0
        for idx_comp in range(len(dices)):
            [dice1_wins, dice2_wins] = count_wins(dices[idx], dices[idx_comp])
            if dice1_wins > dice2_wins:
                win+=1
                if win==len(dices)-1:
                    return idx
            else:
                continue


    return -1

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True

    # write your code here
    best_idx = find_the_best_dice(dices)

    if best_idx == -1:
        strategy["choose_first"] = False
        for i in range(len(dices)):
                for idx_comp in range(len(dices)):
                    [dice1_wins, dice2_wins] = count_wins(dices[i], dices[idx_comp])
                    if dice2_wins > dice1_wins:
                        strategy[i] = idx_comp % len(dices)
                        break
    else:
        strategy["first_dice"] = best_idx
        return strategy
    
    return strategy

compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]])