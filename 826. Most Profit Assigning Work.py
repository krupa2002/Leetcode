class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))  # Sort by difficulty
    
    # Step 2: Sort the workers by their ability
        worker.sort()
    
        max_profit = 0  # This will store the total maximum profit
        max_current_profit = 0  # This will store the maximum profit up to the current job
        job_index = 0  # Pointer for jobs array
    
    # Step 3: Iterate through each worker
        for ability in worker:
        # Move the job pointer to find the highest profit job the worker can do
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
            # Update the current maximum profit if the current job's profit is higher
                max_current_profit = max(max_current_profit, jobs[job_index][1])
                job_index += 1
        
        # Add the best possible profit for this worker to the total profit
            max_profit += max_current_profit
    
        return max_profit

        
