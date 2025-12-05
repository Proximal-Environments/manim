# clear_all_except() Method - Quick Reference

## What is it?

A new method added to ManimGL's `Scene` and `InteractiveScene` classes that clears all objects from the scene except the ones you specify to keep.

## Quick Start

```python
from manimlib import *

class MyScene(Scene):
    def construct(self):
        # Create objects
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        # Add all to scene
        self.add(circle, square, triangle)
        
        # Keep only the circle, remove everything else
        self.clear_all_except(circle)
```

## Why Use It?

**Before (removing objects manually):**
```python
self.remove(square, triangle, text1, text2, text3)
```

**After (keeping what you want):**
```python
self.clear_all_except(circle)
```

**Benefit**: More intuitive when you want to keep fewer objects than you want to remove!

## Features

- ✓ Works with `Scene` and `InteractiveScene`
- ✓ Keeps multiple objects: `self.clear_all_except(obj1, obj2, obj3)`
- ✓ Method chaining: `self.clear_all_except(circle).add(square)`
- ✓ Clear everything: `self.clear_all_except()` (same as `self.clear()`)
- ✓ Preserves InteractiveScene UI (selection_highlight)

## Files Modified

1. **manimlib/scene/scene.py** - Base implementation (lines 398-409)
2. **manimlib/scene/interactive_scene.py** - Extended implementation (lines 248-268)

## Testing

```bash
# Run unit tests
xvfb-run -a python test_clear_all_except.py

# Run examples (replace <ExampleName> with one below)
xvfb-run -a manimgl example_clear_all_except.py <ExampleName> -w
```

**Available Examples:**
- `SimpleClearExample` - Basic usage
- `ComparisonExample` - Compare with traditional methods
- `PracticalExample` - Real-world use case

## Common Use Cases

### 1. Scene Transitions
```python
# Keep only the title when transitioning
self.clear_all_except(title)
```

### 2. Construction Cleanup
```python
# Remove construction lines, keep final shape
self.clear_all_except(final_shape)
```

### 3. Selective Reset
```python
# Keep context objects, remove temporary ones
self.clear_all_except(axes, labels)
```

### 4. Interactive Development
```python
# In InteractiveScene - quickly clean up while testing
self.clear_all_except(object_under_test)
# selection_highlight is automatically preserved!
```

## Documentation

- **Full Documentation**: `CLEAR_ALL_EXCEPT_DOCUMENTATION.md`
- **Implementation Details**: `IMPLEMENTATION_SUMMARY.md`
- **Test File**: `test_clear_all_except.py`
- **Examples**: `example_clear_all_except.py`
- **Demos**: `demo_clear_all_except.py`

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all mobjects from the scene and adds back only the ones
    specified in mobjects_to_keep.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene
        
    Returns:
        self: Returns the scene instance for method chaining
    """
```

## Implementation

### Scene Class
```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    self.mobjects = []
    self.add(*mobjects_to_keep)
    return self
```

### InteractiveScene Class
```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    # Preserve selection_highlight if present
    has_selection_highlight = self.selection_highlight in self.mobjects
    
    super().clear_all_except(*mobjects_to_keep)
    
    # Re-add selection_highlight if it was present
    if has_selection_highlight and self.selection_highlight not in self.mobjects:
        self.mobjects.insert(0, self.selection_highlight)
    
    self.regenerate_selection_search_set()
    return self
```

## Test Results

All tests passing ✓

```
============================================================
Running tests for clear_all_except method
============================================================
Testing Scene.clear_all_except()...
  ✓ Scene.clear_all_except() test passed!

Testing InteractiveScene.clear_all_except()...
  ✓ InteractiveScene.clear_all_except() test passed!

Testing clear_all_except with no arguments...
  ✓ clear_all_except() with no arguments test passed!

Testing that camera frame is preserved...
  ✓ Camera frame handling test passed!

Testing return value for method chaining...
  ✓ Method chaining test passed!

============================================================
All tests passed! ✓
============================================================
```

## Tips

1. **Use when keeping fewer objects**: If you need to keep 1-2 objects but remove 10, use `clear_all_except`
2. **Use traditional `remove` when removing fewer**: If you need to remove 1-2 objects from many, use `self.remove()`
3. **Method chaining**: Take advantage of the return value: `self.clear_all_except(obj).add(new_obj)`
4. **InteractiveScene**: Don't worry about selection_highlight - it's automatically preserved!

## Support

For issues, questions, or contributions:
1. Check the test file for examples
2. Read the full documentation
3. Try the example scenes
4. Follow existing code patterns

## License

This implementation follows the same license as ManimGL.

---

**Implementation Date**: December 2024  
**Version**: 1.0  
**Status**: Production Ready ✓
