# clear_all_except() Method - Implementation Complete ✅

## Summary

Successfully added the `clear_all_except()` method to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides an intuitive way to clear all objects from the scene while keeping only specified ones.

## Quick Start

```python
from manimlib import *

class Example(Scene):
    def construct(self):
        # Create objects
        title = Text("My Animation").to_edge(UP)
        circle = Circle(color=RED)
        square = Square(color=BLUE)
        
        # Add all
        self.add(title, circle, square)
        self.wait()
        
        # Keep only title and circle
        self.clear_all_except(title, circle)
        self.wait()
```

## Implementation Details

### Modified Files

1. **manimlib/scene/scene.py** (Lines 398-417)
   - Added `clear_all_except()` method to Scene class
   - Handles deduplication of arguments
   - Uses `@affects_mobject_list` decorator
   - Returns `self` for method chaining

2. **manimlib/scene/interactive_scene.py** (Lines 248-258)
   - Added `clear_all_except()` method to InteractiveScene class
   - Calls parent implementation
   - Regenerates selection search set
   - Returns `self` for method chaining

## Key Features

✅ **Selective Clearing**: Keep specified objects, remove everything else  
✅ **No Duplicates**: Handles duplicate arguments gracefully  
✅ **Method Chaining**: Returns `self` for fluent API  
✅ **InteractiveScene Support**: Updates selection search sets automatically  
✅ **Edge Case Handling**: Works with no arguments, non-existent objects, groups, etc.  

## Testing

All tests pass successfully:

```bash
# Run basic tests
xvfb-run -a python test_clear_all_except.py

# Run comprehensive tests  
xvfb-run -a python test_clear_all_except_comprehensive.py

# Run simple verification
xvfb-run -a python simple_test.py
```

### Test Coverage

- ✅ Basic functionality in Scene
- ✅ Basic functionality in InteractiveScene
- ✅ Clearing with no arguments
- ✅ Keeping single/multiple objects
- ✅ Handling groups
- ✅ Non-existent objects
- ✅ Duplicate arguments
- ✅ Multiple successive calls
- ✅ Method chaining
- ✅ Selection search set updates

## Usage Examples

### Basic Usage
```python
# Keep only one object
self.clear_all_except(circle)

# Keep multiple objects
self.clear_all_except(title, circle, label)

# Clear everything (same as clear())
self.clear_all_except()
```

### Method Chaining
```python
self.add(c1, c2, c3) \
    .clear_all_except(c1) \
    .add(c2)
```

### Multi-Stage Visualization
```python
def construct(self):
    title = Text("Title").to_edge(UP)
    self.add(title)
    
    # Stage 1
    self.show_stage_1()
    
    # Transition: keep only title
    self.clear_all_except(title)
    
    # Stage 2
    self.show_stage_2()
```

### InteractiveScene
```python
class MyInteractiveScene(InteractiveScene):
    def construct(self):
        objects = [Circle(), Square(), Triangle()]
        self.add(*objects)
        
        # Selection search set updates automatically
        self.clear_all_except(objects[0])
```

## Documentation Files

- **IMPLEMENTATION_SUMMARY.md** - Detailed implementation summary
- **CLEAR_ALL_EXCEPT_DOCUMENTATION.md** - Comprehensive documentation
- **README_CLEAR_ALL_EXCEPT.md** - This file (quick reference)

## Test Files

- **test_clear_all_except.py** - Basic functionality tests
- **test_clear_all_except_comprehensive.py** - Comprehensive test suite
- **simple_test.py** - Quick verification test
- **demo_clear_all_except.py** - Visual demonstrations

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all mobjects from the scene and adds back only the specified ones.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene after clearing
        
    Returns:
        self: The scene instance for method chaining
    """
```

## Comparison with Existing Methods

| Method | Use When |
|--------|----------|
| `clear()` | You want to remove everything |
| `remove(*objs)` | You know exactly what to remove |
| `clear_all_except(*objs)` | Easier to specify what to keep |

## When to Use clear_all_except()

Use `clear_all_except()` when:

1. **Multi-stage animations** - Keep persistent UI elements across stages
2. **Progressive disclosure** - Focus on important objects by removing others
3. **Scene transitions** - Clean slate while keeping titles/labels
4. **Interactive scenes** - Manage selectable objects efficiently
5. **Fewer objects to keep** - When it's easier to list what to keep vs. what to remove

## Performance

- O(n) complexity where n is the number of arguments
- Efficient deduplication using set-based lookups
- Triggers render group assembly once via decorator

## Compatibility

- ✅ Works with all mobject types
- ✅ Compatible with animations
- ✅ Supports both Scene and InteractiveScene
- ✅ Follows ManimGL naming conventions
- ✅ Uses existing infrastructure

## Troubleshooting

**Q: Objects disappear unexpectedly**  
A: Make sure objects are added to scene before calling clear_all_except

**Q: Object appears multiple times**  
A: This is handled automatically - duplicates in arguments are removed

**Q: InteractiveScene selection not working**  
A: Ensure setup() is called - it's called automatically in construct()

## Examples in Action

Run the demo:
```bash
manimgl demo_clear_all_except.py DemoClearAllExcept
manimgl demo_clear_all_except.py InteractiveDemoClearAllExcept
manimgl demo_clear_all_except.py PracticalExample
```

## Verification

To verify the implementation:

```bash
# Quick test
xvfb-run -a python simple_test.py

# Should output:
# Testing Scene.clear_all_except()...
# Added 3 objects. Total: 4
# After clear_all_except(circle): 1
# ✅ Scene test passed!
#
# Testing InteractiveScene.clear_all_except()...
# Added 3 objects. Search set: 3
# After clear_all_except(c1, c2). Search set: 2
# ✅ InteractiveScene test passed!
#
# 🎉 All simple tests passed!
```

## Integration Status

✅ **Implemented** in both Scene and InteractiveScene  
✅ **Tested** with comprehensive test suite  
✅ **Documented** with usage examples  
✅ **Production Ready** - All tests passing  

## Credits

Implementation follows ManimGL coding standards and conventions.
Uses existing infrastructure (add, remove, affects_mobject_list) for consistency.

---

**Status**: ✅ Complete and Ready for Use

For detailed documentation, see `CLEAR_ALL_EXCEPT_DOCUMENTATION.md`  
For implementation details, see `IMPLEMENTATION_SUMMARY.md`
