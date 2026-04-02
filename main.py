from human_vs_ai import play_human_vs_ai
from simulation import run_ai_simulation
from human_vs_human import play_human_vs_human

def main():
    while True:
        print("\n========================================")
        print(" Task 3: Connect Four AI Prototype")
        print("========================================")
        print("1. Play Game (Human vs Human)")
        print("2. Play Game (Human vs AI)")
        print("3. Run Simulation (AI vs AI)")
        print("4. Exit")
        print("========================================")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            play_human_vs_human()
        elif choice == '2':
            play_human_vs_ai()
        elif choice == '3':
            run_ai_simulation()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()