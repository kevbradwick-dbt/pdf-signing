from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import signers


signer = signers.SimpleSigner.load_pkcs12(
    pfx_file='keyStore.p12'
)

with open('dummy.pdf', 'rb') as doc:
    w = IncrementalPdfFileWriter(doc)
    out = signers.sign_pdf(
        w, signers.PdfSignatureMetadata(field_name='Signature1'),
        signer=signer,
    )

    with open('dummy-signed.pdf', 'wb') as wb:
        wb.write(out.getbuffer())
