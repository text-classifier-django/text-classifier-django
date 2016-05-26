var $class_api = '/api/classifiers/';
var $user_api = '/api/users/';
var $cat_api = '/api/categories';
// $form = $('.classifier_form')
// var $csrf = $form.find('input[name="csrfmiddlewaretoken"]')
// var $name = $form.find('input[name="name"]')
// var $user = $form.find('input[name="user_id"]')


function append_classifier( category ) {
    $('.categories_list').append(
        $('<li>').text(category.name);
};


// function get_classifiers() {
//     $.get($class_api, function( data ) {
//     data.results.forEach(function( category ) {
//         append_classifier( classifier );
//     });
// })};
// get_classifiers()
