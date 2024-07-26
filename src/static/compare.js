// compare.js

document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("compareModal");
    var btn = document.getElementById("compareButton");
    var span = document.getElementsByClassName("close")[0];
    var plotContainer = document.getElementById("plotContainer");
    var plotImage = document.getElementById("plotImage");

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

    document.getElementById('compareForm').onsubmit = function(event) {
        event.preventDefault();

        var formData = new FormData(this);
        fetch(this.action, {
            method: 'POST',
            body: formData
        }).then(response => response.blob())
          .then(blob => {
            var url = URL.createObjectURL(blob);
            plotImage.src = url;
            plotContainer.style.display = "block";
            modal.style.display = "none";
        });
    }
});
