# clear_all_except() Method Documentation

## Overview

The `clear_all_except()` method has been added to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides a convenient way to clear all objects from the scene while keeping only specific objects that you want to preserve.

## Location

- `manimlib/scene/scene.py` - Base Scene class implementation
- `manimlib/scene/interactive_scene.py` - InteractiveScene class implementation

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

## Usage Examples

### Basic Usage with Scene

```python
from manimlib import *

class BasicClearExample(Scene):
    def construct(self):
        # Create some shapes
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN)
        
        # Add all shapes to scene
        self.add(circle, square, triangle)
        self.wait()
        
        # Clear everything except the circle
        self.clear_all_except(circle)
        self.wait()
```

### Keeping Multiple Objects

```python
class MultipleObjectsExample(Scene):
    def construct(self):
        # Create shapes and labels
        circle = Circle(color=BLUE).shift(LEFT)
        square = Square(color=RED).shift(RIGHT)
        label = Text("Keep These", font_size=24).to_edge(UP)
        
        self.add(circle, square, label)
        self.wait()
        
        # Keep both circle and label, remove square
        self.clear_all_except(circle, label)
        self.wait()
```

### Method Chaining

```python
class MethodChainingExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        # Method chaining is supported
        self.add(circle, square).clear_all_except(circle).add(Triangle())
```

### With InteractiveScene

```python
class InteractiveClearExample(InteractiveScene):
    def construct(self):
        # Create interactive elements
        shapes = VGroup(
            Circle(color=BLUE),
            Square(color=RED),
            Triangle(color=GREEN)
        ).arrange(RIGHT)
        
        self.add(shapes)
        self.wait()
        
        # Clear all except the first shape
        # Note: selection_highlight is automatically preserved
        self.clear_all_except(shapes[0])
        self.wait()
```

## Important Notes

### Scene Class Behavior

1. **Camera Frame**: The camera frame is managed separately and is not affected by `clear_all_except()`
2. **Return Value**: Returns `self` to allow method chaining
3. **Decorator**: Uses `@affects_mobject_list` decorator to ensure render groups are properly updated
4. **Empty Call**: Calling `clear_all_except()` with no arguments will clear all objects from the scene

### InteractiveScene Class Behavior

1. **Selection Highlight Preservation**: The `selection_highlight` (part of InteractiveScene's UI) is automatically preserved
2. **Selection Search Set**: Automatically regenerates the selection search set after clearing
3. **Unselectables**: Other unselectable UI elements are managed appropriately
4. **Interactive Features**: All interactive features remain functional after using `clear_all_except()`

## Comparison with Other Methods

### clear() vs clear_all_except()

```python
# Using clear() - removes everything
self.clear()
self.add(circle)  # Need to re-add what you want

# Using clear_all_except() - keeps specified objects
self.clear_all_except(circle)  # More concise
```

### remove() vs clear_all_except()

```python
# Using remove() - need to specify what to remove
self.remove(square, triangle, text)  # Keeps circle

# Using clear_all_except() - specify what to keep
self.clear_all_except(circle)  # More intuitive when keeping fewer objects
```

## Use Cases

1. **Scene Transitions**: Quickly transition between scenes by keeping only key elements
2. **Animation Cleanup**: Remove temporary construction objects while keeping final results
3. **Selective Reset**: Reset part of the scene while maintaining context objects
4. **Memory Management**: Clear unnecessary objects from memory while preserving important ones
5. **Interactive Development**: In InteractiveScene, quickly clean up while testing different visualizations

## Implementation Details

### Scene.clear_all_except()

```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    self.mobjects = []
    self.add(*mobjects_to_keep)
    return self
```

The implementation:
1. Clears the mobjects list
2. Re-adds the specified mobjects using the `add()` method
3. The `@affects_mobject_list` decorator ensures render groups are reassembled
4. Returns `self` for method chaining

### InteractiveScene.clear_all_except()

```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    # Preserve selection_highlight if it's currently in the scene
    has_selection_highlight = self.selection_highlight in self.mobjects
    
    # Call parent's clear_all_except
    super().clear_all_except(*mobjects_to_keep)
    
    # Re-add selection_highlight if it was present before
    if has_selection_highlight and self.selection_highlight not in self.mobjects:
        self.mobjects.insert(0, self.selection_highlight)
    
    self.regenerate_selection_search_set()
    return self
```

The InteractiveScene implementation:
1. Checks if `selection_highlight` is present
2. Calls the parent class's `clear_all_except()`
3. Re-adds `selection_highlight` if it was present
4. Regenerates the selection search set for interactive features
5. Returns `self` for method chaining

## Testing

The implementation has been thoroughly tested with:

1. **Basic Scene Tests**: Verifying correct behavior in standard Scene
2. **InteractiveScene Tests**: Verifying preservation of interactive features
3. **Edge Cases**: Empty arguments, method chaining, camera frame handling
4. **Visual Tests**: Demo scenes showing practical usage

Run tests with:
```bash
xvfb-run -a python test_clear_all_except.py
```

Run demos with:
```bash
xvfb-run -a manimgl demo_clear_all_except.py DemoClearAllExcept -w
xvfb-run -a manimgl demo_clear_all_except.py DemoInteractiveClearAllExcept -w
```

## Performance Considerations

- **Efficiency**: The method is efficient as it uses the existing `add()` mechanism
- **Render Groups**: Automatically reassembled due to `@affects_mobject_list` decorator
- **Memory**: Old objects are properly removed and can be garbage collected
- **Selection Search Set**: In InteractiveScene, the selection search set is regenerated automatically

## Compatibility

- Works with all Mobject types (VMobject, Group, VGroup, etc.)
- Compatible with existing scene methods
- Maintains backward compatibility with existing code
- Works in both headless and windowed modes

## Future Enhancements

Potential future improvements:
1. Add animation support for smooth transitions
2. Add optional callback for objects being removed
3. Add filtering options (e.g., by type or property)
4. Performance optimization for large scenes

## Contributing

If you find any issues or have suggestions for improvements, please:
1. Check existing tests in `test_clear_all_except.py`
2. Add new test cases for edge cases
3. Update documentation as needed
4. Follow the existing code style
