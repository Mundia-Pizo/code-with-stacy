
const truncateString =(str, num)=> {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
}
nodes = document.querySelectorAll('.description')
nodes.forEach(node => {
text = truncateString(node.innerText, 130)
node.innerText=text;
});


// p = document.querySelectorAll('img')

