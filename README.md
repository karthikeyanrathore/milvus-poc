## How to run poc?
steps

1. first you need to run milvus server. https://milvus.io/docs/install_standalone-docker.md
```bash
bash standalone_embed.sh start
```

2. After service is up. insert mock data.
```bash
./insert_vec_db.py
```

3. search data from vector database.
```bash
./get_vecdata.py
```

## Architecture

```mermaid
graph LR

subgraph search
id3["query: image_path like 'x_subject%' "] --> id4[("milvus vector database")]
id4[("milvus vector database")] --> id5["dict ret / all image embeddings where image path contains x_subject"]
end

subgraph Insertion
x_subject_dir -->|"parse n images"| vggface-model

vggface-model --> |"image embedding"| x_subject_img_1
vggface-model --> |"image embedding"| x_subject_img_2
vggface-model --> |"image embedding"| x_subject_img_3
vggface-model --> |"image embedding"| x_subject_img_n

x_subject_img_1 --> id1[("milvus vector database")]
x_subject_img_2 --> id1[("milvus vector database")]
x_subject_img_3 --> id1[("milvus vector database")]
x_subject_img_n --> id1[("milvus vector database")]

end
```

