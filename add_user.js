document.addEventListener('DOMContentLoaded', function() {
    // Get the modal
    var modal = document.getElementById("addUserModal");

    // Get the button that opens the modal
    var btn = document.getElementById("addUserBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Handle the form submission
    document.getElementById('addUserForm').addEventListener('submit', function(event) {
        event.preventDefault();

        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        fetch('/add_user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                alert('User added successfully');
                modal.style.display = "none";
                document.getElementById('addUserForm').reset();
            } else {
                alert('Failed to add user');
            }
        });
    });
});
