# Troubleshooting Guide

This guide helps you identify and resolve common issues when using the PowerPoint Automation tool.

## Table of Contents

- [YAML Validation Errors](#yaml-validation-errors)
- [Missing Files and Resources](#missing-files-and-resources)
- [PowerPoint Generation Errors](#powerpoint-generation-errors)
- [Element-Specific Issues](#element-specific-issues)
- [Performance and Optimization](#performance-and-optimization)
- [Common Error Messages](#common-error-messages)

## YAML Validation Errors

### Invalid YAML Syntax

**Problem**: Your YAML file fails validation with syntax errors.

**Solution**:

- Use the `--validate-only` flag to check your YAML without generating a presentation
- Check for common YAML syntax issues:
  - Indentation must be consistent (typically 2 spaces)
  - Lists must use consistent formatting (all items use same `-` prefix)
  - Quotes may be needed for strings with special characters
  - Multi-line strings should use the pipe character (`|`)
- Use a YAML linter or validator tool (e.g., [yamllint.com](https://www.yamllint.com/))

**Example Error**:

```
YAML validation failed: YAML parsing error: mapping values are not allowed in this context at line 23, column 12
```

**Fix**:
Check line 23 for misaligned indentation or incorrect list formatting.

### Schema Validation Failures

**Problem**: Your YAML content doesn't match the expected schema.

**Solution**:

- Check the specific error message to identify the problem field
- Refer to the [YAML Reference](yaml_reference.md) for valid values
- Ensure required fields are present for each element type
- Verify data types (e.g., numbers for dimensions, strings for text)

**Example Error**:

```
Schema validation error: 'type' is a required property at slides[2]
```

**Fix**:
Add the missing `type` property to the third slide in your configuration.

## Missing Files and Resources

### Missing Image Files

**Problem**: Images referenced in your YAML file cannot be found.

**Solution**:

- Ensure all image paths are correct and relative to the script execution directory
- Check file extensions (case-sensitive on some operating systems)
- Organize images in a subdirectory and update paths accordingly
- Use the `-v` (verbose) flag to see detailed error messages

**Example Error**:

```
Image not found: images/logo.png
```

**Fix**:

- Verify the image exists at the specified path
- Check if the path should be `./images/logo.png` or `../images/logo.png`
- Ensure the image filename and extension match exactly (including case)

### Template File Not Found

**Problem**: The specified PowerPoint template cannot be found.

**Solution**:

- Check the path to your template file
- Ensure you're using the correct `-t` or `--template` argument
- Verify the template file is a valid .pptx file

**Example Error**:

```
Template file not found: templates/corporate.pptx
```

**Fix**:
Correct the path to the template file or place the template in the expected location.

## PowerPoint Generation Errors

### Slides Not Appearing as Expected

**Problem**: The generated presentation doesn't match your YAML configuration.

**Solution**:

- Check slide types and ensure they're supported
- Verify that required properties for each slide type are present
- Ensure text content isn't exceeding available space
- Check for proper nesting of elements and content

**Example Issue**:
Slide content appears cut off or missing.

**Fix**:

- Increase the dimensions of content containers
- Reduce the amount of content
- Split content across multiple slides

### Font Problems

**Problem**: Specified fonts don't appear in the generated presentation.

**Solution**:

- Ensure the fonts are installed on your system
- Use common fonts that are widely available
- Consider specifying fallback fonts

**Example Issue**:
The specified "Montserrat" font appears as "Calibri" in the output.

**Fix**:
Either install the Montserrat font on your system or use a different installed font.

## Element-Specific Issues

### Table Formatting Issues

**Problem**: Tables don't display data correctly or have formatting problems.

**Solution**:

- Ensure the `data` property is a properly formatted 2D array
- Check that all rows have the same number of columns
- Verify that cell data is properly escaped if it contains special characters
- Check dimensions to ensure the table fits on the slide

**Example Issue**:
Table appears with misaligned columns or missing data.

**Fix**:
Ensure all rows in the `data` array have the same number of elements.

### Chart Generation Problems

**Problem**: Charts don't display correctly or show unexpected data.

**Solution**:

- Verify the `chart_type` is one of the supported types
- Ensure `categories` and `series` data match in length
- Check that all values in series are numeric
- Verify series names are unique

**Example Issue**:
Chart appears but doesn't show any data points.

**Fix**:
Check that the series values are numbers, not strings (e.g., `10` instead of `"10"`).

### Shape Rendering Issues

**Problem**: Shapes don't appear or have incorrect properties.

**Solution**:

- Verify the `shape_type` is supported
- Check dimensions and positioning
- Ensure color values are in valid format
- For shapes with text, make sure the text fits within the shape

**Example Issue**:
A shape with text shows only part of the text content.

**Fix**:
Increase the shape dimensions or reduce the text size/content.

## Performance and Optimization

### Slow Generation Time

**Problem**: Generating presentations takes a long time, especially with many slides.

**Solution**:

- Optimize image sizes (don't use unnecessarily large images)
- Reduce complexity of slides with many elements
- Split very large presentations into multiple files
- Consider using a template with pre-defined layouts

**Example Issue**:
A 50-slide presentation with many images takes several minutes to generate.

**Fix**:
Resize large images to appropriate dimensions before including them.

### Large Output File Size

**Problem**: Generated PowerPoint files are unnecessarily large.

**Solution**:

- Compress images before adding them to presentations
- Use vector shapes instead of raster images where possible
- Avoid duplicating the same image across multiple slides
- Consider using linked rather than embedded media if supported

**Example Issue**:
A presentation with 10 slides is 50MB in size.

**Fix**:
Check for uncompressed high-resolution images and optimize them.

## Common Error Messages

Here are some common error messages you might encounter and how to address them:

### "Error parsing YAML file"

**Cause**: There's a syntax error in your YAML file.

**Solution**: Use a YAML validator to identify and fix syntax issues.

### "Slide layout index X not available"

**Cause**: The requested slide layout doesn't exist in the template.

**Solution**: Check the layout types available in your template or use a different layout type.

### "Image not found: [path]"

**Cause**: An image file referenced in your YAML cannot be found.

**Solution**: Verify the image path and ensure the file exists.

### "Invalid color value: [value]"

**Cause**: A color is specified in an unsupported format.

**Solution**: Use a supported color format (RGB array, hex string, or named color).

### "Chart series values must be numeric"

**Cause**: Non-numeric values are used in chart data.

**Solution**: Ensure all values in chart series are numbers.

### "Element of type [type] not supported"

**Cause**: An unsupported element type is specified.

**Solution**: Check the element type and use one of the supported types from the documentation.

---

If you encounter an issue not covered in this guide, please:

1. Run with the `-v` (verbose) flag for detailed logs
2. Check your YAML with `--validate-only` to isolate validation issues
3. Consult the error message for specific guidance
4. Refer to the [YAML Reference](yaml_reference.md) and [Element Types](element_types.md) documentation
5. If the issue persists, report it with a detailed description and the YAML content
