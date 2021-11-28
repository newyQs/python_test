import minio

minio_conf = {
    'endpoint': '0.0.0.0:9000',
    'access_key': 'admin',
    'secret_key': '123456',
    'secure': False
}


def up_data_minio(bucket: str):
    client = minio.Minio(**minio_conf)
    client.fput_object(bucket_name=bucket, object_name='test2',
                       file_path='test.zip',
                       content_type='application/zip'
                       )


up_data_minio('test')
