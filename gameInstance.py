class GameInstance():
    def __init__(self, window, defaultFont, gameComplete, gameVariables):
        self.gameComplete = gameComplete
        self.gameVariables = gameVariables
        self.window = window
        self.defaultFont = defaultFont

class GameVariables():
    def __init__(self, clickCounter, countdownTimer) :
        self.clickCounter = clickCounter
        self.countdownTimer = countdownTimer