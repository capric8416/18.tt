document.addEventListener('DOMContentLoaded', function(){
    fetch('/query/ip')
        .then(function(response) {
	    response.json().then(data => {
                document.getElementById('ip').textContent = data['ip'];
            });
        })
});
