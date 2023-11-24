"""A module containing the call to postman tests"""
from __future__ import annotations

import subprocess


def run_postman_tests(collection_file):
    """A method running postman tests"""
    try:
        # Replace 'newman' with the actual path to the Newman executable if needed
        newman_command = ['newman', 'run', collection_file]

        # Run Newman as a subprocess
        subprocess.run(newman_command, check=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running Postman tests: {e}")
        return False

# Usage
if __name__ == '__main__':
    COLLECTION_FILE_PATH = "PostmanCollection.json"
    POSTMAN_TEST_RESULT = run_postman_tests(COLLECTION_FILE_PATH)

    if POSTMAN_TEST_RESULT:
        print("Postman tests passed.")
    else:
        print("Postman tests failed.")
