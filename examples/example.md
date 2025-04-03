# Markdown to PowerPoint Example

<!-- theme: professional -->
<!-- transition: fade, duration=1.0 -->

## Introduction

<!-- slide: transition=wipe, direction=left -->

This is an example markdown file that demonstrates the features of md2ppt.

- Convert markdown to PowerPoint slides
- Support for advanced PowerPoint features
- Easy-to-use command line interface

## Formatting Examples

You can use **bold text** for emphasis.
You can also use _italic text_ when needed.

Code snippets are supported too:

```python
def hello_world():
    print("Hello, world!")
```

## Images

You can include images in your slides:

![Example Image](example.png)

## Lists

Ordered lists:

1. First item
2. Second item
3. Third item

Unordered lists:

- Item A
- Item B
- Item C

## Quotes

> This is a blockquote example.
> It can span multiple lines.

## Tables

Tables are supported as well:

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

## Slide with Animation

<!-- slide: transition=fade, background_color=lightblue -->

This slide demonstrates animations.

- This item will fade in <!-- animation: fade, duration=0.5, delay=0.2 -->
- This item will fly in from the left <!-- animation: fly_in, direction=left -->
- This item will appear with no animation

## Custom Styling

<!-- slide: transition=zoom -->

You can customize the styling of your presentation.

```json
{
  "colors": {
    "background": [255, 255, 255],
    "title": [0, 0, 128],
    "heading": [0, 64, 128],
    "body": [0, 0, 0]
  }
}
```

## Links

You can include [links to websites](https://example.com) in your slides.

## Math Support

Some implementations might support LaTeX math expressions:

$$E = mc^2$$

## Conclusion

- md2ppt makes it easy to create PowerPoint presentations from Markdown
- Perfect for developers who prefer working with text
- Customizable and extensible

Thanks for using md2ppt!
