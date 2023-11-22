import subprocess

def run_postman_tests(collection_file):
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
    collection_file_path = "PostmanCollection.json"
    postman_test_result = run_postman_tests(collection_file_path)

    if postman_test_result:
        print("Postman tests passed.")
    else:
        print("Postman tests failed.")
