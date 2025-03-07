from src.helper import load_pdf_file,text_split,download_hugging_face_embedding
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os


load_dotenv()


# Load environment variables
PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY
# OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

extra_data = load_pdf_file(data='Data/')
text_chunk=text_split(extra_data)
embeddings=download_hugging_face_embedding()

pc = Pinecone(api_key=PINECONE_API_KEY)

# Create a new index
index_name ="bot"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1",
    )

)

#embedding each chunk and upsert the embeddedings into ur pinecone index
docsearch= PineconeVectorStore.from_documents(
    documents=text_chunk,
    index_name=index_name,
    embedding=embeddings,
)