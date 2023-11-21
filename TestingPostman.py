import subprocess

def run_postman_tests(collection_file):
    # Construct the Newman command
    command = [
        "newman",
        "run",
        collection_file
       
    ]

    try:
        # Run Newman using subprocess
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Check if all tests passed based on the exit code
        if result.returncode == 0:
            print("All tests passed!")
            return True
        else:
            print("Some tests failed.")
            return False

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the Newman execution
        print(f"Error running Newman: {e}")
        return False

# Example usage
collection_file ='PostmanCollection.json'


result = run_postman_tests(collection_file)

# Use the 'result' variable as needed in your application
