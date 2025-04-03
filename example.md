---
slide_width: 10in
slide_height: 5.625in
default_font: "Calibri"
default_font_size: 18
---

# 🚀 STRINGS IN C++

{
layout: "Title Slide",
background: "#1A1A1A"
}

:::text
{x:2in, y:1.5in, width:6in, height:1.5in, font:"Segoe UI Light", font_size:48, font_color:"#00FFFF", align:center, bold:true, animation:"fade", animation_duration:1.5}
🚀 STRINGS IN C++
:::

:::text
{x:2in, y:3in, width:6in, height:0.8in, font:"Segoe UI", font_size:32, font_color:"#BB86FC", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:1.0}
Arrays With Character(s)
:::

:::text
{x:3.5in, y:4in, width:3in, height:0.5in, font:"Segoe UI", font_size:18, font_color:"#E0E0E0", align:center, animation:"appear", animation_trigger:"after_previous"}
#DSAin45 - Day 4
:::

:::text
{x:2.75in, y:4.5in, width:0.5in, height:0.5in, font:"Consolas", font_size:36, font_color:"#00FFFF", align:center, bold:true, animation:"wipe", animation_direction:"right", animation_duration:0.7}
S
:::

:::text
{x:3.25in, y:4.5in, width:0.5in, height:0.5in, font:"Consolas", font_size:36, font_color:"#40FFFF", align:center, bold:true, animation:"wipe", animation_trigger:"after_previous", animation_direction:"right", animation_duration:0.7}
T
:::

:::text
{x:3.75in, y:4.5in, width:0.5in, height:0.5in, font:"Consolas", font_size:36, font_color:"#80FFFF", align:center, bold:true, animation:"wipe", animation_trigger:"after_previous", animation_direction:"right", animation_duration:0.7}
R
:::

:::text
{x:4.25in, y:4.5in, width:0.5in, height:0.5in, font:"Consolas", font_size:36, font_color:"#00BFFF", align:center, bold:true, animation:"wipe", animation_trigger:"after_previous", animation_direction:"right", animation_duration:0.7}
I
:::

:::text
{x:4.75in, y:4.5in, width:0.5in, height:0.5in, font:"Consolas", font_size:36, font_color:"#40BFFF", align:center, bold:true, animation:"wipe", animation_trigger:"after_previous", animation_direction:"right", animation_duration:0.7}
N
:::

:::text
{x:5.25in, y:4.5in, width:0.5in, height:0.5in, font:"Consolas", font_size:36, font_color:"#80BFFF", align:center, bold:true, animation:"wipe", animation_trigger:"after_previous", animation_direction:"right", animation_duration:0.7}
G
:::

# What Exactly ARE Strings?

{
background: "#1A1A1A"
}

:::text
{x:0.5in, y:0.5in, width:9in, height:0.8in, font:"Segoe UI Light", font_size:36, font_color:"#00FFFF", bold:true, animation:"fade", animation_duration:1.0}
What Exactly ARE Strings?
:::

:::text
{x:0.5in, y:1.4in, width:9in, height:0.6in, font:"Segoe UI", font_size:20, font_color:"#E0E0E0", animation:"fade", animation_trigger:"after_previous", animation_duration:0.7}
At their core, strings are sequences of characters. But in C++, there are two main ways to represent them:
:::

:::shape
{x:0.5in, y:2.2in, width:4.4in, height:3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1pt, animation:"wipe", animation_trigger:"after_previous", animation_direction:"left", animation_duration:0.8}
:::

:::text
{x:0.75in, y:2.4in, width:4in, height:0.5in, font:"Segoe UI", font_size:20, font_color:"#00FFFF", bold:true, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}

1. C-style Strings (char arrays)
   :::

:::text
{x:0.75in, y:3in, width:4in, height:0.5in, font:"Consolas", font_size:16, font_color:"#03DAC6", background:"#252525", animation:"appear", animation_trigger:"after_previous", animation_duration:0.5}
char greeting[] = "Hello"; // Adds '\0'
:::

:::text
{x:0.75in, y:3.6in, width:4in, height:1.2in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0", animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
• Fixed size determined at declaration
• Contiguous memory
• Relies on null terminator '\0' to determine end
• Prone to buffer overflows
:::

:::shape
{x:5.1in, y:2.2in, width:4.4in, height:3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt, animation:"wipe", animation_trigger:"after_previous", animation_direction:"right", animation_duration:0.8}
:::

:::text
{x:5.35in, y:2.4in, width:4in, height:0.5in, font:"Segoe UI", font_size:20, font_color:"#BB86FC", bold:true, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5} 2. C++ std::string
:::

:::text
{x:5.35in, y:3in, width:4in, height:0.5in, font:"Consolas", font_size:16, font_color:"#03DAC6", background:"#252525", animation:"appear", animation_trigger:"after_previous", animation_duration:0.5}
std::string greeting = "Hello";
:::

:::text
{x:5.35in, y:3.6in, width:4in, height:1.8in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0", animation:"fade", animation_trigger:"after_previous", animation_duration:0.7}
Under the hood, std::string is a class that manages:
• A dynamically allocated character array
• Size tracking
• Memory management
• Various utility methods
:::

# String Memory Layout

{
background: "#1A1A1A"
}

:::text
{x:0.5in, y:0.5in, width:9in, height:0.8in, font:"Segoe UI Light", font_size:36, font_color:"#00FFFF", bold:true, animation:"fade", animation_duration:0.7}
String Memory Layout
:::

:::text
{x:0.5in, y:1.4in, width:4.5in, height:0.5in, font:"Segoe UI", font_size:22, font_color:"#00FFFF", bold:true, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
C-style String Memory:
:::

:::text
{x:0.5in, y:2in, width:4.5in, height:1.8in, font:"Segoe UI", font_size:18, font_color:"#E0E0E0", animation:"appear", animation_trigger:"after_previous", animation_duration:0.7}
• Fixed size determined at declaration
• Contiguous memory
• Relies on null terminator to determine end
• Prone to buffer overflows
:::

:::shape
{x:0.8in, y:3.8in, width:0.5in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt, animation:"wipe", animation_trigger:"after_previous", animation_duration:0.3, animation_direction:"left"}
:::

:::text
{x:0.93in, y:3.95in, width:0.25in, height:0.25in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.3}
H
:::

:::shape
{x:1.4in, y:3.8in, width:0.5in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt, animation:"wipe", animation_trigger:"after_previous", animation_duration:0.3, animation_direction:"left", animation_delay:0.1}
:::

:::text
{x:1.53in, y:3.95in, width:0.25in, height:0.25in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.3, animation_delay:0.1}
e
:::

:::shape
{x:2in, y:3.8in, width:0.5in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt, animation:"wipe", animation_trigger:"after_previous", animation_duration:0.3, animation_direction:"left", animation_delay:0.1}
:::

:::text
{x:2.13in, y:3.95in, width:0.25in, height:0.25in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.3, animation_delay:0.1}
l
:::

:::shape
{x:2.6in, y:3.8in, width:0.5in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt, animation:"wipe", animation_trigger:"after_previous", animation_duration:0.3, animation_direction:"left", animation_delay:0.1}
:::

:::text
{x:2.73in, y:3.95in, width:0.25in, height:0.25in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.3, animation_delay:0.1}
l
:::

:::shape
{x:3.2in, y:3.8in, width:0.5in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt, animation:"wipe", animation_trigger:"after_previous", animation_duration:0.3, animation_direction:"left", animation_delay:0.1}
:::

:::text
{x:3.33in, y:3.95in, width:0.25in, height:0.25in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.3, animation_delay:0.1}
o
:::

:::shape
{x:3.8in, y:3.8in, width:0.5in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt, animation:"wipe", animation_trigger:"after_previous", animation_duration:0.3, animation_direction:"left", animation_delay:0.1}
:::

:::text
{x:3.93in, y:3.95in, width:0.25in, height:0.25in, font:"Consolas", font_size:16, font_color:"#FF7597", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.3, animation_delay:0.1}
\0
:::

:::text
{x:0.8in, y:4.4in, width:0.5in, height:0.25in, font:"Consolas", font_size:10, font_color:"#808080", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
0x100
:::

:::text
{x:1.4in, y:4.4in, width:0.5in, height:0.25in, font:"Consolas", font_size:10, font_color:"#808080", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
0x101
:::

:::text
{x:2in, y:4.4in, width:0.5in, height:0.25in, font:"Consolas", font_size:10, font_color:"#808080", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
0x102
:::

:::text
{x:2.6in, y:4.4in, width:0.5in, height:0.25in, font:"Consolas", font_size:10, font_color:"#808080", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
0x103
:::

:::text
{x:3.2in, y:4.4in, width:0.5in, height:0.25in, font:"Consolas", font_size:10, font_color:"#808080", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
0x104
:::

:::text
{x:3.8in, y:4.4in, width:0.5in, height:0.25in, font:"Consolas", font_size:10, font_color:"#808080", align:center, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
0x105
:::

:::text
{x:5in, y:1.4in, width:4.5in, height:0.5in, font:"Segoe UI", font_size:22, font_color:"#BB86FC", bold:true, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
std::string Memory:
:::

:::text
{x:5in, y:2in, width:4.5in, height:1.8in, font:"Segoe UI", font_size:18, font_color:"#E0E0E0", animation:"fade", animation_trigger:"after_previous", animation_duration:0.7}
• Uses Small String Optimization (SSO)
• Small strings (<15 chars) stored in object
• Larger strings in dynamically allocated memory
• Tracks both size and capacity
:::

:::shape
{x:5.5in, y:3.8in, width:2.5in, height:1.2in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:2pt, animation:"fade", animation_trigger:"after_previous", animation_duration:0.7}
:::

:::text
{x:5.6in, y:3.9in, width:2in, height:0.3in, font:"Segoe UI", font_size:12, font_color:"#BB86FC", bold:true, animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
String Object
:::

:::text
{x:5.6in, y:4.25in, width:2.3in, height:0.6in, font:"Consolas", font_size:12, font_color:"#FFFFFF", animation:"fade", animation_trigger:"after_previous", animation_duration:0.5}
H e l l o \0
:::

# String Operations & Complexity

{
background: "#1A1A1A"
}

:::text
{x:0.5in, y:0.5in, width:9in, height:0.8in, font:"Segoe UI Light", font_size:36, font_color:"#00FFFF", bold:true, animation:"fade", animation_duration:0.7}
String Operations & Complexity
:::

:::shape
{x:0.5in, y:1.5in, width:9in, height:0.7in, shape_type:rectangle, fill:"#3D3D3D", animation:"wipe", animation_trigger:"after_previous", animation_direction:"top", animation_duration:0.5}
:::

:::text
{x:0.7in, y:1.65in, width:3in, height:0.4in, font:"Segoe UI", font_size:20, font_color:"#FFFFFF", bold:true}
Operation
:::

:::text
{x:3.7in, y:1.65in, width:3in, height:0.4in, font:"Segoe UI", font_size:20, font_color:"#00FFFF", bold:true}
C-style
:::

:::text
{x:6.7in, y:1.65in, width:3in, height:0.4in, font:"Segoe UI", font_size:20, font_color:"#BB86FC", bold:true}
std::string
:::

:::shape
{x:0.5in, y:2.2in, width:9in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", animation:"wipe", animation_trigger:"after_previous", animation_direction:"left", animation_duration:0.5}
:::

:::text
{x:0.7in, y:2.3in, width:3in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Create
:::

:::shape
{x:3.7in, y:2.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:3.8in, y:2.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:6.7in, y:2.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:6.8in, y:2.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:0.5in, y:2.7in, width:9in, height:0.5in, shape_type:rectangle, fill:"#333333", animation:"wipe", animation_trigger:"after_previous", animation_direction:"left", animation_duration:0.5, animation_delay:0.1}
:::

:::text
{x:0.7in, y:2.8in, width:3in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Length
:::

:::shape
{x:3.7in, y:2.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:3.8in, y:2.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:6.7in, y:2.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#4CAF50"}
:::

:::text
{x:6.8in, y:2.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(1)
:::

:::shape
{x:0.5in, y:3.2in, width:9in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", animation:"wipe", animation_trigger:"after_previous", animation_direction:"left", animation_duration:0.5, animation_delay:0.1}
:::

:::text
{x:0.7in, y:3.3in, width:3in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Access
:::

:::shape
{x:3.7in, y:3.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#4CAF50"}
:::

:::text
{x:3.8in, y:3.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(1)
:::

:::shape
{x:6.7in, y:3.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#4CAF50"}
:::

:::text
{x:6.8in, y:3.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(1)
:::

:::shape
{x:0.5in, y:3.7in, width:9in, height:0.5in, shape_type:rectangle, fill:"#333333", animation:"wipe", animation_trigger:"after_previous", animation_direction:"left", animation_duration:0.5, animation_delay:0.1}
:::

:::text
{x:0.7in, y:3.8in, width:3in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Find
:::

:::shape
{x:3.7in, y:3.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:3.8in, y:3.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n\*m)
:::

:::shape
{x:6.7in, y:3.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:6.8in, y:3.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n\*m)
:::

:::shape
{x:0.5in, y:4.2in, width:9in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", animation:"wipe", animation_trigger:"after_previous", animation_direction:"left", animation_duration:0.5, animation_delay:0.1}
:::

:::text
{x:0.7in, y:4.3in, width:3in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Concatenate
:::

:::shape
{x:3.7in, y:4.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:3.8in, y:4.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n+m)
:::

:::shape
{x:6.7in, y:4.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:6.8in, y:4.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n+m)
:::

# String Manipulation Techniques

{
background: "#1A1A1A"
}

:::text
{x:0.5in, y:0.5in, width:9in, height:0.8in, font:"Segoe UI Light", font_size:36, font_color:"#00FFFF", bold:true}
String Manipulation Techniques
:::

:::text
{x:0.5in, y:1.4in, width:9in, height:0.5in, font:"Segoe UI", font_size:24, font_color:"#03DAC6", bold:true}

1. String Traversal
   :::

:::shape
{x:0.5in, y:2in, width:4.25in, height:2in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1pt}
:::

:::text
{x:0.7in, y:2.1in, width:4in, height:0.3in, font:"Segoe UI", font_size:18, font_color:"#00FFFF", bold:true}
For C-style strings:
:::

:::text
{x:0.7in, y:2.5in, width:4in, height:1.4in, font:"Consolas", font_size:14, font_color:"#03DAC6", background:"#252525"}
char str[] = "Hello";
for (int i = 0; str[i] != '\0'; i++) {
char c = str[i];
// Process character c
}
:::

:::shape
{x:5.25in, y:2in, width:4.25in, height:2in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:5.45in, y:2.1in, width:4in, height:0.3in, font:"Segoe UI", font_size:18, font_color:"#BB86FC", bold:true}
For std::string:
:::

:::text
{x:5.45in, y:2.5in, width:4in, height:1.4in, font:"Consolas", font_size:14, font_color:"#03DAC6", background:"#252525"}
std::string str = "Hello";
for (char c : str) {
// Process character c
}
:::

:::text
{x:0.5in, y:4.2in, width:9in, height:0.5in, font:"Segoe UI", font_size:24, font_color:"#03DAC6", bold:true} 2. String Transformation
:::

:::shape
{x:0.5in, y:4.8in, width:4.25in, height:1.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:0.7in, y:5in, width:4in, height:1.2in, font:"Consolas", font_size:14, font_color:"#03DAC6"}
std::string str = "Hello";
std::transform(str.begin(), str.end(),
str.begin(), ::toupper);
// Result: "HELLO"
:::

:::shape
{x:5.25in, y:4.8in, width:4.25in, height:1.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:5.45in, y:5in, width:4in, height:1.2in, font:"Consolas", font_size:14, font_color:"#03DAC6"}
std::string str = "Hello World";
std::string sub = str.substr(6, 5);
// Result: "World"
:::
