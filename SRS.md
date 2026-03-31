## 3. Work Breakdown Structure & Detailed Role Assignments

To guarantee equitable distribution of labor and establish clear accountability for the final project report, engineering responsibilities are strictly compartmentalized as follows:

### Role 1: Game Engine & State Logic
**Assigned to:** KevinPham0418
* **Module Ownership:** `board_logic.py`
* **Technical Specifications:** You are responsible for the foundational data structures. You must engineer a highly optimized board representation (preferably using bitboards or 1D arrays over standard 2D lists to minimize memory overhead during deep searches). 
* **Required Deliverables:**
  * Implementation of `apply_move(column, player)` and `undo_move(column)`.
  * Implementation of `get_legal_moves()` returning a prioritized list of valid columns.
  * A highly efficient `is_terminal_state()` function to detect a win or draw condition in constant or near-constant time.
* **Internal Dependencies:** All other modules depend on the speed and accuracy of this component.

### Role 2: Minimax Algorithm Implementation
**Assigned to:** Student 2
* **Module Ownership:** `minimax_search.py`
* **Technical Specifications:** You will construct the core recursive search tree. You must accurately model the adversarial nature of the game, alternating between the maximizing agent (the AI) and the minimizing agent (the opponent).
* **Required Deliverables:**
  * A recursive `minimax(state, depth, maximizing_player)` function.
  * Integration of a depth-limit parameter to force the algorithm to halt and evaluate the board if it cannot reach a terminal state.
  * Ensuring the function correctly propagates both the optimal score and the optimal corresponding move index up the recursive call stack.

### Role 3: Alpha-Beta Pruning Optimization
**Assigned to:** Student 3
* **Module Ownership:** `alpha_beta_pruning.py`
* **Technical Specifications:** You are tasked with reducing the time complexity of the Minimax algorithm. You must track the highest guaranteed score for the maximizer ($\alpha$) and the lowest guaranteed score for the minimizer ($\beta$).
* **Required Deliverables:**
  * Modification of the baseline Minimax search to accept and update $\alpha$ and $\beta$ parameters.
  * Implementation of branch termination logic (`break` conditions) when $\beta \le \alpha$.
  * Instrumentation of the search function to continuously log the aggregate number of "pruned" nodes per move for later empirical analysis.

### Role 4: Heuristic/Utility Function Design
**Assigned to:** Student 4
* **Module Ownership:** `heuristic_evaluator.py`
* **Technical Specifications:** You must mathematically define what constitutes an advantageous board position. Since the AI cannot compute the game to its conclusion in the mid-game, your utility function $U(s)$ dictates its intelligence.
* **Required Deliverables:**
  * Identification and extraction of board features (e.g., center column occupation, open-ended three-in-a-rows).
  * Implementation of a static `evaluate_board(state, player)` function that returns an integer/float score.
  * Rigorous empirical tuning of the heuristic weights to balance offensive threat generation with defensive block prioritization.

### Role 5: Experimental Data & Performance Metrics
**Assigned to:** Jonardzz
* **Module Ownership:** `performance_metrics.py`
* **Technical Specifications:** You are responsible for generating the quantitative evidence required for Dr. Eick's grading rubric. You must prove that the Alpha-Beta optimization works and analyze the AI's performance at varying depths.
* **Required Deliverables:**
  * Automation scripts to simulate hundreds of AI vs. AI matches (e.g., Unpruned Minimax at Depth 4 vs. Alpha-Beta at Depth 6).
  * Logging and statistical aggregation of two primary metrics: Execution time per move and Total nodes expanded per move.
  * Creation of professional data visualizations (graphs and tables) comparing these metrics, directly formatted for inclusion in the final 4-6 page report and class presentation.

### Role 6: UI/UX & Technical Documentation
**Assigned to:** Student 6
* **Module Ownership:** `main.py`, `README.md`, and the Final Report
* **Technical Specifications:** You oversee the repository architecture and user experience. You must synthesize the components built by Roles 1-4 into a seamless, executable application.
* **Required Deliverables:**
  * Development of the main game loop, including handling human input validation and triggering the AI's response.
  * Enforcement of version control standards within the repository (e.g., ensuring no broken code is merged into the `main` branch).
  * Leadership and final editorial control over the mandatory 4-6 page academic report, ensuring all individual contributions are thoroughly documented and cited.
