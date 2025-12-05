# clear_all_except() Method - Implementation Summary

## What Was Added

A new method `clear_all_except()` has been added to both `Scene` and `InteractiveScene` classes in ManimGL.

## Files Modified

1. **manimlib/scene/scene.py** (lines 398-416)
   - Added `clear_all_except()` method to the `Scene` class
   - Method automatically preserves the camera frame
   - Decorated with `@affects_mobject_list` for proper render group management

2. **manimlib/scene/interactive_scene.py** (lines 248-270)
   - Added `clear_all_except()` method to the `InteractiveScene` class
   - Extends parent implementation to also preserve internal interactive objects
   - Regenerates selection search set after clearing

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Self
```

## Key Features

### Scene Class
- Clears all mobjects from the scene
- Automatically preserves the camera frame
- Adds back only the specified mobjects
- Returns self for method chaining
- Properly updates render groups

### InteractiveScene Class
- All features from Scene class
- Additionally preserves internal interactive objects:
  - selection_highlight
  - selection_rectangle
  - crosshair
  - information_label
- Regenerates selection search set after clearing

## Usage Example

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle

class MyScene(Scene):
    def construct(self):
        # Create objects
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        # Add all
        self.add(circle, square, triangle)
        
        # Clear all except circle and square
        self.clear_all_except(circle, square)
        # Now only circle and square remain (plus the camera frame)
```

## Testing

A comprehensive test suite has been created in `test_clear_all_except.py` that:
- Tests basic functionality in Scene
- Tests functionality in InteractiveScene
- Verifies frame preservation
- Verifies internal object preservation in InteractiveScene
- Tests multiple sequential clear operations
- Tests edge cases (empty scene, single object, etc.)

### Run Tests

```bash
xvfb-run -a python test_clear_all_except.py
```

All tests pass successfully.

## Additional Files Created

1. **test_clear_all_except.py** - Comprehensive unit tests
2. **demo_clear_all_except.py** - Visual demonstration scenes
3. **example_clear_all_except.py** - Simple usage example
4. **CLEAR_ALL_EXCEPT_DOCS.md** - Detailed documentation
5. **CLEAR_ALL_EXCEPT_SUMMARY.md** - This file

## Benefits

1. **Convenience**: No need to manually track and remove individual objects
2. **Clean Code**: More readable than multiple `remove()` calls
3. **Safe**: Automatically preserves essential objects (frame, interactive elements)
4. **Flexible**: Works with any mobject type
5. **Chainable**: Returns self for method chaining

## Implementation Design Decisions

### Frame Preservation
The camera frame is automatically preserved because:
- It's essential for scene rendering
- Users rarely want to remove it
- Consistent with `remove()` behavior
- Can still be removed if needed (by manual removal before calling the method)

### InteractiveScene Internal Objects
Internal objects are preserved because:
- They're not user-facing content
- They're required for InteractiveScene functionality
- Users shouldn't need to think about them
- Listed in `unselectables` for easy identification

### Method Chaining
Returns `self` to allow fluent API usage:
```python
self.add(obj1).clear_all_except(obj2).add(obj3)
```

## Compatibility

- Fully backward compatible
- No breaking changes to existing code
- Works with all mobject types
- Compatible with animations and transitions
- Works in both interactive and non-interactive modes

## Future Enhancements (Optional)

Possible future improvements:
1. Add optional parameter to control frame preservation
2. Add optional parameter to specify additional auto-preserve objects
3. Add callback hooks for pre/post clear events
4. Performance optimizations for very large scenes
