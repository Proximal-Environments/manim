#!/bin/bash

echo "================================================================================"
echo "RUNNING ALL TESTS FOR clear_all_except() IMPLEMENTATION"
echo "================================================================================"
echo ""

# Counter for test results
PASSED=0
FAILED=0

# Function to run a test
run_test() {
    local test_name=$1
    local test_file=$2
    
    echo "Running: $test_name"
    echo "------------------------------------------------------------------------"
    
    if xvfb-run -a python "$test_file" > /dev/null 2>&1; then
        echo "✅ PASSED: $test_name"
        ((PASSED++))
    else
        echo "❌ FAILED: $test_name"
        ((FAILED++))
    fi
    echo ""
}

# Run all tests
run_test "Basic Functionality Tests" "test_clear_all_except.py"
run_test "Edge Case Tests" "test_edge_cases.py"
run_test "Visual Demonstrations" "demo_clear_all_except.py"
run_test "Practical Examples" "example_practical_use.py"
run_test "Final Validation" "final_test.py"

echo "================================================================================"
echo "TEST RESULTS SUMMARY"
echo "================================================================================"
echo "Tests Passed: $PASSED"
echo "Tests Failed: $FAILED"
echo "Total Tests:  $((PASSED + FAILED))"
echo ""

if [ $FAILED -eq 0 ]; then
    echo "🎉 ALL TESTS PASSED! Implementation is complete and working correctly."
    echo ""
    echo "Files modified:"
    echo "  • manimlib/scene/scene.py"
    echo "  • manimlib/scene/interactive_scene.py"
    echo ""
    echo "Method added: clear_all_except(*mobjects_to_keep)"
    echo ""
    echo "Features:"
    echo "  ✓ Clears all objects except specified ones"
    echo "  ✓ Automatic deduplication"
    echo "  ✓ Method chaining support"
    echo "  ✓ InteractiveScene support with selection_highlight preservation"
    echo "  ✓ Comprehensive test coverage"
    echo "  ✓ Complete documentation"
    echo ""
    exit 0
else
    echo "⚠️  Some tests failed. Please review the implementation."
    exit 1
fi
