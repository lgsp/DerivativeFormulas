def incr_score(score, condition, answer):
    if condition:
        score += 1
        print(f"Bien joué ! Ton score actuel est : {score}")
    else:
        print(f"Faux ! Ton score est toujours : {score}")
        print(f"La bonne réponse était : {answer}")
    return score



def final_score(attempts, score):
    print(f"Your final score is {score}")
    if attempts < 2: print(f"You have made {attempts} attempt.")
    else: print(f"You have made {attempts} attempts.")
    print(f"So you percentage of success is {100*score/attempts:.2f}%")
    ggb = "https://geogebra.org/classic"
    print(f"Go visit Geogebra to experiment with different values: {ggb}")
