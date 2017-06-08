function vote_update(url){
    $.ajax({
            url: url,
            headers: {
                'Content-Type':'application/json'
            },
            method: 'POST',
            dataType: 'json',
            success: function(data){
                window.location.replace(`/blog/list/`);
            },
            error: function(data, status, error) {
                handleFormError(data.responseJSON)
            }
        });
}

function delete_blog(url){
    $.ajax({
            url: url,
            headers: {
                'Content-Type':'application/json'
            },
            method: "DELETE",
            dataType: 'json',
            success: function(data){
                window.location.replace(`/blog/list/`)
            },
            error: function(data, status, error) {
                handleFormError(data.responseJSON)
            }
        });
}

$(document).ready(function() {
    $('body').on('click', '.upvote', function(event){
        event.preventDefault();
        var $blogId = $(this).data('blogId');
        vote_update('/blog/upvote/' + $blogId + '/');
    });

    $('body').on('click', '.downvote', function(event){
        event.preventDefault();
        var $blogId = $(this).data('blogId');
        vote_update('/blog/downvote/' + $blogId + '/');
    });

    $('body').on('click', '.delete-blog', function(event){
        event.preventDefault();
        var $blogId = $(this).data('blogId');
        console.log($blogId);
        delete_blog('/blog/delete/' + $blogId + '/')
    });
});

