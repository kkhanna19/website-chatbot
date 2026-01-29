from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text, url, title, chunk_size=500, overlap=100):
    """
    Splits website text into chunks and attaches metadata.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    chunks = splitter.split_text(text)

    documents = []
    for chunk in chunks:
        documents.append({
            "content": chunk,
            "metadata": {
                "source": url,
                "title": title
            }
        })

    return documents
