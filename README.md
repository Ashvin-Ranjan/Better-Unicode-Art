# Better Unicode Art

I have sorted all of the Chinese Unicode characters based on how much space they take up. I have also made a program which can convert an 8-bit greyscale image into text (mostly) preserving all 256 colors (some characters are used for multiple greyscale values).

See [Example.md](EXAMPLE.md) for an example.

## Project Breakdown

- [256_characters.txt](256_characters.txt) These are the 256 characters which are closest to the 256 greyscale values
- [better_unicode.py](better_unicode.py) This takes in an `image.png` and prints unicode art which uses the 256 characters
- [density_calculator.html](density_calculator.html) This creates the data for `text_density.json`, in order to run it open it and copy the final output from the console
- [sorted_characters.txt](sorted_characters.txt) These are all of the Chinese characters sorted from least to most bright
- [text_density.json](text_density.json) This is the data for each of the Chinese characters. The number is how many black pixels there are out of `2500`. To get a percent coverage, just divide the number by `2500`

## Other Things
This could be expanded to cover all of unicode, but I am currently too lazy to do that.