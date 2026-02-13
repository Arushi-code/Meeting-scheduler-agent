"""
AI Meeting Scheduler Agent
Author: Arushi
"""

def find_common_slot(schedules):
    common = set(schedules[0])
    for schedule in schedules[1:]:
        common = common.intersection(schedule)
    return sorted(list(common))

def main():
    print("AI Meeting Scheduler Agent")
    print("--------------------------")

    n = int(input("Enter number of participants: "))
    schedules = []

    for i in range(n):
        slots = input(f"Enter available slots for Person {i+1} (comma separated): ")
        schedules.append([slot.strip() for slot in slots.split(",")])

    result = find_common_slot(schedules)

    if result:
        print("\nCommon available slots:", result)
        print("Suggested meeting time:", result[0])
    else:
        print("\nNo common slot available.")

if __name__ == "_main_":
    main()