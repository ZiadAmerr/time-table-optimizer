# 15-Day Project Plan for Examination Timetabling Problem

This project plan outlines a comprehensive 15-day schedule (4 hours per day) to develop a solution for the **Examination Timetabling Problem**. The plan is structured according to phases 0 through 10 of the roadmap, with each day’s goals and tasks clearly defined. Each day’s section details the implementation approach, suggests Python tools (functions, classes, libraries), provides pseudocode where useful, notes key considerations and pitfalls, and shows how it connects to subsequent phases. The focus is on clean, efficient implementation using popular libraries (e.g., NumPy, Pandas, Matplotlib) when appropriate.

## Day 1: Project Setup and Preliminary Research (Phase 0)

**Goals:** Initialize the development environment and gain a clear understanding of the examination timetabling problem scope. Phase 0 involves setting up tools and conducting preliminary research on problem characteristics and known methods.

1. **Environment Setup:** Prepare a Python development environment for the project. Install and verify all necessary libraries:
   - **Python version:** Ensure Python 3.x is installed.
   - **Libraries:** Install common libraries such as `numpy` (for numeric operations), `pandas` (for data handling if needed), and possibly `networkx` (for graph-based approaches) and `matplotlib` (for visualizing schedules or results). For example, use `pip` to install packages and test importing them.
   - **Project Structure:** Create a project folder and initialize a Git repository (optional but recommended) to track progress. Set up a basic file structure (e.g., a main Python script or notebook, and modules for scheduling algorithms, data models, etc.).
   - **Tip:** Establish a consistent coding environment (e.g., using a virtual environment or conda environment) to avoid dependency issues. This preparation prevents technical delays later.
   - **Pitfall to Avoid:** Skipping environment setup can lead to last-minute library conflicts. Also, ensure any random-based algorithms will be reproducible by setting a random seed in code when needed.

2. **Problem Familiarization:** Research and summarize the Examination Timetabling Problem:
   - **Definition:** Understand that the problem involves assigning a set of exams into time slots (and possibly rooms) given a set of constraints ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Examination%20timetabling%20problem%20can%20be,simple%20example%20of%20a%20soft)) ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=,known%20as%20a%20clashing%20constraint)). Typically, **hard constraints** (which must be satisfied for a timetable to be feasible) include conditions like *no student should have two exams at the same time* ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=,known%20as%20a%20clashing%20constraint)). **Soft constraints** (which are desirable but not absolutely required) improve solution quality, such as *spreading a student’s exams as far apart as possible* ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=as%20a%20clashing%20constraint%29)).
   - **Complexity:** Note that this is an NP-hard scheduling problem (meaning it’s computationally intractable to find optimal solutions by brute force for large instances) ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Examination%20timetabling%20is%20a%20type,have%20been%20proposed%20in%20scientific)). This justifies using heuristic or approximate algorithms. For instance, many researchers use heuristic and meta-heuristic approaches to find good solutions within reasonable time ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Examination%20timetabling%20is%20a%20type,have%20been%20proposed%20in%20scientific)).
   - **Existing Approaches:** Identify known methods from literature or prior art. Common approaches include **graph coloring heuristics**, integer linear programming formulations, and local search/metaheuristics (e.g., simulated annealing, genetic algorithms). For example, examination timetabling can be modeled as a graph coloring problem where each exam is a node and an edge signifies a conflict (shared student) ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=place%20in%20the%20same%20time,exams%20and%20orders%20them%20in)). Such models have been successfully tackled with greedy coloring algorithms in past research ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=timetabling%20problems%20,the%20University%20Malaysia%20Pahang%20examination)). Recognize that our roadmap phases will likely incorporate a heuristic approach first, given time constraints.
   - **Scope and Roadmap:** Review the provided roadmap Phases 1–10. Outline the major milestones (from requirements gathering to final testing) to ensure you understand how the work will progress. This day’s research will inform decisions in upcoming days and ensure clarity moving forward.
   - **Documentation:** Create a brief document (or notes) summarizing key constraints and objectives discovered. This will serve as a reference when formalizing requirements and designing the solution.

**Connection to Next Phase:** By the end of Day 1, the development environment is ready and you have a solid conceptual grounding of the problem. This preparation leads into Phase 1, where you will formally define requirements and constraints (in Day 2). The knowledge of NP-hardness and known strategies (graph coloring, etc.) will influence the choice of solution approach in Phase 3 and beyond.

## Day 2: Requirement Analysis and Constraint Definition (Phase 1)

**Goals:** Phase 1 focuses on understanding and documenting all requirements for the timetabling problem. This includes identifying hard and soft constraints and deciding on the criteria for a “good” timetable. By the end of Day 2, you should have a clear specification of the problem your code will solve.

1. **Hard Constraints Identification:** List all the non-negotiable constraints:
   - The primary hard constraint (clashing constraint) is *no student can sit for more than one exam at the same time* ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=,known%20as%20a%20clashing%20constraint)). This means if two exams share at least one student, they must be scheduled in different time slots.
   - If the problem involves room assignments, another hard constraint is that each exam must fit in a room with enough seating capacity, and a room cannot host two exams at the same time (this introduces room constraints, though if the dataset/roadmap treats it as un-capacitated, we may ignore room capacity for now).
   - Note any institution-specific hard constraints: e.g., certain exams cannot occur at the same time due to administrative reasons, or a particular exam must happen in a specific period. In general, ensure you gather *all* hard rules that the schedule must obey.
   - **Approach:** Represent these constraints clearly, possibly by writing small Python checks or assertions in plain language. For example, you might outline a function `is_feasible(schedule)` that will later verify these conditions (ensuring no student is double-booked, etc.).
   - **Pitfall:** Missing a hard constraint can lead to producing invalid timetables. Double-check requirements (perhaps from problem description or dataset documentation) so that you implement all of them.

2. **Soft Constraints and Objectives:** Determine the desirable, but not strictly required, constraints that improve schedule quality:
   - The common soft constraint is to **maximize the spacing between exams for any student**, which equates to minimizing students’ having exams too close together ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=as%20a%20clashing%20constraint%29)). In practice, this is often measured by a penalty score: if a student has two exams close in time (e.g., back-to-back or on the same day), it incurs a penalty. The objective is to minimize the total penalty across all students ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=The%20Toronto%20dataset%20has%20one,which%20are%20defined%20as%20follows)).
   - For example, the well-known *Toronto dataset* uses a specific penalty scheme: if a student has two exams in consecutive time slots, a penalty of 16 is added; if they are one slot apart (with one free slot in between) a penalty of 8 is added; gaps of 2, 3, and 4 slots have penalties 4, 2, and 1 respectively; any gap of 5 or more slots yields 0 penalty ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Equation%20,hard%20constraint%20of%20the%20problem)). We can adopt a similar scheme for evaluating timetable quality.
   - Other soft constraints might include: avoiding scheduling any student’s exams on the same day (if possible), or not having too many exams on a single day for fairness. List whichever soft constraints are relevant. Each will translate into a component of the objective function or a penalty calculation in code.
   - **Approach:** Define how you will quantify the soft constraint satisfaction. Likely, you will create a function later (e.g., `calculate_penalty(schedule)`) that computes the total soft constraint penalty for a given timetable. Today, you outline what that function needs to consider (e.g., iterate over each student’s exam schedule to measure spacing).
   - **Key Consideration:** Soft constraints can sometimes conflict with each other or with hard constraints. It’s important to clarify the priority: **hard constraints must always be satisfied first** (feasibility), then within the feasible solutions, we aim to optimize soft constraints. This means our implementation will likely be a two-step approach: (a) find a conflict-free timetable, and (b) refine it to improve soft criteria.

3. **Data & Input Understanding:** Determine what input data is needed to enforce these constraints:
   - Typically, input might consist of a list of exams, a list of students, and a mapping of which students are enrolled in which exams (or equivalently, which exams conflict because they share students). If using a standard dataset, understand its format (e.g., a conflict matrix, or a list of student-exam pairs).
   - Plan how to represent this data in Python. For instance, a convenient structure is a dictionary mapping each exam to the set of students taking it, or vice versa (student to exams). Also, a conflict matrix (an `N x N` matrix where entry `[i,j]` is the number of students common to exam i and j) is useful for quick lookup of conflicts ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=,students%20%2C%20otherwise%20is%20zero)).
   - Decide on how to label or index exams and timeslots. It’s typical to number exams (0,1,2,...) and timeslots (0,1,2,...). Also note the total number of timeslots available (if fixed by an exam period schedule). If not given, we might treat timeslots as an extendable resource initially.
   - **Suggested Tools:** Use `pandas` or simple file I/O to load input data. For example, if the input is a CSV with columns (Student, Exam), you can use `pandas.read_csv` to load it and then group by Exam to get students. If input is in a custom format, plan to write a parser. Ensure you have a small example data on hand to test with (you can create a toy example manually for now).
   - **Output Requirements:** Also clarify what the output should look like. Typically, the result might be a schedule listing for each exam its assigned timeslot (and room if relevant). Knowing this now will help in designing data structures. For example, the output could be a dictionary `{exam: timeslot}` for each exam or a schedule matrix.
   - **Pitfall:** Incomplete understanding of input can cause delays. Make sure you know how you will get data into your program. If a real dataset is not readily available, plan to generate synthetic data for testing the algorithm.

**Connection to Next Phase:** After Day 2, you have a formal definition of the problem: all constraints and the objective are clearly specified. This feeds directly into Phase 2 (Day 3), where you will design data structures and representations that embody these requirements in code. The constraints identified today will be implemented as checks or calculation functions in later phases (Phase 4 for hard constraints, Phase 5-6 for soft constraint evaluation).

## Day 3: Data Model Design and Representation (Phase 2)

**Goals:** In Phase 2, design efficient data structures to represent the exam timetabling problem in code. By end of Day 3, you should have a clear model for exams, students, and timeslots, and possibly some helper functions to manipulate this data.

1. **Data Structure Definition:** Decide how to represent core entities:
   - **Exam Representation:** Each exam could be represented by an ID or code (e.g., an integer or a string). You might create a class `Exam` with attributes like `exam_id`, `enrolled_students`, etc., but a simpler representation can be just using the exam ID as key in dictionaries that hold needed info. For example, use a dict `exam_students` where `exam_students[exam_id]` is a set of student IDs taking that exam.
   - **Student Representation:** Students can be represented by IDs as well. A dict `student_exams` can map each student to the set of exams they take. This is effectively the inverse of `exam_students`. It will be useful for quickly checking a student’s exam schedule or generating constraints.
   - **Timeslots:** Determine how to label timeslots. If the number of timeslots is fixed (say the exam period has 20 slots), you might keep that as a constant or parameter. If not fixed, your algorithm can assign new slot numbers as needed. A timeslot could simply be an integer index. If needed, maintain a mapping of slot index to real date/time (for output readability), but internally integer indices suffice.
   - **Schedule Representation:** The timetable (schedule) can be represented as a mapping from exam -> timeslot (e.g., a dictionary `schedule` where `schedule[exam] = timeslot` for each scheduled exam). This is convenient for checking an exam’s slot. Additionally, for checking conflicts quickly, you might want a mapping of timeslot -> exams scheduled in that slot, or timeslot -> students (union of students of exams in that slot).
   - **Conflict Matrix or Graph:** Pre-compute a structure that identifies which exams conflict. For example, an `N x N` conflict matrix `conflicts[i][j]` = number of shared students between exam i and j ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=,students%20%2C%20otherwise%20is%20zero)). Or build a graph using `networkx` where nodes are exams and an edge connects two exams that conflict (edge weight could be number of common students). This will be heavily used by the scheduling algorithm.
   - **Suggested Python Tools:**
       - Use Python’s `set` type for lists of students in exams and for conflict checking (set intersections are efficient and readable).
       - Use `collections.defaultdict` for building maps like `student_exams` from a list of (student, exam) pairs.
       - If using a conflict matrix, consider using `numpy` arrays or a `pandas.DataFrame` for convenience in calculations (e.g., penalty computation later).
       - If representing as a graph, the `networkx` library’s graph structures can be used (with exam IDs as nodes and edges added via `G.add_edge(exam_i, exam_j)` for each conflict).
   - **Pitfall:** Be mindful of memory if the exam count is large. A conflict matrix is size N^2, which might be large if N is in the thousands. In such cases, storing only adjacency lists (e.g., a dict `conflict_list` where `conflict_list[exam]` is the list of exams that conflict with it) is more memory-efficient.

2. **Implement Data Loading (or Preparation):** Write code to populate these structures:
   - If you have an input file (from a real dataset), implement a parser. For example, if given a list of student–exam enrollments, loop through each record to fill in `exam_students` and `student_exams`. If using `pandas`, you can group by exam:

     ```python
     import pandas as pd
     df = pd.read_csv('enrollments.csv')  # assuming columns: student_id, exam_id
     exam_students = df.groupby('exam_id')['student_id'].apply(set).to_dict()
     student_exams = df.groupby('student_id')['exam_id'].apply(set).to_dict()
     ```

     This quickly gives dictionaries of sets for each exam and each student.
   - If no real data is provided, create a synthetic small dataset to work with for now. For example:

     ```python
     exam_students = {
         0: {101, 102},  # exam 0 taken by students 101, 102
         1: {102, 103},  # exam 1 taken by students 102, 103 (conflicts with exam 0 on student 102)
         2: {104},       # exam 2 taken by student 104 (no conflict with others)
         # ... etc.
     }
     # derive student_exams from exam_students
     student_exams = {}
     for exam, students in exam_students.items():
         for s in students:
             student_exams.setdefault(s, set()).add(exam)
     ```

     This ensures you have a working example to test algorithms on in upcoming days.
   - Build the conflict graph or list from this data. For each exam, you can compile the set of conflicting exams by looking at all students in that exam and gathering other exams those students take. Pseudocode:

     ```python
     conflict_list = {exam: set() for exam in exams}
     for exam in exams:
         for student in exam_students[exam]:
             conflict_list[exam].update(student_exams[student])
         conflict_list[exam].discard(exam)  # remove itself if present
     ```

     Each `conflict_list[exam]` will then contain all exams that share at least one student with `exam`.
   - Verify this structure on the example to ensure conflicts are identified correctly (e.g., exam 0’s conflict list should contain exam 1 in the toy data above).
   - **Tip:** If using `networkx`, you could alternatively create a graph and add edges for each conflict:

     ```python
     import networkx as nx
     G = nx.Graph()
     G.add_nodes_from(exam_students.keys())
     for student, exams in student_exams.items():
         for e1 in exams:
             for e2 in exams:
                 if e1 < e2:  # to avoid duplicate edges
                     G.add_edge(e1, e2)
     ```

     This automatically builds an undirected graph of exam conflicts. You can then use `nx.degree` or similar to get conflict counts, etc.
   - **Data Model Documentation:** Write down or comment the structure of your data clearly. This will help when writing scheduling algorithms (so you know what inputs and outputs to expect).

3. **Validation of Data Model:** Do a sanity check to ensure the data representation aligns with the requirements:
   - Confirm that if a student is in two exams, those exams appear in each other’s conflict lists or conflict matrix. Also, test a simple hard constraint check with the structures: iterate through each student in `student_exams` and assert that no student is assigned to two exams in the same timeslot (this is just a conceptual check now, since we haven’t assigned timeslots yet). Basically, you’re confirming that the way we plan to check conflicts (via these structures) is correct.
   - Make sure that your structures can support the operations needed for constraints: for example, given an exam and a timeslot, you’ll need to quickly find if any conflicting exam is already in that timeslot. With `timeslot -> students` sets (which can be built during scheduling), that check is efficient (intersection of sets). With `conflict_list`, you can loop through conflicting exams and check their slot assignments.
   - **Pitfall:** If the data model is flawed, the algorithm stages will be difficult. Ensure clarity now (for instance, avoid having redundant sources of truth that can get out of sync; one representation for each relation is enough).
   - No actual scheduling is done today – only structure and data preparation. If everything checks out, you’re ready to proceed to designing the solution approach.

**Connection to Next Phase:** With the data model in place after Day 3, Phase 3 can begin. On Day 4, you will leverage these structures to outline the actual scheduling algorithm. The conflict information and data mappings created now will be the foundation on which the scheduling (Phase 4) and optimization (Phases 5–7) algorithms operate. Essentially, you’ve built the canvas on which the timetabling solution will be painted.

## Day 4: Algorithm Selection and Design (Phase 3)

**Goals:** Phase 3 is about choosing a solution approach and designing the algorithm in detail before coding. On Day 4, decide which algorithmic strategy to implement (given the constraints and data model) and sketch out its steps (with pseudocode). This will likely involve a greedy graph coloring heuristic for initial scheduling and setting the stage for improvement steps.

1. **Select Initial Scheduling Approach:** Considering the research from Day 1 and the NP-hard nature of the problem, choose a heuristic to construct an initial feasible timetable:
   - **Graph Coloring Heuristic:** A natural choice is a greedy graph coloring algorithm, treating each exam as a node in a conflict graph ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=place%20in%20the%20same%20time,exams%20and%20orders%20them%20in)). The idea: assign time slots (colors) to exams such that no two adjacent nodes (conflicting exams) share the same color. Greedy strategies won’t guarantee the optimal solution, but they can quickly produce a valid one ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=timetabling%20problems%20,the%20University%20Malaysia%20Pahang%20examination)).
   - **Order of Assignment:** Decide an ordering of exams for assignment. A common heuristic is *largest degree first* (also known as degree saturation or difficulty index ordering) ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=place%20in%20the%20same%20time,exams%20and%20orders%20them%20in)) – i.e. schedule the exam with the most conflicts first, since it’s the hardest to place. Other strategies include most-enrolled students first or exams with specific constraints first. For this plan, we will use the largest-degree-first heuristic to maximize the chance of finding a valid slot early for tough exams.
   - **Alternate Approaches:** Acknowledge alternatives like using a **constraint solver or ILP**: e.g., using Google OR-Tools CP-SAT or PuLP to formulate this as an optimization problem. However, those might be overkill or too slow for large instances and may not fit in a 15-day part-time schedule. We prioritize a custom heuristic for clarity and speed of development.
   - **Decision Justification:** The chosen greedy approach will quickly satisfy hard constraints (Phase 4) and produce a baseline schedule we can later improve for soft constraints (Phases 5–7). It’s a straightforward implementation path and aligns with known successful methods for exam timetabling ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=timetabling%20problems%20,the%20University%20Malaysia%20Pahang%20examination)).

2. **Design the Greedy Scheduling Algorithm:** Outline how the algorithm will assign timeslots to exams step-by-step:
   - **Data Needed:** The algorithm will use:
     - The conflict information (e.g., `conflict_list` or graph) to know which exams cannot share a slot.
     - A list of exams sorted by their conflict count (or degree in the conflict graph).
   - **Procedure:** High-level pseudocode for greedy assignment:

     ```text
     exams = list of all exam IDs
     sort exams in descending order by number of conflicts (degree)
     schedule = {}  # exam -> timeslot assignment
     for exam in exams:
         for t in available_timeslots (starting from 0 upward):
             if no conflict with scheduled exams in timeslot t:
                 assign schedule[exam] = t
                 break
         if exam not scheduled (no break happened):
             assign schedule[exam] = new_timeslot  # allocate a new time slot
     ```

     In this pseudocode, “no conflict” means: for every other exam `e` already assigned to timeslot `t`, ensure `e` is not in `conflict_list[exam]` (i.e. they share no student). Or equivalently, none of the students in `exam` are in the set of students already scheduled in slot `t`.
   - **Data Structures for Efficiency:** To implement the check *"no conflict with exams in timeslot t"*, consider maintaining:
     - A dict `slot_students` mapping each timeslot to the set of all students who have an exam in that slot. This can be updated as we assign exams. Then the check is: `slot_students[t]` has no intersection with `exam_students[exam]`.
     - Alternatively, check each already scheduled exam `e` in `slot t` and ensure `e` is not in `conflict_list[exam]`. Using `slot_students` is more direct: intersection of two sets (Python set intersection operation) is efficient in C and quickly tells if any common student exists.
   - **Python Implementation Plan:**
     - We’ll likely implement this as a function, e.g., `assign_timeslots_greedy(exam_students, student_exams)` that returns a `schedule` dict.
     - Use Python loops for assignment; since this is heuristic, minor inefficiencies are okay, but note that nested loops over exams and timeslots can become expensive if not managed (if there are hundreds of timeslots). Our use of sets for conflict checks will mitigate some cost.
     - The maximum number of timeslots needed could be up to the number of exams in worst case (if every exam conflicts with every other). In practice, it will be much less. We can start with an assumption that adding new timeslots as needed is fine.
   - **Pitfall:** If the number of available timeslots is fixed and the greedy algorithm cannot assign an exam (meaning our heuristic fails to find a solution with the given slots), we’d have to implement backtracking or use a different strategy. To keep within scope, we assume either timeslots can grow or that a feasible assignment exists with given timeslots. In a real scenario, careful handling of this (like backtracking on earlier assignments if stuck) would be needed for completeness.

3. **Plan Soft Constraint Integration:** Although the main focus now is getting a feasible schedule, keep in mind how we’ll handle soft constraints later:
   - Realize that the greedy algorithm we design does **not** consider soft constraints at assignment time; it only ensures no conflicts. This might bunch some exams close together (especially if minimizing number of slots). We will handle improvements in later phases.
   - To prepare, ensure the schedule data structure from the greedy algorithm is easy to feed into a penalty calculator. Likely the `schedule` dict and the `student_exams` map are enough to compute soft constraint penalties (we can derive each student’s exam times from these).
   - Consider that after initial assignment, we might want to allow the algorithm to use more timeslots than the minimum required, to give flexibility for spreading exams. We could intentionally leave some slots unused to reduce density. For now, the greedy approach will naturally use new slots when needed, which might implicitly spread some exams out.
   - **Connection to Next Steps:** Document that after this Phase 3 design, Phase 4 (Days 5–6) will implement the greedy algorithm, and Phases 5–7 (Days 7–9) will introduce an improvement algorithm to reduce soft constraint violations.

4. **Pseudocode & Function Outlines:** Write detailed pseudocode or function outlines to guide implementation:
   - Sketch the function `assign_timeslots_greedy` including how it will iterate and how it will update `slot_students`. This pseudocode will be directly translated into Python code on Day 5.
   - Example pseudocode incorporating conflict check:

     ```text
     function assign_timeslots_greedy(exam_list, exam_students):
         initialize empty dict schedule
         initialize dict slot_students = {}  (maps slot -> set of students in that slot)
         slot_count = 0
         for exam in exam_list:  # already sorted by difficulty
             for slot in range(slot_count):
                 # check if exam can go into this slot
                 conflict = False
                 for student in exam_students[exam]:
                     if student in slot_students[slot]:
                         conflict = True
                         break
                 if not conflict:
                     schedule[exam] = slot
                     slot_students[slot].update(exam_students[exam])
                     break
             if exam not in schedule:  # no existing slot could accommodate this exam
                 schedule[exam] = slot_count
                 slot_students[slot_count] = set(exam_students[exam])
                 slot_count += 1
         return schedule
     ```

     This is a rough outline to implement in Python. (We might refine it to use set intersection instead of looping over students for efficiency.)
   - Additionally, outline a stub for `calculate_penalty(schedule, student_exams)` which will be implemented on Day 7, and a stub for `improve_schedule(schedule, ...)` for Day 9. This isn’t coding yet, but thinking ahead helps ensure the greedy schedule format is compatible with those functions.

**Connection to Next Phase:** By the end of Day 4, you have a solid algorithm design for constructing an initial timetable (Phase 4 to implement) and you’ve set the stage for integrating constraint checks and improvements. Day 5 will be about turning this pseudocode into actual Python code and verifying that the algorithm works on the data structures from Phase 2.

## Day 5: Implementing the Greedy Scheduling Algorithm (Phase 4, Part 1)

**Goals:** Start Phase 4 by coding the initial timetable construction algorithm designed in Phase 3. On Day 5, implement the greedy graph coloring heuristic to assign exams to timeslots satisfying all hard constraints. Aim to get a working function that produces a conflict-free schedule.

1. **Code the Initial Assignment Function:** Translate the pseudocode from Day 4 into Python:
   - Implement the function `assign_timeslots_greedy(exam_list, exam_students)`:
     - **Sorting:** First, prepare the list of exams sorted by difficulty (conflict count). For example:

       ```python
       exam_list = sorted(exam_students.keys(), key=lambda ex: len(conflict_list[ex]), reverse=True)
       ```

       This uses the `conflict_list` (or you can compute degree on the fly from `exam_students` data by summing lengths of other sets) to sort descending.
     - **Assignment Loop:** Initialize `schedule = {}` and `slot_students = {}` as planned. Loop through each exam in the sorted list and attempt to place it:

       ```python
       for exam in exam_list:
           placed = False
           for slot, students_in_slot in slot_students.items():
               # check conflict via set intersection
               if exam_students[exam].isdisjoint(students_in_slot):
                   schedule[exam] = slot
                   students_in_slot |= exam_students[exam]  # update in-place
                   placed = True
                   break
           if not placed:
               # assign to a new slot
               new_slot = len(slot_students)
               schedule[exam] = new_slot
               slot_students[new_slot] = set(exam_students[exam])  # copy the set
       ```

       This code uses `set.isdisjoint()` to check if two sets have no elements in common, which efficiently checks for conflicts (returns True if no common student). We update the `slot_students` for the slot when an exam is placed.
     - **Validation:** After building the schedule, it’s good to assert that it’s conflict-free as a sanity check:

       ```python
       for student, exams in student_exams.items():
           assigned_slots = { schedule[e] for e in exams }
           assert len(assigned_slots) == len(exams)
       ```

       This verifies no two exams of the same student got the same timeslot. This should hold if the algorithm is correct.
   - **Edge Cases:** If an exam has no students (unlikely in real scenario) it can go anywhere since it conflicts with nothing. Our loop would assign it to slot 0 likely. That’s fine, just note it.
   - **Logging:** Optionally, print the number of timeslots used and maybe the distribution of exams per slot for insight. This helps to see if the schedule is tightly packed or spread out.

2. **Test the Greedy Algorithm on a Small Example:** Use the synthetic data from Day 3 (or create a simple new one) to verify the function:
   - Example: with the small dataset where exam 0 and 1 conflict (shared student 102) and exam 2 is independent:
     - The sorted order might be [0,1,2] (exams 0 and 1 each have 1 conflict, exam 2 has 0).
     - The algorithm might assign exam 0 to slot 0, exam 1 cannot go to slot 0 (due to student 102 conflict) so it creates slot 1, and exam 2 can go to slot 0 (no conflict with exam 0’s students if exam 2 shares none).
     - Result could be: exam0 -> slot0, exam1 -> slot1, exam2 -> slot0. No student has two in slot0? Check: student 102 has exam0 (slot0) and exam1 (slot1) – OK; student 101 has only exam0; student 103 has exam1; student 104 has exam2 (slot0) – but exam2 (slot0) and exam0 (slot0) share no student, so slot0 has students {101,104} after assignment, which is fine.
   - Print the schedule result to visually inspect it, and verify the hard constraint by scanning: no student appears in two exams with the same slot.
   - If something is off (e.g., if we mistakenly allowed a conflict), debug by checking the logic in the `isdisjoint` condition or how `slot_students` is updated. Common pitfalls might be forgetting to update `slot_students` properly or mis-sorting the exam list.

3. **Refine and Optimize if Necessary:** If the greedy assignment is slow or inefficient on larger tests:
   - Note that our inner loop checks each slot for each exam. In worst case (many slots), this could be somewhat slow (O(#exams *#slots* avg_students_per_exam) operations). However, since each exam goes into a slot fairly quickly usually, this is acceptable for moderate sizes. For large instances (hundreds of exams, dozens of slots), this should still be fine in Python.
   - We can micro-optimize by breaking out of loops early (we already do with the `break` once placed) and using set operations which are fast in Python’s C code.
   - If using `networkx`, note that `networkx.coloring.greedy_color` could be an alternative one-liner to assign slots (colors). For instance:

     ```python
     coloring = nx.coloring.greedy_color(G, strategy='largest_first')
     ```

     This returns a dict of exam -> color (slot) assignment using the largest degree ordering by default. You could compare this result with our custom implementation. Using networkx might be slower in pure Python due to overhead, but it’s an option. In this plan, we continue with our own implementation for transparency.
   - Ensure that the algorithm is clearly documented in code comments for future reference. Mention that this achieves Phase 4’s goal of a feasible timetable under hard constraints.

4. **Handle any Hard-Constraint Variations:** If additional hard constraints exist (like specific exam timing requirements or room capacities):
   - For example, if *room capacity* is a concern and multiple exams can be in the same slot only if in different rooms, our model would need extension (e.g., scheduling an exam into a (room, slot) pair rather than just slot). This would significantly complicate the algorithm (essentially an assignment problem combined with coloring). Given the roadmap, it might be beyond scope to implement fully. For now, assume un-capacitated scenario (which is common in many benchmark problems) ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=The%20examination%20timetabling%20problem%20is,described%20in%20the%20following%20subsections)).
   - If a particular exam must occur in a specific slot (say exam A must be on slot 0 due to external requirement), you can simply assign it upfront and remove it from the list, or during assignment always check that and skip violating slots. We won’t digress into these specifics unless needed.
   - **Tip:** Keep the algorithm focused on core constraints. Extra conditions can often be layered in by adjusting the conflict check (for instance, treat a pre-fixed exam as conflicting with all exams in other slots except its fixed slot, forcing it to remain where required).

**Connection to Next Phase:** At the end of Day 5, you have a functioning algorithm that produces a conflict-free exam schedule (Phase 4 halfway done). Day 6 will continue Phase 4 by thoroughly verifying the schedule and possibly tweaking the algorithm based on test results. After that, you will move to Phase 5, which introduces the soft constraint evaluation using the schedule from this phase.

## Day 6: Hard Constraint Verification and Schedule Validation (Phase 4, Part 2)

**Goals:** Complete Phase 4 by validating that the schedule produced by the greedy algorithm truly meets all hard constraints and is a solid foundation for further improvement. Day 6 is about testing the schedule on various scenarios, fixing any remaining bugs, and confirming we have a correct baseline solution.

1. **Comprehensive Hard-Constraint Testing:** Now that the greedy scheduler is implemented, test it on multiple scenarios to ensure it never violates hard constraints:
   - **Small Handcrafted Cases:** Create a few small test cases with known outcomes:
     - Case 1: No conflicts (e.g., 3 exams, 3 students, each student in one different exam). Expected result: all exams can be in slot 0 since no conflicts.
     - Case 2: All exams mutually conflict (every student takes all exams). Expected: each exam must end up in a distinct slot. If there are N exams, expect N slots.
     - Case 3: A chain of conflicts (e.g., exam1 conflicts with exam2, exam2 with exam3, exam3 with exam1 – a triangle). Expect 3 slots for 3 exams if all conflict with each other; verify the algorithm handles that correctly (greedy might give exam1->slot0, exam2->slot1, exam3 can’t go in slot0 due to conflict with exam1 or slot1 due to conflict with exam2, so gets slot2).
     - Case 4: More complex (mix of conflicts). Use the synthetic dataset or any sample from known benchmarks if available to run a realistic scenario.
   - **Automated Verification:** Write a utility function `check_hard_constraints(schedule, student_exams)` that returns True if no student has two exams in the same slot (and checks any other hard constraints you identified in Day 2):

     ```python
     def check_hard_constraints(schedule, student_exams):
         for student, exams in student_exams.items():
             # gather the slots this student's exams are in
             slots = { schedule[exam] for exam in exams }
             if len(slots) != len(exams):
                 return False  # a student has two exams in one slot
         return True
     ```

     Run this after generating a schedule. It should return True for all test cases. If it returns False, there’s a bug to fix (likely in the assignment logic).
   - If room capacity or other hard constraints were considered, similar checks should be implemented for them (e.g., count students in each room per slot, ensure not over capacity).

2. **Debugging and Fixes:** If any test reveals an issue:
   - Use print statements or a step-by-step trace on the problematic scenario to understand why a conflict slipped through.
   - Common potential issues:
     - The check for conflicts might be flawed (though using `isdisjoint` on student sets is straightforward, but maybe an exam was assigned to a slot where a conflict exam was assigned later? That shouldn’t happen if we schedule in a fixed order).
     - Perhaps we forgot to mark something in `slot_students`. For example, if we did `students_in_slot |= exam_students[exam]`, ensure that actually updates the dictionary’s set. (It does if we fetched the set object and modified it in place, as in the code snippet, but if we accidentally did `students_in_slot = ...` that wouldn’t update the dict. Be careful that the set in the dict is updated by reference.)
     - If using `networkx.greedy_color` alternative, verify it indeed colored properly (some greedy implementations might assign same color to connected nodes if not careful with parameters—less likely, but test it).
   - After fixes, re-run tests until all known scenarios pass the `check_hard_constraints`.

3. **Evaluate Timeslot Utilization:** Although not a primary goal, note how many timeslots the greedy algorithm ended up using for a given test:
   - If it’s using significantly more timeslots than necessary, the schedule might be very spread out (which is actually good for soft constraints but maybe inefficient if timeslots are limited). If it’s using the minimum possible (like equal to the size of the largest clique in the conflict graph), then the schedule is compact and might have many students with back-to-back exams.
   - This observation will inform our improvement phase. A compact schedule may need more reshuffling to satisfy soft constraints, whereas a spread out one might already be decent. If needed, one could tweak the greedy algorithm to bias towards more spreading (like always allocate a new slot even if an exam *could* fit earlier, to artificially space out exams). We will, however, handle spreading via the improvement algorithm rather than complicating the greedy step.
   - **Logging:** If not done already, log the result of schedule creation in a clear format. For example:
     - Print each slot and which exams (or how many exams) are scheduled there.
     - Print if any slot has a lot of exams – those might indicate many exams that don’t conflict with each other, which is fine.
     - Save a copy of a sample schedule output for reference.

4. **Prepare for Soft Constraint Phase:** With a reliable initial schedule, we can move to Phase 5 (soft constraints). Use the end of Day 6 to set up any scaffolding needed:
   - For example, ensure the function stubs for penalty calculation (`calculate_penalty`) exist so you can fill them in Day 7.
   - If you have the conflict matrix available, that will help in computing penalties quickly. If not, you can compute penalty via student lists.
   - Confirm that data structures from earlier phases (like `student_exams`) are still accessible for use in calculating soft constraint violations.
   - **Documentation:** Update your project notes or docstring for the scheduling function to indicate it achieves a feasible schedule (Phase 4 result). Mention complexity or any assumption (e.g., it will always find a schedule if one exists, given enough timeslots).

**Connection to Next Phase:** By finishing Day 6, Phase 4 is complete – you have a functioning baseline solution that meets hard constraints. Phase 5 (Day 7) will introduce measuring the soft constraints (penalty) on this schedule, and Phase 6–7 (Days 8–9) will tackle improving the schedule to reduce that penalty. The groundwork from Phase 4 ensures that the improvement phase starts from a valid timetable.

## Day 7: Soft Constraint Evaluation and Penalty Calculation (Phase 5)

**Goals:** Begin Phase 5 by quantifying how well the current schedule meets soft constraints. On Day 7, implement a function to calculate the soft constraint penalty (or any objective metric) for a given timetable. This will allow us to evaluate the quality of the timetable and guide the improvement algorithm in subsequent days.

1. **Define the Penalty Function:** Design the computation for the total penalty due to soft constraint violations:
   - Based on our identified soft constraint (spacing out exams for each student), define how to calculate the penalty. We will use the scheme from Day 2 (e.g., the Toronto benchmark penalties ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Equation%20,hard%20constraint%20of%20the%20problem))):
     - For each student, look at the timeslots of their exams in the current schedule. For every pair of exams that student has, determine the gap (difference) in timeslot numbers.
     - Use a mapping for gap to penalty: if gap = 0 (which shouldn’t happen if hard constraints are satisfied) ignore because that’s an invalid schedule; gap = 1 (consecutive slots) -> 16 points, gap = 2 -> 8 points, gap = 3 -> 4 points, gap = 4 -> 2 points, gap = 5 -> 1 point, gap ≥ 6 -> 0 points ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Equation%20,hard%20constraint%20of%20the%20problem)).
     - Sum all these penalties for all students. Usually, to avoid double counting, one can iterate only pairs where timeslot_i < timeslot_j.
   - **Implementation Plan:** Two possible approaches:
     - **Student-by-student loop:**

       ```python
       def calculate_penalty(schedule, student_exams):
           penalty = 0
           for student, exams in student_exams.items():
               # get a sorted list of this student's exam slots
               slots = sorted(schedule[exam] for exam in exams)
               # for each pair of consecutive exams in sorted order, compute gap
               for i in range(len(slots) - 1):
                   gap = slots[i+1] - slots[i]
                   if gap == 1: penalty += 16
                   elif gap == 2: penalty += 8
                   elif gap == 3: penalty += 4
                   elif gap == 4: penalty += 2
                   elif gap == 5: penalty += 1
                   else: penalty += 0
           return penalty
       ```

       This considers each adjacent pair in chronological order for a student. However, note that if a student has more than two exams, pairs beyond adjacent (like exam1 and exam3) also matter if their gap is small. Actually, the typical interpretation is each *pair* of exams contributes if they are within 5 slots. So a student with exams at slots [0, 3, 5] would have pairs (0,3) gap 3 -> 4 points, (0,5) gap 5 -> 1 point, (3,5) gap 2 -> 8 points. The above loop only took adjacent pairs which would miss (0,5). So instead, we should consider all pairs.
               - We can do a double loop or combinations on `slots`. For each combination of two slots for that student, if gap = d, apply penalty as above. To avoid double counting between students, we keep within each student's loop.
     - **Conflict matrix approach:** If we have the conflict matrix (where `conflict[i][j]` = number of students in both exam i and j), we can calculate penalty more globally:
       - For every pair of exams (i,j) that conflict (meaning `conflict[i][j] > 0`, `i < j)`, if they are scheduled in slots $s_i$ and $s_j$, compute gap = $|s_i - s_j|$ and add `conflict[i][j] * penalty_for_gap(gap)` to total. This essentially sums the same as iterating students, but more efficiently if the matrix is sparse.
       - This is a vectorized approach if using numpy: you could loop or even use matrix operations, but double loop is fine given conflicts are usually sparse relative to total pairs.
       - To implement penalty_for_gap, maybe prepare a list or dict: `gap_penalty = {1:16, 2:8, 3:4, 4:2, 5:1}` for quick lookup, and default 0 for >=6.
   - **Choose Approach:** For clarity, the student-by-student approach is easier to implement correctly (less risk of double counting because each student’s pairs are distinct). It might be slightly less efficient if a student has many exams, but typically students have only a few exams.
   - Implement accordingly, making sure to cover all pairs. Python’s `itertools.combinations(sorted_slots, 2)` can generate all unique pairs of exam slots for a student to evaluate.
   - **Test Penalty Calculation:** Manually verify on a small scenario:
     - If a student has exams in slots [0, 1], penalty = 16 (consecutive).
     - If in [0, 2], penalty = 8.
     - If in [0, 5], penalty = 1.
     - If in [0, 6], penalty = 0.
     - If a student has 3 exams in [0,1,3]: pairs -> (0,1)=16, (0,3)=4, (1,3)=? gap 2 (3-1=2) -> 8, total = 28 for that student.
     Confirm that matches expectations. We might cross-check using the conflict matrix if available to ensure consistency.

2. **Calculate Baseline Schedule Quality:** Use the `calculate_penalty` function on the current schedule from Day 6:
   - Get the total penalty of the initial greedy schedule. This number is a measure of soft constraint violations (lower is better, 0 would mean perfectly spread for all).
   - Analyze the result: If it’s a high number, it indicates many students have close-together exams. This is expected if the greedy schedule was compact. This baseline gives us a target to improve upon in Phase 6.
   - For context, if we had a known benchmark, we could compare our penalty to known good values. But in absence, we just use it as relative measure.
   - Print or log some details:
     - Perhaps list a few worst-off students (those with highest individual penalty contributions). You could do this by computing each student’s penalty sum and sorting. This can guide where improvements might focus (e.g., a particular student has two consecutive exams, try to separate them).
     - Example logging: “Initial schedule penalty = 100 (16 students have consecutive exams, 5 have exams with one slot gap, etc.)”.
   - **Visualization (Optional):** Use `matplotlib` to create a histogram of gaps for all exam pairs of each student (1-slot gap count, 2-slot gap count, ...). This could illustrate how compressed the schedule is. This is a bonus analysis for insight.

3. **Validate Penalty Function:** It’s crucial that the penalty calculation is correct, as our improvement algorithm will rely on it:
   - Cross-check the function in a scenario with known expected penalty. For example, make a mini schedule: two exams (A, B) with one student taking both, scheduled in slots 0 and 1 -> expected penalty 16. Or slots 0 and 2 -> expected 8. Ensure the function returns that.
   - If using the conflict matrix method, test with a simple conflict matrix. For instance, conflict matrix for two exams with 1 common student would be [[0,1],[1,0]]. If schedule A=0, B=2, ensure the formula adds 8.
   - Double-check that each pair of exams for a student is only counted once. Our approach per student inherently does that. If using matrix, ensure you restrict to i<j to not double count i-j and j-i.
   - **Pitfall:** Watch out for large numbers if a student has many exams. But typically students have limited exams (like maybe up to 6-7 in university settings). The double loop inside one student is fine for that range.
   - Also consider if there are multiple soft constraints, how to combine them. In this plan we have primarily one (spacing). If there were others (like “no student should have 2 exams in one day” which overlaps with spacing, or “certain exams preferred in morning”), you would add additional terms to the penalty. For simplicity, stick to one dimension of soft constraint in this project.

4. **Set Improvement Goal:** Based on the baseline penalty, decide on a target or at least expect to reduce it:
   - For instance, if initial penalty is 100, perhaps with improvements we aim to cut it by a significant percentage (depending on flexibility of schedule).
   - Understand that completely eliminating penalty might not be possible if timeslots are limited. The aim is to **minimize** it, and often there’s a trade-off: using more timeslots (longer exam period) typically reduces penalty.
   - We may not explicitly set a numeric target, but qualitatively the goal is to reduce occurrences of back-to-back (or close) exams for students.
   - Keep in mind any external limit: If the exam period has a fixed number of slots, we cannot just create unlimited spacing. If initially we used say 10 slots but the schedule is allowed 15, the improvement could assign some exams to later slots to spread out conflicts.
   - **Plan for Next Phase:** With the ability to measure quality, we can now design a heuristic to **modify** the schedule and improve this metric. We’ll proceed to Phase 6 on Day 8 to plan that strategy.

**Connection to Next Phase:** Day 7’s accomplishment (a working penalty calculator and a baseline quality measure) directly feeds Phase 6. On Day 8, you will design the improvement algorithm that uses this penalty function to guide schedule adjustments. The verified `calculate_penalty` function ensures we can objectively compare schedules and know if a change is beneficial (key for any local search or optimization technique in Phase 6–7).

## Day 8: Improvement Strategy Design for Soft Constraints (Phase 6)

**Goals:** In Phase 6, devise a method to improve the timetable by reducing soft constraint violations. Day 8 is about choosing an optimization strategy (e.g., local search, simulated annealing) and designing how it will manipulate the schedule. By end of Day 8, you should have a clear game plan and pseudocode for refining the schedule.

1. **Choose an Optimization Technique:** Given the time and complexity considerations, select a heuristic to improve the schedule:
   - **Local Search (Hill Climbing):** A straightforward approach is to perform local moves on the timetable and accept any change that reduces the penalty. A local move could be *moving one exam to a different timeslot* or *swapping two exams’ timeslots*. Hill climbing repeatedly applies such moves as long as improvements are found.
   - **Simulated Annealing:** To avoid local minima, a simulated annealing (SA) approach is beneficial. It allows occasional worse moves to escape local optima. SA would start at a higher “temperature” (more tolerant of worse moves) and gradually cool (becoming more strict about only accepting improvements).
   - **Great Deluge or Tabu Search:** These are alternatives; Great Deluge gradually lowers a threshold of acceptable cost, and Tabu search keeps a memory of recent moves to avoid cycles. These might be overkill for our small project, but worth noting as sophisticated options.
   - For this plan, we will proceed with a **simulated annealing** style improvement, as it’s a well-known meta-heuristic used in timetabling research and relatively straightforward to implement. It can be simplified to a hill climber by tweaking parameters to accept only better moves eventually.

2. **Define Neighbor Generation (Move Set):** Decide what constitutes a “move” or “neighbor” in the search space:
   - **Single-exam Move:** Pick one exam and assign it to a different timeslot (one that is currently different from its assignment). This could be either an unused new slot or an existing slot (if it doesn’t cause a hard conflict).
   - **Swap Move:** Pick two exams and swap their time slots. Swaps can sometimes produce different effects than single moves (especially if two exams could mutually relieve conflicts by swapping).
   - **Complex Moves:** More complex moves (like moving a group of exams) are possible but not needed for now.
   - We will implement at least the single-exam move. Swaps can be implemented as two single moves (exam A to B’s slot and B to A’s slot) but doing it in one step might sometimes allow exploring states not reachable by sequential single moves under certain constraints.
   - **Hard Constraint Check:** Any generated neighbor must still satisfy hard constraints. This means:
     - When moving an exam to a new slot, ensure none of its conflicting exams are in that target slot (use `slot_students` or conflict list to verify).
     - When swapping, ensure that swapping doesn’t put either exam into conflict. If exam A conflicts with some exam C in exam B’s slot, then swap is illegal, etc.
   - Efficient checking: Since we maintained `slot_students`, we can check an exam’s student set against the target slot’s student set for intersection (same as in initial assignment).
   - Also, consider if removing an exam from its current slot frees up some room that allows others, but focusing on one move at a time is fine.

3. **Design the Simulated Annealing Process:** Outline how the algorithm will iterate and decide on moves:
   - **Initialization:** Start with the current schedule (from greedy) as the initial solution. Calculate its penalty (from Day 7) as the current cost.
   - **Iteration Loop:** Set a number of iterations or a time limit. For example, we might allow, say, 1000 iterations of trying random moves (tune this number based on time; we can start with 1000 and adjust if needed).
   - **Temperature Schedule:** Decide on a cooling schedule if using SA. For simplicity, you can define:
     - `temp_start` (initial temperature, maybe based on initial penalty value or a fraction of it),
     - `temp_end` (near 0 by the end),
     - and a formula to decrease temperature each iteration (linear or geometric).
   - **Move Selection:** In each iteration, randomly choose a move:
     - Randomly pick an exam (uniformly from all exams). Randomly pick a new timeslot for it (could be, for instance, among existing slots ± a few new ones). Or pick a second exam for swap with some probability.
     - Ensure the move is valid (no hard conflict). If not, you can either skip this move or attempt another choice.
   - **Evaluate Move:** Compute the penalty of the new schedule if this move is applied. Instead of recomputing the entire penalty from scratch, optimize by calculating the *delta* change in penalty:
     - When moving one exam, only that exam’s students (and any students in the target slot) are affected. One can recalc penalty contribution for those students before and after the move to get delta. But implementing delta might be error-prone; easier is just recalc total penalty with `calculate_penalty` for clarity, given moderate size (we can optimize later if needed).
     - For a swap, check penalty before and after similarly.
   - **Acceptance Criterion:**
     - If the new penalty is lower (improvement), accept the move (update the schedule).
     - If the new penalty is higher (worse solution), accept it with probability `exp(-(delta)/temp)` where `delta` is the increase in penalty and `temp` is current temperature (this is the SA Metropolis criterion). If not accepted, revert the move.
     - This means we’ll need to keep track of the best solution seen so far as well, so at the end we can return the best schedule found (not just the last one).
   - **Cooling:** Reduce the temperature for next iteration (e.g., `temp = temp * alpha` where `alpha` is 0.995 for slow cooling, or a linear decrement).
   - **Termination:** After the set number of iterations (or if we reach a temperature threshold or if no improvement has been found for a long time), stop.
   - **Pseudocode Sketch:**

     ```text
     best_schedule = current_schedule
     best_penalty = current_penalty
     temp = temp_start
     for iter in range(max_iterations):
         pick a random exam X (or random pair X,Y for swap)
         pick a target slot (or swap slots of X and Y)
         if move is not hard-constraint valid: continue  (try another move)
         new_schedule = schedule with move applied
         new_penalty = calculate_penalty(new_schedule)
         delta = new_penalty - current_penalty
         if delta <= 0:
             # accept better (or equal) solution
             current_schedule = new_schedule
             current_penalty = new_penalty
             if new_penalty < best_penalty:
                 best_penalty = new_penalty
                 best_schedule = new_schedule
         else:
             # accept worse solution with some probability
             if random.random() < exp(-delta / temp):
                 current_schedule = new_schedule
                 current_penalty = new_penalty
             else:
                 # reject the move (implicitly by doing nothing)
                 pass
         # cool down temperature
         temp = temp * alpha
     return best_schedule, best_penalty
     ```

   - **Parameter Tuning:** Note that we might need to adjust `max_iterations` and `alpha` (cooling rate) based on experimentation in Day 9. The values will influence how thoroughly the search explores. For a 4-hour day, an iteration count that results in maybe a minute or two of runtime is fine. If each iteration recomputes full penalty in, say, O(N * avg_exams_per_student) time, 1000 iterations is likely fine for a moderate N (like N=100 exams, with a few thousand student exam pairs).
   - **Simplification:** If simulated annealing seems too complex to implement fully, one can simplify to a repeated hill climb with random restarts:
     - For example, do 100 random single moves that improve penalty (if none found, shuffle something and try again). But we’ll attempt the more systematic SA as above for better results.

4. **Plan Code Structure for Improvement:**
   - We will implement an `improve_schedule` function that encapsulates this logic. It might take parameters for iterations and initial temperature, etc., so we can tweak them.
   - Plan to use Python’s `random` module for choosing random exams and moves. Setting a random seed at the start of improvement can make results reproducible for debugging.
   - Ensure the function uses the global `calculate_penalty` we wrote, and that it uses the `student_exams` and `exam_students` data for conflict checking and penalty calc.
   - Also, using our existing data structures:
     - We have `schedule` as a dict exam->slot.
     - We have `slot_students` from initial assignment; we can keep updating that as we move exams (this helps quickly check conflicts and update when an exam moves slots).
   - We should be careful to copy structures when testing moves so as not to ruin the current schedule if a move is rejected. One strategy: work on a copy of the schedule for each trial move, or remove and re-add exam to `slot_students`.
   - Alternatively, a simpler coding approach: for each move, directly modify and if rejected, modify back. That might be easier than copying large dicts each time. We must ensure to revert exactly what changed.
     - E.g., for moving exam X from slot A to slot B:
       - Store old_slot = A.
       - Remove X’s students from `slot_students[A]`, add to `slot_students[B]`.
       - Compute penalty.
       - If rejected, undo: remove from B, add back to A.
       - If accepted, keep changes.
     - This approach requires careful state management but saves copying cost.
   - Write pseudocode for move application and reversion to guide implementation.
   - **Pitfall:** The biggest challenge is ensuring we never introduce a hard conflict during moves. Our check should catch it, but also our state updates should keep things consistent. If a move is accepted that inadvertently created a conflict due to some oversight, that would violate hard constraints, which is unacceptable. So we'll be strict in checking moves.

5. **Prepare for Implementation:** List any helper functions or data needed:
   - We might want a helper to get a random exam or random slot. Or we can inline it.
   - Perhaps a helper to apply a move and compute delta penalty might simplify main loop.
   - No additional libraries needed beyond `math` for exp (if we use `math.exp` for the acceptance probability) and `random`.
   - Since this is design day, write a clear comment or docstring for the `improve_schedule` function stating what method it uses (so if someone else reads it, they know it’s SA/hill-climbing).
   - By the end of Day 8, you have a pseudocode or written plan for the improvement phase algorithm.

**Connection to Next Phase:** The strategy designed on Day 8 will be implemented on Day 9 (Phase 7). At that point, you will run the improvement algorithm on the initial schedule and hopefully achieve a lower penalty timetable. Day 8’s careful planning ensures that Day 9’s coding will go smoothly and the approach will be effective.

## Day 9: Implementing the Schedule Improvement Algorithm (Phase 7)

**Goals:** Phase 7 is to put the improvement strategy into practice. On Day 9, implement the simulated annealing (or chosen local search) algorithm to reduce the soft constraint penalty. Test it on the current schedule and verify that it produces a better timetable without breaking hard constraints.

1. **Coding the Improvement Function:** Implement the `improve_schedule(schedule, exam_students, student_exams)` function as planned:
   - Use the pseudocode from Day 8. For example:

     ```python
     import math, random
     def improve_schedule(schedule, exam_students, student_exams, iterations=1000, temp_start=1.0, temp_end=0.001):
         current_schedule = schedule.copy()
         current_penalty = calculate_penalty(current_schedule, student_exams)
         best_schedule = current_schedule.copy()
         best_penalty = current_penalty
         temp = temp_start
         cooling_rate = math.pow(temp_end/temp_start, 1.0/iterations)  # geometric cooling
         # Precompute slot_students from current_schedule for quick conflict checks
         slot_students = {}
         for exam, slot in current_schedule.items():
             slot_students.setdefault(slot, set()).update(exam_students[exam])
         for it in range(iterations):
             # pick a random exam and a random slot
             exam = random.choice(list(current_schedule.keys()))
             old_slot = current_schedule[exam]
             # choose a random target slot (could be existing or new)
             if random.random() < 0.5:
                 # 50% chance to pick an existing slot
                 target_slot = random.choice(list(slot_students.keys()))
             else:
                 # 50% chance to consider a new slot (to allow expansion)
                 target_slot = max(slot_students.keys()) + 1
             if target_slot == old_slot:
                 continue  # no change effectively
             # Hard constraint check: ensure no conflict in target slot
             conflict = False
             if target_slot in slot_students:
                 # check if any student of 'exam' in slot_students[target_slot]
                 if not exam_students[exam].isdisjoint(slot_students[target_slot]):
                     conflict = True
             if conflict:
                 continue  # skip this move
             # Apply the move
             # Remove exam from old slot set, add to new slot set
             slot_students[old_slot] -= exam_students[exam]
             if len(slot_students[old_slot]) == 0:
                 slot_students.pop(old_slot)  # remove empty slot to keep things tidy
                 # (optional: we might not remove it to preserve slot count, but removing prevents gaps)
             slot_students.setdefault(target_slot, set()).update(exam_students[exam])
             current_schedule[exam] = target_slot
             # Calculate new penalty
             new_penalty = calculate_penalty(current_schedule, student_exams)
             delta = new_penalty - current_penalty
             # Decide acceptance
             if delta <= 0 or random.random() < math.exp(-delta / temp):
                 # Accept move
                 current_penalty = new_penalty
                 if new_penalty < best_penalty:
                     best_penalty = new_penalty
                     best_schedule = current_schedule.copy()
             else:
                 # Reject move, rollback
                 # Remove exam from target_slot and add back to old_slot in slot_students
                 slot_students[target_slot] -= exam_students[exam]
                 if len(slot_students[target_slot]) == 0:
                     slot_students.pop(target_slot)
                 slot_students.setdefault(old_slot, set()).update(exam_students[exam])
                 current_schedule[exam] = old_slot
             # Cool down
             temp *= cooling_rate
         return best_schedule, best_penalty
     ```

     This code is a direct reflection of the design. (Note: This pseudocode is quite detailed; actual implementation may refine some details like how a new slot is handled.)
   - **Considerations in Code:**
     - We remove an exam from a slot and if that slot becomes empty, we removed it. This might reduce the total number of slot keys, which effectively can shrink the timetable if some slots were freed up. That’s fine but we should be careful: if we remove slot id 5 and later add a new slot, we might reuse id 5 or get id 6, etc. It's not a big issue, but just ensure uniqueness.
     - We allow moves to new_slot = max_slot+1, which means schedule can extend by one slot at most per move. This allows the possibility of spreading out if beneficial.
     - The acceptance criterion uses `math.exp(-delta/temp)` which requires `math` import. If `delta` is negative, we accept immediately (improvement).
     - We update `best_schedule` whenever a new best is found. We keep track of `best_penalty`.
     - Cooling is done geometrically here. We computed a cooling_rate to reduce temp from start to end over the given iterations. This is one strategy; alternatively, linear cooling can be used (temp -= (temp_start-temp_end)/iterations).
     - Randomness: We used `random.choice` and `random.random`. It’s okay for now, but for reproducibility, we might set a seed at the function start (e.g., `random.seed(42)` for testing).
   - **Swaps:** The above pseudocode only implements moving a single exam. If time permits and needed, we could also add a branch to occasionally do a swap:
     - For example, instead of picking a target slot that is empty, pick another exam Y in a random slot and attempt to swap X and Y's slots (ensuring neither conflicts after swap). This adds complexity, so we might skip it if single moves suffice to improve.
   - **Edge Cases:** If the exam is moved to a new slot beyond any existing, we should check that adding a new slot is always allowed. (If the exam period is fixed length, we wouldn’t allow beyond max slot, but we assume flexibility or that improvement won’t exceed some reasonable bound).
   - **Efficiency:** Each iteration calculates a full penalty. This might be the slowest part, but 1000 iterations times a penalty calc (which is maybe O(E * avg_exams_per_student) = O(total student-exam enrollments)) could be okay for moderate sizes (tens of thousands of checks). If not, we will optimize in Day 11 by calculating delta penalty instead.
   - Write the code carefully and comment it for clarity.

2. **Test the Improvement Algorithm:** Run the `improve_schedule` on the schedule from Day 6 and observe results:
   - Start with a small number of iterations (like 200) for a quick test, to ensure it’s making valid moves and not violating hard constraints.
   - Verify that the output schedule still passes `check_hard_constraints`. It absolutely should, because we explicitly avoid conflicts. Still, run the checker on the best_schedule returned to be safe.
   - Check that `best_penalty` is indeed <= initial penalty. If the algorithm is working, it should find some improvement, unless the initial was already optimal (unlikely in a complex case).
   - Print the initial penalty and final penalty:

     ```python
     initial_pen = calculate_penalty(initial_schedule, student_exams)
     best_schedule, best_pen = improve_schedule(initial_schedule, exam_students, student_exams)
     print("Penalty: initial =", initial_pen, " improved =", best_pen)
     ```

     See if `best_pen` is lower.
   - If `best_penalty` stays the same as initial, it might mean our algorithm didn’t find a better solution (maybe the schedule was already spread out or the move selection didn’t explore enough). Potential fixes:
     - Increase iterations or temperature to allow more exploration.
     - Check if our moves are too restricted. Perhaps allow moves to not just one new slot but consider more new slots (though we allow adding a new slot each time, which is flexible).
     - Ensure we didn’t accidentally bias towards always picking moves that do nothing (e.g., if random often picks the exam’s same slot or conflicts and continues).
     - Possibly implement a swap move to diversify moves.
   - If the penalty goes down, inspect a bit what changed:
     - You can compare some sample student’s schedule before and after to see if, for example, a student who had consecutive exams now has them separated by an extra slot (which would reduce penalty).
     - This helps verify qualitatively that the algorithm is making the kind of improvements we expect.

3. **Tune Parameters:** Based on test outcomes, adjust the SA parameters:
   - If the improvement is very slow or minimal, try more iterations. Since each iteration is not extremely heavy, you might try a few thousand iterations if needed (keeping an eye on runtime).
   - If runtime is a concern, you could slow the cooling (so it explores more at higher temp) or implement a quick break if we haven’t improved in a long time (though SA doesn’t usually break early).
   - If wanting to ensure thorough search, you could run multiple trials of SA and take the best (this might be beyond our 4-hour chunk, but for a better final result, sometimes you run the metaheuristic several times).
   - For example, run `improve_schedule` 5 times (with different random seeds) and pick the best schedule among them.
   - Document any changes: e.g., “Increased iterations to 2000 as 1000 wasn’t sufficient to significantly reduce penalty. Also adjusted initial temperature to 5.0 because initial moves needed more freedom.”

4. **Ensure Code Stability:** The improvement loop is somewhat complex; ensure it doesn’t crash or behave unexpectedly:
   - Check for any potential issues like division by zero in exp (our temp_end avoids hitting exactly 0).
   - If a slot gets emptied and removed, ensure no code later tries to iterate over a range of slots by number that now is out-of-sync. We avoided using numeric ranges for slots by using keys of `slot_students`, which is fine even if some numbers are missing.
   - Confirm that after improvement, the schedule structure is still consistent (each exam one slot, etc.). If we removed a slot and didn’t reassign its number, that’s fine (gaps in slot numbering don’t affect validity).
   - Possibly sort the final schedule by slot to see how exams are distributed after improvement, as a sanity check.

**Connection to Next Phase:** By the end of Day 9, you should have a working improvement algorithm and an improved schedule. This completes Phase 7. Now you have a full solution pipeline: input data -> initial schedule (Phase 4) -> improved schedule (Phase 7). Day 10 (Phase 8) will involve integrating and running everything end-to-end, analyzing the results, and making sure the solution meets expectations. The heavy coding work is mostly done; next comes evaluation and refinement.

## Day 10: Integration and Full Pipeline Testing (Phase 8)

**Goals:** Phase 8 is about testing the entire scheduling pipeline as a whole and evaluating results on more realistic scenarios. On Day 10, you will integrate all components (data loading, initial scheduling, improvement, output) and perform a thorough test run. The aim is to verify that the system works end-to-end and to gather preliminary performance and quality metrics.

1. **Integrate Phases into a Main Script:** Create or refine a main function or script that ties everything together:
   - Steps in the pipeline:
     1. **Load Data:** (From Phase 2) – parse input or generate test data. Ensure that `exam_students` and `student_exams` structures are available.
     2. **Initial Schedule:** Use `assign_timeslots_greedy` (Phase 4) to get a conflict-free schedule.
     3. **Initial Evaluation:** Compute initial penalty via `calculate_penalty` (Phase 5) and maybe print it.
     4. **Improvement:** Call `improve_schedule` (Phase 7) to get an improved schedule and its penalty.
     5. **Output Result:** Present the final schedule in a readable format or write to a file.
   - If this is in a Jupyter notebook or script, run these steps sequentially.
   - For clarity, you might structure it as:

     ```python
     def main():
         exam_students, student_exams = load_data(input_file)
         initial_schedule = assign_timeslots_greedy(list(exam_students.keys()), exam_students)
         initial_pen = calculate_penalty(initial_schedule, student_exams)
         print(f"Initial penalty = {initial_pen}")
         best_schedule, best_pen = improve_schedule(initial_schedule, exam_students, student_exams, iterations=2000)
         print(f"Improved penalty = {best_pen}")
         save_schedule(best_schedule, output_file)
     ```

     In this pseudo-code, `load_data` and `save_schedule` would be small helpers to handle I/O.
   - Ensure each function works with the same data structures (for instance, `assign_timeslots_greedy` expects `exam_students`, etc., which we have).
   - If using external libraries (like `pandas` for data or `networkx` for verification), make sure to import and use consistently.

2. **Run on a Realistic Dataset:** If available, test on a larger or realistic dataset:
   - If you have access to a standard dataset (like a small instance of Toronto or ITC2007), attempt to load it. If the format is complex, you might write a quick converter or use a simpler representation (for example, some datasets come with a list of students per exam or a matrix).
   - If no actual dataset, simulate one:
     - For example, generate 50 exams, 200 students, and randomly assign students to exams (with some probability such that each exam has maybe 20 students and each student has ~5 exams). Ensure some realistic overlap.
     - This random generation can help stress test the algorithm. Use `random` or numpy for generation, making sure to avoid trivial or extreme cases (like all students in all exams).
   - Running on a larger case will test performance:
     - Check how long the greedy scheduling takes (should be quick, likely O(E * slots) which is fine).
     - Check how long the improvement takes. If 2000 iterations on 50 exams is fine (should be seconds perhaps), try scaling up a bit (maybe 100 exams, 500 students) to see if it still finishes reasonably (within a minute or so).
     - This helps identify if any part is too slow and needs optimization (Phase 9 will handle if so).
   - After running, verify:
     - Hard constraints: use `check_hard_constraints` again on the final schedule for peace of mind.
     - Improvement: confirm the final penalty is indeed lower than initial.
     - If possible, manually inspect a portion of output. For instance, pick a student and see their exam slots to ensure they seem more spread out after improvement.
   - **Record Results:** Note down the initial vs improved penalty and perhaps how many timeslots used initially vs finally. For example, initial might use 10 slots, final used 12 slots (meaning it allowed two extra slots to spread out, which reduced penalty).
   - If the improvement algorithm uses more slots than originally, that’s fine if schedule length wasn’t fixed. If the exam period length was supposed to be fixed (say 10 slots max), we should constrain the algorithm not to create slot beyond 9. We didn’t enforce that, but if needed, one could modify `target_slot = random.choice(existing_slots)` more often and not allow new slot moves. For now, our flexible approach is acceptable since no fixed limit was specified in our assumptions.

3. **Evaluate Solution Quality and Efficiency:** Assess if the solution is satisfactory:
   - Quality: Is the final penalty reasonably low? If a student had, say, 5 exams, are those fairly spread out? We can derive metrics like average penalty per student or maximum penalty any single student has (which corresponds to worst-case student schedule).
   - Check if any soft constraints remain severely violated (e.g., do any students still have back-to-back exams? If yes, maybe they were inevitable due to conflict density or time slots count).
   - Efficiency: Check the runtime roughly. Our improvement might be the slowest part. If it took too long for a moderate test, we may need to optimize or reduce iterations. If it’s fast, maybe we can even increase iterations for better quality.
   - If using a small dataset for tests, consider the scale you ultimately need to handle. If the final target is, say, 200 exams and 1000 students, will our approach scale? Possibly not linearly – penalty calc is quadratic in worst case. But for the purpose of this project, we may not need to handle extremely large instances, just demonstrate the method.
   - **Memory**: Ensure no memory issues. Our structures are mostly dictionaries and sets – which should be fine. The conflict matrix (if created for large N) could be memory heavy, but we actually used conflict_list and slot_students which is more efficient for sparse conflicts.

4. **Document Findings:** Summarize what this test run shows:
   - “The integrated system successfully produced a conflict-free timetable and then improved it to reduce student conflict proximity. For example, initial total penalty was 250, which dropped to 90 after improvement. The algorithm used 12 timeslots out of an available 20, and no student has back-to-back exams in the final schedule. The runtime for scheduling was about X seconds and improvement Y seconds for Z exams and W students, which is reasonable.”
   - Note any anomalies: e.g., if the improvement got stuck or if random nature means results vary, mention that repeated runs can yield slightly different outcomes due to the metaheuristic.
   - If the final schedule still isn’t perfect, acknowledge the possibility of further improvement with more iterations or advanced methods (to be handled in Phase 9 if possible).
   - This completes Phase 8: demonstrating the working solution on test data.

**Connection to Next Phase:** With a full pipeline tested on Day 10, you’re ready to refine and optimize in Phase 9. Day 11 will focus on any performance improvements or addressing any shortcomings discovered (like speed issues or the need for alternative approaches). The project is functional now; the remaining days aim to polish and ensure it’s robust and efficient.

## Day 11: Performance Profiling and Optimization (Phase 9, Part 1)

**Goals:** Phase 9 is about refining the solution for efficiency, scalability, and possibly exploring alternative methods if needed. On Day 11, profile the code to find bottlenecks and optimize critical sections. Also, consider if any part of the approach should be adjusted (e.g., more efficient penalty calculation or leveraging libraries for speed).

1. **Profile the Code:** Use Python profiling tools or manual timing to identify slow spots:
   - The likely suspects for heavy computation are:
     - The penalty calculation in each iteration of improvement (since we recalc penalty frequently).
     - The improvement loop itself if iterations are high.
     - Data loading and initial scheduling are typically much faster in comparison.
   - You can use Python’s `cProfile` or simple timestamps. For example, time how long `calculate_penalty` takes for a typical schedule and how many times it’s called in `improve_schedule`.
   - If `calculate_penalty` is indeed a bottleneck, consider optimizing it:
     - **Delta Penalty Calculation:** Instead of full recompute on each move, compute how the penalty changes when an exam moves.
       - For a move of exam X from slot A to slot B, only students of X (and any students in exams that were in B or X’s exams in A) are affected. We can calculate before/after for each such student.
       - For each student in `exam_students[X]`: calculate their penalty contribution before move and after move. Only X’s slot changed for them.
       - For each student in `slot_students[B]` (because exams in B now have X added to their slot which might affect their penalty if they also share X? Actually, if a student is in X and others in B, we handled by first group. If some student is not in X, X’s move doesn’t affect them directly except if slot B was empty, now that student sees an extra exam in same slot? Actually, a student not in X isn’t directly affected by X moving, unless they had multiple exams and slot B’s occupancy changed relative to them? That gets complicated beyond direct share, likely only those who have X or another exam in X’s old or new slot matter.)
       - This is doable but complex to implement correctly. Given moderate size, a full penalty recompute might be fine, especially if we lowered iterations or optimized other ways.
     - **Vectorization:** If using numpy and a conflict matrix, we could vectorize penalty calculation, but the iterative approach per move still calls it many times.
     - Considering project scope, a simpler step: try to reduce number of penalty computations by not evaluating too many bad moves. Our SA already does that to some extent (skips conflicts and likely has modest acceptance of worse moves).
   - Check if the improvement loop had any redundant work. Perhaps generating a move sometimes does nothing (we skip if conflict or same slot). If a lot of iterations are wasted on invalid moves, we could improve move selection:
     - For example, pick an exam and directly find a non-conflicting slot for it randomly, rather than random picking possibly the same slot or a conflicting one. We can do this by:

       ```python
       possible_slots = [s for s in slot_students if exam_students[exam].isdisjoint(slot_students[s])]
       possible_slots.append(max(slot_students)+1)  # consider new slot
       pick one from possible_slots
       ```

       If `possible_slots` only contains the old slot, then no move possible for that exam (means exam conflicts with exams in all other slots). Then skip this exam.
       - This way, we avoid checking conflict after picking a bad slot; we choose from valid ones directly.
     - This enhancement could drastically reduce wasted iterations and slightly speed up convergence.
   - If the profile shows the improvement step is fine but initial scheduling was heavy (which is unlikely unless extremely large input), one could optimize that by using a more efficient data structure (but our approach was already quite efficient using sets).
   - Memory usage: If using large sets/dicts, memory might be okay. If conflict matrix was built, it might be memory heavy; if not needed beyond penalty, you could drop it from memory to save space. Not usually an issue in a 4-hour-a-day project but mention if relevant.

2. **Optimize Critical Code Sections:** Apply optimizations based on profiling:
   - Implement the smarter move selection described above to reduce wasted checks in SA.
   - Possibly switch some Python loops to numpy operations:
     - For example, computing the penalty: we could derive a vector of gaps for each student’s sorted slots and use numpy to apply the penalty formula. However, given penalty formula is piecewise, loops are fine and likely not the dominating factor compared to doing it thousands of times.
   - Another angle: multithreading or multiprocessing – probably not needed. But if one wanted to parallelize, one could run multiple improvement trials in parallel and take best, but that’s advanced and likely unnecessary for our scale.
   - **Test after optimizations:** Ensure the algorithm still yields the same or better results. Check that no bug introduced by optimizing. For instance, if we add the new move selection logic, test that it indeed finds moves and improves penalty.
   - If moving an exam that conflicts in all other existing slots (a highly constrained exam), the only possible move is to a new slot or not at all. Our logic accounts for adding a new slot as a possibility. If even a new slot doesn’t help because that exam has conflicts? Actually, new slot always avoids conflicts because it’s empty. So exam can always move to a new slot if allowed, which will never violate hard constraints (just extends schedule). But maybe that increases penalty for that exam’s students if they had others? Actually it can only reduce or keep same because moving to an empty slot gives them more gap likely.
   - Thus the algorithm might always have at least one possible move for any exam (worst case, new slot), giving a wide search space.
   - If running time is still high but improvement saturates early, consider terminating SA early. For instance, if no improvement found in last X iterations, break out. This can cut time if stuck.
   - Document any changes in the code or parameters.

3. **Optional: Explore Alternative Approaches** (if improvement approach is unsatisfactory or time remains):
   - If our heuristic solution is not reaching a good quality, consider formulating a small instance for an ILP solver to see optimal results:
     - **ILP with PuLP/OR-Tools:** Formulate binary variable x_{e,s} = 1 if exam e in slot s. Hard constraints: for each student and each pair of distinct exams (i,j) they take, x_{i,s} + x_{j,s} ≤ 1 for each slot s (ensures they’re not in same slot). Also each exam must be in exactly one slot: sum_s x_{e,s} = 1 for each exam. To limit slots, set s range or add constraint if needed.
     - Objective: minimize $\sum_{i<j} \text{conflict}[i][j] * \text{penalty}(|s_i - s_j|)$. But the penalty with $|s_i - s_j|$ in objective makes it tricky for ILP because of absolute difference. You can linearize by introducing variables for distances or only consider penalty for known slot gaps (like have to multiply by those differences).
     - This gets complicated to model exactly due to piecewise penalty. Alternatively, fix maximum slots and define for each pair of slots whether they count as 1-gap, 2-gap etc. Given the limited time, implementing ILP fully may not be feasible. But mentioning that one could use OR-Tools CP-SAT which can directly handle such scheduling with constraints (they have some scheduling API too).
     - For educational purposes, maybe implement a very small ILP (like treat penalty simpler or limit exam count) just to verify on a tiny dataset if we find a better solution than our heuristic. This can validate our approach’s effectiveness.
   - **Conclusion on alternatives:** Acknowledge that while exact methods exist, they can be slow for larger problems ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Examination%20timetabling%20is%20a%20type,have%20been%20proposed%20in%20scientific)), which is why we stick to heuristics. But exploring them on small cases can provide insights.
   - If time doesn’t allow implementation, simply ensure to mention these possibilities in the report as future work or alternatives.

4. **Re-run with Optimizations:** Use the improved code to run some tests again:
   - Check if runtime improved for the same test case used on Day 10. Note any difference (e.g., “improvement algorithm runtime reduced from 30s to 20s after optimizing move selection”).
   - Confirm final results (penalty, slots) remain as good or better.
   - If results improved (maybe a lower penalty due to more iterations or better exploration), note that.
   - If you introduced any changes like early termination, ensure it didn’t cut off too early (i.e., still got to a good solution).

**Connection to Next Phase:** After optimizing on Day 11, Phase 9 continues to Day 12 where you’ll finalize any remaining improvements or additional features. The project by now should be efficient and robust. Day 12 can be used to wrap up Phase 9 and start final documentation (Phase 10 prep).

## Day 12: Final Refinements and Additional Features (Phase 9, Part 2)

**Goals:** Use Day 12 to address any remaining improvements, possibly add minor features, and ensure the solution is polished. This wraps up Phase 9 and transitions to final Phase 10 (documentation and wrap-up).

1. **Final Algorithmic Tweaks:** If any aspect of the algorithm could be improved or has unresolved issues, address them now:
   - Ensure that the improvement algorithm’s parameters (iterations, cooling schedule) are tuned for a good balance of performance and quality. Perhaps do one more test with a different random seed to ensure consistency (the heuristic may give slightly different results each run; if so, maybe decide to take the best of a few runs or set a fixed seed for predictability).
   - Check if the solution could be improved by slight changes:
     - For example, if after improvement some students still have back-to-back exams, maybe run a targeted post-processing: go through students who have a consecutive exam and see if you can swap one of those exams with another one in a different slot without conflict to fix it.
     - This is like a final greedy tweak that can be done deterministically: e.g., for each student with consecutive exams A and B, try to move B to an available slot later if possible. This is a heuristic layer that might catch any low-hanging fruit that SA missed. Implement if quick.
   - If not needed or beneficial, skip, as the schedule might already be good.

2. **Implement Additional Features (if any):** Think of any small enhancements that would make the project output more useful:
   - **Output Formatting:** Create a neat output of the final timetable. For instance, output a CSV or text like:

     ```text
     Timeslot 0: Exams [1, 5, 7]
     Timeslot 1: Exams [0, 2]
     ...
     ```

     Or produce an Excel/CSV where each exam with its slot is listed, which could be given to another system or easily read by a person.
   - **Visualization:** (Optional) Use `matplotlib` to draw a simple chart: e.g., bar chart of how many exams in each slot, or a heatmap matrix of students vs timeslots (sparse).
   - **Room Assignment (if needed):** If earlier we ignored room capacity but have data for rooms, consider a simple assignment: for each slot, if multiple rooms are available, assign exams to rooms greedily. This would be another layer (kind of a separate scheduling problem but simpler since times are fixed now). Given limited time, likely skip unless trivial.
   - **User Interface:** If time, one could add a command-line interface to pass input/output file names or parameters for iterations etc., making the tool more user-friendly. Or wrap it in a Jupyter notebook with clear instructions so someone can reuse it easily.
   - Ensure any such additions do not break core functionality and are documented.

3. **Final Verification:** Do one more end-to-end run with everything in final form:
   - Use a test input and generate the final output. Check that the output is correct and nicely formatted.
   - Double-check all constraints one last time on the final output (no conflicts, etc.).
   - If possible, get a peer or someone to review the output for sense (if this were a real scenario, maybe an example where one can manually verify small schedule).
   - Confirm that the code is robust against edge cases: e.g., what if there’s a student with only one exam (trivial spacing), or an exam with no conflicts (should just be placed in slot 0 by initial algorithm – which is fine).
   - Now the algorithm and features are finalized.

4. **Prepare for Documentation:** Gather all the information that will go into the documentation and final report:
   - Summarize the final configuration (which algorithm was used, key parameters, what data structures, etc.) as you will need to write this down in Phase 10.
   - Ensure any references to academic concepts (like graph coloring, simulated annealing) are clear so you can explain them in documentation.
   - It's often useful to outline the structure of the final report or README today, so writing it on Day 13–14 is smoother.
   - Check that code is well-commented so that if included in an appendix or delivered, it’s understandable.

**Connection to Next Phase:** With all development and refinement done by Day 12, the project is technically complete. Phase 10 is up next, which involves creating the final documentation, report, and packaging the project. Day 13 and Day 14 will focus on writing a thorough report and cleaning up, and Day 15 will be a final review.

## Day 13: Documentation and Project Report (Phase 10, Part 1)

**Goals:** Start Phase 10 by creating comprehensive documentation for the project. On Day 13, write the bulk of the project report or README, describing the problem, approach, implementation, and usage. Also, ensure in-code documentation (docstrings, comments) is up-to-date.

1. **Draft the Project Report/README:** Outline and write sections covering all important aspects of the project:
   - **Introduction:** State the problem (Examination Timetabling) and its significance. Mention constraints (hard/soft) and the general goal (feasible and optimized exam schedule). You can reuse some content from Day 1–2 findings, e.g., “In this project we tackle the NP-hard Examination Timetabling Problem ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Examination%20timetabling%20is%20a%20type,have%20been%20proposed%20in%20scientific)), where exams must be assigned to timeslots without student conflicts ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=,known%20as%20a%20clashing%20constraint)) and with minimal hardship (exams spread out) ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=as%20a%20clashing%20constraint%29)).”
   - **Methodology:** Describe the approach taken, phase by phase:
     - Data modeling: how exams/students are represented.
     - Initial scheduling using a graph coloring heuristic (mention greedy largest-degree-first and cite Carter’s approach as inspiration ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=timetabling%20problems%20,the%20University%20Malaysia%20Pahang%20examination))).
     - Improvement via simulated annealing local search to reduce soft constraint penalties.
     - Emphasize how hard constraints are always enforced (via conflict checks) and how the penalty function drives the optimization (maybe even include the penalty formula or values used ([Addressing Examination Timetabling Problem Using a Partial Exams Approach in Constructive and Improvement](https://www.mdpi.com/2079-3197/8/2/46#:~:text=Equation%20,hard%20constraint%20of%20the%20problem))).
   - **Implementation Details:** Dive into how each part is implemented:
     - Data structures (mention using Python sets, dicts, etc., and why they were chosen for efficiency).
     - Functions created: list key functions (load_data, assign_timeslots_greedy, calculate_penalty, improve_schedule) and briefly what each does.
     - Any important modules: e.g., “Uses `math` for exponential in SA, `random` for random moves, and `pandas` for input parsing” (if pandas was used).
     - You might include snippets of pseudocode or actual code for illustration, e.g., the greedy algorithm snippet or SA snippet, to show clarity.
   - **Results:** Summarize the results observed:
     - Provide some metrics from Day 10 testing: e.g., “On a test dataset of X exams and Y students, the initial greedy schedule had a penalty of P, and after improvement the penalty was reduced to Q, eliminating all cases of back-to-back exams for students.”
     - If known, mention how many timeslots were used and if that is reasonable (like maybe the exam period length).
     - Possibly mention performance: “The algorithm generates a schedule in Z seconds and optimizes it in W seconds for the given data size, which is efficient for practical use.”
   - **Usage Instructions:** If someone were to use your code:
     - Explain how to run it, how to provide input (format), and how the output is presented.
     - Mention any configurable parameters (like you can change number of iterations or random seed inside improve_schedule).
     - If you created a CLI or notebook, mention that.
   - **Conclusion:** Conclude with what was achieved and any potential future enhancements:
     - E.g., “The project successfully implemented a complete exam timetabling system that respects all hard constraints and significantly improves soft constraints. Future improvements could explore more advanced metaheuristics or incorporate additional real-world constraints such as room capacities or varying exam durations.”
   - **References:** List any literature or sources referenced. Since we cited sources in our plan (Carter et al., etc.), ensure they are appropriately credited. In a report, you might formally cite those in a bibliography section. (For the answer’s context, our in-line citations serve that purpose).
   - Keep the writing clear, concise, and structured with subheadings if needed. Possibly use bullet points for lists of features or steps.

2. **Update Code Comments and Docstrings:** Go through the code and ensure every function has a docstring explaining its purpose, parameters, and return values:
   - For example, `"""Assign timeslots to exams greedily ensuring no conflicts. Returns a dict of exam->slot."""` for the greedy function.
   - In the improvement function, document what algorithm is used: “Uses simulated annealing to relocate exams and reduce penalty. Always maintains a conflict-free schedule.”
   - Comment tricky parts of code (like the move acceptance criteria or any hacky optimization).
   - This internal documentation is important if the project is shared or revisited later.

3. **Visual Aids for Documentation (optional):** If useful, include any charts or diagrams in the documentation:
   - For instance, a flowchart of the algorithm pipeline (Phase 4 -> Phase 7) could be drawn to illustrate how initial schedule feeds into improvement. This could be done in text or using a simple tool, but given time, it might not be necessary.
   - If you created a visual output (like a timetable chart), you could include that as an example in the report.
   - However, ensure any images or charts serve a purpose (like demonstrating final output format or improvement effect).

4. **Review for Completeness:** Cross-check that every phase of the roadmap is addressed in the documentation:
   - Phase 0/1: Did we explain the initial planning and requirement analysis? Possibly not in the final report introduction explicitly, but implicitly yes. We can add a short section “Problem Requirements” where we list the constraints identified, which covers that.
   - Phase 2: Data modeling is covered under implementation details.
   - Phase 3/4: The scheduling algorithm is covered under methodology.
   - Phase 5/6/7: The improvement and soft constraints are covered.
   - Phase 8: We described results/testing.
   - Phase 9: Mention optimizations done (we can have a section “Performance considerations” where we talk about how we optimized and the complexity).
   - Phase 10: The documentation itself is the deliverable.
   - Ensuring no phase is skipped in the narrative will fulfill the requirement of covering Phase 0–10 tasks.

5. **Proofreading:** Although final proofreading will be on Day 15, start checking the written content for clarity, grammar, and coherence:
   - Make sure explanations are not too technical for the intended audience (if it’s for a class, some detail is fine).
   - Check that all citations in the documentation correspond to references.
   - If using this plan as a basis for the actual report, ensure to remove any conversational instructions; it should read as a formal report.

**Connection to Next Phase:** By the end of Day 13, most of the documentation should be drafted. Day 14 will involve finalizing this documentation (Phase 10 continued) and packaging the project (cleaning up repository, ensuring everything needed is included). The project is essentially done; now it’s about presenting it professionally.

## Day 14: Final Documentation Review and Project Packaging (Phase 10, Part 2)

**Goals:** Complete Phase 10 by finalizing the documentation and packaging the project deliverables. On Day 14, polish the report/README, create any necessary additional documents, and organize the project files for submission or presentation.

1. **Finalize the Written Documentation:** Take the draft from Day 13 and refine it:
   - Correct any typos, unclear sentences, or overly verbose parts. Ensure the report is concise yet comprehensive.
   - Verify that all figures/tables (if any) are properly labeled and referenced.
   - Make sure the report structure flows logically: introduction -> methods -> results -> conclusion.
   - Check that the tone is consistent (likely formal and technical, using present tense for describing the system).
   - If required, format the document according to any guidelines (font, spacing, etc.) or convert to PDF if needed for submission.
   - Re-check that all key points from each phase are mentioned. For example, if Phase 9 involved optimization, mention in methods or a separate section what was optimized.
   - Add a title page or header to the document if appropriate, and your name/affiliation if this is a course project.
   - Ensure citations are properly formatted in the final document. The in-text citations we used would be converted to proper references if needed (since this is an internal plan we wrote, in actual report you might have [1], [2] referencing a bibliography).

2. **Code Packaging:** Organize the code and any scripts:
   - Make sure file names are clear (e.g., `timetable.py` for main code, `README.md` for instructions).
   - If using Jupyter notebooks, ensure they are clean (remove extraneous prints or debug cells, maybe include some results but not too many).
   - If required, prepare a `.zip` or repository link containing all source code, data files (if any), and the documentation.
   - Check that the code runs from start to finish by doing a fresh run (maybe in a new environment or resetting kernel if using notebook).
   - If there are any dependencies, list them in a `requirements.txt` file.
   - If a specific Python version or environment is needed, mention that in README.
   - Include sample input and output (if possible) so the evaluator can quickly test the program. For example, include the small example we used in documentation.

3. **User Guide (if needed):** If the project is meant for someone else to run:
   - Provide step-by-step instructions in the README: “To run the scheduler, do X. To run the improvement, do Y. The output will be in file Z.”
   - If there’s an interactive component or user choices, document how to use them.
   - Possibly include an example command and expected output snippet.
   - Ensure it’s idiot-proof: assume the user knows nothing about the code internals.

4. **Presentation Preparation (if applicable):** If you need to present the project or create slides:
   - Start outlining slides focusing on the problem, approach, and results. (This might be beyond the scope of what's needed, but if so, one could allocate time here for it).
   - Use visuals like charts or bullet points for clarity.
   - Not a main task unless explicitly required, so only do this if needed and time permits.

5. **Backup and Version Control:** Make sure the final version of everything is saved and version-controlled:
   - Commit the final changes to Git if using it. Tag a release if that’s relevant.
   - Keep a backup copy of important files (report and code) on a separate drive or cloud, just as a safety measure.

**Connection to Next Phase:** At this point, by end of Day 14, the project is essentially complete and documented. Day 15 will be a buffer to double-check everything and make any last-minute improvements or corrections. It’s the final quality assurance before delivering the project.

## Day 15: Final Review and Buffer Day

**Goals:** Use Day 15 as a buffer for any remaining tasks, final review, and ensuring all project components are ready for submission. This day is about quality assurance and addressing any unexpected last-minute issues.

1. **Full Project Review:** Re-read the entire documentation and perhaps skim through the code one last time:
   - Check coherence between code and documentation (do they describe the same approach? Did you change something in code that wasn’t updated in the report?).
   - Validate that all references to figures or code in the text are accurate after any last edits.
   - Ensure the language is polished. This is the time for a final proofreading, maybe reading the report aloud or using a spell checker.
   - If possible, have someone else review the report or even test the code with the README instructions to see if anything is confusing.

2. **Double-Check Requirements:** Cross-verify the initial requirements (from Phase 1) against the final solution:
   - Hard constraints: We must be absolutely sure no hard constraints are violated. Perhaps run one more random test with the final code to be safe.
   - Soft constraints: Are we addressing them as intended (yes, via penalty minimization).
   - If any secondary requirements (like output format or specific data handling) were given at the start (in the roadmap or project description), ensure those are fulfilled (for example, if it was expected to output a certain format or handle a certain input size, ensure you demonstrated that).
   - Confirm that all roadmap phases got attention. Perhaps in the documentation’s introduction or methodology, explicitly mention the phased development approach followed, to highlight that you planned and executed in stages (if that’s something to be reported).

3. **Performance Validation:** If there was a goal to handle a certain size or time, double-check that:
   - Maybe run one more somewhat large test to ensure no performance regression from last changes.
   - If performance isn’t as high as hoped but acceptable, be prepared to explain why (e.g., NP-hard nature) if asked.
   - Given this is the final day, avoid making any major code changes unless a severe bug is found. Minor tweaks are fine.

4. **Final Deliverables Checklist:** Ensure you have everything required for submission:
   - The project report (Phase 10 documentation) – likely a PDF or DOCX or Markdown.
   - The source code files and possibly an example input/output.
   - Any separate analysis or log of results if needed.
   - If submission portal requires certain formats, have them ready.
   - If this were a real scenario, this is where you’d upload or email the deliverables.

5. **Reflection:** Take a moment to summarize the journey (this could be just personally or in a project journal if maintained):
   - Note what was achieved in these 15 days, any lessons learned (like which approach worked well or what you’d do differently next time).
   - This is not necessarily delivered, but it’s good for personal knowledge and could be included as a short “Lessons Learned” section in the report if appropriate.
