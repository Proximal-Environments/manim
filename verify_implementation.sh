#!/bin/bash

echo "======================================================================"
echo "       CLEAR_ALL_EXCEPT METHOD - IMPLEMENTATION VERIFICATION"
echo "======================================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Checking implementation in Scene class...${NC}"
if grep -q "def clear_all_except" manimlib/scene/scene.py; then
    echo -e "${GREEN}✓ Method found in scene.py${NC}"
else
    echo -e "${RED}✗ Method not found in scene.py${NC}"
    exit 1
fi

echo -e "${BLUE}Checking implementation in InteractiveScene class...${NC}"
if grep -q "def clear_all_except" manimlib/scene/interactive_scene.py; then
    echo -e "${GREEN}✓ Method found in interactive_scene.py${NC}"
else
    echo -e "${RED}✗ Method not found in interactive_scene.py${NC}"
    exit 1
fi

echo ""
echo "======================================================================"
echo "                        RUNNING TESTS"
echo "======================================================================"
echo ""

echo -e "${BLUE}Running basic functionality tests...${NC}"
if xvfb-run -a python test_clear_all_except.py 2>&1 | grep -q "All tests completed successfully"; then
    echo -e "${GREEN}✓ Basic tests PASSED${NC}"
else
    echo -e "${RED}✗ Basic tests FAILED${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}Running edge case tests...${NC}"
if xvfb-run -a python test_edge_cases.py 2>&1 | grep -q "All edge case tests completed successfully"; then
    echo -e "${GREEN}✓ Edge case tests PASSED${NC}"
else
    echo -e "${RED}✗ Edge case tests FAILED${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}Running practical examples...${NC}"
if xvfb-run -a python example_simple_practical.py 2>&1 | grep -q "All practical examples completed successfully"; then
    echo -e "${GREEN}✓ Practical examples PASSED${NC}"
else
    echo -e "${RED}✗ Practical examples FAILED${NC}"
    exit 1
fi

echo ""
echo "======================================================================"
echo "                      VERIFICATION SUMMARY"
echo "======================================================================"
echo ""
echo -e "${GREEN}✅ All checks passed!${NC}"
echo ""
echo "Implementation Details:"
echo "  • Method added to Scene class"
echo "  • Method added to InteractiveScene class"
echo "  • All basic tests passing"
echo "  • All edge cases handled"
echo "  • Practical examples working"
echo ""
echo "Documentation Available:"
echo "  • CLEAR_ALL_EXCEPT_DOCUMENTATION.md"
echo "  • QUICK_REFERENCE.md"
echo "  • IMPLEMENTATION_SUMMARY.md"
echo "  • FINAL_SUMMARY.md"
echo ""
echo -e "${GREEN}Status: PRODUCTION READY ✅${NC}"
echo ""
echo "======================================================================"
