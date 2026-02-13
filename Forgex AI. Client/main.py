from ai_client import ButlerAI
from robot_control import ClawbotController

def main():
    # Initialize components
    ai = ButlerAI()
    robot = ClawbotController()

    print("--- Butler is Active ---")
    user_query = "Use Gemini to help me pick up the ball"
    
    # 1. Ask AI for advice
    decision = ai.ask_gemini(user_query)
    print(f"AI Decision: {decision}")

    # 2. Command the robot
    robot.operate_claw("OPEN")
    robot.move_forward(10)
    robot.operate_claw("CLOSE")

if __name__ == "__main__":
    main()
