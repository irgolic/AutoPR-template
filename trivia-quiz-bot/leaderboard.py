import json
import operator

def get_leaderboard(scores):
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    leaderboard_text = "Leaderboard:\n\n"

    for i, (user, score) in enumerate(sorted_scores):
        leaderboard_text += f"{i + 1}. {user}: {score}\n"

    return leaderboard_text