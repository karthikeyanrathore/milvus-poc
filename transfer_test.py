#!/usr/bin/env python3

# Milvus vector database
MILVUS_HOST =  "127.0.0.1"
MILVUS_PORT = "19530"
MIL_COLLECTION_NAME = "image_mil_poc"

from pymilvus import (
    connections, utility, FieldSchema, CollectionSchema,
    Collection, DataType
)


if __name__ == "__main__":
    connections.connect(
        host=MILVUS_HOST,
        port=MILVUS_PORT,
        timeout=5,
    )
    
    img_mil_col = Collection(MIL_COLLECTION_NAME)

    print(f"[INFO] Number of data present in vector DB: {img_mil_col.num_entities}")