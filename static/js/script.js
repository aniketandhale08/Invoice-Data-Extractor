function updateFileList() {
    const fileInput = document.getElementById("file-input");
    const fileListContainer = document.getElementById("file-list-container");
    fileListContainer.innerHTML = "";
    const files = fileInput.files;
    for (let i = 0; i < files.length; i++) {
        const fileItem = document.createElement("div");
        fileItem.className = "file-item";
        const fileName = document.createElement("span");
        fileName.textContent = files[i].name;
        const removeButton = document.createElement("button");
        removeButton.textContent = "Remove";
        removeButton.onclick = function() {
            const dt = new DataTransfer();
            for (let j = 0; j < files.length; j++) {
                if (i !== j) dt.items.add(files[j]);
            }
            fileInput.files = dt.files;
            updateFileList();
        };
        fileItem.appendChild(fileName);
        fileItem.appendChild(removeButton);
        fileListContainer.appendChild(fileItem);
    }
}
