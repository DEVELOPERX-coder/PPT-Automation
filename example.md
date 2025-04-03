---
slide_width: 13.33in
slide_height: 7.5in
default_font: "Segoe UI"
default_font_size: 18
---

# 🚀 STRINGS IN C++

{
layout: "Title Slide",
background: "#1A1A1A"
}

:::text
{x:3.17in, y:3.5in, width:7in, height:1.5in, font:"Segoe UI Light", font_size:48, font_color:"#00FFFF", align:center, bold:true}
🚀 STRINGS IN C++
:::

:::text
{x:3.67in, y:5.2in, width:6in, height:1in, font:"Segoe UI", font_size:32, font_color:"#BB86FC", align:center}
Arrays With Character(s)
:::

:::text
{x:5.17in, y:6.5in, width:3in, height:0.6in, font:"Segoe UI", font_size:18, font_color:"#E0E0E0", align:center}
#DSAin45 - Day 4
:::

:::text
{x:3.65in, y:7.3in, width:0.7in, height:0.7in, font:"Consolas", font_size:36, font_color:"#00FFFF", align:center, bold:true}
S
:::

:::text
{x:4.45in, y:7.3in, width:0.7in, height:0.7in, font:"Consolas", font_size:36, font_color:"#40FFFF", align:center, bold:true}
T
:::

:::text
{x:5.25in, y:7.3in, width:0.7in, height:0.7in, font:"Consolas", font_size:36, font_color:"#80FFFF", align:center, bold:true}
R
:::

:::text
{x:6.05in, y:7.3in, width:0.7in, height:0.7in, font:"Consolas", font_size:36, font_color:"#00BFFF", align:center, bold:true}
I
:::

:::text
{x:6.85in, y:7.3in, width:0.7in, height:0.7in, font:"Consolas", font_size:36, font_color:"#40BFFF", align:center, bold:true}
N
:::

:::text
{x:7.65in, y:7.3in, width:0.7in, height:0.7in, font:"Consolas", font_size:36, font_color:"#80BFFF", align:center, bold:true}
G
:::

# What Exactly ARE Strings?

{
background: "#1A1A1A"
}

:::text
{x:1in, y:0.8in, width:10in, height:1in, font:"Segoe UI Light", font_size:40, font_color:"#00FFFF", bold:true}
What Exactly ARE Strings?
:::

:::text
{x:1in, y:2in, width:10in, height:0.8in, font:"Segoe UI", font_size:20, font_color:"#E0E0E0"}
At their core, strings are sequences of characters. But in C++, there are two main ways to represent them:
:::

:::shape
{x:1in, y:3in, width:5.5in, height:5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1pt}
:::

:::text
{x:1.25in, y:3.2in, width:5in, height:0.7in, font:"Segoe UI", font_size:22, font_color:"#00FFFF", bold:true}

1. C-style Strings (char arrays)
   :::

:::text
{x:1.25in, y:4in, width:5in, height:0.6in, font:"Consolas", font_size:16, font_color:"#03DAC6", background:"#252525"}
char greeting[] = "Hello"; // Compiler adds null terminator '\0'
:::

:::shape
{x:2in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:2.15in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
H
:::

:::shape
{x:2.65in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:2.8in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
e
:::

:::shape
{x:3.3in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:3.45in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
l
:::

:::shape
{x:3.95in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:4.1in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
l
:::

:::shape
{x:4.6in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:4.75in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
o
:::

:::shape
{x:5.25in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:5.4in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FF7597", align:center}
\0
:::

:::text
{x:1.25in, y:5.6in, width:5in, height:0.4in, font:"Segoe UI", font_size:14, font_color:"#E0E0E0", italic:true}
That \0 at the end is the null terminator - it tells functions where the string ends.
:::

:::shape
{x:7.5in, y:3in, width:5.5in, height:5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:7.75in, y:3.2in, width:5in, height:0.7in, font:"Segoe UI", font_size:22, font_color:"#BB86FC", bold:true} 2. C++ std::string
:::

:::text
{x:7.75in, y:4in, width:5in, height:0.6in, font:"Consolas", font_size:16, font_color:"#03DAC6", background:"#252525"}
std::string greeting = "Hello";
:::

:::text
{x:7.75in, y:4.8in, width:5in, height:2.5in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Under the hood, std::string is a class that manages:
• A dynamically allocated character array
• Size tracking
• Memory management
• Various utility methods
:::

:::text
{x:1in, y:8.3in, width:10in, height:0.6in, font:"Segoe UI", font*size:16, font_color:"#E0E0E0", italic:true}
\_If C-style strings are a manual typewriter, std::string is a modern word processor with spell-check, auto-save, and therapy built in.*
:::

# String Memory Layout

{
background: "#1A1A1A"
}

:::text
{x:1in, y:0.8in, width:10in, height:1in, font:"Segoe UI Light", font_size:40, font_color:"#00FFFF", bold:true}
String Memory Layout
:::

:::text
{x:1in, y:2in, width:5in, height:0.7in, font:"Segoe UI", font_size:24, font_color:"#00FFFF", bold:true}
C-style String Memory:
:::

:::text
{x:1in, y:2.8in, width:5in, height:2.5in, font:"Segoe UI", font_size:18, font_color:"#E0E0E0"}
• Fixed size determined at declaration
• Contiguous memory
• Relies on null terminator to determine end
• Prone to buffer overflows
:::

:::shape
{x:1.5in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:1.65in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
H
:::

:::shape
{x:2.15in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:2.3in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
e
:::

:::shape
{x:2.8in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:2.95in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
l
:::

:::shape
{x:3.45in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:3.6in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
l
:::

:::shape
{x:4.1in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:4.25in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FFFFFF", align:center}
o
:::

:::shape
{x:4.75in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1.5pt}
:::

:::text
{x:4.9in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#FF7597", align:center}
\0
:::

:::shape
{x:5.4in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#F44336", border_width:1.5pt}
:::

:::text
{x:5.55in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#F44336", align:center}
X
:::

:::shape
{x:6.05in, y:5in, width:0.6in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#F44336", border_width:1.5pt}
:::

:::text
{x:6.2in, y:5.1in, width:0.3in, height:0.3in, font:"Consolas", font_size:16, font_color:"#F44336", align:center}
Y
:::

:::text
{x:1.5in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x100
:::

:::text
{x:2.15in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x101
:::

:::text
{x:2.8in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x102
:::

:::text
{x:3.45in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x103
:::

:::text
{x:4.1in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x104
:::

:::text
{x:4.75in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x105
:::

:::text
{x:5.4in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x106
:::

:::text
{x:6.05in, y:5.6in, width:0.6in, height:0.3in, font:"Consolas", font_size:10, font_color:"#808080", align:center}
0x107
:::

:::text
{x:7in, y:2in, width:5in, height:0.7in, font:"Segoe UI", font_size:24, font_color:"#BB86FC", bold:true}
std::string Memory:
:::

:::text
{x:7in, y:2.8in, width:5in, height:2.5in, font:"Segoe UI", font_size:18, font_color:"#E0E0E0"}
• Often uses Small String Optimization (SSO)
• Small strings (<15 chars) stored directly in object
• Larger strings stored in dynamically allocated memory
• Tracks both size and capacity
:::

:::shape
{x:8in, y:5in, width:2.5in, height:1.2in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:2pt}
:::

:::text
{x:8.1in, y:5.1in, width:2in, height:0.3in, font:"Segoe UI", font_size:12, font_color:"#BB86FC", bold:true}
String Object
:::

:::shape
{x:8.15in, y:5.5in, width:0.3in, height:0.3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:8.2in, y:5.55in, width:0.2in, height:0.2in, font:"Consolas", font_size:12, font_color:"#FFFFFF", align:center}
H
:::

:::shape
{x:8.5in, y:5.5in, width:0.3in, height:0.3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:8.55in, y:5.55in, width:0.2in, height:0.2in, font:"Consolas", font_size:12, font_color:"#FFFFFF", align:center}
e
:::

:::shape
{x:8.85in, y:5.5in, width:0.3in, height:0.3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:8.9in, y:5.55in, width:0.2in, height:0.2in, font:"Consolas", font_size:12, font_color:"#FFFFFF", align:center}
l
:::

:::shape
{x:9.2in, y:5.5in, width:0.3in, height:0.3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:9.25in, y:5.55in, width:0.2in, height:0.2in, font:"Consolas", font_size:12, font_color:"#FFFFFF", align:center}
l
:::

:::shape
{x:9.55in, y:5.5in, width:0.3in, height:0.3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:9.6in, y:5.55in, width:0.2in, height:0.2in, font:"Consolas", font_size:12, font_color:"#FFFFFF", align:center}
o
:::

:::shape
{x:9.9in, y:5.5in, width:0.3in, height:0.3in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:9.95in, y:5.55in, width:0.2in, height:0.2in, font:"Consolas", font_size:12, font_color:"#FF7597", align:center}
\0
:::

:::text
{x:0.5in, y:8.3in, width:12in, height:0.7in, font:"Segoe UI", font*size:16, font_color:"#E0E0E0", italic:true}
\_Small String Optimization is like keeping a small shopping list in your pocket vs. having to go home to get your big shopping list from the fridge.*
:::

# String Operations & Complexity

{
background: "#1A1A1A"
}

:::text
{x:1in, y:0.8in, width:10in, height:1in, font:"Segoe UI Light", font_size:40, font_color:"#00FFFF", bold:true}
String Operations & Complexity
:::

:::shape
{x:0.5in, y:2in, width:12in, height:0.7in, shape_type:rectangle, fill:"#3D3D3D"}
:::

:::text
{x:0.6in, y:2.1in, width:4in, height:0.5in, font:"Segoe UI", font_size:20, font_color:"#FFFFFF", bold:true}
Operation
:::

:::text
{x:4.6in, y:2.1in, width:4in, height:0.5in, font:"Segoe UI", font_size:20, font_color:"#00FFFF", bold:true}
C-style
:::

:::text
{x:8.6in, y:2.1in, width:4in, height:0.5in, font:"Segoe UI", font_size:20, font_color:"#BB86FC", bold:true}
std::string
:::

:::shape
{x:0.5in, y:2.7in, width:12in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D"}
:::

:::text
{x:0.6in, y:2.8in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Create
:::

:::shape
{x:4.8in, y:2.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:4.9in, y:2.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:8.8in, y:2.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:8.9in, y:2.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:0.5in, y:3.2in, width:12in, height:0.5in, shape_type:rectangle, fill:"#333333"}
:::

:::text
{x:0.6in, y:3.3in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Length
:::

:::shape
{x:4.8in, y:3.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:4.9in, y:3.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:8.8in, y:3.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#4CAF50"}
:::

:::text
{x:8.9in, y:3.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(1)
:::

:::shape
{x:0.5in, y:3.7in, width:12in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D"}
:::

:::text
{x:0.6in, y:3.8in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Concatenate
:::

:::shape
{x:4.8in, y:3.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:4.9in, y:3.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n+m)
:::

:::shape
{x:8.8in, y:3.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:8.9in, y:3.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n+m)
:::

:::shape
{x:0.5in, y:4.2in, width:12in, height:0.5in, shape_type:rectangle, fill:"#333333"}
:::

:::text
{x:0.6in, y:4.3in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Compare
:::

:::shape
{x:4.8in, y:4.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:4.9in, y:4.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:8.8in, y:4.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#FFC107"}
:::

:::text
{x:8.9in, y:4.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(n)
:::

:::shape
{x:0.5in, y:4.7in, width:12in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D"}
:::

:::text
{x:0.6in, y:4.8in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Access
:::

:::shape
{x:4.8in, y:4.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#4CAF50"}
:::

:::text
{x:4.9in, y:4.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(1)
:::

:::shape
{x:8.8in, y:4.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#4CAF50"}
:::

:::text
{x:8.9in, y:4.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#000000", align:center}
O(1)
:::

:::shape
{x:0.5in, y:5.2in, width:12in, height:0.5in, shape_type:rectangle, fill:"#333333"}
:::

:::text
{x:0.6in, y:5.3in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Find
:::

:::shape
{x:4.8in, y:5.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:4.9in, y:5.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n\*m)
:::

:::shape
{x:8.8in, y:5.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:8.9in, y:5.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n\*m)
:::

:::shape
{x:0.5in, y:5.7in, width:12in, height:0.5in, shape_type:rectangle, fill:"#2D2D2D"}
:::

:::text
{x:0.6in, y:5.8in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Insert
:::

:::shape
{x:4.8in, y:5.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:4.9in, y:5.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n+m)
:::

:::shape
{x:8.8in, y:5.77in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:8.9in, y:5.83in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n+m)
:::

:::shape
{x:0.5in, y:6.2in, width:12in, height:0.5in, shape_type:rectangle, fill:"#333333"}
:::

:::text
{x:0.6in, y:6.3in, width:4in, height:0.3in, font:"Segoe UI", font_size:16, font_color:"#E0E0E0"}
Erase
:::

:::shape
{x:4.8in, y:6.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:4.9in, y:6.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n)
:::

:::shape
{x:8.8in, y:6.27in, width:0.8in, height:0.35in, shape_type:rounded_rectangle, fill:"#F44336"}
:::

:::text
{x:8.9in, y:6.33in, width:0.6in, height:0.25in, font:"Segoe UI", font_size:16, font_color:"#FFFFFF", align:center}
O(n)
:::

:::text
{x:0.5in, y:8.3in, width:12in, height:0.7in, font:"Segoe UI", font*size:16, font_color:"#E0E0E0", italic:true}
\_A programmer's evolution: First you love strings, then you hate them, then you understand them, and finally you accept that they'll always be a source of bugs regardless.*
:::

# String Manipulation Techniques

{
background: "#1A1A1A"
}

:::text
{x:1in, y:0.8in, width:10in, height:1in, font:"Segoe UI Light", font_size:40, font_color:"#00FFFF", bold:true}
String Manipulation Techniques
:::

:::text
{x:1in, y:2in, width:12in, height:0.7in, font:"Segoe UI", font_size:28, font_color:"#03DAC6", bold:true}

1. String Traversal
   :::

:::shape
{x:1in, y:2.8in, width:5.5in, height:2.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#00FFFF", border_width:1pt}
:::

:::text
{x:1.2in, y:3in, width:5in, height:0.3in, font:"Segoe UI", font_size:18, font_color:"#00FFFF", bold:true}
For C-style strings:
:::

:::text
{x:1.2in, y:3.4in, width:5in, height:1.8in, font:"Consolas", font_size:14, font_color:"#03DAC6", background:"#252525"}
char str[] = "Hello";
for (int i = 0; str[i] != '\0'; i++) {
char c = str[i];
// Process character c
}
:::

:::shape
{x:7in, y:2.8in, width:5.5in, height:2.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:7.2in, y:3in, width:5in, height:0.3in, font:"Segoe UI", font_size:18, font_color:"#BB86FC", bold:true}
For std::string:
:::

:::text
{x:7.2in, y:3.4in, width:5in, height:1.8in, font:"Consolas", font_size:14, font_color:"#03DAC6", background:"#252525"}
std::string str = "Hello";
for (char c : str) {
// Process character c
}
:::

:::shape
{x:4.95in, y:5.5in, width:0.7in, height:0.7in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#03DAC6", border_width:1.5pt}
:::

:::text
{x:5.1in, y:5.6in, width:0.4in, height:0.5in, font:"Consolas", font_size:24, font_color:"#FFFFFF", bold:true, align:center}
H
:::

:::shape
{x:5.75in, y:5.5in, width:0.7in, height:0.7in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#03DAC6", border_width:1.5pt}
:::

:::text
{x:5.9in, y:5.6in, width:0.4in, height:0.5in, font:"Consolas", font_size:24, font_color:"#FFFFFF", bold:true, align:center}
e
:::

:::shape
{x:6.55in, y:5.5in, width:0.7in, height:0.7in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#03DAC6", border_width:1.5pt}
:::

:::text
{x:6.7in, y:5.6in, width:0.4in, height:0.5in, font:"Consolas", font_size:24, font_color:"#FFFFFF", bold:true, align:center}
l
:::

:::shape
{x:7.35in, y:5.5in, width:0.7in, height:0.7in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#03DAC6", border_width:1.5pt}
:::

:::text
{x:7.5in, y:5.6in, width:0.4in, height:0.5in, font:"Consolas", font_size:24, font_color:"#FFFFFF", bold:true, align:center}
l
:::

:::shape
{x:8.15in, y:5.5in, width:0.7in, height:0.7in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#03DAC6", border_width:1.5pt}
:::

:::text
{x:8.3in, y:5.6in, width:0.4in, height:0.5in, font:"Consolas", font_size:24, font_color:"#FFFFFF", bold:true, align:center}
o
:::

:::text
{x:1in, y:6.3in, width:12in, height:0.7in, font:"Segoe UI", font_size:28, font_color:"#03DAC6", bold:true} 2. String Transformation
:::

:::shape
{x:1in, y:7in, width:5.5in, height:1.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:1.2in, y:7.2in, width:5in, height:1.2in, font:"Consolas", font_size:14, font_color:"#03DAC6"}
std::string str = "Hello";
std::transform(str.begin(), str.end(),
str.begin(), ::toupper);
// Result: "HELLO"
:::

:::shape
{x:7in, y:7in, width:5.5in, height:1.5in, shape_type:rectangle, fill:"#2D2D2D", border_color:"#BB86FC", border_width:1pt}
:::

:::text
{x:7.2in, y:7.2in, width:5in, height:1.2in, font:"Consolas", font_size:14, font_color:"#03DAC6"}
std::string str = "Hello World";
std::string sub = str.substr(6, 5);
// Result: "World"
:::
