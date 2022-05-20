import minio

minio_conf = {
    'endpoint': '10.251.210.122:9000',
    'access_key': 'admin',
    'secret_key': '12345678',
    'secure': False
}


def load_data_minio(bucket: str):
    client = minio.Minio(**minio_conf)
    if not client.bucket_exists(bucket):
        return None
    data = client.get_object(bucket, 'test2')
    path = "receive.zip"
    with open(path, 'wb') as file_data:
        for d in data.stream(32 * 1024):
            file_data.write(d)
    return data.data


print(type(load_data_minio("test")))
