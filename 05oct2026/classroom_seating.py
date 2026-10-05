students = 73
bench_capacity = 3

occupied_benches = students // bench_capacity
leftover_students = students % bench_capacity

print(f"occupied benches:{occupied_benches}")
print(f"students left over:{leftover_students}")