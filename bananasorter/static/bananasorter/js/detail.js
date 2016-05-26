var $class_api = '/api/classifiers/';
var $user_api = '/api/users/';
var $cat_api = '/api/categories';
var $use_form = $('#classify')
var $classifier = $use_form.find('input[name="classifier_id"]')
// var $csrf = $form.find('input[name="csrfmiddlewaretoken"]')
// var $name = $form.find('input[name="name"]')
// var $user = $form.find('input[name="user_id"]')


function append_category( category ) {
    $('.categories_list').append(
        $('<li>').text(category.name);
};


function get_classifiers() {
    $.get(
        $cat_api + '?classifier_id=' + $classifier.val(),
        function( data ) {
            data.results.forEach(function( category ) {
                append_category( category );
            })
    });
};
get_classifiers()
