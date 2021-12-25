
tinymce.init({
    selector: 'textarea',  // change this value according to your HTML
    images_upload_url:'/upload/',
    // images_upload_base_path: '/static/tinymce',
    height: 1080,
    plugins: [
        'advlist autolink lists link image charmap print preview anchor',
        'searchreplace visualblocks code fullscreen',
        'insertdatetime media table paste code help wordcount codesample',
        'textcolor save link image media preview codesample contextmenu',
        'table code lists fullscreen insertdatetime nonbreaking',
        'contextmenu directionality searchreplace wordcount visualblocks',
        'visualchars code fullscreen autolink lists charmap print hr',
        'anchor pagebreak',
    ],
    menubar: 'favs file edit view insert format tools table help',
    toolbar: 'undo redo | formatselect | ' +
        'bold italic backcolor | alignleft aligncenter ' +
        'alignright alignjustify | bullist numlist outdent indent | ' +
        'code image | codesample' +
        'removeformat | help',
    
});


