class ClawbotController:
    def __init__(self):
        print("[Hardware] Clawbot Motors Ready.")

    def move_forward(self, distance):
        print(f"[Action] Moving forward {distance}cm")

    def operate_claw(self, state):
        # state could be "OPEN" or "CLOSE"
        if state.upper() == "OPEN":
            print("[Action] Opening Claw")
        else:
            print("[Action] Closing Claw")

    def stop_all(self):
        print("[Action] Emergency Stop")
