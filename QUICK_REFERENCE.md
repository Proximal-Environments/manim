# clear_all_except() Quick Reference

## Basic Syntax
```python
self.clear_all_except(*mobjects_to_keep)
```

## Common Use Cases

### 1. Keep specific objects
```python
self.clear_all_except(circle, square)
```

### 2. Clear everything
```python
self.clear_all_except()
```

### 3. Keep title while changing content
```python
title = Text("My Animation")
self.add(title, obj1, obj2, obj3)
# ... later ...
self.clear_all_except(title)  # Only title remains
```

### 4. Method chaining
```python
self.clear_all_except(title).add(new_content)
```

### 5. With groups
```python
group = Group(obj1, obj2)
self.clear_all_except(group)
```

## Key Features

✓ Automatic deduplication  
✓ Order preservation  
✓ Method chaining support  
✓ Works with groups  
✓ InteractiveScene compatible  

## Files Modified

- `manimlib/scene/scene.py` - Added base method
- `manimlib/scene/interactive_scene.py` - Added override with selection support

## Running Tests

```bash
# Basic tests
xvfb-run -a python test_clear_all_except.py

# Edge cases
xvfb-run -a python test_edge_cases.py

# Visual demos
xvfb-run -a python demo_clear_all_except.py
```

## Quick Example

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import LEFT, RIGHT, UP, RED, BLUE

class QuickDemo(Scene):
    def construct(self):
        # Setup
        title = Text("Demo").to_edge(UP)
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE).shift(RIGHT)
        
        # Show all
        self.add(title, circle, square)
        self.wait(1)
        
        # Keep only title and circle
        self.clear_all_except(title, circle)
        self.wait(1)
```

## Remember

- Camera frame is NOT automatically preserved (unless specified)
- In InteractiveScene, selection_highlight IS automatically preserved
- Duplicates are automatically removed
- Objects not in scene will be added
