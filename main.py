import ascii_magic
# place picture file in Quotations
output = ascii_magic.from_image_file("Example.png", columns=200, char="#")

ascii_magic.to_terminal(output)
