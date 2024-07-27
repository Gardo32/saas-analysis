document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("inputModal");
    var btn = document.getElementById("openModalButton");
    var span = document.getElementsByClassName("close")[0];

    btn.onclick = function() {
        modal.style.display = "block";
    }

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
// This script is similar to the one in compare.js, but it has some differences: