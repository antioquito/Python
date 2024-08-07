import paramiko
from scp import SCPClient
import gzip
import shutil
import os

def compress_file(local_file_path):
    compressed_file_path = local_file_path + '.gz'
    with open(local_file_path, 'rb') as f_in:
        with gzip.open(compressed_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return compressed_file_path

def decompress_file(local_file_path):
    decompressed_file_path = local_file_path.replace('.gz', '')
    with gzip.open(local_file_path, 'rb') as f_in:
        with open(decompressed_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return decompressed_file_path

def scp_transfer(source_host, source_port, source_username, source_password, source_file_path,
                 dest_host, dest_port, dest_username, dest_password, dest_file_path):
    # Create SSH clients
    source_client = paramiko.SSHClient()
    dest_client = paramiko.SSHClient()

    # Automatically add the source host key (for simplicity, in real scenarios use known_hosts)
    source_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    dest_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the source server
        source_client.connect(source_host, port=source_port, username=source_username, password=source_password)

        # Compress the file on the source server
        sftp_source = source_client.open_sftp()
        local_file_path = '/tmp/temp_file'
        compressed_file_path = compress_file(local_file_path)

        # Download and compress the file from the source server
        sftp_source.get(source_file_path, local_file_path)
        sftp_source.close()
        
        # Connect to the destination server
        dest_client.connect(dest_host, port=dest_port, username=dest_username, password=dest_password)

        # Upload the compressed file to the destination server
        scp = SCPClient(dest_client.get_transport())
        scp.put(compressed_file_path, dest_file_path)
        scp.close()

        print("File transferred and compressed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        source_client.close()
        dest_client.close()
        os.remove(local_file_path)
        os.remove(compressed_file_path)

# Example usage
scp_transfer(
    source_host='source.server.com',
    source_port=22,
    source_username='source_user',
    source_password='source_password',
    source_file_path='/path/to/source/file.txt',
    dest_host='dest.server.com',
    dest_port=22,
    dest_username='dest_user',
    dest_password='dest_password',
    dest_file_path='/path/to/destination/file.txt.gz'
)
