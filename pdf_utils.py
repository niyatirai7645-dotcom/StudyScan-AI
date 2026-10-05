import fitz
from PIL import Image


BATCH_SIZE = 10


def get_pdf_page_count(uploaded_pdf):
    """
    Return the number of pages in the uploaded PDF.
    """

    pdf_bytes = uploaded_pdf.getvalue()

    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    try:
        return len(pdf)

    finally:
        pdf.close()


def pdf_to_image_batches(uploaded_pdf, batch_size=BATCH_SIZE):
    """
    Convert a PDF into batches of page images.

    Pages are processed in groups instead of treating the
    entire PDF as one large image collection.
    """

    pdf_bytes = uploaded_pdf.getvalue()

    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    batches = []
    current_batch = []

    try:

        for page in pdf:

            pix = page.get_pixmap(
                dpi=150,
                alpha=False
            )

            image = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            current_batch.append(image)

            if len(current_batch) == batch_size:

                batches.append(current_batch)

                current_batch = []

        # Add remaining pages
        if current_batch:
            batches.append(current_batch)

    finally:

        pdf.close()

    return batches