# clear_all_except() Method Documentation

## Overview

The `clear_all_except()` method has been added to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides a convenient way to clear all objects from the scene while keeping only specified objects.

## Location

- `manimlib/scene/scene.py` - Base `Scene` class implementation
- `manimlib/scene/interactive_scene.py` - Extended `InteractiveScene` implementation

## Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all objects from the scene and adds back only the ones
    specified in mobjects_to_keep.
    """
```

## Parameters

- `*mobjects_to_keep`: Variable number of `Mobject` instances to keep on screen after clearing
  - Can be empty (clears everything)
  - Duplicate references are automatically deduplicated
  - Objects not currently in the scene will be added

## Returns

- `self`: Returns the scene instance for method chaining

## Behavior

### In Scene class:
1. Clears all mobjects from the scene (including camera frame if not specified)
2. Deduplicates the list of mobjects to keep (preserving order)
3. Adds back only the specified mobjects
4. Reassembles render groups automatically

### In InteractiveScene class:
Additionally:
- Automatically preserves the `selection_highlight` to maintain interactive functionality
- Regenerates the selection search set after clearing

## Usage Examples

### Basic Usage

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.constants import LEFT, RIGHT, RED, BLUE, GREEN

class MyScene(Scene):
    def construct(self):
        # Create objects
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT)
        
        # Add all objects
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Keep only circle and square
        self.clear_all_except(circle, square)
        self.wait(1)
```

### Clear Everything

```python
# Remove all objects from scene
self.clear_all_except()
```

### Method Chaining

```python
# Clear and immediately add new objects
new_circle = Circle(color=YELLOW)
self.clear_all_except(title).add(new_circle)
```

### Keep Multiple Objects

```python
# Keep several objects
self.clear_all_except(obj1, obj2, obj3, label1, label2)
```

### With Groups

```python
# Works with groups
group = Group(circle, square)
self.add(group, triangle)
self.clear_all_except(group)  # Keeps the entire group
```

## Implementation Details

### Deduplication

The method automatically deduplicates mobjects while preserving order:

```python
# These are equivalent:
self.clear_all_except(circle, circle, circle)
self.clear_all_except(circle)
```

### Order Preservation

Objects are added back in the order they appear in the arguments (after deduplication), respecting z-index ordering as per the standard `add()` method.

### Camera Frame

The camera frame is treated like any other mobject:
- It will be removed if not specified in `mobjects_to_keep`
- To keep it: `self.clear_all_except(self.camera.frame, other_objects)`

### InteractiveScene Special Handling

In `InteractiveScene`, the selection highlight is automatically preserved to maintain interactive capabilities. This happens transparently without requiring explicit inclusion in the arguments.

## Edge Cases

1. **Empty scene**: Works correctly on an empty scene
2. **No arguments**: Equivalent to `clear()` - removes everything
3. **Non-existent objects**: Objects not in the scene will be added
4. **Duplicates**: Automatically deduplicated
5. **Groups**: Entire groups can be kept as units

## Performance

The method has the same performance characteristics as calling:
```python
self.clear()
self.add(*mobjects)
```

Plus a small overhead for deduplication (O(n) where n is the number of arguments).

## Testing

Comprehensive tests are available in:
- `test_clear_all_except.py` - Basic functionality tests
- `test_edge_cases.py` - Edge case coverage
- `demo_clear_all_except.py` - Visual demonstrations

Run tests with:
```bash
xvfb-run -a python test_clear_all_except.py
xvfb-run -a python test_edge_cases.py
xvfb-run -a python demo_clear_all_except.py
```

## Comparison with Alternative Approaches

### Before `clear_all_except()`:
```python
# Manual approach
to_keep = [obj1, obj2, obj3]
to_remove = [m for m in self.mobjects if m not in to_keep]
self.remove(*to_remove)
```

### With `clear_all_except()`:
```python
# Cleaner and more intuitive
self.clear_all_except(obj1, obj2, obj3)
```

## Notes

- The method is decorated with `@affects_mobject_list` which automatically calls `assemble_render_groups()`
- Compatible with all existing ManimGL features
- Does not affect animation state or timeline
- Works in both window and headless modes

## Examples from Tests

See the test files for comprehensive examples:

1. **Basic clearing**: `test_clear_all_except.py`
2. **Edge cases**: `test_edge_cases.py`  
3. **Visual demos**: `demo_clear_all_except.py`

## Version Information

- Added in: ManimGL (current development version)
- Tested on: Python 3.11.9
- Compatible with: All ManimGL versions with Scene class
