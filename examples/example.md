# Title Slide

<!-- theme: professional -->
<!-- transition: fade -->

🚀 STRINGS IN C++

Arrays With Character(s)

#DSAin45 - Day 4

# What Exactly ARE Strings?

<!-- slide: transition=wipe, direction=left -->

At their core, strings are sequences of characters. But in C++, there are two main ways to represent them:

## 1. C-style Strings (char arrays)

```cpp
char greeting[] = "Hello"; // Compiler adds null terminator '\0'
```

That \0 at the end is the null terminator - it tells functions where the string ends.

## 2. C++ std::string

```cpp
std::string greeting = "Hello";
```

Under the hood, std::string is a class that manages:

- A dynamically allocated character array
- Size tracking
- Memory management
- Various utility methods

> _If C-style strings are a manual typewriter, std::string is a modern word processor with spell-check, auto-save, and therapy built in._

# String Memory Layout

<!-- slide: transition=fade -->

## C-style String Memory

- Fixed size determined at declaration
- Contiguous memory
- Relies on null terminator to determine end
- Prone to buffer overflows

Memory representation of "Hello":
H | e | l | l | o | \0

## std::string Memory

- Often uses Small String Optimization (SSO)
- Small strings (<15 chars) stored directly in object
- Larger strings stored in dynamically allocated memory
- Tracks both size and capacity

> _Small String Optimization is like keeping a small shopping list in your pocket vs. having to go home to get your big shopping list from the fridge._

# String Operations & Complexity

<!-- slide: transition=zoom -->

| Operation   | C-style | std::string | Notes                        |
| ----------- | ------- | ----------- | ---------------------------- |
| Create      | O(n)    | O(n)        | Both copy characters         |
| Length      | O(n)    | O(1)        | std::string caches length    |
| Concatenate | O(n+m)  | O(n+m)      | Both require copying         |
| Compare     | O(n)    | O(n)        | Character-by-character       |
| Access      | O(1)    | O(1)        | Direct indexing              |
| Find        | O(n\*m) | O(n\*m)     | Naive search                 |
| Insert      | O(n)    | O(n)        | Requires shifting characters |
| Erase       | O(n)    | O(n)        | Requires shifting characters |

> _A programmer's evolution: First you love strings, then you hate them, then you understand them, and finally you accept that they'll always be a source of bugs regardless._

# String Manipulation Techniques

<!-- slide: transition=fade, background_color=lightblue -->

## 1. String Traversal

For C-style strings:

```cpp
char str[] = "Hello";
for (int i = 0; str[i] != '\0'; i++) {
    char c = str[i];
    // Process character c
}
```

For std::string:

```cpp
std::string str = "Hello";
for (char c : str) {
    // Process character c
}
```

## 2. String Transformation

Case conversion:

```cpp
std::string str = "Hello";
std::transform(str.begin(), str.end(),
              str.begin(), ::toupper);
// Result: "HELLO"
```

Substring extraction:

```cpp
std::string str = "Hello World";
std::string sub = str.substr(6, 5);
// Result: "World"
```

# Common String Operations

<!-- slide: transition=wipe, direction=right -->

## String Concatenation

C-style (using strcat):

```cpp
char str1[20] = "Hello";
char str2[] = " World";
strcat(str1, str2);  // str1 becomes "Hello World"
```

std::string:

```cpp
std::string str1 = "Hello";
std::string str2 = " World";
std::string result = str1 + str2;  // "Hello World"
```

## String Comparison

C-style (using strcmp):

```cpp
char str1[] = "Hello";
char str2[] = "World";
if (strcmp(str1, str2) < 0) {
    // str1 comes before str2 lexicographically
}
```

std::string:

```cpp
std::string str1 = "Hello";
std::string str2 = "World";
if (str1 < str2) {
    // str1 comes before str2 lexicographically
}
```

# Best Practices

<!-- slide: transition=fade -->

- Use std::string by default
- Only use C-style strings when interfacing with C APIs
- Be careful with string literals vs. string objects
- Always check string bounds before accessing
- For performance-critical code, consider string_view (C++17)
- Remember that strings are mutable in C++

> _"Always use std::string unless you have a very compelling reason not to. Your future self will thank you."_
