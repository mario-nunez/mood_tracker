import datetime

MAX_REACTION_RATE = 5


MORNING = {
    'start': datetime.time(6, 0, 1),
    'end': datetime.time(12, 0, 0),
    'value': 'Morning'
}

AFTERNOON = {
    'start': datetime.time(12, 0, 1),
    'end': datetime.time(17, 0, 0),
    'value': 'Afternoon'
}

EVENING = {
    'start': datetime.time(17, 0, 1),
    'end': datetime.time(20, 0, 0),
    'value': 'Evening'
}

NIGHT = {
    'start': datetime.time(20, 0, 1),
    'end': datetime.time(6, 0, 0),
    'value': 'Night'
}
