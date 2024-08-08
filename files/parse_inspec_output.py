import re
import sys
from collections import defaultdict

def parse_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_passed = 0
    total_failed = 0
    failed_tasks = defaultdict(lambda: {"title": "", "description": ""})

    task_pattern = re.compile(r"cis-dil-benchmark-\d+\.\d+")
    status_pattern = re.compile(r":status: (\w+)")
    title_pattern = re.compile(r":title: (.+)")

    current_task = None
    current_title = None

    for line in lines:
        task_match = task_pattern.search(line)
        if task_match:
            current_task = task_match.group()

        title_match = title_pattern.search(line)
        if title_match:
            current_title = title_match.group(1)


        status_match = status_pattern.search(line)
        if status_match:
            status = status_match.group(1)
            if status == "passed":
                total_passed += 1
            elif status == "failed":
                total_failed += 1
                if current_task:
                    failed_tasks[current_task]["title"] = current_title

    return total_passed, total_failed, failed_tasks

def generate_report(total_passed, total_failed, failed_tasks):
    print("Summary Report")
    print(f"Number of passed tests: {total_passed}")
    print(f"Number of failed tests: {total_failed}")
    print("\nFailed Tasks:")
    for task, details in failed_tasks.items():
        print(f"Task ID: {task}")
        print(f"Title: {details['title']}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_inspec_output.py <path_to_output_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    total_passed, total_failed, failed_tasks = parse_output(file_path)
    generate_report(total_passed, total_failed, failed_tasks)
