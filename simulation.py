# Import the modular game engine we just built
from simulation_engine import run_match

def run_ai_simulation():
    print("\n" + "="*50)
    print("   AI SIMULATION SWITCHBOARD")
    print("="*50)
    print("Select the matchup you want to run:")
    print("1. Alpha-Beta Pruning (P1) vs Standard Minimax (P2)")
    print("2. Alpha-Beta Pruning (P1) vs Alpha-Beta Pruning (P2)")
    print("3. Standard Minimax (P1) vs Standard Minimax (P2)")
    print("="*50)
    
    choice = input("Select an option (1, 2, or 3): ")
    
    # Route the user's choice directly to the simulation engine
    if choice == '1':
        run_match("Alpha-Beta", "Minimax")
    elif choice == '2':
        run_match("Alpha-Beta", "Alpha-Beta")
    elif choice == '3':
        run_match("Minimax", "Minimax")
    else:
        print("Invalid choice. Defaulting to Option 1.")
        run_match("Alpha-Beta", "Minimax")
        
    input("\nPress Enter to return to the Main Menu...")