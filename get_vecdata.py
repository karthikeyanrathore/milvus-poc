#!/usr/bin/env python3

from pymilvus import (
    connections, utility, FieldSchema, CollectionSchema,
    Collection, DataType
)

MILVUS_HOST =  "127.0.0.1"
MILVUS_PORT = "19530"
MIL_COLLECTION_NAME = "image_mil_poc"



if __name__ == "__main__":
    # make connection first
    connections.connect(
        host=MILVUS_HOST,
        port=MILVUS_PORT
    )

    img_mil_col = Collection(MIL_COLLECTION_NAME)

    # print(img_mil_col)

    # print(img_mil_col.name)

    img_mil_col.load()
    ret = img_mil_col.query(expr="image_path like 'lfw/x_subject%' ", output_fields=["image_path", "embeds"])
    # print(ret)
    # print(result)

    print(f"found: {len(ret)}")

    assert (ret[0]["image_path"]) == 'lfw/x_subject/image_1.jpg'
    assert (ret[1]["image_path"]) == 'lfw/x_subject/image_2.jpg'
    assert ret[0]["embeds"] != ret[1]["embeds"] 