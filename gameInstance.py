class GameInstance():
    def __init__(self, window, defaultFont, countdownTimer, gameComplete, clickCounter):
        self.countdownTimer = countdownTimer
        self.gameComplete = gameComplete
        self.clickCounter = clickCounter
        self.window = window
        self.defaultFont = defaultFont