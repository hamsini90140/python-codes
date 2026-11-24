# python-activity-based-learning.py
CASE STUDY 1: University Scholarship Allocation

1. Problem Statement:
Design a system that evaluates applicants using aggregate marks, subject-wise minimum scores, attendance, and income criteria, ranks eligible students, and resolves ties using predefined rules[cite: 1].

2. Objectives:
Automate applicant screening and academic ranking using multi-criteria conditional logic and list sorting[cite: 1].

3. Assumptions:
Minimum attendance is 75%, aggregate marks >= 80%, subject minimum >= 60%, and annual income <= $50,000[cite: 1].

4. Algorithm:
Step 1: Input applicant records containing name, aggregate marks, subject minimum, attendance, and income[cite: 1].
Step 2: Iterate through records and validate against eligibility thresholds[cite: 1].
Step 3: Store eligible candidates in a list using tuples[cite: 1].
Step 4: Sort the list descending by aggregate marks and attendance[cite: 1].
Step 5: Display the final ranked list[cite: 1].

5. Flowchart (Textual):
Start -> Input Data -> Validate Criteria -> Is Eligible? -> [Yes: Add to List / No: Reject] -> Sort & Display -> End.

6. Pseudocode:
FOR each applicant in applicants:
    IF aggregate >= 80 AND subject >= 60 AND attendance >= 75 AND income <= 50000:
        add to eligible_list
ENDFOR
Sort eligible_list by marks DESC, attendance DESC
PRINT eligible_list

7. Python Source Code:

applicants = [
    ("Alice", 88, 65, 82, 45000),
    ("Bob", 92, 70, 90, 48000),
    ("Charlie", 75, 55, 80, 40000),
    ("Diana", 88, 75, 95, 35000)
]

eligible = []
for app in applicants:
    name, agg, min_sub, att, inc = app
    if agg >= 80 and min_sub >= 60 and att >= 75 and inc <= 50000:
        eligible.append((agg, att, name))

eligible.sort(reverse=True)
print("--- Scholarship Results ---")
for rank, item in enumerate(eligible, start=1):
    print(f"Rank {rank}: {item[2]} (Marks: {item[0]}%, Attendance: {item[1]}%)")
--------------------------------------------------

8. Test Cases:
- Test 1: Alice (88, 65, 82, 45000) -> Eligible (Rank 2)[cite: 1]
- Test 2: Charlie (75, 55, 80, 40000) -> Rejected due to subject mark < 60[cite: 1]

9. Output Screenshots (Simulated):
--- Scholarship Results ---
Rank 1: Bob (Marks: 92%, Attendance: 90%)
Rank 2: Diana (Marks: 88%, Attendance: 95%)
Rank 3: Alice (Marks: 88%, Attendance: 82%)

10. Conclusion:
Successfully implemented multi-criteria selection rules and tuple-based ranking[cite: 1].
