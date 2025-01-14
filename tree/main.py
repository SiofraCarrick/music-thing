import os
import tkinter as tk
from tkinter import ttk


def get_directory_structure(rootdir):
    """Generate the directory structure for the rootdir"""
    dir_structure = {}
    for root, dirs, files in os.walk(rootdir):
        path_parts = root.split(os.sep)
        subdir = dir_structure
        for part in path_parts:
            subdir = subdir.setdefault(part, {})
        for file in files:
            subdir[file] = None
    return dir_structure


class FileExplorer(tk.Tk):
    def __init__(self, rootdir):
        super().__init__()
        self.title("Directory Tree Viewer")
        self.geometry("500x400")

        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(tree_frame)
        self.tree.pack(fill="both", expand=True)

        # Populate the tree view with the directory structure
        self.populate_tree(rootdir)

    def populate_tree(self, rootdir):
        # Get directory structure as a dictionary
        dir_structure = get_directory_structure(rootdir)

        # Insert the root node
        root_node = self.tree.insert("", "end", text=rootdir, open=True)

        # Recursively insert subfolders and files
        self.insert_nodes(root_node, dir_structure)

    def insert_nodes(self, parent, node_structure):
        """Recursively insert nodes into the Treeview widget"""
        for key, value in node_structure.items():
            if value is None:
                # It's a file
                self.tree.insert(parent, "end", text=key, open=False)
            else:
                # It's a directory
                dir_node = self.tree.insert(parent, "end", text=key, open=False)
                self.insert_nodes(dir_node, value)


# Run the application
if __name__ == "__main__":
    # Change this to the directory you want to start from
    start_dir = "D:\shovel ware graphics"  # Example for Windows
    # start_dir = "/path/to/your/directory"  # Example for Unix-based systems
    app = FileExplorer(start_dir)
    app.mainloop()
