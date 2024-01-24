class File:
    
    def __init__(self, content):
        self.content = content
        
    def add_content(self, content):
        self.content += content
    
    def read_content(self):
        return self.content

class Directory:
    
    def __init__(self):
        self.files = {}
        self.sub_d = {}
        

class FileSystem:

    def __init__(self):
        self.root_dir = Directory()
        self.file_index = {}
        

    def ls(self, path: str) -> List[str]:
        # get file path
        out = []
        curr_dir = self.root_dir
        clean_path = path[1:]
        if clean_path:
            folders = clean_path.split("/")
            end = folders[-1]
            for folder in folders[:-1]:
                # move to last folder
                curr_dir = curr_dir.sub_d[folder]
            if end in curr_dir.files:
                out = [end]
            elif end in curr_dir.sub_d:
                curr_dir = curr_dir.sub_d[end]
                out = list(curr_dir.files.keys()) + list(curr_dir.sub_d.keys())
        else:
            out = list(self.root_dir.files.keys()) + list(self.root_dir.sub_d.keys())
        return sorted(out)
        

    def mkdir(self, path: str) -> None:
        clean_path = path[1:]
        curr_dir = self.root_dir
        folders = clean_path.split("/")
        for folder in folders:
            if folder not in curr_dir.sub_d:
                curr_dir.sub_d[folder] = Directory()
            curr_dir = curr_dir.sub_d[folder]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.file_index:
            # create file
            file = File(content)
            # traverse the path
            current_dir = self.root_dir
            path_trimmed = filePath[1:]
            path_tokens = path_trimmed.split("/")
            file_name = path_tokens[-1]
            iterate_dirs = path_tokens[:-1]
            if iterate_dirs:
                for dir in iterate_dirs:
                    current_dir = current_dir.sub_d[dir]
            # place the file
            current_dir.files[file_name] = file
            # index the file
            self.file_index[filePath] = file
        else:
            # access the index directly
            self.file_index[filePath].add_content(content)

    def readContentFromFile(self, filePath: str) -> str:
        return self.file_index[filePath].read_content()


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)