# clear_all_except() Quick Reference

## Syntax
```python
self.clear_all_except(*mobjects_to_keep)
```

## Quick Examples

### Keep One Object
```python
self.clear_all_except(circle)
```

### Keep Multiple Objects
```python
self.clear_all_except(header, footer, logo)
```

### Clear Everything
```python
self.clear_all_except()
```

### Method Chaining
```python
self.clear_all_except(title).add(new_content)
```

## When to Use

✅ **Good Use Cases:**
- Transitioning between sections in a presentation
- Keeping persistent UI elements (headers, footers, navigation)
- Resetting a scene while preserving certain reference objects
- Simplifying complex scene management

❌ **Not Needed When:**
- You want to remove just one or two objects (use `remove()` instead)
- You want to clear everything (use `clear()` instead)
- You're working with animations that already handle object lifecycle

## Common Patterns

### Pattern 1: Presentation Slides
```python
# Keep title and navigation, change content
self.clear_all_except(title, nav_bar)
self.add(new_slide_content)
```

### Pattern 2: Tutorial Steps
```python
# Keep problem statement, clear solution steps
self.clear_all_except(problem_text)
self.add(next_step_content)
```

### Pattern 3: Data Visualization Updates
```python
# Keep axes and labels, update data
self.clear_all_except(axes, x_label, y_label)
self.add(new_data_plot)
```

## Files Modified
- `manimlib/scene/scene.py` (line 398)
- `manimlib/scene/interactive_scene.py` (line 248)

## Test Command
```bash
xvfb-run -a python test_clear_all_except_unit.py
```

## Documentation
- Full docs: `CLEAR_ALL_EXCEPT_DOCUMENTATION.md`
- Examples: `example_clear_all_except.py`
- Tests: `test_clear_all_except_unit.py`
