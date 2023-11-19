// Event Listener

var buttonClick = document.getElementById('core').addEventListener('click', function(event) {
    if (event.target.nodeName == "BUTTON") {
        var tar = event.target.id;
        console.log(tar);
        fetch('/' + tar) 
        return false;
    }
    });