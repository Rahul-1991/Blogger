# Blogger
A website to write on topics and enable upvotes and down votes.
The user can edit posts and delete posts.
The homepage is sorted such that top 20 posts are visible. The sorting is performed on the number of upvotes count such that the 20 posts having the highest upvotes count are visible.

##### Technology Stack
This project is powered by the **Django** web framework of python. A pinch of **jquery** is used to provide the functionality of upvotes and downvotes. Also **bootstrap** is used for providing UI to the website.

##### Data Storage
No database or any type of persistent data storage is used. The app runs on in memory data structure to support storage. Once the app is restarted the data is lost.
The Dictionary data structure of python is used to store the information. The basic of CRUD operations which are performed on database have been provided for querying on the dictionary.

##### Information stored
The dictionary has primary key as its key which is auto incremented every time a new post is created.
The value contains information about the post. The value itself is a dictionary having fields as: -
* pk - primary key
* content - post content
* created_at - date of post creation
* updated_at - date of post last updation
* upvotes_count - The number of upvotes count
* downvotes_count - The number of downvotes count

##### Installing instructions
1. Creating Virtual Environment
    ```
    virtualenv venv
    ```
2. Start Virtual Environment
    ```
    source venv/bin/activate
    ```
3. Clone Repo
    ```
    git clone https://github.com/Rahul-1991/Blogger.git
    ```
4. Install dependencies
    ```
    cd Blogger
    pip install -r requirements.txt
    ```
5. Run app
    ```
    python manage.py runserver
    ```

There may be some warnings which can be safely ignored.


##### List of APIs
* create - To create a post
* list - To get the list of top 20 posts
* update - To update the post
* delete - To delete the post
* read - To get the info of a particular post

