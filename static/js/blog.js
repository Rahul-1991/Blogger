$(document).ready(function() {
    $('body').on('click', '.glyphicon-thumbs-up', function(event){
        event.preventDefault();
        console.log('thumbs up');
    });

    $('body').on('click', '.glyphicon-thumbs-down', function(event){
        event.preventDefault();
        console.log('thumbs down');
    });
});

