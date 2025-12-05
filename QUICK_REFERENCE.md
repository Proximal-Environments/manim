# clear_all_except() - Quick Reference

## Syntax

```python
scene.clear_all_except(*mobjects_to_keep)
```

## Basic Usage

```python
# Keep one object
self.clear_all_except(circle)

# Keep multiple objects
self.clear_all_except(circle, square, text)

# Clear everything (frame is still preserved)
self.clear_all_except()
```

## What Gets Preserved

### In Scene
- ✓ Camera frame (automatic)
- ✓ Objects you specify

### In InteractiveScene
- ✓ Camera frame (automatic)
- ✓ selection_highlight (automatic)
- ✓ selection_rectangle (automatic)
- ✓ crosshair (automatic)
- ✓ Other internal objects (automatic)
- ✓ Objects you specify

## Common Patterns

### Pattern 1: Title + Changing Content
```python
title = Tex("Title").to_edge(UP)
self.add(title)

# Scene 1
content1 = Circle()
self.add(content1)
self.wait()

# Scene 2
content2 = Square()
self.clear_all_except(title)
self.add(content2)
self.wait()
```

### Pattern 2: Progressive Filtering
```python
shapes = [Circle(), Square(), Triangle()]
self.add(*shapes)
self.wait()

# Keep only first two
self.clear_all_except(shapes[0], shapes[1])
self.wait()

# Keep only first
self.clear_all_except(shapes[0])
self.wait()
```

### Pattern 3: Method Chaining
```python
self.clear_all_except(title).add(new_content).wait()
```

## Comparison

| Want to... | Use... |
|------------|--------|
| Remove everything | `clear()` |
| Remove specific objects | `remove(obj1, obj2)` |
| Keep specific objects | `clear_all_except(obj1, obj2)` |

## Remember

- Frame is auto-preserved (usually what you want)
- Returns self (chain methods)
- Works with any mobject type
- No need to track what to remove

## Test Command

```bash
xvfb-run -a python test_clear_all_except.py
```

## More Info

See `README_CLEAR_ALL_EXCEPT.md` for complete documentation.
