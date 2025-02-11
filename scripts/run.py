import subprocess
import os
import time

def run_tests():
    allure_dir = "allure_results"
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)

    command = [
        "python", "-m", "pytest",
        "config/",
        "--alluredir", allure_dir,
        "-n", "auto"
    ]

    print("Running config...")
    result = subprocess.run(command)

    if result.returncode == 0:
        print(f"passed")
    else:
        print(f"failed")

if __name__ == "__main__":
    run_tests()