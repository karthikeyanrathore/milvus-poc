#!/usr/bin/env python3

from pymilvus import (
    connections, utility, FieldSchema, CollectionSchema,
    Collection, DataType
)
import numpy as np

MILVUS_HOST =  "127.0.0.1"
MILVUS_PORT = "19530"
MIL_COLLECTION_NAME = "image_mil_poc"

# resnet50
MODEL_OUTPUT_DIM = 2048 # d


def milvus_collection():
    if utility.has_collection(MIL_COLLECTION_NAME):
        utility.drop_collection(MIL_COLLECTION_NAME)

    img_path_col = FieldSchema(
        name="image_path", 
        dtype=DataType.VARCHAR,
        description="path to image",
        is_primary=True,
        auto_id=False,
        max_length=535,
    )
    embed_col = FieldSchema(
        name="embeds",
        description="image embeddings output from resnet50 model.",
        dtype=DataType.FLOAT_VECTOR,
        dim=MODEL_OUTPUT_DIM,
    )
    coll_schema = CollectionSchema(fields=[img_path_col, embed_col])
    collect = Collection(name=MIL_COLLECTION_NAME, schema=coll_schema)

    # index
    index_params = {
        "metric_type": 'L2',
        "index_type": 'IVF_FLAT',
        "params": {"nlist": 2048}
    }
    collect.create_index(field_name="embeds", index_params=index_params)
    return collect



if __name__ == "__main__":

    connections.connect(
        host=MILVUS_HOST,
        port=MILVUS_PORT
    )
    
    mil_coll = milvus_collection()
    print(f"[INFO] created collection: {MIL_COLLECTION_NAME}")
    # print(dir(mil_coll)) 

    image_subject = ["lfw/x_subject/image_1.jpg", "lfw/x_subject/image_2.jpg"]

    feature_1 = np.random.rand(MODEL_OUTPUT_DIM)
    feature_2 = np.random.rand(MODEL_OUTPUT_DIM)
    print(feature_1)

    out_features_embeddings= []
    out_features_embeddings.append(feature_1)
    out_features_embeddings.append(feature_2)
    data = [
        image_subject,
        out_features_embeddings
    ]
    mil_coll.insert(data)
    mil_coll.flush()

    assert (mil_coll.is_empty) == False
    print(f"[INFO] Number of data inserted: {mil_coll.num_entities}")


    # ret_search = mil_coll.search(
    #     data=[["x", "u"]],
    #     anns_field="image_path",
    #     param={"metric_type": "L2", "params": {"nprobe": 10}},
    #     limit=10,
    # )
    # print(ret_search)