from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
#from mysite.settings import *

# Set the connection string for the Azurite Blob service
CONNECTION_STRING = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://host.docker.internal:10000/devstoreaccount1;"

# Name of the container in which you want to store the file
CONTAINER_NAME = "pathfinderbackups"

"""
    @Author: DeanLogan123
    @Description: Retrieves or creates a Blob Storage container client using a connection string and container name.
    @return: A container client object for interacting with the specified container.
    """
def getContainerClient():
    blobServiceClient = BlobServiceClient.from_connection_string(CONNECTION_STRING) # Create a BlobServiceClient using the provided connection string
    containerClient = blobServiceClient.get_container_client(CONTAINER_NAME) # Get or create a container client using the specified container name
    
    # Check if the container exists; if not, create it
    if not containerClient.exists():
        containerClient.create_container()
    
    return containerClient # Return the container client object for further interaction

"""
@Author: DeanLogan123
@Description: Uploads a file from the local file system to a specified Blob Storage container.
@param: filePath - The local path of the file to be uploaded.
@param: destinationBlobName - The name to assign to the uploaded blob in the container.
@return: True if the upload is successful, False otherwise.
"""
def uploadFileToBlob(filePath, destinationBlobName):
    containerClient = getContainerClient()  # Get a container client using the defined function
    try:
        # Upload the file to Blob Storage
        with open(filePath, "rb") as file:
            blobClient = containerClient.get_blob_client(destinationBlobName)
            blobClient.upload_blob(file)  # Upload the file to the blob storage
        
        return True  # Return True if the upload is successful
    except:
        return False  # Return False if there's any exception during the upload


"""
@Author: DeanLogan123
@Description: Checks if a specified blob exists in a Blob Storage container.
@param: destinationBlobName - The name of the blob to check for.
@return: True if the blob exists in the container, False otherwise.
"""
def blobInBlobContainer(destinationBlobName):
    containerClient = getContainerClient()  # Get a container client using the defined function
    
    # Check if the container exists
    if not containerClient.exists():
        return False
    
    blobs = containerClient.list_blobs() # List all blobs in the container
    
    # Check if the uploaded file exists in the container
    for blob in blobs:
        if blob.name == destinationBlobName:
            return True
    
    return False  # Return False if the blob doesn't exist in the container


"""
@Author: DeanLogan123
@Description: Deletes a specified blob from a Blob Storage container, if it exists.
@param: blobNameToDelete - The name of the blob to delete.
@return: True if the blob was deleted successfully, False if the blob doesn't exist.
"""
def deleteBlob(blobNameToDelete):
    containerClient = getContainerClient()  # Get a container client using the defined function
    
    # Get the blob client for the specified blob name
    blobClient = containerClient.get_blob_client(blobNameToDelete)
    
    # Check if the blob exists
    if blobClient.exists():
        blobClient.delete_blob()  # Delete the blob
        return True  # Return True if the blob was deleted successfully
    else:
        return False  # Return False if the blob doesn't exist in the container

"""
@Author: DeanLogan123
@Description: Lists all blobs in a Blob Storage container.
"""
def listBlobs():
    containerClient = getContainerClient()  # Get a container client using the defined function
    
    blobList = containerClient.list_blobs() # List all blobs in the container
    
    print(f"Blobs in container '{CONTAINER_NAME}':")
    count = 0
    if not blobList:
        print("No blobs found in the container.")
    else:
        for blob in blobList:
            count += 1
            print(f"- {blob.name}")  # Print the name of each blob in the container
    print(count)

if __name__ == "__main__":
    listBlobs()