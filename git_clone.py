from git import Repo
import git


def clone_repo():
    
    repo_url = "https://github.com/PhonePe/pulse.git/"
    destination_path = "D:\Phonepe Pulse\clone"
    
    try:
        clone = Repo.clone_from(repo_url, destination_path)
        print(f"Repository cloned successfully to {destination_path}.")
    except git.GitError as e:
        print(f"Failed to clone repository: {str(e)}")
        
    return clone
        

