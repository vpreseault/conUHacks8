import random

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [
    "00:00",
    "01:00",
    "02:00",
    "03:00",
    "04:00",
    "05:00",
    "06:00",
    "07:00",
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
    "19:00",
    "20:00",
    "21:00",
    "22:00",
    "23:00",
]
regions = ["NAE", "NAW", "EUNE", "EUW", "OCE", "BR", "ASIA"]
platforms = ["steam", "epg", "xsx", "ps5"]
# 30 k 70 survivor
roles = ["killer", "survivor"]
skills = [
    "1",
    "2",
    "3",
    "4",
    "5",
    # "6",
    # "7",
    # "8",
    # "9",
    # "10",
    # "11",
    # "12",
    # "13",
    # "14",
    # "15",
    # "16",
    # "17",
    # "18",
    # "19",
    # "20",
]


def random_number():
    return round(random.random() * 10) / 10


dict_skeleton = {
    "NAE": {
        "steam": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "epg": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "xsx": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "ps5": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
    },
    "NAW": {
        "steam": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "epg": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "xsx": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "ps5": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
    },
    "EUNE": {
        "steam": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "epg": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "xsx": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "ps5": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
    },
    "EUW": {
        "steam": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "epg": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "xsx": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "ps5": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
    },
    "OCE": {
        "steam": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "epg": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "xsx": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "ps5": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
    },
    "BR": {
        "steam": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "epg": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "xsx": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "ps5": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
    },
    "ASIA": {
        "steam": {
            "1": {
                "killer": [], 
                "survivor": []
            },
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "epg": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "xsx": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
        "ps5": {
            "1": {"killer": [], "survivor": []},
            "2": {"killer": [], "survivor": []},
            "3": {"killer": [], "survivor": []},
            "4": {"killer": [], "survivor": []},
            "5": {"killer": [], "survivor": []},
            "6": {"killer": [], "survivor": []},
            "7": {"killer": [], "survivor": []},
            "8": {"killer": [], "survivor": []},
            "9": {"killer": [], "survivor": []},
            "10": {"killer": [], "survivor": []},
            "11": {"killer": [], "survivor": []},
            "12": {"killer": [], "survivor": []},
            "13": {"killer": [], "survivor": []},
            "14": {"killer": [], "survivor": []},
            "15": {"killer": [], "survivor": []},
            "16": {"killer": [], "survivor": []},
            "17": {"killer": [], "survivor": []},
            "18": {"killer": [], "survivor": []},
            "19": {"killer": [], "survivor": []},
            "20": {"killer": [], "survivor": []},
        },
    },    
}

size_probability = [1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
player_distribution = [
    [
        28285,
        27484,
        26235,
        25279,
        24362,
        25109,
        26704,
        30989,
        36166,
        40231,
        41391,
        40006,
        38662,
        37413,
        37272,
        38149,
        38242,
        36639,
        34047,
        30850,
        29072,
        28527,
        29444,
        29591,
    ],
    [
        29761,
        29633,
        28826,
        27627,
        26895,
        26060,
        27919,
        32109,
        37079,
        40324,
        40308,
        37954,
        36199,
        36091,
        36995,
        37721,
        36633,
        33447,
        29081,
        26391,
        25663,
        26191,
        26731,
        25861,
    ],
    [
        24477,
        22853,
        21030,
        19976,
        19067,
        18709,
        20253,
        24091,
        29133,
        32419,
        32496,
        31140,
        30792,
        31971,
        33402,
        11474,
        19912,
        25001,
        27925,
        26586,
        25981,
        26145,
        26687,
        25394,
    ],
    [
        23309,
        21532,
        19908,
        18939,
        18637,
        18519,
        20092,
        24242,
        28813,
        31881,
        32690,
        30995,
        31363,
        33176,
        34647,
        35831,
        35234,
        32183,
        28456,
        23966,
        25944,
        27018,
        27439,
        25851,
    ],
    [
        24187,
        22544,
        20790,
        20096,
        19697,
        19971,
        22075,
        26559,
        31818,
        35675,
        35083,
        33599,
        32073,
        32320,
        33354,
        34310,
        33247,
        30295,
        27248,
        25428,
        25337,
        26594,
        26699,
        25549,
    ],
    [
        23892,
        22346,
        20582,
        19781,
        19444,
        19586,
        21755,
        25993,
        30724,
        34674,
        34826,
        33029,
        31676,
        32202,
        33072,
        33657,
        32282,
        29615,
        26607,
        24678,
        24654,
        25459,
        26442,
        25181,
    ],
    [
        24070,
        22354,
        21030,
        20000,
        19403,
        19322,
        21429,
        25497,
        30411,
        34564,
        36561,
        35604,
        33904,
        33230,
        33198,
        34009,
        32456,
        31873,
        30322,
        27933,
        26448,
        26839,
        28106,
        28627,
    ],
]
