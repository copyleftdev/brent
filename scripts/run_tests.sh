#!/bin/bash

# This script runs all the unit tests in the project.

# Set the project root directory
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Find all Python test files
TEST_FILES=$(find "$PROJECT_ROOT" -name "test_*.py")

# Check if any test files were found
if [ -z "$TEST_FILES" ]; then
  echo "No test files found."
  exit 1
fi

# Run the tests
echo "Running tests..."
for test_file in $TEST_FILES; do
  echo "Running $test_file..."
  python "$test_file"
  if [ $? -ne 0 ]; then
    echo "Test failed: $test_file"
    exit 1
  fi
done

echo "All tests passed."
exit 0
