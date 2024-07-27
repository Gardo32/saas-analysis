document.addEventListener('DOMContentLoaded', (event) => {
    const processForm = document.getElementById('processForm');
    const plotButton = document.getElementById('plotButton');
    const deleteButton = document.getElementById('deleteButton');

    if (processForm) {
        processForm.addEventListener('submit', (e) => {
            const chartTitle = document.getElementById('chartTitle').value.trim();
            const indexColumn = document.getElementById('indexColumn').value.trim();
            const plotColumn = document.getElementById('plotColumn').value.trim();

            if (!chartTitle || !indexColumn || !plotColumn) {
                alert('Please fill out all fields');
                e.preventDefault();
            }
        });
    }

    if (deleteButton) {
        deleteButton.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete this file?')) {
                e.preventDefault();
            }
        });
    }
});
// This script is similar to the one in compare.js, but it has some differences: