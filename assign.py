from ortools.linear_solver import pywraplp


def main():
    # Data
    costs = [
        [75, 76, 80,95,100,115,120,124,190],
        [75, 76, 80,95,100,115,120,124,190],
        [75, 76, 80,95,100,115,120,124,190],  # here i am considering that there is 9 locations to visit:
                                              #0 - the distance between location is 0-10km and the level of task is easy 
      #1 - the distance between location is 0-10km and the level of task is medium 
      #2 - the distance between location is 0-10km and the level of task is hard 
      #3 - the distance between location is 10-2 0km and the level of task is easy #4 - the distance between location is 10-20km and the level of task is medium and so on... 
      #here the matrix data represents the cost of each technician to go and attend the emergency. 
      
        [75, 76, 80,95,100,115,120,124,190],
       
    ]
    num_workers = len(costs)
    num_tasks = len(costs[0])

    # Solver
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')


    # Variables
    # x[i, j] is an array of 0-1 variables, which will be 1
    # if worker i is assigned to task j.
    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = solver.IntVar(0, 1, '')

    # Constraints
    # Each worker is assigned to at most 4 locations to visit task.
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 4)

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i, j])
    solver.Minimize(solver.Sum(objective_terms))

    # Solve
    status = solver.Solve()

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print('Total cost = ', solver.Objective().Value(), '\n')
        for i in range(num_workers):
            for j in range(num_tasks):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if x[i, j].solution_value() > 0.5:
                    print('Worker %d assigned to task %d.  Cost = %d' %
                          (i, j, costs[i][j]))


if __name__ == '__main__':
    main()
    
    
    #On performing the above operation, we get the locations each should visit to reduce the cost
