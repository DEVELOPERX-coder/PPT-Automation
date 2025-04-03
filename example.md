---
slide_width: 13.33in
slide_height: 7.5in
default_font: "Segoe UI"
default_font_size: 18
footer_text: "#DSAin45 - Strings in C++"
---

# 🚀 STRINGS IN C++

{
layout: "Title Slide",
background: "#1A1A1A",
transition: "fade",
transition_speed: "medium"
}

:::text[x:3.17in, y:3.5in, width:7in, height:1.5in]
{
font: "Segoe UI Light",
font_size: 48,
font_color: "#00FFFF",
align: center,
bold: true,
animation: "float_in",
animation_direction: "left",
animation_trigger: "with_previous",
animation_duration: 1.5
}
🚀 STRINGS IN C++
:::

:::text[x:3.67in, y:5.2in, width:6in, height:1in]
{
font: "Segoe UI",
font_size: 32,
font_color: "#BB86FC",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.3,
animation_duration: 1.0
}
Arrays With Character(s)
:::

:::text[x:5.17in, y:6.5in, width:3in, height:0.6in]
{
font: "Segoe UI",
font_size: 18,
font_color: "#E0E0E0",
align: center,
animation: "appear",
animation_trigger: "after_previous",
animation_delay: 0.5
}
#DSAin45 - Day 4
:::

:::text[x:3.65in, y:7.3in, width:0.7in, height:0.7in]
{
font: "Consolas",
font_size: 36,
font_color: "#00FFFF",
align: center,
bold: true,
animation: "wipe",
animation_direction: "right",
animation_trigger: "with_previous",
animation_duration: 0.7
}
S
:::

:::text[x:4.45in, y:7.3in, width:0.7in, height:0.7in]
{
font: "Consolas",
font_size: 36,
font_color: "#40FFFF",
align: center,
bold: true,
animation: "wipe",
animation_direction: "right",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.7
}
T
:::

:::text[x:5.25in, y:7.3in, width:0.7in, height:0.7in]
{
font: "Consolas",
font_size: 36,
font_color: "#80FFFF",
align: center,
bold: true,
animation: "wipe",
animation_direction: "right",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.7
}
R
:::

:::text[x:6.05in, y:7.3in, width:0.7in, height:0.7in]
{
font: "Consolas",
font_size: 36,
font_color: "#00BFFF",
align: center,
bold: true,
animation: "wipe",
animation_direction: "right",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.7
}
I
:::

:::text[x:6.85in, y:7.3in, width:0.7in, height:0.7in]
{
font: "Consolas",
font_size: 36,
font_color: "#40BFFF",
align: center,
bold: true,
animation: "wipe",
animation_direction: "right",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.7
}
N
:::

:::text[x:7.65in, y:7.3in, width:0.7in, height:0.7in]
{
font: "Consolas",
font_size: 36,
font_color: "#80BFFF",
align: center,
bold: true,
animation: "wipe",
animation_direction: "right",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.7
}
G
:::

# What Exactly ARE Strings?

{
background: "#1A1A1A",
transition: "split",
transition_speed: "medium",
transition_direction: "horizontal_out"
}

:::text[x:1in, y:0.8in, width:10in, height:1in]
{
font: "Segoe UI Light",
font_size: 40,
font_color: "#00FFFF",
bold: true,
animation: "split",
animation_direction: "horizontal_out",
animation_trigger: "on_click",
animation_duration: 1.0
}
What Exactly ARE Strings?
:::

:::text[x:1in, y:2in, width:10in, height:0.8in]
{
font: "Segoe UI",
font_size: 20,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.7
}
At their core, strings are sequences of characters. But in C++, there are two main ways to represent them:
:::

:::shape[x:1in, y:3in, width:5.5in, height:5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1pt,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_duration: 0.8
}
:::

:::text[x:1.25in, y:3.2in, width:5in, height:0.7in]
{
font: "Segoe UI",
font_size: 22,
font_color: "#00FFFF",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}

1. C-style Strings (char arrays)
   :::

:::text[x:1.25in, y:4in, width:5in, height:0.6in]
{
font: "Consolas",
font_size: 16,
font_color: "#03DAC6",
background: "#252525",
animation: "appear",
animation_trigger: "after_previous",
animation_duration: 0.5
}
char greeting[] = "Hello"; // Compiler adds null terminator '\0'
:::

:::shape[x:2in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:2.15in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
H
:::

:::shape[x:2.65in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:2.8in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
e
:::

:::shape[x:3.3in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:3.45in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
l
:::

:::shape[x:3.95in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:4.1in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
l
:::

:::shape[x:4.6in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:4.75in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
o
:::

:::shape[x:5.25in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:5.4in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FF7597",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
\0
:::

:::text[x:1.25in, y:5.6in, width:5in, height:0.4in]
{
font: "Segoe UI",
font_size: 14,
font_color: "#E0E0E0",
font_style: "italic",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
That \0 at the end is the null terminator - it tells functions where the string ends.
:::

:::shape[x:7.5in, y:3in, width:5.5in, height:5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "wipe",
animation_direction: "right",
animation_trigger: "after_previous",
animation_duration: 0.8
}
:::

:::text[x:7.75in, y:3.2in, width:5in, height:0.7in]
{
font: "Segoe UI",
font_size: 22,
font_color: "#BB86FC",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
} 2. C++ std::string
:::

:::text[x:7.75in, y:4in, width:5in, height:0.6in]
{
font: "Consolas",
font_size: 16,
font_color: "#03DAC6",
background: "#252525",
animation: "appear",
animation_trigger: "after_previous",
animation_duration: 0.5
}
std::string greeting = "Hello";
:::

:::text[x:7.75in, y:4.8in, width:5in, height:2.5in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
Under the hood, std::string is a class that manages:
• A dynamically allocated character array
• Size tracking
• Memory management
• Various utility methods
:::

:::text[x:1in, y:8.3in, width:10in, height:0.6in]
{
font: "Segoe UI",
font*size: 16,
font_color: "#E0E0E0",
font_style: "italic",
animation: "float_in",
animation_direction: "up",
animation_trigger: "after_previous",
animation_delay: 0.5,
animation_duration: 1.0
}
\_If C-style strings are a manual typewriter, std::string is a modern word processor with spell-check, auto-save, and therapy built in.*
:::

# String Memory Layout

{
background: "#1A1A1A",
transition: "fade",
transition_speed: "medium"
}

:::text[x:1in, y:0.8in, width:10in, height:1in]
{
font: "Segoe UI Light",
font_size: 40,
font_color: "#00FFFF",
bold: true,
animation: "fade",
animation_trigger: "on_click",
animation_duration: 0.7
}
String Memory Layout
:::

:::text[x:1in, y:2in, width:5in, height:0.7in]
{
font: "Segoe UI",
font_size: 24,
font_color: "#00FFFF",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
C-style String Memory:
:::

:::text[x:1in, y:2.8in, width:5in, height:2.5in]
{
font: "Segoe UI",
font_size: 18,
font_color: "#E0E0E0",
animation: "appear",
animation_trigger: "after_previous",
animation_duration: 0.7
}
• Fixed size determined at declaration
• Contiguous memory
• Relies on null terminator to determine end
• Prone to buffer overflows
:::

:::shape[x:1.5in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:1.65in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_duration: 0.3
}
H
:::

:::shape[x:2.15in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:2.3in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
e
:::

:::shape[x:2.8in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:2.95in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
l
:::

:::shape[x:3.45in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:3.6in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
l
:::

:::shape[x:4.1in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:4.25in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
o
:::

:::shape[x:4.75in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1.5pt,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#FF7597",
align: center,
animation: "wipe",
animation_direction: "left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.3
}
\0
:::

:::shape[x:5.4in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#F44336",
border_width: 1.5pt,
animation: "transparency",
animation_trigger: "on_click",
animation_duration: 0.8
}
:::

:::text[x:5.55in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#F44336",
align: center,
animation: "transparency",
animation_trigger: "on_click",
animation_duration: 0.8
}
X
:::

:::shape[x:6.05in, y:5in, width:0.6in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#F44336",
border_width: 1.5pt,
animation: "transparency",
animation_trigger: "on_click",
animation_duration: 0.8
}
:::

:::text[x:6.2in, y:5.1in, width:0.3in, height:0.3in]
{
font: "Consolas",
font_size: 16,
font_color: "#F44336",
align: center,
animation: "transparency",
animation_trigger: "on_click",
animation_duration: 0.8
}
Y
:::

:::text[x:1.5in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x100
:::

:::text[x:2.15in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x101
:::

:::text[x:2.8in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x102
:::

:::text[x:3.45in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x103
:::

:::text[x:4.1in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x104
:::

:::text[x:4.75in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x105
:::

:::text[x:5.4in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x106
:::

:::text[x:6.05in, y:5.6in, width:0.6in, height:0.3in]
{
font: "Consolas",
font_size: 10,
font_color: "#808080",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
0x107
:::

:::text[x:7in, y:2in, width:5in, height:0.7in]
{
font: "Segoe UI",
font_size: 24,
font_color: "#BB86FC",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
std::string Memory:
:::

:::text[x:7in, y:2.8in, width:5in, height:2.5in]
{
font: "Segoe UI",
font_size: 18,
font_color: "#E0E0E0",
animation: "appear",
animation_trigger: "after_previous",
animation_duration: 0.7
}
• Often uses Small String Optimization (SSO)
• Small strings (<15 chars) stored directly in object
• Larger strings stored in dynamically allocated memory
• Tracks both size and capacity
:::

:::shape[x:8in, y:5in, width:2.5in, height:1.2in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 2pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.8
}
:::

:::text[x:8.1in, y:5.1in, width:2in, height:0.3in]
{
font: "Segoe UI",
font_size: 12,
font_color: "#BB86FC",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
String Object
:::

:::shape[x:8.15in, y:5.5in, width:0.3in, height:0.3in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
:::

:::text[x:8.2in, y:5.55in, width:0.2in, height:0.2in]
{
font: "Consolas",
font_size: 12,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
H
:::

:::shape[x:8.5in, y:5.5in, width:0.3in, height:0.3in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
:::

:::text[x:8.55in, y:5.55in, width:0.2in, height:0.2in]
{
font: "Consolas",
font_size: 12,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
e
:::

:::shape[x:8.85in, y:5.5in, width:0.3in, height:0.3in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:5.55in, width:0.2in, height:0.2in]
{
font: "Consolas",
font_size: 12,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
l
:::

:::shape[x:9.2in, y:5.5in, width:0.3in, height:0.3in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
:::

:::text[x:9.25in, y:5.55in, width:0.2in, height:0.2in]
{
font: "Consolas",
font_size: 12,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
l
:::

:::shape[x:9.55in, y:5.5in, width:0.3in, height:0.3in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
:::

:::text[x:9.6in, y:5.55in, width:0.2in, height:0.2in]
{
font: "Consolas",
font_size: 12,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
o
:::

:::shape[x:9.9in, y:5.5in, width:0.3in, height:0.3in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
:::

:::text[x:9.95in, y:5.55in, width:0.2in, height:0.2in]
{
font: "Consolas",
font_size: 12,
font_color: "#FF7597",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_delay: 0.2,
animation_duration: 0.3
}
\0
:::

:::text[x:0.5in, y:8.3in, width:12in, height:0.7in]
{
font: "Segoe UI",
font*size: 16,
font_color: "#E0E0E0",
font_style: "italic",
animation: "float_in",
animation_direction: "up",
animation_trigger: "after_previous",
animation_duration: 0.8
}
\_Small String Optimization is like keeping a small shopping list in your pocket vs. having to go home to get your big shopping list from the fridge.*
:::

# String Operations & Complexity

{
background: "#1A1A1A",
transition: "fade",
transition_speed: "medium"
}

:::text[x:1in, y:0.8in, width:10in, height:1in]
{
font: "Segoe UI Light",
font_size: 40,
font_color: "#00FFFF",
bold: true,
animation: "fade",
animation_trigger: "on_click",
animation_duration: 0.7
}
String Operations & Complexity
:::

:::shape[x:0.5in, y:2in, width:12in, height:0.7in]
{
shape_type: "rectangle",
fill: "#3D3D3D",
animation: "wipe",
animation_direction: "from_top",
animation_trigger: "after_previous",
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:2.1in, width:4in, height:0.5in]
{
font: "Segoe UI",
font_size: 20,
font_color: "#FFFFFF",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Operation
:::

:::text[x:4.6in, y:2.1in, width:4in, height:0.5in]
{
font: "Segoe UI",
font_size: 20,
font_color: "#00FFFF",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
C-style
:::

:::text[x:8.6in, y:2.1in, width:4in, height:0.5in]
{
font: "Segoe UI",
font_size: 20,
font_color: "#BB86FC",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
std::string
:::

:::shape[x:0.5in, y:2.7in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:2.8in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Create
:::

:::shape[x:4.8in, y:2.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#FFC107",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:2.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n)
:::

:::shape[x:8.8in, y:2.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#FFC107",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:2.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n)
:::

:::shape[x:0.5in, y:3.2in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#333333",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:3.3in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Length
:::

:::shape[x:4.8in, y:3.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#FFC107",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:3.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n)
:::

:::shape[x:8.8in, y:3.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#4CAF50",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:3.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(1)
:::

:::shape[x:0.5in, y:3.7in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:3.8in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Concatenate
:::

:::shape[x:4.8in, y:3.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:3.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n+m)
:::

:::shape[x:8.8in, y:3.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:3.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n+m)
:::

:::shape[x:0.5in, y:4.2in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#333333",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:4.3in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Compare
:::

:::shape[x:4.8in, y:4.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#FFC107",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:4.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n)
:::

:::shape[x:8.8in, y:4.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#FFC107",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:4.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n)
:::

:::shape[x:0.5in, y:4.7in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:4.8in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Access
:::

:::shape[x:4.8in, y:4.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#4CAF50",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:4.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(1)
:::

:::shape[x:8.8in, y:4.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#4CAF50",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:4.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#000000",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(1)
:::

:::shape[x:0.5in, y:5.2in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#333333",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:5.3in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Find
:::

:::shape[x:4.8in, y:5.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:5.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n\*m)
:::

:::shape[x:8.8in, y:5.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:5.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n\*m)
:::

:::shape[x:0.5in, y:5.7in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:5.8in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Insert
:::

:::shape[x:4.8in, y:5.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:5.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n+m)
:::

:::shape[x:8.8in, y:5.77in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:5.83in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n+m)
:::

:::shape[x:0.5in, y:6.2in, width:12in, height:0.5in]
{
shape_type: "rectangle",
fill: "#333333",
animation: "wipe",
animation_direction: "from_left",
animation_trigger: "after_previous",
animation_delay: 0.1,
animation_duration: 0.5
}
:::

:::text[x:0.6in, y:6.3in, width:4in, height:0.3in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#E0E0E0",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
Erase
:::

:::shape[x:4.8in, y:6.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:4.9in, y:6.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n)
:::

:::shape[x:8.8in, y:6.27in, width:0.8in, height:0.35in]
{
shape_type: "rounded_rectangle",
fill: "#F44336",
radius: 3,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.9in, y:6.33in, width:0.6in, height:0.25in]
{
font: "Segoe UI",
font_size: 16,
font_color: "#FFFFFF",
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
O(n)
:::

:::text[x:0.5in, y:8.3in, width:12in, height:0.7in]
{
font: "Segoe UI",
font*size: 16,
font_color: "#E0E0E0",
font_style: "italic",
animation: "float_in",
animation_direction: "up",
animation_trigger: "after_previous",
animation_duration: 0.8
}
\_A programmer's evolution: First you love strings, then you hate them, then you understand them, and finally you accept that they'll always be a source of bugs regardless.*
:::

# String Manipulation Techniques

{
background: "#1A1A1A",
transition: "fade",
transition_speed: "medium"
}

:::text[x:1in, y:0.8in, width:10in, height:1in]
{
font: "Segoe UI Light",
font_size: 40,
font_color: "#00FFFF",
bold: true,
animation: "fade",
animation_trigger: "on_click",
animation_duration: 0.7
}
String Manipulation Techniques
:::

:::text[x:1in, y:2in, width:12in, height:0.7in]
{
font: "Segoe UI",
font_size: 28,
font_color: "#03DAC6",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}

1. String Traversal
   :::

:::shape[x:1in, y:2.8in, width:5.5in, height:2.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#00FFFF",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
:::

:::text[x:1.2in, y:3in, width:5in, height:0.3in]
{
font: "Segoe UI",
font_size: 18,
font_color: "#00FFFF",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
For C-style strings:
:::

:::text[x:1.2in, y:3.4in, width:5in, height:1.8in]
{
font: "Consolas",
font_size: 14,
font_color: "#03DAC6",
background: "#252525",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
char str[] = "Hello";
for (int i = 0; str[i] != '\0'; i++) {
char c = str[i];
// Process character c
}
:::

:::shape[x:7in, y:2.8in, width:5.5in, height:2.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
:::

:::text[x:7.2in, y:3in, width:5in, height:0.3in]
{
font: "Segoe UI",
font_size: 18,
font_color: "#BB86FC",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
For std::string:
:::

:::text[x:7.2in, y:3.4in, width:5in, height:1.8in]
{
font: "Consolas",
font_size: 14,
font_color: "#03DAC6",
background: "#252525",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
std::string str = "Hello";
for (char c : str) {
// Process character c
}
:::

:::shape[x:4.95in, y:5.5in, width:0.7in, height:0.7in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#03DAC6",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:5.1in, y:5.6in, width:0.4in, height:0.5in]
{
font: "Consolas",
font_size: 24,
font_color: "#FFFFFF",
bold: true,
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
H
:::

:::shape[x:5.75in, y:5.5in, width:0.7in, height:0.7in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#03DAC6",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:5.9in, y:5.6in, width:0.4in, height:0.5in]
{
font: "Consolas",
font_size: 24,
font_color: "#FFFFFF",
bold: true,
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
e
:::

:::shape[x:6.55in, y:5.5in, width:0.7in, height:0.7in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#03DAC6",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:6.7in, y:5.6in, width:0.4in, height:0.5in]
{
font: "Consolas",
font_size: 24,
font_color: "#FFFFFF",
bold: true,
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
l
:::

:::shape[x:7.35in, y:5.5in, width:0.7in, height:0.7in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#03DAC6",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:7.5in, y:5.6in, width:0.4in, height:0.5in]
{
font: "Consolas",
font_size: 24,
font_color: "#FFFFFF",
bold: true,
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
l
:::

:::shape[x:8.15in, y:5.5in, width:0.7in, height:0.7in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#03DAC6",
border_width: 1.5pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
:::

:::text[x:8.3in, y:5.6in, width:0.4in, height:0.5in]
{
font: "Consolas",
font_size: 24,
font_color: "#FFFFFF",
bold: true,
align: center,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.3
}
o
:::

:::text[x:1in, y:6.3in, width:12in, height:0.7in]
{
font: "Segoe UI",
font_size: 28,
font_color: "#03DAC6",
bold: true,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
} 2. String Transformation
:::

:::shape[x:1in, y:7in, width:5.5in, height:1.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
:::

:::text[x:1.2in, y:7.2in, width:5in, height:1.2in]
{
font: "Consolas",
font_size: 14,
font_color: "#03DAC6",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
std::string str = "Hello";
std::transform(str.begin(), str.end(),
str.begin(), ::toupper);
// Result: "HELLO"
:::

:::shape[x:7in, y:7in, width:5.5in, height:1.5in]
{
shape_type: "rectangle",
fill: "#2D2D2D",
border_color: "#BB86FC",
border_width: 1pt,
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
:::

:::text[x:7.2in, y:7.2in, width:5in, height:1.2in]
{
font: "Consolas",
font_size: 14,
font_color: "#03DAC6",
animation: "fade",
animation_trigger: "after_previous",
animation_duration: 0.5
}
std::string str = "Hello World";
std::string sub = str.substr(6, 5);
// Result: "World"
:::
