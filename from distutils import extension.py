from distutils import extension
from pytesseract import image_to_string
from PIL import Image
import pytesseract

print(pytesseract.image_to_pdf_or_hocr('F:/L2/S2/Work-based Professional Project in Computer Science (I)/New folder/licencePlatesUPDATE/Data Collection/Plates/fd276a0a-303e-495f-9231-df6b47b69274.jpg', lang='ara',extension='hocr'))