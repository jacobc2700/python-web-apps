import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

# Gets the text in the file.
def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text