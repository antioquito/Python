import paramiko
from paramiko import SSHClient
from scp import SCPClient

def sftp_transfer(source_host, source_port, source_username, source_password, source_file_path,
                  dest_host, dest_port, dest_username, dest_password, dest_file_path):
    # Create SSH clients
    source_client = SSHClient()
    dest_client = SSHClient()
    
    # Automatically add the source host key (for simplicity, in real scenarios use known_hosts)
    source_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    dest_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the source server
        source_client.connect(source_host, port=source_port, username=source_username, password=source_password)
        
        # Connect to the destination server
        dest_client.connect(dest_host, port=dest_port, username=dest_username, password=dest_password)
        
        # Create SFTP session for source
        sftp_source = source_client.open_sftp()
        
        # Download file from the source server
        local_file_path = '/tmp/temp_file'  # Temporary file path
        sftp_source.get(source_file_path, local_file_path)
        sftp_source.close()
        
        # Create SFTP session for destination
        sftp_dest = dest_client.open_sftp()
        
        # Upload file to the destination server
        sftp_dest.put(local_file_path, dest_file_path)
        sftp_dest.close()
        
        print("File transferred successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        source_client.close()
        dest_client.close()

# Example usage
sftp_transfer(
    source_host='source.server.com',
    source_port=22,
    source_username='source_user',
    source_password='source_password',
    source_file_path='/path/to/source/file.txt',
    dest_host='dest.server.com',
    dest_port=22,
    dest_username='dest_user',
    dest_password='dest_password',
    dest_file_path='/path/to/destination/file.txt'
)
