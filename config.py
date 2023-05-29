#General Configs
CHARACTER_NAME="Hakom"
PICK_UP_ZEN=True
PICK_UP_JEWELS=True
PICK_UP_ITEMS_EXC=True
WRITE_MESSAGES=False
BACK_TO_INITIAL_POSITION=False
CLEAN_INVENTORY=True
WINDOW_SCREEN_SIZE="1440"
COORDINATES_SCREEN_SIZE={
    "1440": {
        "MOVE_CELL_DISTANCE": 44,
        "START_ANALYZE_INVENTORY": {
            "x": 1068,
            "y": 390
        },
        "DROP_ITEM": {
            "x": 763,
            "y": 863
        }
    },
    "1024": {
        "MOVE_CELL_DISTANCE": 32,
        "START_ANALYZE_INVENTORY": {
            "x": 758,
            "y": 336
        },
        "DROP_ITEM": {
            "x": 543,
            "y": 741
        },
    }
}


#OCR -> API/LOCAL
OCR_PROCESSOR="API"

#WRITE_MESSAGES -> Write Messages Feature (Allow user to write random difined messages)
WRITE_MESSAGES_TEXTS=["lg", "laaaag", "lggggg", "+", "laggg" "lllag" + "+++++++++", "lgg"]

#BACK_TO_INITIAL_POSITION -> How many times need to execute this
BACK_TO_INITIAL_POSITION_TIMES = 20