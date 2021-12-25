
// this fuunction adds a class name to the blog post video 
node = document.querySelectorAll('iframe')
node.forEach(node => {
    node.parentNode.classList.add('video-position')
});

// this function is for limiting the input characters to numbers 
inputNode = document.querySelectorAll('.input-control')

inputNode.forEach(node=>{
    node.addEventListener("keypress", function (e) {
        var allowedChars = '0123456789';
        function contains(stringValue, charValue) {
            return stringValue.indexOf(charValue) > -1;
        }
        var invalidKey = e.key.length === 1 && !contains(allowedChars, e.key)
                || e.key === '.' && contains(e.target.value, '.');
        invalidKey && e.preventDefault();});
})
