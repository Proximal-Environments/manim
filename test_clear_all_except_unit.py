#!/usr/bin/env python3
"""Unit tests for the clear_all_except method"""

import unittest
from manimlib import Scene, InteractiveScene, Square, Circle, Triangle
from manimlib.constants import RED, BLUE, GREEN, LEFT, RIGHT


class TestClearAllExceptScene(unittest.TestCase):
    """Unit tests for Scene.clear_all_except"""
    
    def setUp(self):
        """Create a scene for each test"""
        self.scene = Scene()
        # Scene automatically adds camera.frame to mobjects
        self.initial_mobjects_count = len(self.scene.mobjects)
        
    def test_clear_all_except_single_object(self):
        """Test clearing all except a single object"""
        square = Square(color=RED)
        circle = Circle(color=BLUE)
        triangle = Triangle(color=GREEN)
        
        self.scene.add(square, circle, triangle)
        self.assertEqual(len(self.scene.mobjects), self.initial_mobjects_count + 3)
        
        self.scene.clear_all_except(circle)
        
        self.assertEqual(len(self.scene.mobjects), 1)
        self.assertIn(circle, self.scene.mobjects)
        self.assertNotIn(square, self.scene.mobjects)
        self.assertNotIn(triangle, self.scene.mobjects)
        
    def test_clear_all_except_multiple_objects(self):
        """Test clearing all except multiple objects"""
        square = Square(color=RED)
        circle = Circle(color=BLUE)
        triangle = Triangle(color=GREEN)
        
        self.scene.add(square, circle, triangle)
        # Save camera.frame reference
        frame = self.scene.camera.frame
        self.scene.clear_all_except(square, triangle)
        
        # Should have square, triangle (and possibly frame if it was kept)
        self.assertIn(square, self.scene.mobjects)
        self.assertIn(triangle, self.scene.mobjects)
        self.assertNotIn(circle, self.scene.mobjects)
        
    def test_clear_all_except_no_arguments(self):
        """Test clearing all with no arguments (clear everything)"""
        square = Square(color=RED)
        circle = Circle(color=BLUE)
        
        self.scene.add(square, circle)
        self.scene.clear_all_except()
        
        self.assertEqual(len(self.scene.mobjects), 0)
        
    def test_clear_all_except_empty_scene(self):
        """Test clearing an empty scene"""
        self.scene.clear_all_except()
        self.assertEqual(len(self.scene.mobjects), 0)
        
    def test_clear_all_except_nonexistent_object(self):
        """Test that non-existent objects don't cause errors"""
        square = Square(color=RED)
        circle = Circle(color=BLUE)
        triangle = Triangle(color=GREEN)  # Not added to scene
        
        self.scene.add(square, circle)
        # This should not raise an error even though triangle is not in the scene
        self.scene.clear_all_except(circle, triangle)
        
        self.assertEqual(len(self.scene.mobjects), 1)
        self.assertIn(circle, self.scene.mobjects)
        
    def test_clear_all_except_returns_self(self):
        """Test that the method returns self for chaining"""
        square = Square(color=RED)
        circle = Circle(color=BLUE)
        
        self.scene.add(square, circle)
        result = self.scene.clear_all_except(circle)
        
        self.assertIs(result, self.scene)
        
    def test_clear_all_except_preserves_order(self):
        """Test that the order of kept objects is preserved"""
        square = Square(color=RED).shift(LEFT)
        circle = Circle(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT)
        
        self.scene.add(square, circle, triangle)
        self.scene.clear_all_except(square, triangle)
        
        self.assertEqual(len(self.scene.mobjects), 2)
        # Check that order is preserved
        self.assertEqual(self.scene.mobjects[0], square)
        self.assertEqual(self.scene.mobjects[1], triangle)


class TestClearAllExceptInteractiveScene(unittest.TestCase):
    """Unit tests for InteractiveScene.clear_all_except"""
    
    def setUp(self):
        """Create an interactive scene for each test"""
        self.scene = InteractiveScene()
        
    def test_clear_all_except_preserves_selection_highlight(self):
        """Test that selection_highlight is preserved in InteractiveScene"""
        square = Square(color=RED)
        circle = Circle(color=BLUE)
        
        self.scene.add(square, circle)
        
        # selection_highlight should be in mobjects
        self.assertIn(self.scene.selection_highlight, self.scene.mobjects)
        
        self.scene.clear_all_except(circle)
        
        # After clear_all_except, selection_highlight should still be there
        self.assertIn(self.scene.selection_highlight, self.scene.mobjects)
        self.assertIn(circle, self.scene.mobjects)
        self.assertNotIn(square, self.scene.mobjects)
        
    def test_clear_all_except_updates_selection_search_set(self):
        """Test that selection_search_set is updated after clear_all_except"""
        square = Square(color=RED)
        circle = Circle(color=BLUE)
        
        self.scene.add(square, circle)
        initial_search_set_size = len(self.scene.selection_search_set)
        
        self.scene.clear_all_except(circle)
        
        # The search set should be updated (smaller now)
        self.assertLess(len(self.scene.selection_search_set), initial_search_set_size)
        
    def test_clear_all_except_returns_self(self):
        """Test that the method returns self for chaining"""
        square = Square(color=RED)
        result = self.scene.clear_all_except(square)
        
        self.assertIs(result, self.scene)


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestClearAllExceptScene))
    suite.addTests(loader.loadTestsFromTestCase(TestClearAllExceptInteractiveScene))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("Running Unit Tests for clear_all_except")
    print("=" * 60)
    print()
    
    result = run_tests()
    
    print()
    print("=" * 60)
    if result.wasSuccessful():
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
    print("=" * 60)
    
    # Exit with appropriate code
    exit(0 if result.wasSuccessful() else 1)
