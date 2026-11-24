# University Scholarship Allocation System
# Format: (Name, Aggregate_Marks, Min_Subject_Mark, Attendance, Income)
applicants = [
    ("Alice", 88, 65, 82, 45000),
    ("Bob", 92, 70, 90, 48000),
    ("Charlie", 75, 55, 80, 40000),  # Fails min subject mark
    ("Diana", 88, 75, 95, 35000),
    ("Evan", 82, 60, 70, 30000),    # Fails attendance
]

eligible = []
for app in applicants:
  name, agg, min_sub, att, inc = app
  if agg >= 80 and min_sub >= 60 and att >= 75 and inc <= 50000:
    eligible.append((agg, att, name))

# Sort descending by aggregate marks, then attendance
eligible.sort(reverse=True)

print("--- Scholarship Allocation Results ---")
rank = 1
for item in eligible:
  print(
      f"Rank {rank}: {item[2]} (Marks: {item[0]}%, Attendance: {item[1]}%)"
  )
  rank += 1