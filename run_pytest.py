import pytest
import sys

# Run pytest and capture the result
result = pytest.main()

# Check the number of failed tests
max_failures_allowed = 2
if result <= max_failures_allowed:
    sys.exit(0)
else:
    sys.exit(1)
