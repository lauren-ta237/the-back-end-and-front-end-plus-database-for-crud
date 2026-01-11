// creating a file to implement CRUD operations

// link to my api
const API_URL_V2 = 'http://127.0.0.1:8000'
const API_URL = 'http://127.0.0.1:8000/posts';


//function to create new post
async function createPost(data) {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    return response.json();
}

//function to read all posts
async function getPost() {
    const response = await fetch(API_URL);
    const data = await response.json();
    console.log(data);
    return data;
}

//function to update an existing post
async function updatePost(id, data) {
    const response = await fetch(`${API_URL}/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    return response.json();
}

// function to delete post
async function deletePost(id) {
    await fetch(`${API_URL}/${id}`, {
        method: 'DELETE',
    });
}

//load and displays posts
async function loadPosts() {
    const posts = await getPost();
    createPostElementV2(posts);
    
}
function createPostElementV2(posts) {
    const postList = document.getElementById('postsContainer');
    // Use map and join to render all posts efficiently at once
    postList.innerHTML = posts.map(post => `
        <div class="post">
          <h3>${post.title}</h3>
          <p>${post.content}</p>
          <small>User ID: ${post.user_id}</small>
          <div class="post-actions">
            <button class="edit-btn" onclick="updatePostHandler(${post.id})">Edit</button>
            <button class="delete-btn" onclick="deletePostHandler(${post.id})">Delete</button>
          </div>
        </div>
    `).join('');
}
function createPostElement(posts) {
    const postList = document.getElementById('postsContainer');
    postList.innerHTML = ''; //clear existing posts anddisplay new one
    
    posts.forEach(post => {
        const listItem = document.createElement('li');
        listItem.textContent = `${post.title}: ${post.content}`;

        //create update and delete buttons
        const updateButton = document.createElement('button');
        updateButton.textContent = 'Update';
        updateButton.onclick = () => updatePostHandler(post.id);

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = () => deletePostHandler(post.id);

        listItem.appendChild(updateButton);
        listItem.appendChild(deleteButton);
        postList.appendChild(listItem);
    });
}

//create post handler
document.getElementById('postForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const user_id = document.getElementById('userId').value;
    const id = document.getElementById('postId').value; // Get the hidden ID

    if (id) {
        // If ID exists, we are updating
        await updatePost(id, {title, content});
    } else {
        // If no ID, we are creating
        await createPost({title, content, user_id});
    }
    
    loadPosts();//reload the posts
    document.getElementById('postForm').reset();// clear the form
    document.getElementById('postId').value = ''; // Clear the hidden ID
});

//delete post handler 
async function deletePostHandler(id){
    await deletePost(id);
    loadPosts(); //refresh the post list
}

//update post handler example
async function updatePostHandler(id) {
    // 1. Fetch the current data for this post
    const response = await fetch(`${API_URL}/${id}`);
    const post = await response.json();

    // 2. Populate the form fields
    document.getElementById('title').value = post.title;
    document.getElementById('content').value = post.content;
    document.getElementById('userId').value = post.user_id;
    document.getElementById('postId').value = post.id; // Set the hidden ID
}

//initial fetch
loadPosts()