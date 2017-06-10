function vote_update(url){
    $.ajax({
            url: url,
            headers: {
                'Content-Type':'application/json'
            },
            method: 'POST',
            dataType: 'json',
            success: function(data){
                window.location.replace(`/blog/v1/list/`);
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
        vote_update('/blog/v1/upvote/' + $blogId + '/');
    });

    $('body').on('click', '.downvote', function(event){
        event.preventDefault();
        var $blogId = $(this).data('blogId');
        vote_update('/blog/v1/downvote/' + $blogId + '/');
    });
});

